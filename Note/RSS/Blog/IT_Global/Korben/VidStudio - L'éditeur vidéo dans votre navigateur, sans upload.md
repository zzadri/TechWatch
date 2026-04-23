---
title: "VidStudio - L'éditeur vidéo dans votre navigateur, sans upload"
author: "Korben ✨"
date: 2026-04-22T12:15:54.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "multimedia-culture"
  - "alternative open source"
  - "éditeur vidéo en ligne"
  - "Éditeur vidéo open source"
  - "Montage vidéo"
  - "privacy"
rss_source: Blog
url: https://korben.info/vidstudio-app-editeur-video-navigateur.html
note: 0
seen: false
---

<p>Un éditeur vidéo qui redimensionne, compresse et coupe vos clips... sans rien uploader nulle part, ça vous dit ???</p>
<p>Ça tombe bien puisque
<a href="https://vidstudio.app/">VidStudio</a>
fait tourner FFmpeg directement dans votre navigateur ! Vous allez sur vidstudio.app, vous déposez votre vidéo, et tout le traitement se fait ensuite côté client. Les fichiers ne quittent jamais votre machine, ce qui fait que niveau vie privée, ça nous change clairement des éditeurs cloud type Clipchamp ou Canva où une partie du traitement passe par leurs serveurs avec toutes les joyeusetés que ça implique côté données.</p>
<p>Sous le capot, le truc tient debout grâce à trois briques. Il y a WebCodecs qui s'occupe du décodage frame par frame pour la timeline, en utilisant les décodeurs hardware du navigateur quand ils sont dispos. FFmpeg compilé en WebAssembly prend ensuite le relais pour l'encodage final et les conversions de format. Et pour le rendu, c'est
<a href="https://pixijs.com/">Pixi.js</a>
sur une canvas WebGL, avec un fallback logiciel quand la carte graphique ne suit pas.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vidstudio-app-editeur-video-navigateur/vidstudio-app-editeur-video-navigateur-2.png" alt="" loading="lazy" decoding="async">
<p>Les projets sont sauvegardés dans IndexedDB, du coup vous pouvez fermer l'onglet et revenir plus tard, car tout est conservé et les traitements lourds tournent dans des Web Workers, ce qui évite de geler l'interface quand vous compressez un fichier de 2 Go déjà bien lourd.</p>
<p>Ensuite, côté outils, y'a de quoi faire avec un éditeur multi-piste avec source monitor et la possibilité de parcourir la vidéo à la frame près. Il y a également de quoi redimensionner pour YouTube ou TikTok, un mode batch pour convertir plusieurs vidéos d'un coup, un compresseur avec cible de taille exacte, un extracteur audio, un générateur de thumbnails et storyboards, et un système de watermarks avec positionnement et timing. Les sous-titres sont également gérés, avec possibilité de les incruster dans la vidéo ou de les sortir séparément.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vidstudio-app-editeur-video-navigateur/vidstudio-app-editeur-video-navigateur-3.png" alt="" loading="lazy" decoding="async">
<p>Niveau problèmes que vous pourriez rencontrer avec cet outil, ce sera surtout à cause des codecs HEVC qui galèrent sur Firefox. De plus, les vidéos 10-bit ne passent pas toujours sur Windows, et certains WEBM avec des codecs audio exotiques refusent de charger. Bon après c'est pas grand chose de dramatique pour du contenu classique filmé avec un smartphone ou un appareil photo, mais si vous bossez avec du matos pro en 10-bit, allez plutôt voir ailleurs.</p>
<p>Après si vous aimez ce genre d'outils, dans la famille &quot;traitement vidéo dans le navigateur&quot;, VidStudio rejoint
<a href="https://korben.info/cutia-editeur-video-ia-navigateur.html">Cutia</a>
qui mise sur l'open source, et
<a href="https://korben.info/vous-avez-deja-essaye-de-faire-du-traitement-video.html">MediaBunny</a>
qui propose une bibliothèque bas niveau pour les devs et dont je vous ai déjà parlé. Cependant, je préfère VidStudio qui se positionne plutôt sur du grand public, avec une interface qui ressemble à un vrai logiciel de montage.</p>
<p>Ça tourne d'ailleurs sur smartphone, ce qui est franchement impressionnant. Donc si vous avez juste une vidéo à retoucher vite fait sans passer par une usine à gaz type Adobe Premiere ou Final Cut, ça fera bien le job, et vos fichiers restent sagement au chaud chez vous !</p>