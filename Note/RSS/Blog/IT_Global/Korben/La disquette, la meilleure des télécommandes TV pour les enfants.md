---
title: "La disquette, la meilleure des télécommandes TV pour les enfants"
author: "Korben"
date: 2026-01-13T12:56:42.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy"
  - "Arduino"
  - "Chromecast"
  - "disquettes"
  - "DIY"
  - "ESP8266"
  - "hardware hacking"
rss_source: Blog
url: https://korben.info/disquettes-telecommande-tv-enfants-tangible-hacking.html
note: 0
seen: false
---

<p>Est-ce que vous vous souvenez du bruit d'un lecteur de disquette ? Ce &quot;clac-clac&quot; mécanique qui signifiait qu'on allait enfin lancer Monkey Island ou Doom ?</p>
<p>Et bien, si vous avez encore un carton de disquettes 3,5 pouces qui traîne au fond du grenier, vous allez pouvoir enfin en faire quelque chose de nouveau en vous inspirant de ce bidouilleur de génie, Mads Chr. Olesen, qui vient de transformer ces reliques en <strong>télécommande TV physique</strong> pour les enfants.</p>
<p>Partant du constat que les télécommandes modernes sont devenues des usines à gaz et que les applis de streaming sont conçues pour nous faire scroller à l'infini, il a voulu créer un truc tangible où une disquette = un déclencheur pour une vidéo (ou une playlist). L'enfant choisit sa disquette, l'insère, et hop, le film se lance sur la TV via un Chromecast. Pas besoin de stocker le film sur les 1,44 Mo de la galette (ce qui serait un exploit en soi), la disquette contient juste une commande de lecture. C'est magique !</p>
<div class="video-container" id="video-container-disquettes-telecommande-tv-enfants-tangible-hacking-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/disquettes-telecommande-tv-enfants-tangible-hacking/disquettes-telecommande-tv-enfants-tangible-hacking-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/disquettes-telecommande-tv-enfants-tangible-hacking/disquettes-telecommande-tv-enfants-tangible-hacking-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Côté technique, c'est du hacking de hardware comme je les aime... Le boîtier cache un duo de choc composé d'un ATmega (type Arduino) pour piloter le lecteur de disquettes et d'un ESP8266 pour causer en WiFi avec le Chromecast. Alors pourquoi deux puces ? Hé bien parce que la lecture des données brutes d'une disquette demande un timing ultra précis que l'ESP8266 a du mal à gérer tout seul à cause de ses tâches WiFi.</p>
<p>Hé ce n'est que ce n'est pas du simple RFID collé sur une disquette puisque le système lit vraiment les données physiques ! Sur chaque disquette préparée, on trouve un petit fichier autoexec.sh (généralement placé sur les premiers secteurs du disque). Ainsi, quand on insère la galette, l'ATmega réveille l'ESP, lit la commande et l'envoie via la liaison série. L'ESP n'a alors plus qu'à piloter le Chromecast via le réseau local pour lancer la vidéo.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/disquettes-telecommande-tv-enfants-tangible-hacking/disquettes-telecommande-tv-enfants-tangible-hacking-2.png" alt="" loading="lazy" decoding="async">
<p>Pour alimenter tout ça, il utilise des batteries 18650 (attention les amis, si vous reproduisez ça, n'oubliez pas le circuit de protection BMS, ça ne rigole pas avec le Lithium) et tout ce petit monde repart en sommeil 30 secondes après l'action pour économiser l'énergie. Et après lecture, petit détail bien geek, la tête se déplace vers la piste 20. Ce n'est pas pour éviter de rayer le disque, mais plutôt pour s'assurer que la tête n'exerce pas de pression prolongée sur la zone de données critique (piste 0) en cas de choc.</p>
<p>Les doigts dans le nez !</p>
<div class="video-container" id="video-container-disquettes-telecommande-tv-enfants-tangible-hacking-2.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/disquettes-telecommande-tv-enfants-tangible-hacking/disquettes-telecommande-tv-enfants-tangible-hacking-2.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/disquettes-telecommande-tv-enfants-tangible-hacking/disquettes-telecommande-tv-enfants-tangible-hacking-2.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Voilà, j'ai trouvé ça très cool, surtout avec ce côté bien retro, mais au delà de ça, c'est un super moyen de redonner du sens au contenu. Ça apprend aux gamins qu'un film, c'est un objet physique qu'on choisit, pas juste un flux infini. Voilà, si vous avez envie de ressortir le fer à souder, foncez voir les détails du projet.</p>
<p>Et bravo à Mads pour cette superbe bidouille !</p>
<p>
<a href="https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/">Source</a>
</p>