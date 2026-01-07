import os
import re
import glob
import requests
import yaml
from datetime import datetime, timedelta, timezone

GH_TOKEN = os.environ["GH_TOKEN"]
REPO = os.environ["GITHUB_REPO"]
PROJECT_NUMBER = os.environ.get("PROJECT_NUMBER")
DEFAULT_ASSIGNEE = os.environ.get("DEFAULT_ASSIGNEE", "")

HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

def read_frontmatter(md_text: str) -> dict:
    """
    Parse YAML frontmatter: --- ... ---
    """
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md_text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}

def classify(score: float):
    if score >= 4.0:
        return "must", "Backlog"
    if 3.0 <= score <= 3.5:
        return "watch", "À surveiller"
    return "archive", "Archivé"

def gh_api(method, url, **kwargs):
    r = requests.request(method, url, headers=HEADERS, **kwargs)
    if r.status_code >= 300:
        raise RuntimeError(f"{method} {url} -> {r.status_code}\n{r.text}")
    return r.json() if r.text else None

def search_issue_by_source(source_path: str):
    q = f'repo:{REPO} "Source: {source_path}" in:body type:issue'
    url = "https://api.github.com/search/issues"
    data = gh_api("GET", url, params={"q": q})
    items = data.get("items", [])
    return items[0] if items else None

def create_or_update_issue(title, body, labels, assignee, source_path):
    existing = search_issue_by_source(source_path)
    if existing:
        issue_url = existing["url"]
        gh_api("PATCH", issue_url, json={"title": title, "body": body})
        gh_api("PUT", issue_url + "/labels", json={"labels": labels})
        if assignee:
            gh_api("POST", issue_url + "/assignees", json={"assignees": [assignee]})
        return existing["number"], issue_url, True
    else:
        url = f"https://api.github.com/repos/{REPO}/issues"
        payload = {"title": title, "body": body, "labels": labels}
        if assignee:
            payload["assignees"] = [assignee]
        created = gh_api("POST", url, json=payload)
        return created["number"], created["url"], False

def close_issue(issue_url):
    gh_api("PATCH", issue_url, json={"state": "closed"})

def main():
    md_files = glob.glob("Note/**/*.md", recursive=True)

    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()

        fm = read_frontmatter(txt)
        if not fm:
            continue

        score_raw = fm.get("note", None)
        if score_raw is None:
            continue

        try:
            score = float(score_raw)
        except Exception:
            continue

        title = fm.get("title") or os.path.splitext(os.path.basename(path))[0]
        url = fm.get("url") or ""
        source = fm.get("rss-source") or fm.get("rss_source") or ""
        date_val = fm.get("date") or ""
        bucket, status_name = classify(score)
        due = (datetime.now(timezone.utc) + timedelta(days=14)).date().isoformat() if bucket == "must" else None
        base_labels = ["veille"]
        if bucket == "must":
            labels = base_labels + ["must-do"]
        elif bucket == "watch":
            labels = base_labels + ["watch"]
        else:
            labels = base_labels + ["archived"]

        assignee = DEFAULT_ASSIGNEE if bucket == "must" else ""

        body_lines = [
            f"Score: **{score}**",
            f"Status cible: **{status_name}**",
        ]
        if date_val:
            body_lines.append(f"Date: {date_val}")
        if source:
            body_lines.append(f"Source: {source}")
        if url:
            body_lines.append(f"URL: {url}")
        if due:
            body_lines.append(f"Échéance (J+14): **{due}**")
        body_lines.append("")
        body_lines.append(f"Source: {path}")
        body = "\n".join(body_lines)
        existing = search_issue_by_source(path)
        if bucket == "archive":
            if existing:
                issue_url = existing["url"]
                gh_api("PUT", issue_url + "/labels", json={"labels": labels})
                close_issue(issue_url)
            continue
        issue_number, issue_url, updated = create_or_update_issue(
            title=f"[Veille] {title}",
            body=body,
            labels=labels,
            assignee=assignee,
            source_path=path,
        )

        print(("UPDATED" if updated else "CREATED"), path, "->", issue_number)

if __name__ == "__main__":
    main()
