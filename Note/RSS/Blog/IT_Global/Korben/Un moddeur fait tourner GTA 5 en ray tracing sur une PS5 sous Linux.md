---
title: "Un moddeur fait tourner GTA 5 en ray tracing sur une PS5 sous Linux"
author: "Korben"
date: 2026-03-09T11:18:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "jeux-video/pc-gaming"
  - "Linux"
  - "GTA"
  - "PS5"
  - "steam machine"
  - "raytracing"
  - "gtav"
rss_source: Blog
url: https://korben.info/un-moddeur-fait-tourner-gta-5-en-ray-tracing-sur-une-ps5-sous-linux.html
note: 0
seen: false
---

<p>Andy Nguyen, chercheur en sécurité informatique, a réussi à installer Linux sur une PlayStation 5 et à faire tourner GTA 5 Enhanced Edition en 1440p à 60 images par seconde, ray tracing activé. La console se transforme alors en une sorte de « Steam Machine ». Mais l'exploit ne fonctionne que sur les toutes premières PS5, celles qui n'ont jamais été mises à jour depuis leur achat.</p>
<h2 id="gta-5-enhanced-en-1440p-à-60-fps">GTA 5 Enhanced en 1440p à 60 FPS</h2>
<p>Le résultat est assez bluffant. Andy Nguyen, connu sous le pseudo theflow0, a partagé une vidéo montrant GTA 5 Enhanced Edition qui tourne à 60 images par seconde en 1440p avec le ray tracing activé, le tout sur une PS5 standard, pas la Pro. Le processeur tourne à 3,2 GHz et le GPU à 2,0 GHz, des fréquences volontairement bridées parce que la console commence à surchauffer au-delà. En théorie, le CPU pourrait monter à 3,5 GHz et le GPU à 2,23 GHz, mais le système de refroidissement ne suit pas. La sortie vidéo 4K en HDMI fonctionne, le son aussi, et tous les ports USB sont opérationnels. Pour les pilotes graphiques, Nguyen a travaillé avec le projet open source Mesa pour ajouter le support du GPU de la PS5.</p>
<div class="twitter-container" id="twitter-2030011206040256841">
<div class="social-embed-placeholder twitter-placeholder" onclick="loadTwitterEmbed('2030011206040256841')">
<svg class="social-embed-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
</svg>
<div class="social-embed-title">Post X (Twitter)
<div class="social-embed-warning">
En cliquant sur "Charger le post", vous acceptez que X (Twitter) puisse déposer des cookies et collecter des données.
<button class="social-embed-button">Charger le post</button>
<script>
function loadTwitterEmbed(tweetId) {
const container = document.getElementById('twitter-' + tweetId);
container.innerHTML = `
<center class="social-embed-loaded">
<blockquote class="twitter-tweet" data-dnt="true">
<a href="https://twitter.com/x/status/${tweetId}" rel="noopener nofollow"></a>
</blockquote>
</center>
`;
if (!window.twttr) {
const script = document.createElement('script');
script.async = true;
script.src = 'https://platform.twitter.com/widgets.js';
script.charset = 'utf-8';
document.body.appendChild(script);
} else {
window.twttr.widgets.load();
}
}
</script>
<h2 id="un-exploit-réservé-aux-premières-ps5">Un exploit réservé aux premières PS5</h2>
<p>Pour faire tourner Linux sur la console, il faut passer par un exploit appelé Byepervisor, développé par la communauté PS5Dev. Ce hack contourne l'hyperviseur de Sony, la couche de sécurité qui empêche l'exécution de code non autorisé sur la console. Sauf que l'exploit ne marche que sur les firmwares 1.xx à 2.xx, les tout premiers sortis au lancement de la console fin 2020. Si vous avez connecté votre PS5 à Internet ne serait-ce qu'une fois, il y a de grandes chances que le firmware ait été mis à jour automatiquement. On parle donc clairement de consoles qui n'ont pas bougé de leur boîte depuis plus de cinq ans.</p>
<h2 id="la-ps5-transformée-en-steam-machine">La PS5 transformée en Steam Machine</h2>
<p>Nguyen a promis de publier les instructions « avant la sortie de GTA 6 ». Le projet transforme la PS5 en ce qu'il appelle une « Steam Machine », un clin d'œil aux consoles de Valve qui avaient tenté de combiner PC et salon en 2015. Et il y a un argument qui tient la route : avec le prix actuel de la RAM, une PS5 d'occasion toujours équipée de l'ancien firmware pourrait coûter moins cher qu'un PC à performances équivalentes pour jouer sous Linux. Mais bon, encore faut-il trouver une PS5 qui n'a jamais vu la couleur d'une mise à jour, et ce n'est pas exactement le genre de chose qu'on déniche facilement. Si vous en avez une qui traîne, il y a peut-être moyen de vous faire un peu de sous avec !</p>
<p>Quoi qu'il en soit, c'est du beau boulot. On est là sur de l'ingénierie de haut vol, même si on est hélas quand même loin de la bidouille grand public.</p>
<p>Source :
<a href="https://www.xda-developers.com/someone-got-linux-working-on-the-ps5-and-it-runs-gta-5-with-ray-tracing/">XDA Developers</a>
</p>