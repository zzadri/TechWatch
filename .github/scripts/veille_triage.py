import os, re, glob, requests, yaml
from datetime import datetime, timedelta, timezone

GH_TOKEN = os.environ["GH_TOKEN"]
REPO = os.environ["GITHUB_REPO"]
DEFAULT_ASSIGNEE = os.environ.get("DEFAULT_ASSIGNEE", "")
WATCH_ROOT = os.environ.get("WATCH_ROOT", "Note")  # <-- ton repo utilise Note/

API = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

def gh(method, url, **kwargs):
    r = requests.request(method, url, headers=HEADERS, **kwargs)
    if r.status_code >= 300:
        raise RuntimeError(f"{method} {url} -> {r.status_code}\n{r.text}")
    return r.json() if r.text else None

def parse_frontmatter(text: str):
    # tolère BOM + espaces avant le frontmatter
    m = re.search(r"(?s)^\ufeff?\s*---\s*\n(.*?)\n---\s*\n", text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}

def parse_score(raw):
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return float(raw)
    s = str(raw).strip()
    m = re.search(r"[-+]?\d+(\.\d+)?", s)
    return float(m.group(0)) if m else None

def classify(score: float):
    if score >= 4.0:
        return "must"
    if 3.0 <= score <= 3.5:
        return "watch"
    return "archive"

def ensure_label(name: str, color="ededed", description="Auto-created by veille workflow"):
    # crée le label si absent
    r = requests.get(f"{API}/repos/{REPO}/labels/{name}", headers=HEADERS)
    if r.status_code == 200:
        return
    if r.status_code != 404:
        raise RuntimeError(f"GET label {name} -> {r.status_code}\n{r.text}")
    gh("POST", f"{API}/repos/{REPO}/labels", json={
        "name": name,
        "color": color,
        "description": description
    })

def list_existing_issues_by_source():
    """
    Récupère toutes les issues avec label=veille (open + closed) et construit un mapping:
    source_path -> issue_object
    """
    mapping = {}
    page = 1
    while True:
        issues = gh("GET", f"{API}/repos/{REPO}/issues", params={
            "state": "all",
            "labels": "veille",
            "per_page": 100,
            "page": page,
        })
        if not issues:
            break

        for it in issues:
            body = it.get("body") or ""
            m = re.search(r"^Source:\s*(.+)\s*$", body, re.MULTILINE)
            if m:
                mapping[m.group(1).strip()] = it

        if len(issues) < 100:
            break
        page += 1

    return mapping

def put_labels(issue_url: str, labels):
    gh("PUT", issue_url + "/labels", json={"labels": labels})

def close_issue(issue_url: str):
    gh("PATCH", issue_url, json={"state": "closed"})

def create_issue(title, body, labels, assignee):
    payload = {"title": title, "body": body, "labels": labels}
    if assignee:
        payload["assignees"] = [assignee]
    return gh("POST", f"{API}/repos/{REPO}/issues", json=payload)

def update_issue(issue_url, title, body, labels, assignee):
    gh("PATCH", issue_url, json={"title": title, "body": body})
    put_labels(issue_url, labels)
    if assignee:
        gh("POST", issue_url + "/assignees", json={"assignees": [assignee]})

def main():
    # labels nécessaires
    ensure_label("veille")
    ensure_label("must-do")
    ensure_label("watch")
    ensure_label("archived")

    files = glob.glob(f"{WATCH_ROOT}/**/*.md", recursive=True)
    print(f"[INFO] Scanning root='{WATCH_ROOT}' -> {len(files)} markdown files")

    existing_map = list_existing_issues_by_source()
    print(f"[INFO] Found {len(existing_map)} existing veille issues (mapped by Source:)")

    processed = 0
    created = 0
    updated = 0
    archived = 0

    for path in files:
        text = open(path, "r", encoding="utf-8").read()
        fm = parse_frontmatter(text)
        if not fm:
            continue

        score = parse_score(fm.get("note"))
        if score is None:
            continue

        processed += 1
        bucket = classify(score)

        title = fm.get("title") or os.path.splitext(os.path.basename(path))[0]
        url = fm.get("url") or ""
        src = fm.get("rss-source") or ""
        d = fm.get("date") or ""

        issue = existing_map.get(path)
        issue_url = issue["url"] if issue else None

        base_labels = ["veille"]
        assignee = ""
        due = None

        if bucket == "must":
            labels = base_labels + ["must-do"]
            assignee = DEFAULT_ASSIGNEE
            due = (datetime.now(timezone.utc) + timedelta(days=14)).date().isoformat()
        elif bucket == "watch":
            labels = base_labels + ["watch"]
        else:
            labels = base_labels + ["archived"]

        # archive => ferme si déjà une issue existe, sinon rien
        if bucket == "archive":
            if issue_url:
                put_labels(issue_url, labels)
                close_issue(issue_url)
                archived += 1
                print(f"[ARCHIVE] closed {issue_url} <- {path} (score={score})")
            continue

        body = "\n".join([
            f"Score: **{score}**",
            f"Date: {d}" if d else "",
            f"Source: {src}" if src else "",
            f"URL: {url}" if url else "",
            f"Échéance (J+14): **{due}**" if due else "",
            "",
            f"Source: {path}",
        ]).strip()

        issue_title = f"[Veille] {title}"

        if issue_url:
            update_issue(issue_url, issue_title, body, labels, assignee)
            updated += 1
            print(f"[UPDATE] {issue_url} <- {path} (score={score})")
        else:
            new_issue = create_issue(issue_title, body, labels, assignee)
            created += 1
            print(f"[CREATE] {new_issue['html_url']} <- {path} (score={score})")

    print(f"[INFO] processed={processed} created={created} updated={updated} archived={archived}")

if __name__ == "__main__":
    main()
