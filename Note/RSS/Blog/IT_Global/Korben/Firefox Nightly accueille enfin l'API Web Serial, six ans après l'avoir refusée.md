---
title: "Firefox Nightly accueille enfin l'API Web Serial, six ans après l'avoir refusée"
author: "Korben"
date: 2026-04-15T08:22:25.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "reseaux-internet/navigateurs-web"
  - "Firefox"
  - "web serial"
rss_source: Blog
url: https://korben.info/firefox-nightly-accueille-enfin-lapi-web-serial-six-ans-apres-lavoir-refusee.html
note: 0
seen: false
---

<p>Six ans. C'est le temps qu'il aura fallu à Mozilla pour changer d'avis sur l'API Web Serial. Firefox Nightly 151 l'intègre désormais, avec activation via un flag à aller chercher dans le menu. Le premier commit côté code date de mi-janvier, et le déploiement pour les utilisateurs Nightly est effectif depuis le 13 avril.</p>
<p>Pour ceux qui ne connaissent pas, Web Serial est l'API standardisée qui permet à une page web de communiquer directement avec un périphérique série connecté en USB, en Bluetooth ou via un vrai port série.</p>
<p>Imprimante 3D, Arduino, carte ESP32, débogueur JTAG, microcontrôleur industriel, hub domotique, tout ce qui expose une liaison série peut être piloté depuis du JavaScript. C'est par exemple ce qui fait tourner l'IDE Arduino en ligne, Espruino, les flasheurs ESP dans le navigateur, et une bonne partie de la scène maker moderne.</p>
<p>Chrome, Edge, Opera et Vivaldi supportent Web Serial depuis 2020. Firefox, lui, tenait une position claire, trop risqué, le consentement utilisateur ne protège pas assez, la surface d'attaque sur le matériel connecté est bien trop large.</p>
<p>Un ingénieur de Mozilla l'avait écrit noir sur blanc à l'époque. Les utilisateurs Firefox qui bidouillaient avec des cartes électroniques étaient de fait poussés sur Chrome ou sur une extension tierce bancale. En 2026, Mozilla rend les armes et aligne Firefox sur le reste de l'écosystème, Apple mis à part.</p>
<p>Apple, justement, reste fermement opposé à Web Serial, WebUSB et WebHID côté WebKit. Les arguments avancés sont les mêmes qu'à l'époque Mozilla, fingerprinting, sécurité, risques sur l'OS.</p>
<p>Safari n'intégrera pas l'API dans un avenir prévisible. Donc en pratique, si vous avez une webapp qui dialogue avec du matos, iOS et iPadOS restent hors-jeu pour cet usage.</p>
<p>Côté permissions, Web Serial exige une validation utilisateur explicite pour chaque périphérique, avec une fenêtre de sélection gérée par le navigateur. Le site ne peut pas lister les ports disponibles sans action.</p>
<p>C'est un garde-fou correct, mais qui ne supprime pas le risque de phishing physique (un site malveillant qui vous demande de sélectionner un périphérique sous un prétexte bidon).</p>
<p>Pour les makers, l'arrivée dans Firefox est une vraie bonne chose. Ça fait un navigateur supplémentaire pour flasher un ESP depuis le web, une option pour ceux qui refusent Chrome par principe, et un moins gros verrou à faire sauter pour les tutoriels d'électronique amateur. La version stable devrait arriver dans quelques mois si les retours Nightly sont propres.</p>
<p>Bref, Firefox s'aligne, Apple s'isole, et la bidouille matérielle reprend ses droits dans le navigateur, tout va bien.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/14/firefox_nightly_web_serial/">The Register</a>
</p>