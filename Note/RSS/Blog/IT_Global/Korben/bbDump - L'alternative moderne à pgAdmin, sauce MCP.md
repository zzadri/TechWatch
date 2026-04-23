---
title: "bbDump - L'alternative moderne à pgAdmin, sauce MCP"
author: "Korben ✨"
date: 2026-04-23T07:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "intelligence-artificielle/chatbots-llm"
  - "mcp"
rss_source: Blog
url: https://korben.info/bbdump-lalternative-moderne-a-pgadmin-sauce-mcp.html
note: 0
seen: false
---

<p><strong>pgAdmin</strong>, l'outil &quot;officiel&quot; pour administrer vos bases PostgreSQL, c'est le type d'interface qu'on n'a pas vraiment envie d'ouvrir un lundi matin ! C'est lent, c'est cheum de ouf en mode figé dans les années 2000 et ça rame sérieusement dès qu'on tente un export un peu costaud. Alors oui je sais, <strong>DBeaver</strong>, c'est plus joli, mais faut se coltiner Java et un workspace qui traîne au démarrage.</p>
<p>Du coup quand
<a href="https://poups.dev/bbdump">bbDump</a>
est passé sur mon radar, j'ai eu envie de creuser un peu. C'est un gestionnaire PostgreSQL moderne, en Electron + Vue + TypeScript, signé par Poups, un dev indé français. L'outil reprend tout ce que vous faites habituellement en CLI (pg_dump, pg_restore, coups d'œil aux tables, schéma de la DB) et met ça dans une interface vraiment propre.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/bbdump-lalternative-moderne-a-pgadmin-sauce-mcp/bbdump-lalternative-moderne-a-pgadmin-sauce-mcp-2.png" alt="" loading="lazy" decoding="async">
<p><em>Le dashboard bbDump, tout de suite plus respirable que pgAdmin</em></p>
<p>Côté fonctionnalités classiques, vous avez ce qu'on attend d'un client PostgreSQL correct. Gestion multi-bases organisée par projet, backups avec liste, restauration, filtre par base, tailles et dates. De leur côté, les tâches planifiées via expressions cron sont configurables par base, et il y a même une visionneuse de logs en temps réel qui trace chaque opération pg_dump.</p>
<p>Ajoutez à ça un navigateur de tables avec édition inline (avec support complet des types), un constructeur de requêtes SQL visuel en plus de l'éditeur brut, l'export CSV, et un diagramme entité-relation interactif via Vue Flow pour visualiser les tables et les clés étrangères. Grâce à bbDump, plus besoin d'aller chercher un outil externe pour comprendre une base héritée d'un projet qui traîne !!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/bbdump-lalternative-moderne-a-pgadmin-sauce-mcp/bbdump-lalternative-moderne-a-pgadmin-sauce-mcp-3.png" alt="" loading="lazy" decoding="async">
<p><em>Le schema visualizer en mode ERD interactif, pratique pour décortiquer une base héritée</em></p>
<p>Mais le vrai twist, c'est l'intégration du MCP (Model Context Protocol) puisque bbDump expose 31 outils MCP aux agents IA, ce qui veut dire que votre Claude d'amour ou votre LLM peut interroger la DB, regarder un schéma, tester une requête. Et comme les mutations passent par un système de confirmation, pas de DROP TABLE à l'insu de votre plein gré !</p>
<p>Je vous avais déjà parlé de cette approche avec
<a href="https://korben.info/ghidra-mcp-reverse-engineering-ia.html">Ghidra MCP</a>
côté reverse engineering et
<a href="https://korben.info/browserwing-automatisation-navigateur-ia-mcp.html">BrowserWing</a>
côté automatisation navigateur. bbDump rejoint donc la famille côté backend de données.</p>
<p>Autre détail sympa, le dev a pensé à la sécurité puisque les backups sont chiffrés en AES-256-GCM, donc si vous synchronisez vos dumps sur un cloud random, pas de panique sur les données sensibles. Sur macOS, y'a même une mini-app menu bar pour accéder aux bases et aux connexions proxy sans ouvrir l'app complète.</p>
<p>Côté installation, c'est facile :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -fsSL https://poups.dev/bbdump.sh | bash
</span></span></code></pre><p>sur macOS et Linux (qui reste en beta). Bien sûr, si balancer un script dans bash direct vous fait tiquer (normal), vous pouvez aussi chopper le DMG ou l'AppImage en release sur
<a href="https://github.com/poup-s/bbdump">GitHub</a>
et inspecter avant. Le code est sous licence MIT, avec une doc dédiée et une page Ko-fi si vous voulez soutenir le projet. Par contre, rien pour Windows pour l'instant.</p>
<p>Le projet est encore tout jeune puisque sorti fin mars de cette année donc si vous cherchez un outil ultra-stable pour une prod critique, attendez un peu. Mais pour vos projets perso, votre dev local, ou juste pour arrêter de râler sur pgAdmin, ça vaut clairement le coup d'œil.</p>
<p>Bref, un dev français de talent qui se lance en indé sur un créneau pourri d'outils vieillots, avec une vision cohérente et une intégration MCP propre, moi j'aime bien. Je pense que Poups mérite d'être soutenu sur ce coup-là, d'où mon article !</p>