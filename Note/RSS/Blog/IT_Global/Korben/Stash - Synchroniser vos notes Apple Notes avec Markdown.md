---
title: "Stash - Synchroniser vos notes Apple Notes avec Markdown"
author: "Korben"
date: 2026-02-01T08:15:12.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/iphone-ipad"
  - "developpement/outils-developpement"
  - "tutoriels-guides"
  - "Apple Notes"
  - "AppleScript"
  - "application de productivité"
  - "CLI"
  - "éditeur Markdown"
  - "Homebrew"
  - "Pandoc"
  - "sync"
rss_source: Blog
url: https://korben.info/stash-markdown-apple-notes-sync.html
note: 0
seen: false
---

<p>Si vous êtes comme moi et que vous vivez dans Apple Notes parce que c'est fluide, synchronisé partout, et que ça marche sans qu'on ait à se poser de questions, cet outil va vous plaire.</p>
<p>Parce que oui, voilà, le jour où vous voulez bidouiller vos notes en ligne de commande, les exporter en Markdown, ou simplement éviter de vous retrouver coincé dans votre prison dorée Apple... Et bien c'est la galère. J'ai longtemps cherché une solution propre. Je me suis même dit à un moment que j'allais coder un script Python foireux pour scrapper la base SQLite locale, mais j'ai vite abandonné l'idée.</p>
<p>Pourquoi ? Parce que j'ai découvert
<a href="https://github.com/shakedlokits/stash">Stash</a>
, un petit outil en ligne de commande qui fait le pont entre vos notes Apple et des fichiers Markdown.</p>
<p>Et le truc cool, c'est que ça marche dans les deux sens. Vous pouvez exporter vos notes Apple en Markdown (comme ici :
<a href="https://korben.info/backup-sauvegarde-apple-notes.html">Exporter pour vos backups</a>
), mais aussi éditer vos fichiers Markdown et renvoyer les changements directement dans Apple Notes. C'est une vrai synchro bidirectionnelle qui vous rend vraiment maître de vos données.</p>
<p>J'ai testé ça sur macOS Tahoe avec un dossier de notes en vrac. J'ai lancé le bousin, et ça m'a fait plaisir de voir mes fichiers .md popper proprement dans le terminal, prêts à être commités ensuite sur un GitHub ou édités dans VS Code.</p>
<p>L'installation est toute bête, via Homebrew :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew tap shakedlokits/stash https://github.com/shakedlokits/stash
</span></span><span class="line"><span class="cl">brew install shakedlokits/stash/stash
</span></span></code></pre><p>Et ensuite, c'est juste 2 commandes. Pour exporter une note Apple vers Markdown, c'est</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">stash pull &#34;Ma Super Note&#34;
</span></span></code></pre><p>Stash va chercher la note dans Apple Notes, la convertit en Markdown propre via Pandoc, et vous la balance dans un fichier local <code>Ma Super Note.md</code>.</p>
<p>Et la seconde commande c'est pour faire l'inverse (éditer votre Markdown et pousser les changements vers Apple Notes). Là faut faire</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">stash push &#34;Ma Super Note.md&#34;
</span></span></code></pre><p>Et là, magie !! Vos modifs se retrouvent dans l'app Notes, synchronisées sur tous vos appareils Apple (iPhone, iPad, Mac). C'est dommage que ça soit pas natif ce truc.</p>
<p>Stash c'est chouette (Oula pas facile à prononcer vite celle là) parce qu'il utilise du YAML front-matter pour lier chaque fichier Markdown à une note Apple spécifique (via un ID unique). Quand vous faites <code>stash push</code>, le contenu du fichier écrase la note. Quand vous faites <code>stash pull</code>, la note écrase le fichier.</p>
<p><strong>Attention toutefois</strong> car c'est là que ça se corse... <strong>Stash écrase sans pitié !!</strong> Si vous modifiez votre note sur l'iPhone ET votre fichier Markdown en même temps, c'est le dernier qui parle qui a raison. Y'a pas de fusion intelligente à la Git, donc gaffe aux conflits. C'est un peu brut de décoffrage, mais au moins c'est clair et prévisible.</p>
<p>Bref, pour ceux qui veulent scripter leurs notes, automatiser des backups, ou simplement bosser en Markdown avec leur éditeur préféré, c'est le chaînon manquant. J'avais testé Obsidian et Joplin par le passé, mais la synchro iCloud ou WebDAV m'avait saoulé. Là, c'est le bon compromis avec l'interface Apple pour la saisie, le Markdown pour le stockage long terme.</p>