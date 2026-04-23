---
title: "Street Fighter II - Une faute d'orthographe corrigée grâce au mollet de Guile"
author: "Korben"
date: 2026-02-12T10:53:41.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/retrogaming-emulation"
  - "multimedia-culture/culture-geek"
  - "arcade"
  - "borne arcade"
  - "Capcom"
  - "rétro gaming"
  - "Street Fighter"
rss_source: Blog
url: https://korben.info/street-fighter-2-typo-jambe-guile.html
note: 0
seen: false
---

<p>Street Fighter II, c'est dans l'esprit de la plupart d'entre nous, 1991, les salles d'arcade qui puent la clope et les pièces de 10 francs qui s'enchaînent... et surtout un écran-titre qui affiche &quot;<strong>WORLD WARRIER</strong>&quot; au lieu de &quot;WORLD WARRIOR&quot;. Ouais, y'avait une coquille dans le titre d'un des jeux de baston les plus légendaires de l'univers et personne ne l'a jamais su !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/street-fighter-2-typo-jambe-guile/street-fighter-2-typo-jambe-guile-2.png" alt="" loading="lazy" decoding="async">
<p>Magnifique hein ?</p>
<p>Le problème, c'est que sur les bornes d'arcade Capcom CPS1, les graphismes sont gravés dans des puces ROM. Du vrai read-only qu'on grave une bonne fois pour toutes et qu'on ne touche PLUS après. Et en 1991, les puces ROM coûtaient un bras et les délais de production étaient assez dingues... Donc impossible pour Capcom de faire regraver quoi que ce soit même pour une malheureuse lettre.</p>
<p>Nous sommes donc toujours en 1991, à 3 jours de la deadline pour livrer le code ROM (la seule puce encore modifiable à ce stade) et quelqu'un se rend compte du bug.</p>
<p>Horreur malheur ! C'est la panique et tout le monde se met à réfléchir à une solution... Quand soudain, un hack digne des plus belles bidouilles émerge de ces cerveaux endoloris par tant de travail.</p>
<p>Il faut savoir que sur le CPS1, chaque graphisme est découpé en &quot;tiles&quot; c'est à dire des petits carrés de 8×8 pixels. Et le truc important, c'est que chaque tile ne contient pas une lettre entière mais un BOUT de lettre. Le logo &quot;WORLD WARRIOR&quot;, c'est en fait une mosaïque de 16 tiles collées les unes aux autres, et chaque carreau contient des fragments des lettres voisines. Impossible donc de toucher à ces carreaux une fois gravés dans la ROM graphique... Mais la table qui dit &quot;<em>colle CE carreau ICI avec CETTE palette de couleurs</em>&quot;... ça, c'était encore modifiable dans la ROM code.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/street-fighter-2-typo-jambe-guile/street-fighter-2-typo-jambe-guile-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le hic c'est qu'il fallait composer avec les tiles existantes car pas moyen d'en créer de nouvelles !</p>
<p>Du coup, l'équipe s'est mise à passer au crible les centaines de tiles déjà gravées dans la ROM, une par une, pour trouver des morceaux compatibles avec les bonnes lettres. Et bonne nouvelle... pour certaines tiles, ils ont trouvé des équivalents dans le mot &quot;WORLD&quot; sur l'écran-titre. Et en réarrangeant le puzzle, ils ont réussi à afficher presque tout &quot;WARRIOR&quot; correctement. Presque. Parce que le &quot;i&quot;, lui, ressemblait maintenant à un &quot;L&quot; minuscule... il manquait le point mes amis !!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/street-fighter-2-typo-jambe-guile/street-fighter-2-typo-jambe-guile-4.png" alt="" loading="lazy" decoding="async">
<p>Et c'est là que ça devient du grand art car pour dessiner ce petit point, il leur fallait un carreau avec quasi rien dessus. Ils ont fini par repérer la tile 0x96 dans la ROM... un carré de 8×8 avec UN SEUL pixel allumé dans le coin bas gauche. Ce pixel appartient en fait au mollet de Guile. Ni plus ni moins.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/street-fighter-2-typo-jambe-guile/street-fighter-2-typo-jambe-guile-5.png" alt="" loading="lazy" decoding="async">
</p>
<p>En changeant sa palette (exit la teinte vert kaki, bonjour la couleur du logo), ils l'ont ensuite collé 3 fois au bon endroit pour dessiner le point du &quot;I&quot;. Et personne n'a finalement rien capté pendant des DÉCENNIES.</p>
<p>Hé voilà comment, si vous avez joué à Street Fighter II en arcade dans les années 90, vous aviez littéralement un bout de la jambe de Guile planqué dans l'écran-titre sans le savoir. Magnifique non ?</p>
<p>C'est
<a href="https://fabiensanglard.net/sf2_warrier/index.html">Fabien Sanglard</a>
qui a déterré toute cette histoire il y a quelques années, en analysant le code source du CPS1, aidé d'une interview d'Akira Nishitani (un des créateurs du jeu) datant de 1991.</p>
<p>C'est le genre de bidouille qu'on ne fait plus aujourd'hui avec les mises à jour en ligne mais à l'époque, quand la ROM était gravée, c'était FINITO donc fallait se débrouiller avec ce qu'on avait sous la main quand y'avait un souci.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/dUkLYOPRYH4?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>