---
title: "GNU TeXmacs - Écrivez vos équations comme dans Word"
author: "Korben ✨"
date: 2026-04-23T09:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "tutoriels-guides"
  - "équations"
  - "gnu"
  - "LaTeX"
  - "maths"
  - "WYSWYG"
rss_source: Blog
url: https://korben.info/texmacs-alternative-libre-latex.html
note: 0
seen: false
---

<p>Ah, LaTeX...</p>
<p>Si vous avez un jour essayé de poser 3 équations dans un document sérieux, vous voyez le genre de galère que c'est. Le rendu est magnifique, les maths sont propres, mais faut d'abord digérer son langage de markup avant de réussir à imprimer la moindre intégrale. Heureusement, c'est là qu'arrive
<a href="https://www.texmacs.org/">GNU TeXmacs</a>
, un éditeur scientifique libre qui fait pareil mais en WYSIWYG.</p>
<p>Ça tourne sur Linux, macOS et même des OS du passé comme Windows ^^ et ça devrait ravir étudiants en sciences, thésards, chercheurs, enseignants, ou autres curieux qui veulent voir à quoi ressemble un éditeur scientifique vraiment libre. Faut vous imaginer un Google Docs avec un mode maths natif, dans lequel vous tapez directement votre équation comme dans un bon vieux Word avec du gras (c'est bon le gras ^^ !), de l'italique, des fractions, ou encore des racines carrées que vous pouvez faire à la souris ou via des raccourcis clavier. Et le moteur vous sort alors une typographie de niveau publication académique. Comme ça, pas besoin de &quot;recompiler&quot; votre document à chaque correction car tout s'affiche en direct !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/texmacs-alternative-libre-latex/texmacs-alternative-libre-latex-2.png" alt="" loading="lazy" decoding="async">
<p><em>Une formule rendue directement dans l'éditeur, sans recompilation</em></p>
<p>Le truc qu'il faut comprendre, c'est que TeXmacs n'est PAS un frontend graphique pour LaTeX. C'est un moteur de typographie complètement indépendant, qui s'inspire des idées de TeX sans en recycler le code. Vous pouvez donc exporter vers du .tex si un collègue en a besoin, mais ce n'est pas ce qui tourne sous le capot pendant que vous écrivez.</p>
<p>L'autre truc sympa, c'est que TeXmacs sert aussi d'interface pour de nombreux systèmes de calcul formel libres tels que Maxima, Sage, Pari ou Axiom qui peuvent balancer leurs résultats directement dans votre document, formatés proprement. R et Octave sont aussi de la partie pour le côté stats et numérique.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/texmacs-alternative-libre-latex/texmacs-alternative-libre-latex-3.png" alt="" loading="lazy" decoding="async">
<p><em>TeXmacs servant d'interface à un système de calcul formel, le résultat tombe déjà formaté</em></p>
<p>Derrière le projet, y'a Joris van der Hoeven, un mathématicien néerlandais et Directeur de recherche au CNRS. Il bosse sur TeXmacs depuis la fin des années 90, et maintient en parallèle Mathemagix, un système de calcul formel libre qui se marie forcément bien avec. Le projet est sous licence GPL et fait partie du
<a href="https://korben.info/richard-stallman-revolution-logiciel-libre.html">projet GNU</a>
. Ce n'est donc pas un truc vibe codé en un weekend just 4 fun !</p>
<p>TeXmacs reste quand même un logiciel de niche. Et gaffe en particulier à l'import depuis LaTeX, qui laissera tomber les fichiers de style custom et ne gèrera qu'un sous-ensemble du langage. L'interface a aussi un côté très années 2000 assumé, et la communauté est plus petite que celle de LaTeX.</p>
<p>Mais peu importe, moi ce qui me plaît dans la démarche, c'est cette indépendance assumée vis à vis de TeX avec un moteur refait à zéro et pas une surcouche contraignant comme LyX. Alors oui forcément, on perd un peu de compatibilité mais ça rend tellement service que c'est pas très grave.</p>
<p>Voili voilou, si vous êtes amateur de maths et de formules ou que vous voulez voir à quoi ressemble un éditeur scientifique vraiment WYSIWYG, ça vaut son petit téléchargement. Puis c'est gratuit alors foncez !</p>