---
title: "Un dev prend le contrôle de milliers d'aspirateurs DJI Romo"
author: "Korben"
date: 2026-02-24T14:54:28.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "robots-drones-vehicules/robots-robotique"
  - "aspirateur robot"
  - "DJI"
  - "faille"
  - "MQTT"
rss_source: Blog
url: https://korben.info/dji-romo-faille-securite-aspirateur-robot-7000.html
note: 0
seen: false
---

<p>Un développeur espagnol vient de prendre le contrôle de plus de 10 000 appareils DJI (dont
<a href="https://amzn.to/4ccHUH0">7 000 robots aspirateurs Romo</a>
- <em>lien affilié</em>) répartis dans 24 pays... en voulant juste piloter le sien avec une manette PS5.</p>
<p>Oui oui c'est un grand malade ^^.</p>
<p>À la base, Sammy Azdoufal, responsable IA chez Emerald Stay, voulait juste s'amuser avec son aspi alors il a d'abord essayé d'y connecter sa manette DualSense en Bluetooth, et puis il a fini par utiliser Claude Code pour décompiler l'appli mobile DJI (version Android) et reverse-engineerer les protocoles MQTT de DJI. Bien sûr, il lui fallait un token d'auth pour prouver qu'il était bien proprio du Romo et jusque-là, rien de méchant...</p>
<p>Sauf que le broker MQTT de DJI n'avait AUCUN contrôle d'accès au niveau des topics (c'est la chaîne de caractères qui sert d'adresse pour router les messages entre les publishers et les subscribers). Du coup, avec un seul token TLS, il voyait le trafic de tous les appareils en clair sur le broker cloud de DJI. Pas de brute force, pas d'exploit sophistiqué mais juste un pauvre token et un client MQTT.</p>
<p>Et hop, le voilà avec les flux vidéo des caméras embarquées, les micros, les plans 2D des maisons, les adresses IP et les numéros de série de milliers de machines. Un journaliste de
<a href="https://www.theverge.com/tech/879088/dji-romo-hack-vulnerability-remote-control-camera-access-mqtt">The Verge</a>
lui a même filé son numéro de série, et depuis Barcelone, Azdoufal a pris le contrôle de son Romo, a pu voir qu'il était à 80% de batterie et en train de nettoyer le salon, pour finir par générer le plan de l'appart. Flippant hein ??</p>
<p>En gros, DJI avait un problème de validation de permissions côté backend. Ils l'ont patché début février sauf que... Azdoufal a trouvé une DEUXIÈME faille (un bypass du PIN caméra) qui serait toujours pas corrigée. Cerise sur le gâteau, les batteries DJI Power étaient aussi accessibles via cette archi MQTT. Ce sont de grosses batteries portables qu'on garde chez soit pour avoir un peu de jus en cas de coupure de courant ou quand on est off the grid..</p>
<p>Attention par contre, si vous avez un Romo, vérifiez bien que le firmware est à jour. Vous vous en doutez, DJI a d'abord nié le problème avant de finalement patcher mais bon, moi aussi j'ai une caméra sur mon aspi robot et comme j'adore me balader en slip chez moi, je plains le hacker qui passera par là... Et je vous raconte pas quand on aura des robots humanoïdes comme ce qu'on a vu avec la
<a href="https://korben.info/robot-unitree-faille-bluetooth-ble-hack-securite.html">faille des robots Unitree</a>
, tiens...</p>
<p>
<a href="https://www.techspot.com/news/111443-developer-accidentally-gained-control-more-than-10000-dji.html">Source</a>
</p>