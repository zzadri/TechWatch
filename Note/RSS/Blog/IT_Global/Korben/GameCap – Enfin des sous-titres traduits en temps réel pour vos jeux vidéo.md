---
title: "GameCap – Enfin des sous-titres traduits en temps réel pour vos jeux vidéo"
author: "Korben"
date: 2026-01-30T09:32:00.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/pc-gaming"
  - "Deepgram"
  - "GameCap"
  - "jeux vidéo"
  - "jrpg"
  - "open source"
  - "sous-titres"
  - "traduction temps réel"
rss_source: Blog
url: https://korben.info/gamecap-sous-titres-traduction-jeux-video-ia.html
note: 0
seen: false
---

<p>Vous avez déjà ressenti cette frustration monumentale de vouloir lancer un JRPG obscur sorti uniquement au Japon, ou de tomber sur un stream coréen de Starcraft sans comprendre un traître mot de ce qui se raconte ?</p>
<p>Moi non ^^, mais j'imagine que quand on est passionné de gaming, c'est le genre de barrière linguistique qui peut vite briser une hype, voire une vie. Heureusement, y’a un petit outil open source qui vient de débarquer sur Windows et qui va vous la changer (la vie...) : <strong>
<a href="https://vicpitic.github.io/gamecap-lp/">GameCap</a>
</strong>.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gamecap-sous-titres-traduction-jeux-video-ia/gamecap-sous-titres-traduction-jeux-video-ia-2.png" alt="" loading="lazy" decoding="async">
<p>Contrairement à d'autres outils qui essaient de lire le texte à l'écran (souvent avec des résultats foireux), GameCap s'attaque directement au son de votre PC. En gros, il utilise le mécanisme de <strong>WASAPI loopback</strong> pour capturer l'audio de votre système en temps réel. Ce flux sonore est ensuite envoyé vers l'API de <strong>Deepgram</strong> qui s'occupe de la transcription (transformer la voix en texte) avant de passer par les moulinettes de Google Translate pour la traduction finale.</p>
<p>Comme le traitement se fait via des API cloud, notez que vos flux audio partent faire un petit tour sur les serveurs de Deepgram. C'est pas cool mais c'est le prix à payer pour avoir une transcription de haute volée avec une latence quasi imperceptible. Le résultat s'affiche ensuite dans un overlay personnalisable (police, taille, position) que vous pouvez caler n'importe où sur votre écran pour ne pas gêner l'interface de votre jeu ou de votre vidéo. C'est un peu dans la même veine que ce que propose
<a href="https://korben.info/buzz-traduire-transcrire-audio.html">Buzz</a>
, mais optimisé pour l'affichage en surimpression pendant que vous jouez.</p>
<div class="video-container" id="video-container-gamecap-sous-titres-traduction-jeux-video-ia-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/gamecap-sous-titres-traduction-jeux-video-ia/gamecap-sous-titres-traduction-jeux-video-ia-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/gamecap-sous-titres-traduction-jeux-video-ia/gamecap-sous-titres-traduction-jeux-video-ia-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Côté langues, c'est plutôt la fête puisqu'il y a plus de 30 langues supportées, dont les indispensables japonais, coréen et chinois. Et le truc cool, c'est que ça ne se limite pas aux jeux. Que vous soyez sur YouTube, Twitch, VLC ou même en plein call Zoom, GameCap peut vous générer des sous-titres traduits pour n'importe quelle source sonore qui sort de vos enceintes.</p>
<p>Pour l'installer, c'est un projet Python, donc rien de bien méchant. Il vous faudra <strong>Python 3.8</strong> ou plus sur votre bécane. Commencez par cloner le repo GitHub de VicPitic, installez les dépendances avec un classique <code>pip install -r requirements.txt</code> et lancez le launcher.</p>
<p>Il faudra aussi vous créer un compte gratuit sur Deepgram pour récupérer une clé API, sinon l'outil restera muet.</p>
<p>Une fois configuré, vous pouvez même utiliser le launcher pour détecter automatiquement vos jeux Steam et les lancer directement avec l'overlay activé. C'est top pour ceux qui aiment déjà bidouiller leurs jeux, comme avec le
<a href="https://korben.info/sn-operator-epilogue-snes-usb.html">SN Operator</a>
pour lire ses propres cartouches. Et si les sous-titres vous saoulent à un moment, un petit raccourci <code>Ctrl+Shift+S</code> et hop, ils disparaissent.</p>
<p>Voilà, pour du contenu interactif ou pour enfin profiter de ces pépites japonaises jamais traduites, c'est un sacré bel outil. Et en plus c'est gratuit !</p>