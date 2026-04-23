---
title: "Il transforme une carte à 15 euros en station météo sous Windows 95"
author: "Korben"
date: 2026-03-20T09:53:04.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "hardware-diy/impression-3d"
  - "multimedia-culture/culture-geek"
  - "ESP32"
  - "impression3d"
  - "meteo"
  - "Windows95"
rss_source: Blog
url: https://korben.info/il-transforme-une-carte-a-15-euros-en-station-meteo-sous-windows-95.html
note: 0
seen: false
---

<p>Un maker français a fabriqué une station météo miniature avec une interface façon Windows 95, logée dans un boîtier imprimé en 3D en forme de vieux moniteur cathodique. Le projet tourne sur une carte ESP32 à une quinzaine d'euros et récupère la météo en temps réel via Wi-Fi. Prévisions, vent, images satellite, tout y est.</p>
<h2 id="un-mini-écran-façon-années-90">Un mini écran façon années 90</h2>
<p>Jordan Blanchard a publié son projet sur Hackaday.io et le résultat a de quoi plaire aux nostalgiques. L'interface reprend les codes visuels de Windows 95 : fenêtres avec barres de titre, panneaux biseautés, typographie pixelisée.</p>
<p>On y retrouve la météo du jour, les prévisions heure par heure, la vitesse du vent avec boussole, et même des images satellite et radar. Le tout sur un écran TFT de 2,8 pouces en 320 x 240 pixels, ce qui colle parfaitement au style rétro.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/BpXJD4my1uU?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le boîtier est imprimé en 3D et reproduit la forme d'un petit moniteur cathodique. Un mécanisme a été ajouté sur la face avant pour actionner les boutons physiques de la carte, qui se trouvent à l'arrière.</p>
<h2 id="une-quinzaine-deuros-de-matériel">Une quinzaine d'euros de matériel</h2>
<p>La base du projet, c'est un ESP32-2432S028, plus connu sous le nom de Cheap Yellow Display. C'est une carte de développement vendue autour de 15 euros, qui intègre un processeur ESP32 avec Wi-Fi et Bluetooth, un écran tactile TFT de 2,8 pouces, un lecteur micro-SD et un connecteur haut-parleur. Pas besoin de soudure, la carte arrive montée.</p>
<p>Les données météo viennent de l'API Open-Meteo, et le système gère aussi l'affichage d'images de webcams et de satellites. Une batterie lithium avec un module de charge permet de faire fonctionner le tout sans fil.</p>
<h2 id="du-code-arduino-en-libre-accès">Du code Arduino en libre accès</h2>
<p>Le sketch Arduino est téléchargeable sur la page du projet. Jordan précise avoir utilisé ChatGPT pour l'aider sur certaines parties de l'interface, ce qui est assez courant dans la communauté maker.</p>
<p>Le système utilise du réseau asynchrone pour que l'affichage reste fluide pendant le téléchargement des données, et un cache local en SPIFFS pour garder la météo accessible même sans connexion.</p>
<p>C'est le genre de petit projet qui donne envie de s'y mettre. Pour une quinzaine d'euros de matériel et un peu de temps, on obtient un objet qui a du charme et qui est utile au quotidien. Et puis retrouver l'interface de Windows 95 sur un écran de 2,8 pouces, ça a quand même un petit côté régressif assez plaisant.</p>
<p>Source :
<a href="https://hackaday.io/project/205193-win95-retro-weather-display">Hackaday</a>
</p>