---
title: "Cette mini borne d'arcade tient dans la main et tourne sur un ESP32"
author: "Korben"
date: 2026-03-11T16:54:00.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "hardware-diy/impression-3d"
  - "jeux-video/retrogaming-emulation"
  - "emulateur"
  - "emulation"
  - "ESP32"
  - "galagino"
  - "PacMan"
rss_source: Blog
url: https://korben.info/cette-mini-borne-darcade-tient-dans-la-main-et-tourne-sur-un-esp32.html
note: 0
seen: false
---

<p>Un développeur a créé Galagino, un émulateur open source qui fait tourner Pac-Man, Galaga, Donkey Kong et trois autres classiques de l'arcade sur un simple microcontrôleur ESP32. Le projet est gratuit, le code est sur GitHub, et avec quelques composants et une imprimante 3D vous fabriquez votre propre mini borne pour presque rien.</p>
<h2 id="six-jeux-darcade-sur-une-puce-à-quelques-euros">Six jeux d'arcade sur une puce à quelques euros</h2>
<p>Galagino est un projet open source développé par Till Harbaum. Le principe : émuler des jeux d'arcade des années 80 sur un ESP32, cette petite puce à double coeur cadencée à 240 MHz qui coûte une poignée d'euros. Et ça ne rigole pas côté catalogue, puisque six titres sont pris en charge : Galaga, Pac-Man, Donkey Kong, Frogger, Dig Dug et 1942.</p>
<p>L'émulation est complète, avec le son et la vidéo, le tout affiché sur un petit écran TFT de 320 x 240 pixels en 2 à 3 pouces. Pour les contrôles, cinq boutons poussoirs suffisent, ou un joystick si vous préférez. Le Galaga d'origine tournait sur trois processeurs Z80 plus deux puces dédiées aux entrées et au son. Ici, l'ESP32 gère tout seul, et les deux coeurs sont quand même bien sollicités.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/Nz3LRrY3Ukw?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<h2 id="le-cheap-yellow-display-la-solution-tout-en-un">Le Cheap Yellow Display, la solution tout-en-un</h2>
<p>Pour ceux qui ne veulent pas souder trop de composants, il existe une alternative bien pratique : le Cheap Yellow Display. C'est une carte ESP32 qui intègre l'écran tactile, un slot micro SD, la sortie audio et le module Wi-Fi dans un seul boîtier.</p>
<p>Il suffit d'y brancher une manette Nunchuk de Wii et un petit haut-parleur pour avoir une borne fonctionnelle. La communauté a aussi développé des boîtiers imprimés en 3D, et certains ont même recyclé des coques de mini bornes My Arcade du commerce pour y glisser la carte.</p>
<p>Tout le code, les fichiers 3D et les instructions de montage sont disponibles sur GitHub. Seul détail : les ROM des jeux ne sont pas incluses pour des raisons évidentes de licence, il faut les fournir vous-même.</p>
<h2 id="un-projet-qui-vit-bien">Un projet qui vit bien</h2>
<p>Le dépôt GitHub compte 186 commits et une communauté active qui continue d'ajouter des jeux comme Frogger, Dig Dug et 1942, et des contributeurs travaillent sur d'autres titres. Davide Gatti, du collectif Survival Hacking, a même porté le projet sur Arduino et publié un tuto vidéo complet pour fabriquer sa borne de A à Z. Le résultat tient dans la paume de la main, avec en option un éclairage LED pour le fronton, histoire de faire comme les vraies.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/a3-wctRAIds?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>C’est trop chouette, et c’est exactement le genre de projet qui donne envie de ressortir le fer à souder. Pour quelques euros de composants et un week-end de bricolage, vous repartez avec une borne d'arcade de poche qui fait tourner Pac-Man et Donkey Kong.</p>
<p>Difficile de faire plus chouette en termes de rapport effort/résultat. Et puis le fait que la communauté continue d'ajouter des jeux montre que le projet a de beaux restes devant lui. En tout cas, si vous cherchiez une excuse pour acheter un ESP32, la voilà.</p>
<p>Source :
<a href="https://www.hackster.io/news/galagino-miniature-esp32-arcade-emulator-b1c34feccd9a">Hackster</a>
</p>