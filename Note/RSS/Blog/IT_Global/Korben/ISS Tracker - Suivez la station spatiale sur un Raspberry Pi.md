---
title: "ISS Tracker - Suivez la station spatiale sur un Raspberry Pi"
author: "Korben"
date: 2026-03-16T07:52:53.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/impression-3d"
  - "hardware-diy/raspberry-pi"
  - "impression 3D"
  - "ISS"
  - "maker"
  - "Raspberry Pi"
rss_source: Blog
url: https://korben.info/iss-tracker-raspberry-pi-station-spatiale.html
note: 0
seen: false
---

<p>La <strong>Station Spatiale Internationale</strong> file à 28 000 km/h au-dessus de nos têtes, et y'a un mec qui a décidé de suivre ça en direct depuis un petit écran 3.5 pouces posé sur un Raspberry Pi 3b. Le projet s'appelle
<a href="https://github.com/filbot/iss-tracker">ISS Tracker</a>
, c'est open source, et franchement... c'est plutôt classe !</p>
<p>Concrètement, l'écran affiche un globe terrestre en 3D qui tourne, avec la position de l'ISS en temps réel. Latitude, longitude, altitude, vitesse, et même la région survolée. En fait, la position est récupérée toutes les 30 secondes via des APIs gratuites et interpolée entre les mises à jour pour que le rendu reste fluide. Vous branchez le câble micro-USB, vous attendez le boot, et ça tourne tout seul !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iss-tracker-raspberry-pi-station-spatiale/iss-tracker-raspberry-pi-station-spatiale-1.webp" alt="" loading="lazy" decoding="async">
<p><em>L'ISS Tracker monté au mur, façade alu et globe 3D sur l'écran</em></p>
<p>Côté matos, c'est sobre : un Pi 3b (ou plus récent), un écran LCD Waveshare 3.5 pouces qui se clipse directement sur le GPIO, et un interrupteur à bascule optionnel. Celui-là, c'est la petite touche sympa effet NASA. En un coup de &quot;switch&quot;, vous passez ainsi du tracking orbital à la liste des astronautes actuellement en orbite, groupés par vaisseau.
<a href="https://satellitemap.space/">Du coup vous savez qui est là-haut en ce moment, et dans quel engin</a>
(merci Lorenper).</p>
<p>Mais le truc vraiment cool dans ce projet, c'est le boîtier. Filbot a imprimé la structure en 3D avec du PLA renforcé carbone (les
<a href="https://makerworld.com/en/models/2510676-iss-tracker-housing#profileId-2761043">fichiers STL sont sur MakerWorld</a>
), puis a fraisé la façade en aluminium sur sa CNC personnelle. Plus d'une heure d'usinage pour une plaque (les vrais machinistes pleurent ^^) et la cerise sur la Lune (non c'est pas une hallucination IA, c'est juste que je suis fou) c'est qu'il a séché la peinture dans la chambre chauffée de son imprimante 3D. L'IA qu'il a utilisé pour le guider lui a dit que c'était du génie... on va pas la contredire.</p>
<p>Pour la touche finale, une décalcomanie en transfert à l'eau avec le logo NASA &quot;worm&quot; et des données inventées pour faire officiel + le garde-interrupteur en alu style aviation qui protège le switch, c'est purement cosmétique mais ça envoie grave !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iss-tracker-raspberry-pi-station-spatiale/iss-tracker-raspberry-pi-station-spatiale-2.webp" alt="" loading="lazy" decoding="async">
<p><em>Le globe 3D en action avec la position de l'ISS et la télémétrie</em></p>
<p>Sous le capot, le globe est affiché sous forme de 144 frames pré-calculées avec
<a href="https://cartopy.readthedocs.io/stable/">Cartopy</a>
. Au premier lancement, comptez quelques minutes sur un Pi 3b pour générer le cache et ensuite ça démarre en 3 secondes. Par contre, attention, il faut augmenter le buffer SPI à 307 200 octets parce que le défaut de 4 Ko est beaucoup trop petit pour pousser des frames complètes sur l'écran. Oubliez pas ça, sinon l'affichage ne marchera pas.</p>
<p>D'ailleurs, si vous voulez que l'engin tourne H24, y'a un service systemd fourni avec watchdog, auto-restart et limitation mémoire à 250 Mo. Notez que le fichier <code>theme.toml</code> permet de changer toutes les couleurs, polices et le layout sans toucher au code. Ambiance cockpit Boeing par défaut (labels verts, valeurs blanches sur fond noir), mais vous pouvez faire du cyan fluo si ça vous chante et que vous avez des goûts de chiottes ^^.</p>
<p>Les APIs utilisées sont toutes gratuites et sans clé :
<a href="https://wheretheiss.at">Where the ISS at?</a>
en principal, Open Notify en fallback. Pas d'inscription, pas de token, ça marche direct ! Et si vous aimez les projets Raspberry Pi dans cet esprit, vous pouvez jeter un oeil au
<a href="https://korben.info/rover-martien-imprimer-3d.html">rover martien à imprimer en 3D</a>
ou aux
<a href="https://korben.info/talkiepi-talkie-walkie-a-base-de-raspberry-pi.html">talkies-walkies DIY</a>
à base de Pi.</p>
<p>Bref, de quoi passer kiffer ses soirées à regarder un point lumineux traverser le globe. C'est plutôt méditatif !</p>
<p>
<a href="https://blog.adafruit.com/2026/03/13/international-space-station-tracker-piday-raspberrypi/">Source</a>
</p>