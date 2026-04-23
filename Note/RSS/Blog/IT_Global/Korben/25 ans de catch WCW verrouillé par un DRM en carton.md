---
title: "25 ans de catch WCW verrouillé par un DRM en carton"
author: "Korben"
date: 2026-03-10T09:06:40.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture/culture-geek"
  - "vie-privee-anonymat/chiffrement"
  - "DRM"
  - "reverse engineering"
rss_source: Blog
url: https://korben.info/wcw-cyberring-drm-reverse-engineering.html
note: 0
seen: false
---

<p>C'est fou hein, mais un CD-ROM de catch sorti en 1999 a gardé ses vidéos sous DRM durant 25 piges et tout ça juste parce que le serveur qui filait les clés de déchiffrement a disparu. Du coup personne pouvait plus rien lire.</p>
<p>Jusqu'à maintenant.</p>
<p>Le <strong>WCW Internet Powerdisk</strong>, c'était un disque promo glissé dans le magazine WCW. 61 clips vidéo de catch dessus, des matchs Hogan vs Goldberg, des profils de Sting, des intros Monday Nitro... le tout en MPEG-1 à 320x240, 30 fps, et audio MP2 mono à 64 kbps. Pour lire ces vidéos, fallait passer par UlPlayer.exe qui allait chercher une clé sur un serveur distant. Et quand le serveur a disparu vers 2000, 51 minutes de contenu sont devenues inaccessibles. Du jour au lendemain. Verrouillé pour TOUJOURS... enfin presque.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wcw-cyberring-drm-reverse-engineering/wcw-cyberring-drm-reverse-engineering-1.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Car un dev a décidé de s'attaquer au problème en analysant le programme de chiffrement utilisé à l'époque. Et le chiffrement PAVENCRYPT (oui c'est son petit nom), c'est juste une clé qui boucle sur chaque octet du fichier. Chaque fichier a sa propre clé, mais on est clairement sur du niveau exercice de première année en crypto, dans l'esprit du ROT13.</p>
<p>Et comme les fichiers MPEG-1 ont une structure connue, il suffit de regarder la fin du fichier chiffré pour deviner la clé. Un simple calcul, quelques secondes, et c'est plié. Sauf si le fichier est corrompu (là bon courage).</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wcw-cyberring-drm-reverse-engineering/wcw-cyberring-drm-reverse-engineering-2.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Résultat, 61 fichiers sur 61 récupérés ! 51 minutes de catch WCW avec des matchs, des promos, des segments scénarisés... tout ça converti en H.264 et mis en ligne sur l'
<a href="https://archive.org/details/wcw-cyberring-powerdisk-1999">Internet Archive</a>
. Le
<a href="https://github.com/blakebratcher/wcw-cyberring-pav-decryptor">déchiffreur est en Python</a>
mais attention par contre, ça ne marche que sur les fichiers .PAV au format PAVENCRYPT, et pas sur n'importe quel chiffrement des années 90 ^^.</p>
<p>D'ailleurs, ce genre de DRM propriétaire des années 90, c'était monnaie courante. Y'a tout un tas de
<a href="https://korben.info/retro-exo-collections-jeux-dos-windows-scummvm.html">vieux contenus numériques qui pourrissent derrière des verrous obsolètes</a>
. Ici la protection a survécu plus longtemps que l'entreprise qui l'a fabriquée, qui a purement et simplement disparu.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wcw-cyberring-drm-reverse-engineering/wcw-cyberring-drm-reverse-engineering-3.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Après, le chiffrement était tellement basique que c'est pas non plus un exploit de DINGUE. N'importe qui avec Python et des notions de crypto aurait pu faire pareil, sauf que personne n'avait essayé, donc voila, bravo !!</p>
<p>Comme quoi, un DRM n'a pas besoin d'être costaud pour bloquer du contenu pendant un quart de siècle. Suffit que personne ne s'y intéresse.</p>