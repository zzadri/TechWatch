---
title: "La Xbox One enfin hackée après 12 ans d'invincibilité"
author: "Korben"
date: 2026-03-16T11:40:09.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "jeux-video/consoles"
  - "piratage console"
  - "reverse engineering"
rss_source: Blog
url: https://korben.info/xbox-one-hack-boot-rom-unhackable.html
note: 0
seen: false
---

<p>La <strong>Xbox One</strong> n'a jamais été hackée ! Eh oui, depuis 2013, la console de Microsoft narguait la communauté du
<a href="https://korben.info/splinter-cell-xbox-lin-format-reverse-engineering.html">reverse engineering</a>
pendant que les PlayStation, les Switch et autres 3DS tombaient les unes après les autres. Microsoft la décrivait même comme &quot;<em>le produit le plus sécurisé jamais créé</em>&quot; mdrrrr.</p>
<p>Bon bah c'est fini comme vous vous en doutez car à la conférence
<a href="https://www.youtube.com/watch?v=FTFn4UZsA5U">RE//verse 2026</a>
à Orlando, Markus &quot;doom&quot; Gaasedelen a réussi à exécuter du code arbitraire sur le boot ROM de la console, autrement dit c'est un hack hardware impossible à corriger.</p>
<p>Du coup, comment on casse un truc réputé incassable ?</p>
<p>Eh bien toute la sécurité de la Xbox One repose sur un minuscule processeur ARM Cortex R4, le Platform Security Processor (PSP), planqué dans un coin du SoC AMD.</p>
<p>Ce PSP contient un boot ROM gravé directement dans le silicium... et <strong>c'est le seul composant que Microsoft ne peut pas mettre à jour</strong>. L'architecte de la sécu Xbox, Tony Chen, l'avait dit lui-même en 2019 : &quot;<em>le seul bug logiciel dont on ne peut pas se remettre, c'est un bug dans le boot ROM</em>&quot;.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xbox-one-hack-boot-rom-unhackable/xbox-one-hack-boot-rom-unhackable-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le die shot du SoC Xbox One. Le PSP est planqué tout en bas à droite.</em></p>
<p>Sauf que Markus n'a pas cherché de bug logiciel, parce y'en a pas. Le code du boot ROM est linéaire, hyper audité, sans la moindre faille. Du coup, il est passé par le hardware avec du voltage glitching.</p>
<p>Le principe c'est de faire s'effondrer brièvement le rail d'alimentation du processeur (en gros, on colle un
<a href="https://fr.wikipedia.org/wiki/Transistor_%C3%A0_effet_de_champ_%C3%A0_grille_m%C3%A9tal-oxyde">MOSFET</a>
sur le rail et on tire la tension vers le bas pendant 100 à 200 nanosecondes) pour corrompre l'exécution d'une instruction. Et Microsoft avait quand même blindé le truc en prenant soin de ne pas mettre de pin reset accessible, pas d'UART, pas de JTAG, pas de post codes de diagnostic (désactivés par des fusibles), et surtout 37 stalls randomisés qui décalent le timing du boot à chaque démarrage. En gros, c'est comme essayer de crocheter une serrure dans le noir, avec des moufles, et la serrure qui change de position toutes les 2 secondes.</p>
<p>D'ailleurs, c'était la première fois que Markus faisait du glitching de sa vie. Au début, il a galéré sur le mauvais rail d'alimentation (la tension 1.8V, finalement un cul-de-sac) avant de trouver le bon (le North Bridge core). Et là, en balançant ses impulsions de voltage au bon moment, il a réussi à activer les post codes que Microsoft avait désactivés par fusibles. Premier signe que la bête était vulnérable !!!!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xbox-one-hack-boot-rom-unhackable/xbox-one-hack-boot-rom-unhackable-2.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le setup de glitching : oscilloscope, carte mère Xbox One et fils partout.</em></p>
<p>Ensuite, il a ciblé les opérations memcopy du boot ROM, là où les données contrôlées par l'attaquant transitent dans les registres du processeur. Un glitch bien placé pendant un memcopy, et hop, le pointeur d'instruction du processeur part n'importe où. Résultat : 0x41414141 qui sort sur le bus I2C, la preuve qu'on contrôle l'exécution du boot ROM !</p>
<p>Bon par contre, il était enfermé dans un &quot;user jail&quot;, une sandbox ARM avec seulement quelques Ko de code accessible. Et c'est pas si simple d'en sortir.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xbox-one-hack-boot-rom-unhackable/xbox-one-hack-boot-rom-unhackable-3.jpg" alt="" loading="lazy" decoding="async">
<p><em>0x41414141 sur le bus I2C. ROP'd OUT MY POST CODE !</em></p>
<p>Et là, coup de génie du mec : un double glitch sur le même boot.</p>
<p>Le premier casse la boucle d'initialisation du MPU (la protection mémoire ARM, les 12 régions qui créent les jails), le second hijack le pointeur d'instruction pendant le memcopy.</p>
<p>Combiner les deux sur un seul démarrage, c'est du genre 1 chance sur 100 par glitch, soit environ 1 sur 10 000 pour le combo donc autant dire qu'il faut laisser tourner la machine des centaines de milliers de fois. Mais ça marche !! Avec le MPU désactivé et le pointeur d'instruction sous son contrôle, Markus obtient alors l'exécution de code en mode superviseur, avant même que le boot ROM n'ait vérifié les signatures ou déchiffré quoi que ce soit.</p>
<p>Bingo !! Et les conséquences sont radicales puisque grâce à ce hack, il peut maintenant déchiffrer tous les jeux, les firmwares et les mises à jour passés, présents et futurs.</p>
<p>Il peut aussi dé-pairer les NAND et lecteurs optiques pour la réparation. Et comme c'est gravé dans le silicium, c'est
<a href="https://korben.info/xbox360-reset-glitch-hack.html">impatchable, comme le Reset Glitch Hack de la 360</a>
à l'époque. Pour l'instant, ça concerne uniquement le modèle
<a href="https://korben.info/moddeur-fait-tourner-halo-2-720p-xbox-origine.html">Xbox One</a>
Fat de 2013.</p>
<p>Ah et petit détail croustillant.... Microsoft avait prévu des moniteurs anti-glitch dans le SoC pour détecter les perturbations de voltage, mais sur les premières révisions ils n'arrivaient pas à les stabiliser, du coup ils les ont désactivés par fusibles. Pas de bol. Après sur les modèles suivants (One S, One X) ils sont activés, mais Markus pense que ses techniques pourraient quand même être adaptées.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xbox-one-hack-boot-rom-unhackable/xbox-one-hack-boot-rom-unhackable-4.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le boot flow du PSP. Le hijack se produit à l'étape 4, avant toute vérification crypto.</em></p>
<p>Le plus dingue c'est que le hack en version finale ne nécessite que 3 fils soudés sur la carte mère ! Tout le reste, les dizaines de sondes à crochet, l'oscilloscope 4 voies, l'analyseur logique branché sur le bus I2C et les GPIO, c'était juste pour comprendre ce qui se passait.</p>
<p>Et le fait qu'il ait construit un émulateur du boot ROM avec l'aide de l'IA pour étudier le comportement du processeur, je trouve ça encore plus incroyable !</p>
<p>Bref, je vous laisse avec la conf en intégralité pour les plus motivés :</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/FTFn4UZsA5U?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Et voilà comment 12 ans de &quot;IMPOSSIBLE À PIRATER&quot; se termine avec 3 fils soudés et 2 glitches bien placés. Pas mal !</p>
<p>Bravo Markus !</p>