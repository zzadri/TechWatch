---
title: "Un bidouilleur fait tourner des DVD sur Dreamcast avec un Raspberry Pi"
author: "Korben"
date: 2026-04-07T10:04:30.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/raspberry-pi"
  - "jeux-video/retrogaming-emulation"
  - "Dreamcast"
  - "DVD"
  - "raspberry"
rss_source: Blog
url: https://korben.info/un-bidouilleur-fait-tourner-des-dvd-sur-dreamcast-avec-un-raspberry-pi.html
note: 0
seen: false
---

<p>Un développeur connu sous le pseudo ThroatyMumbo vient de réussir un petit exploit : faire lire des DVD à une Sega Dreamcast, la console qui n'a jamais eu droit à cette fonctionnalité.</p>
<p>Sa méthode passe par un Raspberry Pi 5, un Raspberry Pi Pico 2 et le port manette de la console, le tout sans la moindre modification hardware. Vingt-cinq ans après, la Dreamcast peut enfin lire des DVD.</p>
<h2 id="une-vieille-histoire-de-format">Une vieille histoire de format</h2>
<p>La Dreamcast est sortie en 1998 au Japon et utilisait le format GD-ROM, un disque propriétaire développé avec Yamaha capable de stocker jusqu'à 1 Go de données. Sega avait choisi ce format pour éviter les frais de licence du DVD Forum et garder des coûts de production proches de ceux d'un CD classique.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/ntj_tUHKAaE?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Sur le papier, la console avait les capacités techniques pour lire des DVD, mais Sega n'a jamais franchi le pas. Un prototype d'extension DVD avait même été montré à l'E3 2000 avant de disparaitre dans les cartons. En face, Sony sortait la PlayStation 2 avec un lecteur DVD intégré, et on connait la suite.</p>
<h2 id="du-raspberry-pi-et-un-faux-accessoire-photo">Du Raspberry Pi et un faux accessoire photo</h2>
<p>Le montage imaginé par ThroatyMumbo est malin. Un Raspberry Pi 5 est connecté à un lecteur DVD USB externe et se charge d'encoder la vidéo en temps réel. Cette vidéo est ensuite envoyée par USB à un Raspberry Pi Pico 2, qui se fait passer pour un DreamEye, le petit accessoire photo que Sega avait sorti au Japon en 2000.</p>
<p>Le Pico 2 communique avec la Dreamcast via le bus Maple, le protocole qu'utilise la console pour ses manettes et périphériques. La Dreamcast croit recevoir des images d'une caméra, alors qu'elle affiche le contenu d'un DVD. Le créateur admet lui-même que le résultat est &quot;un peu bancal&quot;, mais la vidéo de démonstration montre que ça tourne avec un DVD d'Aqua Teen Hunger Force.</p>
<h2 id="tout-passe-par-le-port-manette">Tout passe par le port manette</h2>
<p>Le gros avantage de cette bidouille, c'est qu'elle ne demande aucune modification de la Dreamcast. Tout transite par le port manette, ce qui veut dire que n'importe quelle console en état de marche peut en profiter.</p>
<p>Le code source et les instructions sont disponibles sur GitHub. Ça reste du bricolage : il faut un Raspberry Pi 5, un Pico 2, un lecteur DVD USB et de quoi relier tout ça. Pas le genre de truc qu'on met en place en deux minutes.</p>
<p>C'est quand même rigolo de se dire que la Dreamcast aura attendu plus de vingt-cinq ans pour lire un DVD. Sega avait prévu un accessoire dédié qui n'est jamais sorti, et c'est un bidouilleur avec deux Raspberry Pi qui finit par régler la question.</p>
<p>L'idée de détourner un accessoire photo japonais en lecteur DVD, c'est bien trouvé. Pas sûr que Sega aurait apprécié la méthode, mais bon, le résultat est là.</p>
<p>Source :
<a href="https://www.thedreamcastjunkyard.co.uk/2026/04/a-dreamcast-dvd-player-appears.html">The Dreamcast Junkyard</a>
</p>