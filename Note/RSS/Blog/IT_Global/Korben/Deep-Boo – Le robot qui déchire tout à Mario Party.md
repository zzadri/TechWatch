---
title: "Deep-Boo – Le robot qui déchire tout à Mario Party"
author: "Korben"
date: 2026-01-13T13:47:49.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video"
  - "robots-drones-vehicules/robots-robotique"
rss_source: Blog
url: https://korben.info/deep-boo-ia-detection-fantome-mario-party-robot-switch.html
note: 0
seen: false
---

<p>Voici un projet open source qui risque de faire vibrer votre fibre de geek !</p>
<p>Prénommé Deep-Boo, ce robot joueur de Mario Party taillé comme Tibo In Shape est capable de manipuler physiquement une manette pour exploser ses adversaires.</p>
<p>Son créateur, Josh Mosier, a présenté ce petit bijou à l'
<a href="https://opensauce.com/">Open Sauce 2025</a>
et vous allez voir, c'est aussi bien pensé que c'est fun.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/deep-boo-ia-detection-fantome-mario-party-robot-switch/deep-boo-ia-detection-fantome-mario-party-robot-switch-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le robot Deep-Boo prêt à en découdre (
<a href="https://joshmosier.com/posts/deep-boo/deep-boo-hero.jpg">Source</a>
)</em></p>
<p>En fait, Deep-Boo ne se contente pas de tricher uniquement via du code car c'est un vrai automate physique qui &quot;voit&quot; l'écran grâce à une carte de capture HDMI et réagit ainsi presque instantanément à ce qui se passe. Pour arriver à cela, Josh a utilisé <strong>OpenCV</strong> pour analyser les formes et les couleurs en 720p / 60 FPS. Cela permet au robot de détecter les moments cruciaux du gameplay, comme les compte à rebours ou les positions des joueurs.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/eds4vgwhJgQ?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Côté matériel, on est sur de la bidouille high level puisque l'automate de Josh embarque un microcontrôleur <strong>ESP32</strong> qui pilote 12 solénoïdes pour presser les boutons A, B, X, Y et les gâchettes. Mais le vrai défi, c'était le joystick car pour contrôler les mouvements à 360°, il a fallu concevoir un manipulateur parallèle sphérique (SPM) avec des moteurs pas à pas NEMA 17.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/deep-boo-ia-detection-fantome-mario-party-robot-switch/deep-boo-ia-detection-fantome-mario-party-robot-switch-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'architecture complexe du manipulateur de joystick (
<a href="https://joshmosier.com/posts/deep-boo/cad-model.png">Source</a>
)</em></p>
<p>Et là où ça devient vraiment impressionnant, c’est son utilisation de la fonction <strong>StallGuard</strong> des drivers TMC2209. Ça permet de calibrer les moteurs sans interrupteurs physiques en détectant quand le joystick arrive en butée. C’est pas idiot et ça offre une sacrée précision pour les mini-jeux qui demandent de la finesse.</p>
<p>Josh a même prévu un &quot;Puppet System&quot; c'est à dire un troisième Joy-Con connecté en Bluetooth à l'ESP32 pour reprendre la main manuellement si besoin. C’est un peu comme
<a href="https://korben.info/mario-boite-carton.html">Mario Party en carton</a>
mais avec des muscles en métal et un cerveau dopé à la vision intelligente.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/deep-boo-ia-detection-fantome-mario-party-robot-switch/deep-boo-ia-detection-fantome-mario-party-robot-switch-2.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le stand Deep-Boo a attiré les foules à l'Open Sauce 2025 (
<a href="https://joshmosier.com/posts/deep-boo/booth-setup.jpg">Source</a>
)</em></p>
<p>Lors de l'évènement, le petit fantôme mécanique a même défié
<a href="https://www.youtube.com/channel/UCrPseYLGpNygVi34QpGNqpA">Ludwig</a>
, le célèbre streameur, au jeu de &quot;button mashing&quot; Domination.</p>
<p>Et sans surprise, notre petit robot l'a complétement fumé avec un score de 99 !</p>
<p>Voilà et comme vous connaissez mon amour pour le DIY, vous vous doutez bien que je ne vais pas vous laisser comme ça sur votre faim ! En effet, si vous voulez vous lancer dans la robotique de gaming, tout le code et les fichiers de design sont dispo sur
<a href="https://github.com/joshmosier/Deep-Boo">le dépôt GitHub de Josh</a>
!</p>
<p>
<a href="https://joshmosier.com/posts/deep-boo">Source</a>
</p>