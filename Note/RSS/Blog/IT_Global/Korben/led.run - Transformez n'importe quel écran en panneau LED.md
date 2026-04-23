---
title: "led.run - Transformez n'importe quel écran en panneau LED"
author: "Korben"
date: 2026-02-12T13:42:16.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/gadgets-crowdfunding"
  - "linux-open-source/logiciels-libres"
  - "affichage web"
  - "décoration LED"
  - "panneau LED navigateur"
  - "signalétique numérique"
  - "vanilla JavaScript"
rss_source: Blog
url: https://korben.info/led-run-ecran-panneau-led-navigateur.html
note: 0
seen: false
---

<p>Transformer n'importe quel écran en panneau LED géant, avec juste une URL... ça vous chauffe ? C'est en tout cas ce que propose
<a href="https://led.run/">led.run</a>
, un petit outil open source sous licence MIT qui fait le taf sans avoir besoin d'installer quoi que ce soit.</p>
<p>En gros, vous tapez votre texte directement dans l'URL, genre
<a href="https://led.run/KORBEN%20JE%20T%27AIME">led.run/KORBEN JE T'AIME</a>
et hop, votre navigateur affiche un gros panneau lumineux comme ce qu'on retrouve dans les concerts ou dans les vitrines de magasin.</p>
<p>Et ça tourne dans n'importe quel navigateur (même celui de votre grille-pain connecté).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/led-run-ecran-panneau-led-navigateur/led-run-ecran-panneau-led-navigateur-2.png" alt="" loading="lazy" decoding="async">
<p><em>led.run en action avec le thème par défaut - sobre mais efficace</em></p>
<p>Le truc sympa, c'est qu'il y a une vingtaine de thèmes disponibles. Du néon qui clignote au style rétro avec des scanlines façon vieux moniteur CRT, en passant par un mode &quot;panneau routier&quot;, un effet feu d'artifice ou encore une ambiance Shibuya sous la pluie. Y'a même un thème &quot;bois artisanal&quot; pour ceux qui veulent faire chic. Attention par contre, sur un vieux smartphone certains effets un peu chargés peuvent ramer.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/led-run-ecran-panneau-led-navigateur/led-run-ecran-panneau-led-navigateur-1.jpeg" alt="" loading="lazy" decoding="async">
<p>Et tout se paramètre via l'URL. Vous voulez du texte rouge ? Ajoutez <code>?c=ff0000</code>. Un fond blanc semi-transparent ? <code>?bg=40ffffff</code>. Du défilement vers la droite à vitesse turbo ? <code>?speed=120&amp;dir=right</code>. C'est super car avec ça vous pouvez automatiser plein de trucs. Par exemple je me ferais bien un panneau d'affichage au dessus de la porte du bureau pour dire aux enfants de pas débouler en plein pendant mes
<a href="https://twitch.tv/korbenfr">lives Twitch</a>
(oui c'est les vacances en ce moment...).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/led-run-ecran-panneau-led-navigateur/led-run-ecran-panneau-led-navigateur-3.png" alt="" loading="lazy" decoding="async">
<p><em>Vive l'éducation positive !</em></p>
<p>D'ailleurs, l'outil détecte automatiquement si votre texte est court ou long. Dix caractères ou moins, ça s'affiche en mode panneau statique. Au-delà, ça défile tout seul. En fait c'est plutôt bien foutu, sauf si vous voulez un long texte en statique... dans ce cas, forcez avec <code>?mode=sign</code> ou <code>?mode=flow</code>.</p>
<p>Voilà c'est parfait pour transformer un vieil iPad ou une tablette Android en enseigne de bar (&quot;HAPPY HOUR JUSQU'À 21H&quot;), brandir votre téléphone en mode pancarte à un concert pour dire à Taylor Swift que vous voulez l'épouser, ou afficher un &quot;NE PAS DÉRANGER ON BRASSE DU VENT&quot; sur l'écran de la salle de réunion.</p>
<p>Voilà voilà. Si vous avez une vieille tablette qui traîne, vous savez quoi en faire maintenant.</p>
<p>C'est
<a href="https://github.com/led-run/led.run">sur GitHub</a>
!</p>
<p>Merci à Lorenper pour la découverte !</p>