---
title: "Il fabrique un robot qui joue tout seul au jeu du dinosaure de Chrome"
author: "Korben"
date: 2026-03-16T09:12:54.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "tutoriels-guides/tutoriels-avances"
  - "ATtiny85"
  - "Chrome"
  - "dinosaure"
rss_source: Blog
url: https://korben.info/il-fabrique-un-robot-qui-joue-tout-seul-au-jeu-du-dinosaure-de-chrome.html
note: 0
seen: false
---

<p>Un bricoleur a assemblé un petit montage à base d'ATtiny85 qui joue automatiquement au jeu du dinosaure caché dans Google Chrome. Le tout pour moins de 10 euros de composants et avec un microcontrôleur pas plus grand qu'un pouce.</p>
<h2 id="deux-capteurs-et-un-microcontrôleur-cest-tout">Deux capteurs et un microcontrôleur, c'est tout</h2>
<p>Le projet est signé Albert David, et le principe est assez malin. Une carte Digispark ATtiny85, qui coûte entre 2 et 5 euros, est branchée en USB sur un PC et se fait passer pour un clavier grâce au protocole HID. Pour le reste, vous avez deux modules LM393 photorésistants qui sont collés directement sur l'écran, le premier au niveau du sol pour voir les cactus, et le second plus haut pour voir les oiseaux.</p>
<p>C'est au passage de chaque obstacle que la luminosité change, et donc que le capteur s'active pour envoyer la touche espace ou la flèche du bas pour sauter et baisser la tête, le tout à travers le microcontrôleur, et seulement 8 ko de mémoire flash.</p>
<h2 id="un-système-qui-sadapte-à-la-vitesse-du-jeu">Un système qui s'adapte à la vitesse du jeu</h2>
<p>Encore plus fort, l'ensemble intègre un système de timing interactif, avec un firmware qui mesure la largeur des obstacles, et surtout conserve un historique de cinq mesures, pour estimer au mieux la vitesse du jeu.</p>
<p>Le délai entre la détection et l'appui sur la touche est recalculé en permanence, avec des bornes minimales et maximales pour éviter les ratés. Il y a aussi un délai de 400 millisecondes entre chaque action pour ne pas mitrailler les touches.</p>
<p>Côté calibration, il faut quand même un peu de patience. Les deux capteurs doivent être positionnés à 30-40 mm devant le dinosaure, et les potentiomètres des modules LM393 ajustés pour que le fond blanc de l'écran ne déclenche rien mais que les obstacles foncés soient bien détectés.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/C7ZEAQUwPDA?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Albert David recommande de tester sur une vingtaine d'obstacles avant de considérer le réglage comme bon. Et si le jeu passe en mode nuit, une commande JavaScript dans la console du navigateur empêche l'inversion de contraste qui fausserait les capteurs.</p>
<p>Bref, vous l'avez compris, c'est le genre de projet qui ne sert strictement à rien, et c'est pour ça qu'on aime bien. Avec moins de 10 euros de composants, un bout de code en C et deux capteurs de luminosité scotchés sur un écran, on obtient un système qui joue au jeu du dinosaure mieux que la plupart d'entre nous.</p>
<p>Le code est disponible sur GitHub pour ceux qui voudraient essayer,
<a href="https://prolinix.com/blog/chrome-dino-auto-player/">et vous avez tous les détails ici</a>
. Tout ceci rappelle quand même que ce petit jeu caché de Chrome, que Google avait glissé là pour meubler les coupures internet, continue de mobiliser les bidouilleurs du dimanche.</p>
<p>Sources :
<a href="https://hackaday.com/2026/03/16/attiny85-plays-the-chrome-dinosaur-game/">Hackaday</a>
,
<a href="https://prolinix.com/blog/chrome-dino-auto-player/">Prolinix</a>
</p>