---
title: "VidBee - yt-dlp en version graphique avec RSS auto"
author: "Korben"
date: 2026-03-10T09:25:25.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/logiciels-libres"
  - "multimedia-culture/streaming-video"
  - "Docker"
  - "open source"
  - "téléchargement"
  - "Vidéo"
  - "yt-dlp"
rss_source: Blog
url: https://korben.info/vidbee-telechargeur-video-open-source.html
note: 0
seen: false
---

<p>yt-dlp, tout le monde connaît. C'est l'outil parfait pour télécharger des vidéos depuis à peu près n'importe quel site. Sauf que bon, la ligne de commande, c'est pas le truc de tout le monde. Du coup, les interfaces graphiques pour habiller tout ça, y'en a un paquet... mais trouver celle qui est jolie ET sous licence libre, c'est pas gagné.</p>
<p>Heureusement,
<a href="https://github.com/nexmoe/VidBee">VidBee</a>
est un nouveau venu qui coche pas mal de cases. L'appli tourne sur Windows, macOS et Linux, elle est sous licence MIT, et l'interface est plutôt clean. On colle une URL, on choisit le format MP4 ou MKV, on sélectionne la qualité entre 720p et 8K et hop, ça télécharge.</p>
<p>Fastoche !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vidbee-telechargeur-video-open-source/vidbee-telechargeur-video-open-source-2.png" alt="" loading="lazy" decoding="async">
<p><em>Interface principale de VidBee</em></p>
<p>Bon, jusque-là, vous allez me dire que
<a href="https://korben.info/stacher-meilleur-telechargeur-youtube.html">Stacher7</a>
fait déjà ça. Sauf que VidBee a un petit truc en plus qui vaut le détour : <strong>un système de flux RSS intégré</strong>. En gros, vous vous abonnez à vos chaînes YouTube préférées via RSS, et l'outil télécharge automatiquement les nouvelles vidéos en arrière-plan. Comme ça, y'a plus besoin de vérifier manuellement si votre créateur favori a sorti un truc. Attention par contre, prévoyez du stockage parce que ça peut vite remplir un disque dur si vous suivez plusieurs chaînes...</p>
<p>Côté technique, ça gère les résolutions jusqu'à la 8K (si votre écran suit), l'extraction audio seule en MP3, les sous-titres dans plus de 50 langues au format SRT, et même le téléchargement de playlists entières ou de contenus privés si vous êtes connecté à votre compte. Y'a aussi un support proxy pour contourner les restrictions géographiques (genre si votre FAI bloque certains sites) et une extension navigateur pour lancer les téléchargements en un clic.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vidbee-telechargeur-video-open-source/vidbee-telechargeur-video-open-source-3.png" alt="" loading="lazy" decoding="async">
<p><em>File de téléchargement VidBee</em></p>
<p>Et pour les plus bidouilleurs d'entre vous, VidBee propose carrément un mode serveur avec une API Fastify et une interface web, le tout déployable en Docker. Perso, c'est ça que je trouve le plus malin. Un <code>docker compose up -d</code>, l'API écoute sur le port 3100, l'interface web sur le 3000, et vous avez votre propre service de téléchargement accessible depuis n'importe quel appareil du réseau local. Attention quand même à pas le rendre accessible publiquement non plus, hein... sauf si vous voulez des ennuis ^^.</p>
<p>Le projet est plutôt actif, codé en TypeScript et basé sur Electron pour le desktop. D'ailleurs, le monorepo inclut aussi une extension navigateur et un site de doc complet. Par contre, c'est encore en développement très actif, du coup y'a forcément des bugs qui traînent par-ci par-là et des trucs qui cassent de temps en temps mais vu la qualité du service rendu, c'est pas bien grave !</p>
<p>Bref, c'est gratuit, c'est open source, et ça marche sur Windows, macOS et Linux. Allez voir !</p>
<p>Merci à Lorenper pour le partage !</p>