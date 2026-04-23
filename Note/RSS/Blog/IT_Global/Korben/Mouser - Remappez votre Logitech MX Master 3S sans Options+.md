---
title: "Mouser - Remappez votre Logitech MX Master 3S sans Options+"
author: "Korben"
date: 2026-03-16T11:50:48.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "Logitech"
  - "souris"
rss_source: Blog
url: https://korben.info/mouser-remapper-souris-logitech-sans-bloatware.html
note: 0
seen: false
---

<p>Logitech Options+, c'est quand même un truc de fou... Vous achetez une souris à 100 balles, et pour configurer 6 malheureux boutons, faut se créer un compte, accepter de la télémétrie et laisser tourner cette usine à gaz en tâche de fond. Le problème, c'est que sans ce truc, votre
<a href="https://amzn.to/3P3fGF5">MX Master 3S</a>
(<em>lien affilié</em>) est bridée avec des réglages par défaut.</p>
<p>Toutefois un dev bien inspiré a pondu
<a href="https://github.com/TomBadash/Mouser">Mouser</a>
, une alternative open source qui fait la même chose... mais sans le bloatware.</p>
<p>En gros, vous téléchargez un zip de 45 Mo (un exe portable, pas besoin de Python), vous extrayez tout, vous le lancez et boom, vous pouvez alors remapper les boutons de votre
<a href="https://korben.info/test-de-la-nouvelle-logitech-mx-master-4-la-souris-ultime.html">MX Master</a>
3S, les 6 que Mouser prend en charge (clic milieu, bouton geste, retour, avancer, scroll horizontal gauche/droite) + 22 actions prédéfinies : Alt+Tab, copier-coller, contrôle média, navigation web... tout y passe !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mouser-remapper-souris-logitech-sans-bloatware/mouser-remapper-souris-logitech-sans-bloatware-2.png" alt="" loading="lazy" decoding="async">
<p>Le truc cool, c'est ce qui se passe sous le capot puisque Mouser communique directement avec votre souris via le protocole HID++ de Logitech sur Bluetooth. Sur Windows, il intercepte les événements souris avec un hook bas niveau, et sur macOS c'est via CGEventTap. Pour le fameux bouton geste sous le pouce, c'est plus subtil puisqu'il envoie une commande HID++ pour &quot;divertir&quot; le bouton et récupérer les événements bruts plutôt que de laisser le firmware gérer. Y'a eu un peu de reverse engineering de protocole propriétaire, en somme.</p>
<p>Autre truc chouette dans cette appli, ce sont les profils par application. Vous pouvez assigner des actions différentes selon que vous soyez sur Firefox, VS Code ou VLC, et le switch se fait automatiquement en détectant la fenêtre active toutes les 300 ms. C'est grosso modo ce que le logiciel officiel propose pour le remapping, sauf que là ça tourne sans envoyer quoi que ce soit chez Logitech !</p>
<p>Côté réglages, vous pouvez aussi jouer sur le DPI (de 200 à 8 000) et inverser le sens du scroll vertical ou horizontal. Y'a même un moniteur de batterie avec badge coloré et une reconnexion automatique quand la souris sort de veille. C'est carrément pas mal pour un projet communautaire.</p>
<p>Pour le moment, Mouser ne supporte QUE la MX Master 3S connectée en Bluetooth (le récepteur USB n'est que partiellement supporté). Le code est pensé pour être extensible à d'autres souris HID++ de Logitech, mais c'est la seule testée actuellement. Donc au boulot les gars ! Et pour le portage Linux, faudra aussi vous bouger le cul car actuellement seuls macOS et Windows sont supportés.</p>
<p>Ah et il faut absolument qu'Options+ ne tourne pas en même temps, parce que les deux se marchent dessus pour l'accès HID++ ! Et aussi, pas la peine de chercher des options Logitech Flow ou SmartShift là-dedans, car Mouser se concentre uniquement sur le remapping et le DPI, et pas (encore ?) sur le multi-machine.</p>
<p>
<a href="https://github.com/TomBadash/Mouser?tab=readme-ov-file">À découvrir ici !</a>
</p>