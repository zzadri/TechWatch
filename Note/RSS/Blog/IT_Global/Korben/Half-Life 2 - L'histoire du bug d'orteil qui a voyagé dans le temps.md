---
title: "Half-Life 2 - L'histoire du bug d'orteil qui a voyagé dans le temps"
author: "Korben"
date: 2026-01-17T07:47:30.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/retrogaming-emulation"
  - "multimedia-culture/culture-geek"
  - "bug"
  - "développement"
  - "Half-Life 2"
  - "jeux vidéo"
  - "Valve"
  - "virgule flottante"
  - "vr"
rss_source: Blog
url: https://korben.info/half-life-2-bug-porte-orteil-valve.html
note: 0
seen: false
---

<p>Si vous êtes du genre à avoir passé des heures sur Half-Life 2 à vous en retourner les paupières (et je sais que vous êtes nombreux), oubliez tout ce que vous pensiez savoir sur la stabilité légendaire du <strong>Source Engine</strong>. Car figurez-vous qu'un bug totalement improbable vient de refaire surface grâce à Tom Forsyth, un ancien de chez Valve, et c'est clairement un truc de fou, vous allez voir...</p>
<p>Tout commence en 2013. À l'époque, Valve bosse sur le portage de HL2 pour le tout premier Oculus Rift (le fameux DK1 qui nous donnait tous envie de vomir au bout de 5 minutes). Pour tester la VR, ils se disent que le mieux, c'est de reprendre un bon vieux classique. Tout se passe bien jusqu'à ce que Tom Forsyth reste bloqué dès l'intro du jeu, juste après la séquence de la canette. Un garde Barney censé vous ouvrir une porte reste planté là, et la porte refuse de bouger. Coincé. Rideau. On ferme.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/half-life-2-bug-porte-orteil-valve/half-life-2-bug-porte-orteil-valve-1.webp" alt="" loading="lazy" decoding="async">
<p>Le truc qu'il constate alors, c'est qu'en recompilant le code source original de 2004, le bug est là aussi ! Pourtant, personne ne l'avait jamais croisé en neuf ans. Du coup, l'équipe a cru à une sorte de malédiction ou à un bug qui aurait voyagé dans le temps pour infecter l'original. (si si...)</p>
<p>Mais après une journée de spéléologie dans les outils de debug, ils ont fini par trouver le coupable : <strong>l'orteil d'un garde PNJ</strong> ! Le pauvre couillon était placé un millimètre trop près de la porte et en s'ouvrant, la porte tapait dans son pied, rebondissait et se verrouillait. Imaginez un peu la vie du gars, à se faire matraquer l'orteil depuis +20 ans sans pouvoir crier ou se décaler d'un millimètre... Dur !</p>
<p>Mais alors pourquoi ça marchait en 2004 et plus en 2013 ?</p>
<p>Hé bien la réponse tient en deux mots qui vont rappeler des souvenirs aux plus geeks d'entre vous : ✨ <strong>virgule flottante</strong> ✨.</p>
<p>Car en 2004, le jeu tournait avec les instructions x87 (80 bits de précision, un beau bordel hérité de l'époque)et en 2013, avec le passage au SSE (32 ou 64 bits), les calculs physiques sont devenus plus &quot;stricts&quot;. Dans les deux versions, la porte tape l'orteil mais avec le x87, la micro-rotation infligée au garde suffisait à dégager son pied juste assez pour que la porte passe au millième de seconde suivant. Avec le SSE par contre, le garde pivotait un chouïa moins loin... et paf, collision, porte bloquée !</p>
<p>C'est encore une preuve que même dans un chef-d'œuvre comme Half-Life 2, tout ne tient qu'à un orteil et quelques bits. D'ailleurs, si vous voulez vous replonger dans l'ambiance, sachez que
<a href="https://korben.info/half-life-2023-telechargement-gratuit-week-end.html">Half-Life a fêté ses 25 ans</a>
récemment avec une belle mise à jour, et pour les nostalgiques de la VR qui veulent souffrir avec style,
<a href="https://korben.info/vorpx-driver-oculus-rift.html">le driver VorpX</a>
permet toujours de faire des miracles. Ce serait dommage de passer à côté !</p>
<p>Allez, je vous laisse, je vais vérifier si mon gros orteil ne bloque pas ma porte d'entrée.</p>
<p>
<a href="https://www.pcgamer.com/games/fps/a-former-valve-dev-revealed-how-while-a-vr-version-of-half-life-2-was-being-made-a-single-metro-cops-toe-created-a-time-travelling-bug-that-softlocked-all-versions-of-the-game/">Source</a>
</p>