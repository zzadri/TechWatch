---
title: "Iron Wolf - Wolfenstein 3D recréé en Rust et jouable en ligne"
author: "Korben"
date: 2026-04-15T07:23:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/langages-programmation"
  - "jeux-video/retrogaming-emulation"
  - "Id Software"
  - "retrogaming"
  - "WebAssembly"
  - "Wolfenstein 3D"
  - "Wolfenstein 3D navigateur"
rss_source: Blog
url: https://korben.info/iron-wolf-wolfenstein-3d-rust.html
note: 0
seen: false
---

<p><strong>Wolfenstein 3D</strong>, pour ceux qui n'étaient pas nés en 1992, c'est le FPS qui a tout lancé. Le jeu de Carmack et sa bande chez id Software, qui a directement mené à DOOM l'année suivante.</p>
<p>Eh bien un dev Rust vient de le recréer de zéro, et c'est 100% jouable dans le navigateur.</p>
<p>
<a href="https://github.com/Ragnaroek/iron-wolf">Iron Wolf</a>
, c'est donc le projet de Michael Bohn, un allemand, qui bosse sur ce truc depuis mai 2021, soit près de cinq ans. On n'est donc pas sur un portage vibe codé à l'arrache. C'est vraiment une réécriture complète.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iron-wolf-wolfenstein-3d-rust/iron-wolf-wolfenstein-3d-rust-2.png" alt="" loading="lazy" decoding="async">
<p><em>La version web d'Iron Wolf tournant dans le navigateur</em></p>
<p>Le bonhomme a carrément créé ses propres crates Rust pour émuler la carte VGA et la puce sonore OPL. J'ai d'abord cru qu'il réutilisait une lib existante, mais non, il a tout écrit from scratch en Rust. Bah ouais, développer ses propres librairies d'émulation hardware juste pour un side-project, what else ?? Je trouve que ça force le respect !</p>
<p>Le truc cool, c'est que la version shareware du jeu est incluse directement dans le dossier <code>testdata/</code> du repo. Du coup sur macOS, Linux ou Windows, un <code>git clone</code> + <code>just run-sdl-shareware</code> et hop, vous voilà dans les couloirs du château. Attention sur Ubuntu 22.04, faut avoir libsdl2-dev d'installé avec <code>apt install libsdl2-dev</code>, sinon la compilation plante avec une erreur cryptique. Par contre, si vous êtes sur la version Ubuntu 24.04, là ça passe direct. Et si vous avez les fichiers WAD du jeu complet qui traînent sur un vieux CD-ROM quelque part, ce sera encore mieux car la version web permet de les uploader pour jouer à l'intégrale.</p>
<p>Ça tourne donc en WebAssembly sur
<a href="https://wolf.ironmule.dev/">wolf.ironmule.dev</a>
, sans plugin, juste Chrome ou Firefox récent. Voilà, si vous vous demandiez si on peut encore
<a href="https://korben.info/fps-wolfenstein-3d.html">jouer au classique</a>
en 2026... la réponse est carrément oui !</p>
<p>Pour les curieux, le raycasting, cette technique de rendu qu'utilisait Wolfenstein 3D, est réimplémenté très fidèlement puisque le moteur de Michael dessine les murs comme le code de Carmack le faisait à l'époque... sauf que là ça tourne dans un onglet de navigateur. Vos fichiers de jeu sont également stockés localement via IndexedDB et un service worker gère le mode hors-ligne ce qui est très pratique pour jouer en avion ou quand on est chez Free (je décoooonnnne, humour humour).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iron-wolf-wolfenstein-3d-rust/iron-wolf-wolfenstein-3d-rust-3.png" alt="" loading="lazy" decoding="async">
<p>Le projet en est à sa version 0.9.0, sous licence GPL-3.0 et si les
<a href="https://korben.info/commander-keen-code-source-release-id-software.html">classiques d'id Software recréés par des passionnés</a>
vous branchent, sachez que
<a href="https://korben.info/doom-retro-portage-windows.html">DOOM aussi a ses portages</a>
bien sympas.</p>
<p>Bref, si la nostalgie du raycasting vous titille, allez faire un tour sur wolf.ironmule.dev.</p>