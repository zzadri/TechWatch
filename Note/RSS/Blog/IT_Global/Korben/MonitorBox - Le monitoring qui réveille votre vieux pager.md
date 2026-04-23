---
title: "MonitorBox - Le monitoring qui réveille votre vieux pager"
author: "Korben"
date: 2026-02-01T11:48:15.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "hardware-diy"
  - "Debian"
  - "monitoring"
  - "open source"
  - "pager"
  - "POCSAG"
  - "recycler"
rss_source: Blog
url: https://korben.info/monitorbox-le-monitoring-qui-reveille-votre-vieux-pager.html
note: 0
seen: false
---

<p>Brice, un lecteur de Korben, m'a bel et bien scotché. Il y a quelques semaines, je vous parlais du
<a href="https://korben.info/wifi-pineapple-histoire-darren-kitchen-hak5.html">Pineapple Pager</a>
et ça a visiblement réveillé une fibre nostalgique chez certains d'entre vous. Donc merci à Brice pour l'info, car il a carrément passé sa soirée à coder un truc <strong>énoooOOOooorme</strong> (et super utile) qui s'appelle <strong>
<a href="https://www.ihaveto.be/2026/01/pourquoi-jai-ressuscite-le-pager-des.html">MonitorBox</a>
</strong>.</p>
<p>Parce qu'on va pas se mentir, on croule tous sous les notifications. Entre Slack, les emails, et les alertes de sécurité, notre cerveau a fini par développer un mécanisme de défense radical : <strong>il ignore TOUT !!!</strong> C'est ce qu'on appelle la &quot;<em>fatigue de l'alerte</em>&quot;. J'avoue que pour un admin sys en astreinte, c'est le début de la fin. Le jour où le serveur de prod tombe vraiment, on swipe la notif comme si c'était une pub pour des croquettes bio... Pas terrible donc pour la continuité de service.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/monitorbox-le-monitoring-qui-reveille-votre-vieux-pager/monitorbox-le-monitoring-qui-reveille-votre-vieux-pager-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de MonitorBox - sobre mais efficace (
<a href="https://github.com/simple-group/MonitorBox">Source</a>
)</em></p>
<p>Et c'est là que Brice intervient justement avec son idée de génie : <strong>Ressusciter le bon vieux pager des années 90</strong>. Au début je pensais que c'était juste pour le fun (un délire de vieux geek quoi), mais en réalité c'est un vrai outil de surveillance pro.</p>
<p><strong>MonitorBox</strong> est conçu pour tourner sur un vieux PC recyclé (genre un vieux <strong>Dell Optiplex GX270</strong> ou un <strong>ThinkPad T60</strong>) sous <strong>Debian 12 Bookworm</strong> et l'idée, c'est de sortir l'alerte critique du flux continu de votre smartphone pour l'envoyer sur un appareil qui ne sert qu'à ça. Ainsi, quand le beeper à votre ceinture se met à gueuler sur la fréquence <strong>466.975 MHz</strong>, vous savez que la maison brûle, sans même regarder l'écran.</p>
<p>Et techniquement, c'est hyper propre !!! Le système utilise une vue Terminal (parfaite pour un vieil écran CRT qui traîne) et un dashboard web moderne sous <strong>JavaScript</strong> pour le suivi. L'arme secrète reste ensuite le support du protocole <strong>POCSAG</strong>.</p>
<p>Via le port série (type <code>/dev/ttyS0</code> ou un adaptateur <strong>FTDI</strong>), <strong>MonitorBox</strong> pilote un émetteur radio qui se charge de balancer les infos sur les ondes. Et toudoum, voilà comment votre vieux Tatoo ou Tam-Tam reprend du service !</p>
<p>⚠️ <em>Attention quand même, émettre sur des fréquences radio est ultra-réglementé. Vérifiez donc bien la législation avant de jouer les apprentis sorciers, car pas moyen de plaider l'ignorance si les mecs de l'ANFR débarquent chez vous avec leur camionnette de détection Agence Tous Risques...</em></p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/monitorbox-le-monitoring-qui-reveille-votre-vieux-pager/monitorbox-le-monitoring-qui-reveille-votre-vieux-pager-3.png" alt="" loading="lazy" decoding="async">
<p>J'adore perso son approche qui vise le &quot;<em>Zéro faux positif</em>&quot;. En effet, le script s'appuie sur <strong>Shell</strong>, <strong>curl</strong> et <strong>espeak</strong> pour la synthèse vocale locale, et intègre une logique de &quot;Retry&quot; comme ça si un service ne répond pas, l'outil vérifie à nouveau avant de vous réveiller en pleine nuit. Ça réduit drastiquement les fausses alertes, contrairement aux outils de
<a href="https://korben.info/btop-alternative-htop-monitoring-systeme-gpu.html">monitoring</a>
habituels qui hurlent parfois au loup pour une micro-latence passagère de rien du tout.</p>
<p>MonitorBox est léger (pas besoin de base de données SQL compliquée, juste un fichier <code>servers.conf</code>), souverain, et permet de redonner vie à du matos qu'on croyait bon pour la déchetterie.</p>
<p>Brice nous propose en gros un mix parfait entre low-tech et haute performance. Et si vous voulez tester le bousin, tout le code est open source (licence MIT) et
<a href="https://github.com/simple-group/MonitorBox">disponible sur GitHub</a>
. Seul petit bémol, il vous faudra bel et bien un vrai câble <strong>DB9</strong> ou <strong>DB25</strong> et un adaptateur qui tient la route, sinon votre VM va juste vous envoyer bouler violemment. Aaaah ces drivers USB chinois, je vous jure...</p>
<p>Bref, merci Brice pour l'inspiration et pour ce beau projet à la fois rétro et moderne !</p>