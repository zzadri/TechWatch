---
title: "Banjo-Kazooie - Le portage PC 4K est dispo"
author: "Korben"
date: 2026-01-28T07:19:38.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/pc-gaming"
  - "jeux-video/retrogaming-emulation"
  - "banjo-kazooie"
  - "dariosamo"
  - "nintendo-64"
  - "pc-port"
  - "recompilation"
  - "retrogaming"
rss_source: Blog
url: https://korben.info/banjo-recomp.html
note: 0
seen: false
---

<p>Si contrairement à moi, vous avez grandi avec la Nintendo 64, vous avez forcément passé des heures à collecter des Jiggies et à insulter cette sorcière de
<a href="https://banjokazooie.fandom.com/fr/wiki/Gruntilda_Clindoignon">Gruntilda</a>
. Ceux qui savent, savent... Mais ceux qui ne savent pas hé bien préparez-vous aussi à prendre une claque de nostalgie en 4K, car <strong>Banjo-Kazooie</strong> vient de débarquer sur PC en version 100% native !</p>
<p>Comme d'hab, c'est de la <strong>recompilation statique</strong> et pas une ROM émulée. C'est le même type de procédé magique qui nous a déjà offert le portage de
<a href="https://korben.info/zelda-64-recompiled-portage-natif-ray-tracing-4k.html">Zelda Majora's Mask</a>
(via N64: Recompiled) ou encore
<a href="https://korben.info/sonic-unleashed-recompiled-revolution-retrogaming.html">Sonic Unleashed</a>
récemment (via XenonRecomp).</p>
<p>En gros, le projet
<a href="https://github.com/BanjoRecomp/BanjoRecomp">Banjo-Kazooie: Recompiled</a>
utilise l'outil N64: Recompiled pour traduire le code original du jeu en une application PC native. Comme ça le jeu tourne sans l'overhead de l'émulation CPU traditionnelle, ce qui nous permet de profiter d'un framerate débloqué (fini les petits ralentissements de l'époque), d'un support pour les écrans ultra-larges, et d'une fluidité absoluuuue.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/0906Cz-59eU?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Et surtout, ce portage intègre le moteur de rendu <strong>RT64</strong>. Pour l'instant, ça sert surtout à lisser tout ça et à gérer les hautes résolutions, mais le moteur est techniquement capable de gérer le Ray Tracing, ce qui laisse rêveur pour les futures mises à jour. Je vous laisse imagine la fameuse Montagne de Spirale avec des éclairages ultra réalistes... ça va être quelque chose !</p>
<p>Bref, voici ce qu'on retrouve dans ce portage :</p>
<ul>
<li>Support natif du clavier/souris et des manettes modernes.</li>
<li><strong>Sauvegarde des notes</strong> : Plus besoin de ramasser toutes les notes d'un niveau en une seule fois sans mourir (le traumatisme de mon enfance, je vous jure).</li>
<li>Temps de chargement quasi-instantanés.</li>
<li>Support des mods et des packs de textures.</li>
</ul>
<p>Alors comment on y joue ?</p>
<p>C'est assez simple en fait. Comme pour les autres projets de ce style, les dév ne fournissent aucun asset illégal. Vous devez donc posséder votre propre ROM de <strong>Banjo-Kazooie</strong>. Attention par contre, il faut impérativement la version <strong>NTSC 1.0 (US)</strong>, sinon ça ne passera pas lors de l'extraction. Ensuite, au premier lancement, l'outil va extraire les textures, les modèles et les sons de votre ROM pour construire le jeu PC.</p>
<p>Il y a même un support pour le Steam Deck et Linux via Flatpak, donc vous pouvez emmener l'oiseau et l'ours partout avec vous (sauf sous l'eau, évidemment ^^).</p>
<p>A vous maintenant de foncer récupérer
<a href="https://github.com/BanjoRecomp/BanjoRecomp">le launcher sur GitHub</a>
.</p>