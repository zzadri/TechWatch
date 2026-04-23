---
title: "Onlook - Fini les allers-retours entre Figma et le code"
author: "Korben"
date: 2026-02-26T09:23:24.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/web-developpement"
  - "linux-open-source/logiciels-libres"
  - "figma"
  - "Next.js"
  - "open source"
  - "React"
  - "tailwind-css"
rss_source: Blog
url: https://korben.info/onlook-dev.html
note: 0
seen: false
---

<p>Bonne nouvelle pour ceux qui en ont raz la casquette de se taper des allers-retours entre Figma et VS Code ! Parce qu'avec
<a href="https://onlook.dev">Onlook</a>
, l'éditeur visuel open source qui vous permet de modifier le design de vos apps React directement dans le navigateur, vous allez pouvoir cliquer simplement sur un élément de design, et en changer la couleur, la typo...etc et hop, ça modifiera le code derrière.</p>
<p>Pas mal, non ?</p>
<p>Vous ouvrez votre projet Next.js dans Onlook, et vous vous retrouvez avec une interface à la Figma, sauf que c'est branché sur votre code source. Vous sélectionnez un titre, un bouton, n'importe quel composant, et vous modifiez son style visuellement... couleurs, padding, marges, polices, tout y passe.</p>
<img src="https://korben.info/onlook-dev/onlook-dev-1.gif" alt="" loading="lazy" decoding="async">
<p>Et en fait, le truc qui change tout par rapport à un inspecteur CSS classique, c'est que quand vous cliquez sur &quot;Publish&quot;, les modifications atterrissent DIRECTEMENT dans vos fichiers .tsx. C'est donc du vrai code propre, pas du CSS inline dégueulasse.</p>
<p>Côté technique, l'outil gère nativement TailwindCSS (parce que bon, en 2026, si vous faites du React sans Tailwind, vous aimez forcément le cuir qui claque et la souffrance). Vous éditez en mode visuel, ça génère les bonnes classes Tailwind, et vous gardez un contrôle total. Y'a aussi un mode LLM intégré... &quot;<em>rends ce bouton bleu avec des coins arrondis</em>&quot; et hop, c'est fait. Comme ça, pas besoin de chercher si c'est rounded-lg ou rounded-xl dans la doc.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/RSX_3EaO5eU?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Pour ceux qui connaissent
<a href="https://korben.info/bolt-diy-assistant-ia-developpement-web.html">Bolt.DIY</a>
ou qui se souviennent d'
<a href="https://korben.info/amplify-studio.html">Amplify Studio</a>
(le truc de AWS qui tentait de faire le pont Figma vers React), Onlook prend le problème dans l'autre sens. Au lieu de partir du design pour générer du code, on part du code existant et on le modifie visuellement. Du coup, pas de code généré bancal à maintenir, c'est finalement VOTRE codebase qui est éditée.</p>
<p>Le projet est open source sous licence Apache 2.0 sur
<a href="https://github.com/onlook-dev/onlook">GitHub</a>
et la version open source est gratuite et self-hostable, donc vous pouvez la faire tourner chez vous sans débourser un centime. Après pour ceux qui veulent du cloud managé avec collab temps réel, y'a des plans payants.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/onlook-dev/onlook-dev-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Après attention, c'est encore jeune et le support se limite à React et Next.js pour l'instant, donc si votre stack c'est Vue ou Svelte, ça ne marchera pas. Et l'IA mouline un peu sur les layouts complexes mais le projet avance vite, la communauté est active, et pour un outil gratos qui fait le lien entre design et code en open source, y'a pas grand-chose d'équivalent.</p>
<p>Bref, à tester, c'est gratos.</p>