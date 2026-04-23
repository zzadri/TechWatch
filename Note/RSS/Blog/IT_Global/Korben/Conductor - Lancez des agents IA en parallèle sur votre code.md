---
title: "Conductor - Lancez des agents IA en parallèle sur votre code"
author: "Korben"
date: 2026-03-10T09:46:07.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "developpement/outils-developpement"
  - "intelligence-artificielle/chatbots-llm"
  - "Claude Code"
  - "vibe coding"
rss_source: Blog
url: https://korben.info/conductor-build.html
note: 0
seen: false
---

<p>
<a href="https://www.conductor.build/">Conductor</a>
c'est une app macOS qui vous permet de lancer plusieurs agents Claude Code ou Codex en parallèle, chacun dans son propre worktree git histoire qu'ils ne se marchent pas dessus. Le tout est développé par Melty Labs, et c'est gratuit !! (enfin l'app en elle-même, parce que les tokens Claude ou OpenAI, c'est vous qui casquez hein ^^).</p>
<p>Vous ouvrez l'app, Cmd+N pour créer un workspace, et ensuite, chaque agent bosse dans son coin sur sa propre branche git comme ça y'a pas de conflits ni de merge foireux au milieu du boulot ! Et grâce à cet outil, vous voyez d'un coup d'oeil ce que chacun fabrique via le diff viewer intégré. Ensuite, vous reviewez, et quand c'est bon vous mergez. Comme un chef de chantier en fait, sauf que vos ouvriers ce sont des LLM.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/conductor-build/conductor-build-1.webp" alt="" loading="lazy" decoding="async">
<p>Y'a plus qu'à vous acheter un casque !</p>
<p>Côté modèles, ça supporte Claude Code (avec votre clé API ou votre abonnement Pro/Max) et Codex d'OpenAI. Et la dernière release a d'ailleurs ajouté GPT-5.4 tout frais démoulé.</p>
<p>Le truc cool c'est surtout cette isolation par git worktrees. Chaque workspace étant un worktree séparé, les agents peuvent ainsi modifier des fichiers en parallèle sans se marcher dessus. Si vous avez déjà essayé de faire tourner deux
<a href="https://korben.info/vibe-coding-tue-open-source.html">sessions de vibe coding</a>
en même temps sur le même repo... vous savez que ça finit en général en carnage.</p>
<p>Attention quand même, chaque worktree bouffe de l'espace disque (genre un repo de 2 Go × 5 agents, ça peut piquer...) donc pensez-y si votre repo est un peu lourd.</p>
<p>L'app intègre aussi le MCP (Model Context Protocol) pour brancher des outils externes, des slash commands custom, et un système de checkpoints qui permet de revenir en arrière tour par tour si un agent part en vrille (genre il supprime un fichier critique... ça arrive). Perso, le diff viewer c'est pas mal du tout car ça évite de jongler entre le terminal et VS Code.</p>
<p>Après dommage que ce soit pour macOS seulement. Déso hein ^^</p>
<p>En tout cas, vu le rythme des mises à jour, c'est un projet qui avance vite. Des devs de chez Linear, Vercel, Notion ou Stripe l'utilisent déjà, et ça a l'air suffisamment solide pour de la prod (mais testez bien avant hein, faut jamais me faire confiance ^^).</p>