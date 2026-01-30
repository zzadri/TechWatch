---
title: "Ce furieux fait booter son PC depuis un disque vinyle"
author: "Korben"
date: 2026-01-24T17:57:32.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "jeux-video/retrogaming-emulation"
  - "boot vinyle"
  - "FreeDOS"
  - "IBM PC"
  - "insolite"
rss_source: Blog
url: https://korben.info/pc-boot-avec-vinyl-platine-disque.html
note: 0
seen: false
---

<p>Alors là, on touche au sublime les amis ! Parce que si vous pensiez avoir tout vu en matière de boot insolite, genre clé USB, PXE, disquette 5 pouces 1/4... Pffff, vous n'êtes qu'une bande de petits joueurs.</p>
<p>Jozef Bogin,
<a href="https://boginjr.com/it/sw/dev/vinyl-boot/">ce bidouilleur de génie</a>
, que dis-je, ce GOAT, a réussi à faire booter un IBM PC (le modèle 5150, une légende !!) directement depuis... <strong>un disque vinyle</strong>. Oui, un bon vieux 45 tours.</p>
<p>Regardez-moi ça comme c'est beau :</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/bqz65_YfcJg?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Pour réussir ce tour de force, il a gravé une image disque de 64 Ko (contenant un noyau FreeDOS minimal) sous forme de signal audio analogique sur le disque. Grâce à une ROM personnalisée (une puce 2364 insérée dans le socket d'extension du BIOS) qui remplace le code de boot habituel, le PC récupère le son via son interface cassette. Les routines du BIOS se chargent ensuite de la démodulation du signal pour charger le tout en RAM. C'est un peu comme
<a href="https://korben.info/emuler-disquette-cle-usb.html">émuler une disquette avec une clé USB</a>
, mais en version hardcore analogique.</p>
<p>Techniquement, c'est un boulot de dingue. Il a dû adapter l'égalisation audio pour compenser la
<a href="https://fr.wikipedia.org/wiki/%C3%89galisation_RIAA">courbe RIAA</a>
du vinyle, gérer les niveaux au millimètre et coder ce fameux bootloader spécifique pour que la magie opère.</p>
<p>Perso, je trouve ça assez poétique et le son n'est pas sans rappeler celui de nos bons vieux modem 56k. Bref, si vous avez une platine et un PC IBM 5150 qui traînent, vous savez ce qu'il vous reste à faire.</p>
<p>Pour les autres, la vidéo suffira largement ^^.</p>