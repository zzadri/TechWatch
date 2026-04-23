---
title: "CANviz - Analyser le bus CAN de sa voiture dans le navigateur"
author: "Korben ✨"
date: 2026-04-23T13:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "CAN bus"
  - "hacking"
  - "navigateur"
  - "open source"
  - "Python"
  - "sécurité automobile"
rss_source: Blog
url: https://korben.info/can-bus-analyzer-navigateur.html
note: 0
seen: false
---

<p>Vous voulez comprendre ce qui se passe dans le cerveau de votre bagnole ? Hé bien pour cela avant, il fallait du matos pro et des suites logicielles à licence annuelle. Mais maintenant, y'a
<a href="https://github.com/Chanchaldhiman/CANviz">CANviz</a>
.</p>
<p>Un <code>pip install canviz</code>, un module USB à quelques balles branché sur le bus CAN de la voiture, et hop, vous accédez à tous les secrets de votre voiture simplement en ouvrant votre navigateur sur localhost:8080. Toutes les trames qui circulent sur le réseau interne du véhicule s'affichent en direct dans un tableau qui défile sans ramer à 2000 fps si j'en crois le README, donc ça envoie !</p>
<img src="https://korben.info/can-bus-analyzer-navigateur/can-bus-analyzer-navigateur-1.gif" alt="" loading="lazy" decoding="async">
<p>Ce projet signé Chanchal Dhiman tourne sur n'importe quelle config équipée de Python 3.10 ou supérieur, et côté matériel, CANviz se branche sur plein de bazars tels que les modules à firmware Candlelight (genre FYSETC UCAN autour de 8 balles ou CANable 1.0 autour de 15), les périphériques slcan via port COM, et du matériel sérieux type PEAK PCAN-USB, Kvaser, Vector ou même socketcan sur Raspberry Pi. En gros, si votre clé USB CAN est compatible avec python-can, CANviz la gère !</p>
<p>L'interface décode alors les fichiers DBC (le format de base de données du CAN), donc au lieu de lire des paquets hexadécimaux chelous, vous voyez directement &quot;vitesse moteur = 1450 rpm&quot; ou &quot;position accélérateur = 34%&quot;. Vous pouvez aussi filtrer par ID ou par nom de signal, et le filtre se garde dans l'URL. Comme ça, vous pouvez partager une vue à un pote en copiant simplement le lien.</p>
<p>Le truc vraiment pratique, c'est surtout la partie enregistrement. Vous capturez une session en .asc ou .csv, et vous la rejouez plus tard à vitesse variable (de 0.5x pour décortiquer lentement, jusqu'à 10x pour survoler), ou vous forgez vos propres trames depuis l'interface pour tester la réaction d'un module donné. Une API REST et du WebSocket ouvrent aussi la porte aux bricolages en Python, avec une doc interactive accessible sur /docs.</p>
<p>Autre truc malin, vu que c'est un serveur web derrière : vous pouvez déployer CANviz sur un Raspberry Pi planqué dans la bagnole et le consulter à distance en SSH. Par contre, pas de WebUSB ici. L'auteur a explicitement fait le choix de passer par python-can côté serveur pour des raisons de sécurité. L'accès USB reste donc dans le sandbox Python, et le browser ne touche rien. J'avoue, je préfère.</p>
<p>Le projet est sous licence MIT, et est encore jeune, mais l'approche est éprouvée. Pour ceux qui cherchent des alternatives desktop, y'a bien sûr
<a href="https://github.com/Schildkroet/CANgaroo">CANgaroo</a>
côté Qt, ou SavvyCAN qui tourne aussi en natif. Et si vous voulez bidouiller votre voiture comme
<a href="https://korben.info/charlie-miller-hacker-legendaire-histoire-complete.html">Charlie Miller l'a fait avec la Jeep</a>
, y'a toujours le Panda de Comma sorti en 2017 avec son soft Cabana.</p>
<p>Bref, pour quelques euros de module USB et un pip install des familles, vous pouvez transformer votre laptop en analyseur CAN niveau pro et ça c'est plutôt classe !</p>
<p>
<a href="https://hackaday.com/2026/04/21/can-bus-analyzer-runs-in-your-browser/">Source</a>
</p>