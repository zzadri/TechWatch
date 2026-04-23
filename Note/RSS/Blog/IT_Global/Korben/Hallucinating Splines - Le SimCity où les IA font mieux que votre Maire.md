---
title: "Hallucinating Splines - Le SimCity où les IA font mieux que votre Maire"
author: "Korben"
date: 2026-02-12T15:11:34.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "jeux-video"
  - "intelligence artificielle"
  - "jeu de simulation"
  - "SimCity"
rss_source: Blog
url: https://korben.info/hallucinating-splines-simcity-ia.html
note: 0
seen: false
---

<p>SimCity, je pense que tout le monde connaît. Moi c'est vraiment l'un de jeux préférés. Enfin la version SimCity 2000. C'est que des bons souvenirs pour moi. Dans ce jeu, vous posiez des routes, des zones résidentielles, et vous regardiez votre ville grandir... ou cramer, selon les jours. Hé bien
<a href="https://hallucinatingsplines.com/">Hallucinating Splines</a>
, c'est le même délire, sauf que c'est une IA qui joue à votre place.</p>
<p>Ce projet est basé sur
<a href="https://korben.info/micropolis-simcity.html">Micropolis</a>
, la version open source du
<a href="https://korben.info/simcity-2013.html">SimCity</a>
original sorti en 1989 (Et surtout pas les trucs d'EA qui ont suivi ^^). Du coup, on a un vrai moteur de simulation urbaine avec zonage résidentiel, commercial, industriel, gestion des services publics, du trafic... bref le package complet.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hallucinating-splines-simcity-ia/hallucinating-splines-simcity-ia-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Sauf qu'ici, personne ne touche la souris. Des agents autonomes prennent les décisions, construisent les infrastructures et gèrent la croissance de leur ville sans intervention humaine. Enfin, sauf si vous comptez le clic pour lancer la simulation.</p>
<p>Et visiblement ça tient plutôt bien la route (sans mauvais jeu de mots). 96 maires IA, 607 villes construites et une population cumulée de plus de 10 millions d'habitants virtuels. C'est pas mal hein pour des programmes qui n'ont jamais mis les pieds dans un conseil municipal !</p>
<p>En fait, le concept s'appelle &quot;Vibe a City&quot;. Vous cliquez sur un bouton et hop, une IA se met à bâtir sa métropole en temps réel sous vos yeux, sans intervention humain. Les villes portent également des noms générés plutôt poétiques je trouve... Turtle Ziggurat, Storm Cove, Azure Heath, Procedural Mesa (ok celui-là est un peu trop honnête).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hallucinating-splines-simcity-ia/hallucinating-splines-simcity-ia-3.png" alt="" loading="lazy" decoding="async">
<p>Et y'a même un leaderboard avec un système de scoring. Chaque cité a son indicateur d'activité (Tout fraiche, récente, ancienne ou stagnante), les stats se rafraîchissent toutes les 30 secondes et on peut trier par population, par score ou par date. Une certaine Annexed Colony tape par exemple dans les 185 000 habitants en l'an 2428 dans le jeu. C'est foufou !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hallucinating-splines-simcity-ia/hallucinating-splines-simcity-ia-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Côté technique, plutôt que de repartir de zéro, tout repose sur micropolisJS, une implémentation JavaScript/HTML5 de Micropolis sous licence GPL v3, et le code est dispo sur
<a href="https://github.com/andrewedunn/hallucinating-splines">GitHub</a>
(un git clone et c'est parti). Si vous connaissez
<a href="https://korben.info/microlandia-city-builder-simulation-realiste.html">Microlandia</a>
que j'avais présenté il y a quelques semaines, c'est dans la même veine mais avec une couche d'agents IA par-dessus.</p>
<p>Et n'oubliez pas d'aller voir le petit clin d’œil sur la page de crédits ou dans le footer qui affiche le Dr. Wright, le fameux conseiller de SimCity sur SNES. Après le piège, c'est que vous allez y passer des heures à regarder une IA construire ce que vous n'avez jamais réussi à faire dans le jeu. Ahahaha !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hallucinating-splines-simcity-ia/hallucinating-splines-simcity-ia-1.webp" alt="" loading="lazy" decoding="async">
<p>
<a href="https://hallucinatingsplines.com">A découvrir ici !</a>
</p>