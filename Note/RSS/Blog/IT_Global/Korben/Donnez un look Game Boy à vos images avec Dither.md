---
title: "Donnez un look Game Boy à vos images avec Dither"
author: "Korben"
date: 2026-03-18T16:03:54.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "jeux-video/retrogaming-emulation"
  - "outils graphiques"
  - "pixel art"
  - "retro gaming"
rss_source: Blog
url: https://korben.info/dither-neato-images-retro.html
note: 0
seen: false
---

<p>Si vous avez un site web et que vos illustrations ressemblent comme sur mon site, à un joyeux bordel de screenshots pixelisés, de photos libres de droits et d'images IA plus ou moins réussies, y'a peut-être un moyen de donner une certaine cohérence visuelle à tout ça. L'outil s'appelle
<a href="https://dither.neato.fun/">Dither</a>
, ça a été créé par
<a href="https://x.com/Shpigford">Shpigford</a>
, et c'est un générateur de tramage vectoriel qui tourne directement dans Chrome, Firefox ou Safari, sans inscription ni installation.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dither-neato-images-retro/dither-neato-images-retro-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de Dither avec ses réglages d'algorithme et de palette</em></p>
<p>Le principe est simple... Vous balancez un fichier JPEG ou PNG et hop, le moteur JavaScript le transforme en utilisant des algorithmes de dithering comme Bayer (en 2x2, 4x4 ou 8x8), du halftone, des lignes, des croix, des points ou encore des écailles.</p>
<p>Neuf algorithmes au total et ce qui est vraiment cool, c'est qu'il y a des palettes prédéfinies dont une palette <strong>Game Boy</strong> qui donne ce rendu vert olive mythique qu'on avait sur l'écran LCD 160x144 de la jolie brique de Nintendo. Y'a aussi du CGA et du Sepia pour ceux qui veulent varier les ambiances et pour le coup, ça envoie bien du rétro !</p>
<p>Pour les djeuns, sachez que le dithering c'est en fait cette vieille technique qui remonte aux années 70-80 permettant de simuler des dégradés quand on n'a que quelques teintes disponibles. En gros, au lieu d'un dégradé lisse en 16 millions de couleurs RGB, on place des petits points de 2 à 8 couleurs qui, vus de loin, donnent l'illusion d'un mélange. C'est exactement ce qu'on voyait sur les écrans CGA 320x200 des vieux PC IBM XT ou sur la Game Boy sortie en 1989.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dither-neato-images-retro/dither-neato-images-retro-3.png" alt="" loading="lazy" decoding="async">
<p>L'intérêt d'un outil comme Dither, c'est qu'en plus de jouer avec les 9 algorithmes, vous pouvez régler pas mal de paramètres via l'interface. Par exemple, la taille des cellules en pixels (8px par défaut, mais j'ai trouvé que 12px donne un bon compromis lisibilité/esthétique sur des photos 1024x768), l'angle de rotation du motif à 45 degrés, l'échelle à 1.0, et même choisir entre cercle, carré ou diamant pour la forme du rendu.</p>
<p>Vous pouvez aussi partir d'un gradient linéaire, radial ou conique au lieu d'une image existante... pas mal pour générer des fonds d'écran rétro sur macOS ou Linux !</p>
<p>Et surtout, l'export se fait en SVG ou en PNG. Le SVG c'est super pratique si vous voulez intégrer le résultat dans un site web via une balise <code>&lt;img&gt;</code> sans perte de qualité, vu que c'est du vectoriel.</p>
<p>Par contre, attention, le mode Sepia a tendance à écraser les contrastes sur les photos sombres en dessous de 128 de luminosité moyenne... du coup préférez le mode B/W ou CGA sur ce type d'images.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dither-neato-images-retro/dither-neato-images-retro-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Sachez aussi que les photos avec beaucoup de détails fins (genre une photo de foule ou un paysage urbain en 4000x3000) perdent carrément en lisibilité avec les petites cellules de 4px ou 8px. Montez la taille à 16px ou 32px dans ce cas, vous verrez, ça change tout.</p>
<p>Bon après, est-ce que je vais mettre toutes les images de mon site en mode
<a href="https://korben.info/pixel-snapper-repare-pixel-art-ia-baveux.html">pixel art</a>
tramé ? Non, clairement pas, car ça deviendrait monotone à force. Mais pour un projet perso, un portfolio, un zine en ligne ou même une série d'articles thématiques, ça peut donner un look uniforme sympa.</p>
<p>Bref, allez jeter un oeil, c'est gratuit et ça tourne dans le navigateur.</p>
<p>Merci à Lorenper pour la découverte !</p>