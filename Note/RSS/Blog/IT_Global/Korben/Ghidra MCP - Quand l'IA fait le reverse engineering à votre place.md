---
title: "Ghidra MCP - Quand l'IA fait le reverse engineering à votre place"
author: "Korben"
date: 2026-02-06T08:15:24.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "intelligence-artificielle/chatbots-llm"
  - "Ghidra"
  - "intelligence artificielle"
  - "mcp"
  - "reverse engineering"
  - "reverse engineering IA"
rss_source: Blog
url: https://korben.info/ghidra-mcp-reverse-engineering-ia.html
note: 0
seen: false
---

<p>Ghidra, le framework de reverse engineering open source de la NSA, est un outil que tous les analystes sécu utilisent au quotidien pour démonter des binaires. Sauf que voilà... quand vous passez des heures à renommer des fonctions, documenter des structures et tracer des cross-references à la main, ça finit par devenir un poil répétitif.</p>
<p>Du coup, un développeur a eu l'idée de coller un
<a href="https://korben.info/onemcp-serveur-mcp-anthropic-facile.html">serveur MCP</a>
(Model Context Protocol) directement sur Ghidra. &quot;Encore un wrapper IA bidon ??&quot;... mais non les amis car
<a href="https://github.com/bethington/ghidra-mcp">Ghidra MCP Server</a>
est un bridge Python + plugin Java qui expose pas moins de 110 outils d'analyse via le protocole MCP. Rien que ça.</p>
<p>Concrètement, ça veut dire que vous pouvez brancher Claude, ou n'importe quel outil compatible MCP, directement sur votre session Ghidra et lui demander de décompiler des fonctions, tracer des call graphs, renommer des variables en batch ou même créer des structures de données automatiquement.</p>
<p>Au niveau architecture, un plugin Java tourne dans Ghidra et expose une API REST sur localhost:8089, puis un bridge Python fait la traduction entre le protocole MCP et ces endpoints HTTP. Vous lancez Ghidra, vous activez le serveur via Tools &gt; GhidraMCP &gt; Start MCP Server, et hop, votre IA peut causer directement avec le décompileur.</p>
<p>Et c'est pas juste de la décompilation basique. Y'a de l'analyse de structures, de l'extraction de strings, du mapping mémoire complet, de la gestion de scripts Ghidra (plus de 70 scripts d'automatisation livrés avec le projet !) et même un système de documentation cross-binaire.</p>
<p>En gros, vous analysez un malware, vous documentez toutes les fonctions, et si vous tombez sur une variante plus tard, l'outil transfère automatiquement votre doc via un système de hash SHA-256 sur les opcodes. Plutôt chouette ! En revanche, ça marche pas si le code est fortement obfusqué... logique.</p>
<p>Bon, pour ceux qui connaissent déjà
<a href="https://korben.info/oghidra-dopage-a-lia-pour-ghidra-en-local.html">OGhidra</a>
(qui fait tourner des LLM en local dans Ghidra), Ghidra MCP Server c'est l'approche inverse. Au lieu d'embarquer l'IA dans Ghidra, c'est Ghidra qui s'ouvre à l'IA via un protocole standardisé. Du coup vous n'êtes pas limité à un seul modèle... Claude, GPT, Gemini, n'importe quel client MCP fait l'affaire.</p>
<p>Côté prérequis, faut Java 21, Maven 3.9+, Python 3.10+ et évidemment Ghidra 12.0.2. L'install se fait en quelques étapes : cloner le repo, pip install, copier les libs Ghidra dans lib/, compiler avec Maven et déployer le zip dans les extensions. Rien de bien sorcier si vous êtes déjà dans l'écosystème... sauf si vous êtes sous Windows, là faudra peut-être un peu galérer avec Maven.</p>
<p>Les opérations batch sont par exemple très intéressantes... Avec cette fonctionnalité, vous pouvez renommer 50 variables d'un coup, poser des commentaires sur toutes les fonctions d'un module, typer des paramètres en série.</p>
<p>Bref, si vous faites de l'analyse de binaires et que vous voulez arrêter de tout vous taper à la main, c'est le genre de combo reverse engineering + IA qui va vous faire gagner pas mal de temps !</p>