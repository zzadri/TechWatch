---
title: "Un drone imprimé en 3D qui file à 108 km/h grâce à un ESP32"
author: "Korben"
date: 2026-03-16T11:57:25.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/impression-3d"
  - "robots-drones-vehicules/drones"
  - "drone"
  - "ESP32"
  - "impression3d"
  - "open source"
rss_source: Blog
url: https://korben.info/un-drone-imprime-en-3d-qui-file-a-108-km-h-grace-a-un-esp32.html
note: 0
seen: false
---

<p>Un YouTubeur bricoleur a fabriqué un micro-drone de 136 grammes capable de filer à 108 km/h, le tout pour environ 155 dollars de composants et une imprimante 3D. Le petit engin baptisé ESP-Blast tient dans la main, utilise un microcontrôleur ESP32 à quelques dollars et un châssis en plastique PETG. Le créateur compte partager tous les fichiers en open source pour que chacun puisse le reproduire.</p>
<h2 id="un-drone-qui-tient-dans-la-main">Un drone qui tient dans la main</h2>
<p>Le créateur, connu sous le nom de Max Imagination sur YouTube, s'est inspiré de deux équipes qui se disputent le record du drone RC le plus rapide au monde, avec des vitesses qui dépassent les 660 km/h. Son objectif à lui était plus modeste : construire un drone de poche performant avec des composants accessibles à tous.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/pUi1T12QYAU?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le résultat, c'est l'ESP-Blast, un quadcoptère en forme de balle qui décolle à la verticale avant de basculer en vol horizontal. Le châssis est imprimé en PETG sur une Elegoo Neptune 4 Plus et ne pèse que 40 grammes, nez et queue compris.</p>
<h2 id="155-dollars-de-composants">155 dollars de composants</h2>
<p>Côté motorisation, on retrouve quatre moteurs brushless 1104 avec des hélices tripales de 2,5 pouces, pilotés par des variateurs de 8 ampères. Le circuit imprimé a été conçu par Max lui-même dans le logiciel Flux, pour moins de 8 dollars. Il embarque un ESP32 avec accéléromètre, gyroscope, magnétomètre, baromètre et GPS. Le logiciel de vol, c'est du Betaflight en version 10.10.</p>
<p>Une caméra FPV motorisée à l'avant bascule automatiquement selon le mode de vol et transmet en 5,8 GHz la vitesse, la tension batterie et le nombre de satellites. La batterie LiPo 3S de 450 mAh offre environ 5 minutes de vol, ou 2 minutes à fond et 8 en mode tranquille. La portée Wi-Fi de l'ESP32 plafonne à environ 200 mètres. Le budget total tourne autour de 155 dollars, et on peut même descendre à 110 dollars en retirant quelques capteurs.</p>
<h2 id="un-projet-open-source">Un projet open source</h2>
<p>Max prévoit de partager les fichiers 3D et les tutoriels pour que d'autres puissent reproduire ou améliorer le drone. Le projet a demandé pas mal d'assemblage, de tests, de crashs et de réparations avant d'atteindre les 108 km/h en vol.</p>
<p>Il annonce déjà de futures versions pour pousser les performances encore plus loin, et ce n'est visiblement pas son premier essai puisqu'il avait déjà conçu l'ESP-Fly, un micro-drone encore plus petit contrôlable depuis un smartphone.</p>
<p>Pour 155 dollars et un peu de patience, on obtient un
<a href="https://korben.info/drone-fpv-22mm-ingenierie-absurde.html">drone qui</a>
va plus vite que pas mal de modèles du commerce, et qui pèse à peine plus qu'un smartphone. Le fait que tout soit open source et imprimable en 3D rend le projet encore plus intéressant pour les bidouilleurs.</p>
<p>Avec quelques limites quand même, 200 mètres de portée en Wi-Fi et 5 minutes d'autonomie, ça limite un peu l'usage à des vols de démonstration. Mais pour un projet à base d'ESP32 à 3 dollars la puce, les 108 km/h sont impressionnants.</p>
<p>Sources :
<a href="https://www.techspot.com/news/111684-155-esp32-powered-diy-drone-can-hit-67.html">Techspot</a>
,
<a href="https://www.techeblog.com/esp-blast-worlds-smallest-brushless-rocket-drone/">TechEBlog</a>
</p>
<p></p>