---
title: "Nearby Glasses - L'app qui détecte les lunettes caméra Meta"
author: "Korben"
date: 2026-02-26T14:41:47.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "vie-privee-anonymat"
  - "vie-privee-anonymat/surveillance-tracking"
  - "Android"
  - "Bluetooth"
  - "défense de la vie privée"
  - "open source"
  - "Ray-Ban Meta"
rss_source: Blog
url: https://korben.info/nearby-glasses-detection-lunettes-camera-meta.html
note: 0
seen: false
---

<p>Les <strong>Ray-Ban Meta,</strong> c'est quand même le gadget parfait pour les voyeurs technophiles. Ce sont quand même des lunettes qui filment, prennent des photos et diffusent en live... le tout sans que PERSONNE autour ne s'en rende compte (ou presque). Alors forcément, quelqu'un a fini par coder une app pour les détecter !</p>
<p>
<a href="https://github.com/yjeanrenaud/yj_nearbyglasses">Nearby Glasses</a>
, c'est une application Android développée par Yves Jeanrenaud qui scanne en permanence les signaux Bluetooth Low Energy autour de vous. Chaque appareil BLE diffuse en fait des trames pour s'annoncer avec un identifiant constructeur et les lunettes caméra de Meta utilisent les IDs 0x01AB et 0x058E (Meta Platforms) ainsi que 0x0D53 (Luxottica/Ray-Ban). Donc cette app écoute ces identifiants et vous balance une alerte dès qu'elle en capte un.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/nearby-glasses-detection-lunettes-camera-meta/nearby-glasses-detection-lunettes-camera-meta-2.png" alt="" loading="lazy" decoding="async">
<p>La détection repose sur le RSSI, en gros la puissance du signal reçu et par défaut, le seuil est à -75 dBm, soit environ 10-15 mètres en extérieur et 3-10 mètres en intérieur. Donc c'est pas foufou non plus mais c'est configurable, évidemment. Vous pouvez donc le durcir un peu pour ne choper que les lunettes vraiment proches, ou l'assouplir pour ratisser large (au prix de faux positifs en pagaille).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/nearby-glasses-detection-lunettes-camera-meta/nearby-glasses-detection-lunettes-camera-meta-3.png" alt="" loading="lazy" decoding="async">
<p>Les faux positifs, parlons-en d'ailleurs... Les casques Meta Quest utilisent les mêmes identifiants constructeur, du coup ça ne marche pas à tous les coups. Par exemple, si votre voisin joue en VR, votre téléphone va sonner ! L'app détecte aussi les Snap Spectacles (0x03C2)... pour les trois personnes qui en portent encore ^^.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/nearby-glasses-detection-lunettes-camera-meta/nearby-glasses-detection-lunettes-camera-meta-4.png" alt="" loading="lazy" decoding="async">
<p>Ah et l'app est UNIQUEMENT pour Android. La version iOS serait &quot;on the way&quot; selon le développeur... faut donc pas être pressé mais au moins c'est open source (AGPL-3.0), du coup n'importe qui peut vérifier ce que l'app fait de vos données Bluetooth.</p>
<p>Si le sujet vous parle, vous connaissez peut-être
<a href="https://korben.info/banrays-detecteur-lunettes-cameras-meta-ray-ban.html">Ban-Rays</a>
, un projet hardware à base d'Arduino et de LEDs infrarouges qui détecte les Ray-Ban Meta via infrarouge et Bluetooth ! Hé bien Nearby Glasses, c'est l'approche 100% logicielle plutôt que hardware, ce qui est plus accessible mais forcément plus limitée... pas besoin de fer à souder, cela dit ^^.</p>
<p>C'est une rustine mais bon, c'est mieux que de se retrouver à poil sans permission sur le web.</p>
<p>
<a href="https://manualdousuario.net/en/nearby-glasses-app-camera-meta-alert/">Source</a>
</p>