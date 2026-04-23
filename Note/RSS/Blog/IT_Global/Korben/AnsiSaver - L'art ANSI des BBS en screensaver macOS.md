---
title: "AnsiSaver - L'art ANSI des BBS en screensaver macOS"
author: "Korben"
date: 2026-03-09T10:02:37.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "multimedia-culture/culture-geek"
  - "open source"
  - "macOS"
  - "Logo ANSI"
  - "retro"
  - "screensaver"
rss_source: Blog
url: https://korben.info/ansi-saver-economiseur-ecran-ansi-art-macos.html
note: 0
seen: false
---

<p>Si vous êtes pété de thunes, vous avez forcément un Mac. Mais surtout, vous avez un écran de veille par défaut qui vous file le cafard... Mais c'était sans compter sur
<a href="https://github.com/lardissone/ansi-saver">AnsiSaver</a>
qui est un écran de veille capable de piocher dans les archives de
<a href="https://16colo.rs">16colo.rs</a>
, la plus grosse collection d'<strong>art ANSI</strong> au monde, et qui fait défiler tout ça sur votre écran à 60 fps ! Like a boss !</p>
<p>Pour ceux qui débarquent, l'art ANSI c'est ces dessins réalisés caractère par caractère qu'on affiche dans les BBS (les serveurs communautaires d'avant Internet, en gros). Des artistes passaient des heures à composer des fresques en utilisant les 256 caractères du jeu
<a href="https://fr.wikipedia.org/wiki/Page_de_code_437">CP437</a>
... et le résultat est souvent bluffant. Des logos, des paysages, de la typographie, le tout en mode texte UNIQUEMENT. Y'a même eu des groupes mythiques comme ACiD, iCE ou Blocktronics qui ont marqué le truc à l'époque !</p>
<p>En fait, AnsiSaver récupère ces packs directement depuis 16colo.rs, les met en cache dans ~/Library/Caches/AnsiSaver/ et les affiche via libansilove, une lib C spécialisée dans le rendu CP437. Le tout animé par Core Animation, ce qui est vraiment pas mal du tout pour un screensaver !</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/mdlXhbqu4iw?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Côté options, même si j'ai pas réussi à y accéder (??), vous avez le choix entre 3 modes d'affichage. Le défilement vers le haut, le défilement vers le bas (qui empilent les œuvres et scrollent à l'infini) et le mode fondu enchaîné entre chaque pièce. La vitesse de défilement se règle de 10 à 200 pixels par seconde, et ça supporte les écrans Retina.</p>
<p>Le truc sympa c'est que vous pouvez aussi balancer vos propres fichiers puisque AnsiSaver supporte les .ANS, .ICE, .ASC, .BIN, .XB, .PCB et .ADF... du coup si vous avez une collection perso qui traîne sur un vieux disque dur (ça arrive), ou que vous aimez digger Archive.org, vous faites pointer vers le dossier et c'est réglé.</p>
<p>Pour l'install, c'est hyper simple. Vous téléchargez le .saver depuis les
<a href="https://github.com/lardissone/ansi-saver/releases">releases GitHub</a>
, vous double-cliquez et macOS l'ajoute aux Réglages Système.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ansi-saver-economiseur-ecran-ansi-art-macos/ansi-saver-economiseur-ecran-ansi-art-macos-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Attention, le binaire n'est pas signé, du coup il faudra faire un tour dans Réglages &gt; Confidentialité et sécurité pour l'autoriser au premier lancement. Si ça ne marche pas du premier coup, relancez les Réglages Système. Ça fonctionne sur macOS Sequoia minimum (15.0+) et ça tourne aussi bien sur Apple Silicon que sur Intel.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ansi-saver-economiseur-ecran-ansi-art-macos/ansi-saver-economiseur-ecran-ansi-art-macos-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Si vous cherchez d'autres façons de pimper votre
<a href="https://korben.info/bash-screensavers-absurdite-productive-terminal.html">terminal avec des screensavers</a>
en mode rétro, y'a de quoi faire. Et si vous êtes plutôt
<a href="https://korben.info/terminal-au-look-tres-retro.html">nostalgie CRT et phosphore vert</a>
... pareil.</p>
<p>En multi écran chez moi, ça passe pas partout mais sur MacBook Air, ça a CARRÉMENT de la gueule !</p>