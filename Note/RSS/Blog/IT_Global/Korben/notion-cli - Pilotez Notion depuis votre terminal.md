---
title: "notion-cli - Pilotez Notion depuis votre terminal"
author: "Korben"
date: 2026-02-26T13:33:36.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "automatisation"
  - "CLI"
  - "Notion"
rss_source: Blog
url: https://korben.info/notion-cli-automatiser-notion-terminal.html
note: 0
seen: false
---

<p>Si vous utilisez
<a href="https://korben.info/notion-prise-notes.html">Notion</a>
au quotidien et que vous avez toujours rêvé de piloter vos bases de données depuis un terminal... <strong>y'a enfin un truc qui tient la route</strong>.</p>
<p>Ça s'appelle
<a href="https://github.com/4ier/notion-cli">notion-cli</a>
, c'est un binaire Go qui embarque 39 commandes couvrant TOUTE l'API Notion. Il s'agit d'un seul exécutable pour macOS, Linux et Windows (amd64 et arm64) sans dépendance qui vous permet de gérer pages, bases de données, blocs et commentaires sans jamais ouvrir un navigateur.</p>
<p>L'installation, c'est du classique : <code>brew install 4ier/tap/notion-cli</code> sur macOS, <code>go install</code> pour les puristes, <code>npm install -g notion-cli-go</code> ou même Docker. Il faut juste un token d'intégration Notion (le <code>ntn_xxxxx</code> que vous générez sur notion.so/my-integrations), vous le collez dans <code>~/.config/notion-cli/config.json</code> ou en variable <code>NOTION_TOKEN</code>, et c'est parti.</p>
<img src="https://korben.info/notion-cli-automatiser-notion-terminal/notion-cli-automatiser-notion-terminal-1.gif" alt="" loading="lazy" decoding="async">
<p><em>notion-cli en action dans le terminal</em></p>
<p>Le truc cool, ce sont les filtres humain-friendly. Au lieu de se taper du JSON pour filtrer une base, vous écrivez <code>Status=Done</code> et l'outil se débrouille tout seul. En fait, il détecte le type de chaque propriété (texte, date, sélection...) et adapte le filtre automatiquement. C'est carrément pas mal, je trouve.</p>
<p>Et côté Markdown, c'est la fête ! Vous exportez une page entière avec <code>notion block list &lt;page-id&gt; --md --depth 3</code>, et inversement, vous injectez un fichier <code>.md</code> dans Notion via <code>notion block append &lt;page-id&gt; --file notes.md</code>. Pour ceux qui bossent avec de la doc technique, ça simplifie sérieusement les choses. Bon, ça ne marche pas avec les blocs synchronisés ou les embeds exotiques, mais pour le reste c'est nickel.</p>
<p>D'ailleurs le mode &quot;pipé&quot; est vraiment malin. Car dans le terminal, l'outil affiche de jolies tables colorées mais dès que vous le &quot;pipez&quot; vers <code>jq</code> ou un script, il bascule en JSON automatiquement. Du coup, intégrer ça dans un pipeline shell ou un cron... c'est aucun parsing à faire. Voilà quoi.</p>
<p>Après des CLI pour Notion, y'en a déjà quelques-uns. Sauf que la plupart sont soit limités aux tâches (comme
<a href="https://github.com/kris-hansen/notion-cli-go">notion-cli-go</a>
qui gère surtout le côté todo), soit cantonnés à l'export (et souvent liés à un OS ou un langage précis).</p>
<p>Celui de 4ier, c'est donc le premier à couvrir l'API en entier : pages, bases, blocs, commentaires, fichiers, utilisateurs, et même un accès REST brut via <code>notion api GET /v1/endpoint</code>. En gros, c'est le <code>gh</code> de GitHub, mais pour Notion (et pour une fois, c'est pas juste du blabla marketing ^^).</p>
<p>Les cas d'usage qui tuent c'est par exemple un script cron qui crée une entrée hebdo avec <code>notion page create &lt;db-id&gt; --db &quot;Name=Weekly&quot; &quot;Status=Todo&quot;</code>. Un backup qui exporte vos pages critiques en Markdown toutes les nuits. Ou un CI/CD qui met à jour un changelog Notion à chaque deploy. Quelques lignes de bash et c'est réglé, car l'outil gère tout le reste ! C'est hyper rare un CLI qui couvre autant de terrain.</p>
<p>Y'a aussi le côté agent-friendly pour ceux qui kiffent l'IA. L'outil retourne des codes de sortie propres, du JSON exploitable, et s'installe comme skill agent via <code>npx skills add 4ier/notion-cli</code>. Dans la lignée de
<a href="https://korben.info/gemini-cli-google-terminal-ia.html">Gemini CLI</a>
, on voit de plus en plus d'outils pensés terminal-first... et je trouve que c'est carrément bien.</p>
<p>Après comme souvent quand je vous présente des outils, le projet est tout frais (v0.3.0, licence MIT), avec une petite communauté donc attention, car comme tout ce qui dépend d'une API tierce, si Notion bouge ses endpoints... voilà quoi. Mais c'est propre, c'est testé, et ça tourne déjà très bien.</p>
<p>Votre navigateur va pouvoir souffler un peu.</p>