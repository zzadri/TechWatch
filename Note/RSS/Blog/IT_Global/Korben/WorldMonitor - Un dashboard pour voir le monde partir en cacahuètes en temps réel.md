---
title: "WorldMonitor - Un dashboard pour voir le monde partir en cacahuètes en temps réel"
author: "Korben"
date: 2026-02-24T13:52:27.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "linux-open-source/logiciels-libres"
rss_source: Blog
url: https://korben.info/worldmonitor-dashboard-intelligence-temps-reel.html
note: 0
seen: false
---

<p>
<a href="https://worldmonitor.app/">WorldMonitor</a>
, c'est un dashboard open source qui agrège en temps réel à peu près <strong>TOUT ce qui se passe sur la planète</strong>. Géopolitique, conflits armés, marchés financiers, menaces cyber, catastrophes naturelles, trafic maritime... le tout sur une carte interactive avec 35 couches de données superposables !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/worldmonitor-dashboard-intelligence-temps-reel/worldmonitor-dashboard-intelligence-temps-reel-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le truc, c'est que c'est pas juste un agrégateur de news. Là-dedans y'a 150+ flux RSS, du tracking de 220+ bases militaires, du suivi de vols militaires en direct via ADS-B, de la surveillance des câbles sous-marins, et même de la détection de feux de forêt par satellite via NASA FIRMS.</p>
<p>Ah et y'a aussi 8 flux vidéo live (Bloomberg, Al Jazeera, France24...), un index d'instabilité par pays calculé en temps réel et il y a même
<a href="https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_pizza_du_Pentagone">l'indice Pizza du Pentagone</a>
.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/worldmonitor-dashboard-intelligence-temps-reel/worldmonitor-dashboard-intelligence-temps-reel-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Rien que ça !</p>
<p>Côté IA, le dashboard génère des briefs de situation via un LLM et bon, le plus sympa c'est que ça peut tourner en local si vous le désirez (c'est compatible avec Ollama et LM Studio). ZÉRO donnée ne sort de votre machine, du coup, pour ceux qui font de l'
<a href="https://korben.info/intercept-sigint-dashboard-rtl-sdr.html">OSINT</a>
ou qui veulent juste
<a href="https://korben.info/change-detection-surveillance-automatique-sites-web.html">surveiller ce qui bouge</a>
dans le monde, c'est du lourd.</p>
<p>Perso j'ai choisi World pour mon test car l'angle géopolitique est dingue et y'a aussi une variante Tech et une Finance si les marchés c'est votre came. Attention par contre, faut pas être allergique à la surcharge d'infos ! Et sauf si vous avez un écran ultra-wide, ça peut vite devenir le bordel.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/worldmonitor-dashboard-intelligence-temps-reel/worldmonitor-dashboard-intelligence-temps-reel-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Je vous avoue que c'est pas le truc que je vais utiliser au quotidien parce que je suis plutôt à fuir l'actualité internationale et même nationale pour me recentrer uniquement sur moi et sur l'actualité tech que j'aime tant. Mais pour les accro à l'anxiété, je pense que vous allez kiffer.</p>
<p>Voilà, ce projet tourne en TypeScript + React avec deck.gl pour le globe 3D, c'est dispo en 16 langues et y'a même une app desktop via Tauri. Après franchement, faut voir si votre ordi tient le coup avec tous ces flux en temps réel...</p>
<p>Merci à François pour le partage !</p>