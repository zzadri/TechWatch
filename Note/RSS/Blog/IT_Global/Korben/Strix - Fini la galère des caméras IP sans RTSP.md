---
title: "Strix - Fini la galère des caméras IP sans RTSP"
author: "Korben"
date: 2026-03-17T15:51:44.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/domotique-smart-home"
  - "tutoriels-guides"
  - "caméra"
  - "Frigate"
  - "RTSP"
  - "surveillance"
rss_source: Blog
url: https://korben.info/strix-scanner-flux-cameras-ip.html
note: 0
seen: false
---

<p>Vous avez des vieilles caméras de surveillance chinoises qui prennent la poussière parce qu'il vous est impossible de trouver leur flux vidéo ? Y'a pas de RTSP, y'a pas de doc, y'a juste un pauvre port 80 ouvert et une app Android en Mandarin qui est périmée depuis 2021 ?</p>
<p>JE VIENS VOUS SAUVER LES ZAMIS ! Hé oui, grace à
<a href="https://github.com/eduard256/Strix">Strix</a>
qui est capable de tester 102 787 patterns d'URL en 30 secondes et qui vous sort miraculeusement le bon flux vidéo qui marche, avec la config
<a href="https://korben.info/frigate-nvr-local-home-assistant-detection-objets-ia.html">Frigate</a>
prête à être collée.</p>
<p>En fait, le principe est simple. Vous lancez un conteneur Docker, vous entrez l'IP de votre caméra et l'outil bombarde en parallèle toutes les URL connues pour ce type de matos. RTSP sur le port 554, MJPEG sur le 8080, snapshots JPEG sur le 80... et 30 à 60 secondes plus tard, vous avez la liste des flux qui répondent avec résolution, FPS et codec H.264 ou H.265.</p>
<p>L'installation
<a href="https://github.com/eduard256/Strix?tab=readme-ov-file#ubuntu--debian">tient en une ligne</a>
et l'interface web tourne sur le port 4567. Vous entrez l'IP, le login si besoin, et éventuellement le modèle de la caméra IP pour affiner la recherche. Après, même sans modèle, Strix se débrouille avec les 206 patterns les plus courants (sur les 102 787 de la base complète) + la découverte
<a href="https://en.wikipedia.org/wiki/ONVIF">ONVIF</a>
. Du coup ça trouve un flux sur à peu près n'importe quoi, du Dahua au Foscam en passant par les marques fantômes d'AliExpress.</p>
<img src="https://korben.info/strix-scanner-flux-cameras-ip/strix-scanner-flux-cameras-ip-1.gif" alt="" loading="lazy" decoding="async">
<p>Un autre truc vraiment sympa aussi , c'est la génération de config. Vous collez votre fichier frigate.yml existant, même avec 500 caméras dedans, et l'outil ajoute proprement la 501ème sans rien casser ! Il configure automatiquement le flux HD 1080p pour l'enregistrement et le flux 640x480 pour la détection d'objets, le tout passant par
<a href="https://korben.info/go2rtc-couteau-suisse-streaming-video-revolutionner.html">go2rtc</a>
. Résultat, la conso CPU de Frigate peut carrément passer de 30% à 8%.</p>
<p>Et surtout, l'histoire derrière est assez dingue. Le dev derrière ce projet avait des vieux NVR chinois de 2016 qu'il voulait connecter à Frigate. Après 2 ans à tester toutes les URL possibles... rien. Snif... Tous les ports fermés sauf le 80. À vrai dire, ces machins ne parlaient même pas un protocole connu. Alors a fini par faire tout ce que fait un vrai bidouilleur quand il est énervé : Sniffer le trafic de l'app Android avec Wireshark !</p>
<p>Et grâce à cela, il a découvert un truc baptisé BUBBLE, tellement obscur que ça n'existe nulle part sur Google ! Cela lui a permis de construire une base de 67 288 modèles issus de 3 636 marques, des Hikvision jusqu'aux trucs sans nom d'AliExpress.</p>
<p>Et quand y'a pas de RTSP du tout (ce qui arrive souvent avec le matos chinois pas cher), l'outil se rabat sur les snapshots JPEG et les convertit en vrai flux vidéo via FFmpeg. C'est pas aussi clean qu'un vrai stream H.264 (et ça saccade un peu à 10 FPS), mais c'est largement suffisant pour de la détection de personnes ou de bagnoles.</p>
<p>Après, sachez le, ça ne marche qu'avec les caméras présentes sur votre réseau local. Les caméras cloud (Blink, Ring, Xiaomi) ne sont pas supportées. Et aussi, comme on n'est jamais trop prudent d'ailleurs, si vous branchez ce genre de vieux matos chinois, mettez-les dans un VLAN isolé sans accès Internet parce que côté sécurité, c'est la fête du slip sur ce genre de matos : Backdoors, mots de passe en clair sur le port 80, appels serveurs en Chine... va savoir ce qu'elles font quand personne ne regarde.</p>
<p>Strix a même tapé dans l'oeil du développeur de Frigate lui-même, qui a invité l'auteur à soumettre une PR officielle pour l'intégrer dans la doc officielle. Hé ben quelle classe ! Ah et y'a aussi un add-on Home Assistant en beta si vous êtes branchés domotique (pas forcément stable, le soft sous Docker reste plus fiable). Strix est écrit en Go, sous licence MIT, y'a une image Docker de 80-90 Mo sur Alpine Linux, avec FFmpeg et FFprobe embarqués, et ça tourne comme un charme sur AMD64 comme sur ARM64 (votre Raspberry Pi 4 suffit).</p>
<p>Bref, allez tester ça, car y'a clairement de quoi sauver pas mal de matos de la poubelle !</p>