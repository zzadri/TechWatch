---
title: "HA-Animated-cards – 67 cartes animées pour pimper votre dashboard Home Assistant"
author: "Korben"
date: 2026-01-07T09:42:36.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/self-hosting"
  - "domotique"
  - "Home Assistant"
  - "smart home"
rss-source: Blog
url: https://korben.info/ha-animated-cards-home-assistant.html
note: 0
seen: false
---

<p>Après les thèmes sombres, après les cartes Mushroom, après les mini-graphs, voici les
<a href="https://github.com/Anashost/HA-Animated-cards">HA-Animated-cards</a>
!</p>
<p>Si vous avez un dashboard <strong>Home Assistant</strong>, vous connaissez forcement le syndrome du &quot;<em>c'est fonctionnel mais c'est moche</em>&quot;. Des icônes statiques partout, des boutons qui ressemblent à des boutons de formulaire Windows 95... Bref, pas de quoi frimer devant les copains quand ils passent à la maison. Puis je suis tombé grâce à l'ami <strong>G1doot</strong> sur ce petit projet qui devrait vous plaire !</p>
<img src="https://korben.info/ha-animated-cards-home-assistant/ha-animated-cards-home-assistant-1.gif" alt="" loading="lazy" decoding="async">
<p><em>Aperçu des cartes animées en action (
<a href="https://github.com/Anashost/HA-Animated-cards">Source</a>
)</em></p>
<p>HA-Animated-cards, c'est donc une collection de 67 cartes animées pour votre système domotique préféré. Et quand je dis animées, je parle pas d'un bête clignotement. Non non, on a des vraies animations SVG qui donnent vie à vos équipements. Votre
<a href="https://korben.info/hacking-lave-linge-miele-bosch-39c3-domotique.html">lave-linge</a>
tourne vraiment quand il est en cycle, votre ventilateur fait tourner ses pales, votre imprimante 3D montre sa tête d'impression qui bouge... Et hop, votre dashboard passe de triste à vivant !</p>
<p>Le projet signé Anashost propose des cartes pour à peu près tout ce qu'on peut connecter : prises connectées, serrures, projecteurs, sonnettes, arroseurs, radiateurs, rubans LED, lave-vaisselle, cheminées, aspirateurs robots, capteurs de température, d'humidité, de CO2, de qualité d'air... Y'a même des cartes pour votre setup gaming, votre PC, votre serveur home, votre Nintendo Switch ou votre horloge Awtrix.</p>
<p>Bref, de quoi équiper toute la baraque sans vous prendre la tête.</p>
<p>Pour l'installation, c'est pas sorcier. Vous avez besoin de deux dépendances :
<a href="https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/legacy-template.md">mushroom-legacy-template-card</a>
et
<a href="https://forum.hacf.fr/t/personnaliser-ses-cartes-avec-card-mod/4447">card-mod</a>
. Une fois ces deux-là en place, vous copiez le code de la carte qui vous intéresse depuis le GitHub, vous collez dans votre dashboard, vous adaptez les entités à votre config (si vous débutez,
<a href="https://korben.info/comment-faire-fonctionner-un-module-razberry-2-gpio-avec-home-assistant.html">ce tuto peut vous aider</a>
), et hop ça s'affiche ! Le projet propose même des tutoriels YouTube pour ceux qui préfèrent le format vidéo.</p>
<p>Et comme c'est sous licence Creative Commons, vous pouvez bidouiller les animations à votre sauce si le cœur vous en dit.</p>
<p>N'en déplaise aux puristes du &quot;<em>ça marche, on touche plus</em>&quot;, un dashboard qui a de la gueule c'est quand même plus sympa à utiliser au quotidien. Voilà enfin de quoi retrouver le plaisir de piloter sa maison connectée comme un vrai capitaine de vaisseau spatial !</p>
<p>Encore merci à G1doot pour l'info !</p>