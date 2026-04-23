---
title: "ArcadeGPU - Un moteur de jeu rétro qui tourne dans votre navigateur"
author: "Korben"
date: 2026-02-06T15:24:50.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/retrogaming-emulation"
  - "moteur de jeu"
  - "OpenSource"
  - "retrogaming"
  - "WebGPU"
rss_source: Blog
url: https://korben.info/arcadegpu-moteur-jeu-retro-web.html
note: 0
seen: false
---

<p>Et si les meilleures techniques de game dev des années 2000 revenaient dans votre navigateur ?</p>
<p><strong>ArcadeGPU</strong>, c'est un moteur de jeu complet qui tourne dans le navigateur grâce à WebGPU. C'est une vraie architecture de jeu avec walkmesh, hitbox BSP, moteur de script, pipeline graphique à la PS1 et même la physique Jolt intégrée (un moteur open source utilisé dans certains gros jeux).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/arcadegpu-moteur-jeu-retro-web/arcadegpu-moteur-jeu-retro-web-2.png" alt="" loading="lazy" decoding="async">
<p>Le truc c'est que le dev derrière, un Français qui bosse seul sur le projet, a pris le parti de ressusciter des techniques qu'on utilisait entre 2000 et 2010 dans le développement de jeux. Du walkmesh pour la navigation des personnages, du hitmesh pour les collisions, du draw call only pour le rendu... Des trucs qu'on ne voit quasi plus dans les moteurs modernes, et pourtant c'est redoutablement efficace pour les indés. Bon, après faut quand même être à l'aise avec TypeScript et la stack web, car c'est pas un moteur drag-and-drop à la GameMaker.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/arcadegpu-moteur-jeu-retro-web/arcadegpu-moteur-jeu-retro-web-1.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Car oui comme tout est en TypeScript, vous codez votre jeu comme une app web classique. Vous modifiez votre fichier main.ts, le jeu se rafraîchit en temps réel sans avoir à tout relancer. Et vous avez toute la pile web en support, du Web Audio API au CSS en passant par les workers async... Quand on compare avec les 45 secondes de build d'un projet Unity moyen, y'a pas photo.</p>
<p>Y'a aussi un paquet de démos jouables directement sur
<a href="https://aliyah-corp.github.io/">le site du projet</a>
et c'est pas des petits exemples bidon avec un cube qui tourne. Vous y trouverez de vrais prototypes de jeux complets, de la 2D rétro au rendu toon 3D avec ombres volumétriques. L'idée c'est de fournir des templates prêts à l'emploi, vous choisissez le gameplay qui vous correspond et vous partez de là (plutôt que de tout repenser from scratch).</p>
<p>D'ailleurs y'a même
<a href="https://sokobanversus-3117d.web.app/">un jeu en bêta</a>
développé avec le moteur, un Sokoban versus, pour voir ce que ça donne en conditions réelles.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/arcadegpu-moteur-jeu-retro-web/arcadegpu-moteur-jeu-retro-web-3.png" alt="" loading="lazy" decoding="async">
<p>Côté compatibilité, ça tourne sur les navigateurs qui gèrent WebGPU (Chrome, Edge, et Firefox en mode expérimental avec le flag dom.webgpu.enabled). Pour Safari et mobile, c'est plus aléatoire pour le moment donc attention si votre cible c'est iOS. Le projet est open source sous licence Apache 2.0, dispo sur
<a href="https://sourceforge.net/projects/arcadegpu/">SourceForge</a>
et ça pèse environ 400 Mo avec toutes les démos.</p>
<p>Et le rendu... C'est du pipeline PSX complet avec ombrage toon, volumes d'ombre, le tout dans le navigateur. Pour les nostalgiques de la première PlayStation, c'est un peu la papillote Révillon version code (oui ça change des madeleines ^^), sauf que là, c'est vous qui créez les jeux.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/arcadegpu-moteur-jeu-retro-web/arcadegpu-moteur-jeu-retro-web-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Voilà, je trouve que cette approche old-school mixée avec la techno web moderne c'est pas bête du tout. Si vous êtes dev indé et que les usines à gaz style Unity ou Unreal vous donnent des boutons, ça vaut peut-être le coup d'aller jeter un oeil. Seul bémol, la doc est encore un peu légère, donc faudra fouiller dans les exemples pour comprendre l'API.</p>
<p>Bref, merci à Slay3r pour le partage et bravo !</p>