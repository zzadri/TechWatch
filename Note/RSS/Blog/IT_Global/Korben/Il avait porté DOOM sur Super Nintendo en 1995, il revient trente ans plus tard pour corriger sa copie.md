---
title: "Il avait porté DOOM sur Super Nintendo en 1995, il revient trente ans plus tard pour corriger sa copie"
author: "Korben"
date: 2026-03-16T16:10:49.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy"
  - "jeux-video/retrogaming-emulation"
  - "Doom"
  - "raspberry"
  - "SNES"
  - "supernes"
rss_source: Blog
url: https://korben.info/il-avait-porte-doom-sur-super-nintendo-en-1995-il-revient-trente-ans-plus-tard-pour-corriger-sa-copie.html
note: 0
seen: false
---

<p>Randal Linden est le développeur qui avait réussi l'exploit de faire tourner DOOM sur la Super Nintendo en 1995. Trente ans plus tard, il s’est associé à Limited Run Games pour ressortir une version améliorée sur cartouche, avec un processeur Raspberry Pi caché à l'intérieur.</p>
<p>Dans un long échange accordé à Kotaku, il revient sur ce projet un peu fou et sur les coulisses techniques du portage.</p>
<h2 id="reverse-engineerer-son-propre-code-trente-ans-après">Reverse-engineerer son propre code, trente ans après</h2>
<p>À l'époque, Linden bossait chez Sculptured Software, un studio basé à Salt Lake City. L'idée de départ était assez artisanale : acheter des cartouches Star Fox en magasin, les ouvrir, et remplacer la ROM par de la RAM pour tester les capacités de la puce Super FX. Le prototype a suffisamment impressionné ses supérieurs pour qu'ils aillent le présenter directement à id Software au Texas. Le feu vert a suivi.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/DBdBeMfcL04?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le portage de 1995, c'était un moteur entièrement reconstruit de zéro, sans une seule ligne de code d'id Software. Linden avait créé son propre assembleur, son propre linker et son propre débogueur. Mais les contraintes hardware de la SNES avaient imposé des sacrifices : un framerate poussif, pas de textures au sol et au plafond, des niveaux modifiés, et le quatrième épisode supprimé.</p>
<p>Quand Audi Sorlie, de Limited Run Games, lui a posé la question de savoir s'il referait les choses différemment, Linden a répondu qu'il avait « plein d'idées » mais que personne ne lui avait jamais demandé d'y retoucher. Jusqu'à maintenant.</p>
<h2 id="une-puce-raspberry-pi-qui-se-fait-passer-pour-un-super-fx">Une puce Raspberry Pi qui se fait passer pour un Super FX</h2>
<p>La solution technique est plutôt marrante. La cartouche embarque un Raspberry Pi RP2350 qui émule le processeur Super FX. Comme l'explique Linden à Kotaku, « la Super Nintendo ne sait pas qu'elle ne parle pas à un vrai Super FX ».</p>
<p>Le code est quasiment identique à ce qu'il écrirait pour la puce d'origine, mais avec des performances largement supérieures.</p>
<p>Le résultat : circle strafing, framerate amélioré, support du rumble, et les quatre épisodes complets enfin disponibles sur SNES. Linden admet aussi avoir dû reverse-engineerer son propre code vieux de trente ans. « C'était assez compliqué, une partie du code. Je me suis dit : wow, j'étais vraiment intelligent à l'époque. »</p>
<h2 id="bethesda-a-dit-oui-sans-trop-hésiter">Bethesda a dit oui sans trop hésiter</h2>
<p>Côté droits, il fallait quand même convaincre Bethesda, propriétaire de la licence DOOM. Selon Sorlie, la réaction initiale a été plutôt incrédule : « Vous voulez retourner développer pour la Super Nintendo ? Genre, pour de vrai ? » </p>
<p>Mais le retour de Linden sur le projet et les premiers prototypes ont suffi à convaincre. « Ils étaient aussi enthousiastes que nous. »</p>
<p>C'est le genre d'histoire qui rappelle que derrière les jeux vidéo, il y a parfois des parcours assez improbables. Linden n'avait pas pu appeler id Software pour pitcher son idée en 1995, il avait dû bricoler un prototype avec des cartouches Star Fox achetées en magasin, et trente ans plus tard il se retrouve à relire du code assembleur qu'il ne comprend plus lui-même.</p>
<p>Le projet a un côté un peu absurde, mais c'est aussi ce qui le rend attachant. Reste à voir si les fans de retrogaming seront au rendez-vous, mais vu que l'édition collector limitée à 666 exemplaires s'est déjà envolée, on a un début de réponse.</p>
<p>Source :
<a href="https://kotaku.com/doom-snes-id-shooter-original-limited-run-2000678756">Kotaku</a>
</p>