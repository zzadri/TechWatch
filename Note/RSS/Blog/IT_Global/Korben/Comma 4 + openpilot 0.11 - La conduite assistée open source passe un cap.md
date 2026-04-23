---
title: "Comma 4 + openpilot 0.11 - La conduite assistée open source passe un cap"
author: "Korben"
date: 2026-03-19T10:24:11.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "linux-open-source/logiciels-libres"
  - "robots-drones-vehicules/voitures-electriques"
  - "Comma.ai"
  - "Geohot"
  - "OpenPilot"
  - "voiture autonome"
rss_source: Blog
url: https://korben.info/comma-ai-openpilot-v011-comma-4.html
note: 0
seen: false
---

<p>Vous vous souvenez quand je vous parlais de
<a href="https://korben.info/la-voiture-autonome-de-geohot.html">Geohot et de sa voiture autonome en 2015</a>
? Le mec bidouillait une Acura avec des caméras à 13 balles et rêvait de vendre son kit à 1000 balles. Hé bien 10 ans plus tard, c'est fait ! Et si je vous reparle de ça aujourd'hui, c'est parce que sa société
<a href="https://comma.ai">comma.ai</a>
sort la
<a href="https://blog.comma.ai/011release/">v0.11</a>
d'
<a href="https://korben.info/openpilot-une-assistance-a-la-conduite-open-source.html">openpilot</a>
ainsi qu'un nouveau boîtier qui tient dans la main, le Comma 4 !</p>
<div class="video-container" id="video-container-comma-ai-openpilot-v011-comma-4-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Alors qu'est-ce qui change avec cette version 0.11 ?</p>
<p>En gros, c'est le premier système de conduite assistée dont le modèle est entièrement entraîné dans une simulation générée par un réseau neuronal.</p>
<p>Comma est donc sorti du simulateur classique avec des règles codées à la main pour passer officiellement sur <strong>World Model de 2 milliards de paramètres</strong> qui a avalé 2,5 millions de minutes de vidéo de conduite réelle filmées par les dashcams de leurs anciens boîtiers Comma 3 et 3X pour apprendre à simuler tout ce qu'il se passe sur la route.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-1.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et c'est dans cette simulation apprise que le petit réseau neuronal qui pilote votre voiture s'entraîne. Concrètement, openpilot gère le maintien de voie et l'accélération/freinage sur l'autoroute, un peu comme un super régulateur adaptatif. Résultat avec cette v0.11 (qui succède à
<a href="https://korben.info/openpilot-010-tomb-raider.html">la v0.10 sortie il y a quelques mois</a>
), ça converge mieux en vitesse, ça réagit mieux autour des voitures garées, et les utilisateurs qui l'ont testé préfèrent carrément ce mode Experimental au régulateur classique de leur voiture.</p>
<p>George Hotz, alias Geohot (le génie qui avait hacké l'iPhone à 17 ans puis la PS3), continue de faire les choses à sa manière et c'est pour ça que je l'adore ! Pas de levée de fonds à 10 milliards, pas de partenariat avec un constructeur auto. Non, juste sa dream team à San Diego qui conçoit, fabrique et assemble tout sur place et dernièrement, ils ont même ouvert leur propre datacenter avec 600 GPU et 4 pétaoctets de stockage... le tout pour environ 5 millions de dollars alors que la même infra en cloud leur aurait coûté 5 fois plus cher.</p>
<p>Donc bravo George pour les économies ^^ !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-1.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Côté hardware, le Comma 4 est une petite merveille d'ingénierie. Il est cinq fois plus petit que le Comma 3X, avec la même puissance de calcul (Snapdragon 845 MAX), un écran OLED, triple caméra 360 degrés et un système de refroidissement custom qui ne bride jamais le processeur... le tout sans faire un bruit.</p>
<p>Vous le collez sur votre pare-brise, hop, 5 minutes d'install, pas de temps de séchage (le 3X demandait 48 heures de séchage !), pas besoin de Wi-Fi au démarrage et c'est parti mon kiki. Et c'est compatible avec
<a href="https://comma.ai/vehicles">plus de 300 véhicules</a>
, dont Toyota, Hyundai, Honda, Ford et même des Lexus ou des Kia. Cela coûte 999 dollars, ou 699 si vous renvoyez votre ancien appareil, peu importe son état.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et pour ceux qui se demandent comment ça se compare aux gros... Hé bien pendant que
<a href="https://korben.info/mercedes-level-3-scrapped-humour-tesla-trash.html">Mercedes met en pause son Drive Pilot de niveau 3</a>
parce que ça coûte trop cher à développer, et que Tesla promet le niveau 5 depuis une décennie sans jamais le livrer, comma.ai sort un truc open source qui marche sur beaucoup de bagnoles lambda (pas les françaises, désolé ^^).</p>
<p>Donc pas besoin d'acheter une Tesla à 50 000 euros pour avoir de l'assistance à la conduite potable. Vous gardez votre Toyota ou votre Honda, vous branchez le Comma 4 sur le bus CAN (le réseau interne de votre voiture) et vous avez un truc qui envoie du bois ! Attention par contre, c'est du niveau 2 : donc vous devez garder les mains sur le volant et les yeux sur la route !! Car le problème c'est qu'en France, la légalité de ce genre de boîtier reste floue, donc renseignez-vous bien avant de foncer. Et sauf si votre bagnole est dans la liste de compatibilité, ça ne marchera pas forcément et là faudra suer un peu dans le code et le reverse pour le portage !</p>
<div class="video-container" id="video-container-comma-ai-openpilot-v011-comma-4-2.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-2.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/comma-ai-openpilot-v011-comma-4/comma-ai-openpilot-v011-comma-4-2.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>La v0.11 apporte aussi un détail technique qui a son importance. La consommation en veille du Comma 4 est passée de 225 milliwatts à 52 milliwatts, soit une réduction de 77%. Cela veut dire qu'avant ça vidait la batterie de votre bagnole en quelques semaines si vous le laissiez branché sans démarrer la voiture. Mais maintenant c'est plutôt en mois donc on peut le laisser tout le temps actif, ça passe. Pour réussir cette prouesse, ils ont désactivé les périphériques inutiles sur le microcontrôleur STM32, réduit le voltage scaling de VOS1 à VOS3, et mis le CPU en mode stop... du bel embarqué bien optimisé comme on aime !</p>
<p>Ce que je trouve dingue, c'est que c'est open source et qu'il n'y a encore eu aucun constructeur en Europe qui n'a eu la présence d'esprit d'intégrer ça dans ses bagnoles alors que les Chinois ne font que ça depuis des mois.</p>
<p>Perso, j'ai pas encore craqué pour le Comma 4. À vrai dire j'attends qu'il y ait une petite promo parce que 999 dollars ça pique un peu, mais clairement c'est sur ma liste. Mais en tout cas, je ne peux que saluer le chemin parcouru depuis ce prototype de 2015 conçu dans un garage. C'est quand même dingue ce que fait cette boîte avec une fraction des moyens de Tesla ou de Waymo.</p>
<p>Bref, si la conduite assistée open source vous branche, c'est le moment de s'y intéresser.</p>