---
title: "SpinalVoodoo - La 3dfx Voodoo recréée de zéro en FPGA"
author: "Korben"
date: 2026-03-23T07:09:24.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "jeux-video/retrogaming-emulation"
  - "FPGA"
  - "retrocomputing"
rss_source: Blog
url: https://korben.info/spinalvoodoo-3dfx-voodoo-fpga.html
note: 0
seen: false
---

<p>Quand Nvidia a racheté <strong>3dfx</strong>, la Voodoo est morte façon Marion Cotillard dans Batman, et tout le monde était &quot;mui tristé&quot;... Mais vous allez pouvoir sécher vos larmes de &quot;crocrodiles&quot; car un dev vient de la ressusciter... dans un FPGA (c'est une puce reprogrammable).</p>
<p><strong>SpinalVoodoo</strong>, c'est 430 registres de configuration, un pipeline graphique complet et des jeux à l'ancienne qui tournent OKLM du genre Quake ou Screamer 2.</p>
<p>Hé oui, sur un FPGA !</p>
<p>Le projet de Francisco Ayala Le Brun, c'est en fait une réimplémentation complète du GPU Voodoo 1 en
<a href="https://github.com/fayalalebrun/SpinalVoodoo">SpinalHDL</a>
(un langage pour décrire des circuits). Pas de l'émulation logicielle genre 86Box mais une reconstruction totale du pipeline hardware registre par registre dans une puce reprogrammable. Du coup chaque pixel sort comme sur la carte d'origine comme quand elle faisait tourner Quake en 640x480 sous Windows 95. Enfin presque...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/spinalvoodoo-3dfx-voodoo-fpga/spinalvoodoo-3dfx-voodoo-fpga-2.png" alt="" loading="lazy" decoding="async">
<p><em>Screamer 2 par SpinalVoodoo</em></p>
<p>Je dis &quot;enfin presque&quot; parce que la Voodoo original, c'est pas juste un chip qui balance des triangles. Il y a en fait quatre types de registres qui réagissent chacun différemment selon le timing. Du coup si vous changez un paramètre au mauvais moment pendant qu'un triangle traverse le pipeline, les derniers pixels du triangle A se retrouvent avec la config du triangle B. Bref, bonjour la corruption !</p>
<p>SpinalHDL permet donc d'encoder tout ça proprement. Chaque registre déclare son adresse, sa catégorie et son mode d'accès en une seule déclaration. Pour un projet fait en solo, c'est quand même du costaud.</p>
<p>D'ailleurs,
<a href="https://noquiche.fyi/voodoo">le récit de débogage</a>
vaut le détour. L'auteur avait des pixels d'overlay translucides qui devenaient mystérieusement transparents. Il a d'abord soupçonné un problème de framebuffer, changé les priorités d'écriture, ajouté des chemins sans cache... et l'artefact bougeait à peine. Snif...</p>
<p>Et là, avec Conetrace (un outil qui trace le chemin des pixels à travers le design), il a fini par trouver le coupable : 3 micro-erreurs de précision qui, séparément, étaient quasi invisibles, mais qui ensemble foutaient le bordel sur certains pixels. Le &quot;bug mémoire&quot; n'en était finalement pas un. Va savoir combien de développeurs hardware se seraient arrachés les cheveux là-dessus !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/spinalvoodoo-3dfx-voodoo-fpga/spinalvoodoo-3dfx-voodoo-fpga-3.png" alt="" loading="lazy" decoding="async">
<p><em>Quake sur SpinalVoodoo, rendu FPGA fidèle à l'original</em></p>
<p>Côté compatibilité, la majorité du pipeline graphique est implémenté (textures, transparence, brouillard, depth buffer, dithering...) par contre, y'a pas encore de contrôleur d'affichage (pas de sortie VGA native pour le moment), pas de trilinéaire, et pas de multi-texture. Attention aussi, pas de licence spécifiée sur le repo pour le moment, ce qui est un peu dommage si vous comptez réutiliser le code.</p>
<p>Si vous avez suivi
<a href="https://korben.info/homebrew-486-motherboard-carte-mere.html">le mec qui a conçu sa carte mère 486 from scratch</a>
avec un FPGA Spartan II, ou la
<a href="https://korben.info/game-bub-console-retro-fpga-open.html">Game Bub et son FPGA</a>
pour le rétrogaming, SpinalVoodoo pousse le curseur encore plus loin. Reproduire un GPU dédié avec son pipeline fixe et ses subtilités de timing, c'est quand même pas le même délire qu'émuler un CPU.</p>
<p>Bref, qu'une seule personne puisse recréer un GPU complet avec les outils RTL modernes, moi je trouve ça assez foufou !</p>
<p>
<a href="https://hackaday.com/2026/03/22/the-3dfx-voodoo-lives-again-in-an-fpga/">Source</a>
</p>