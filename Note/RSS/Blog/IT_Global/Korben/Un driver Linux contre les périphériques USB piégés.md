---
title: "Un driver Linux contre les périphériques USB piégés"
author: "Korben"
date: 2026-04-07T07:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "linux-open-source/administration-serveur"
  - "badusb"
  - "kernel"
  - "Linux"
  - "sécurité informatique"
  - "USB"
rss_source: Blog
url: https://korben.info/linux-driver-hid-malveillant-protection-noyau.html
note: 0
seen: false
---

<p>Vous vous souvenez de BadUSB ? Mais siiii, c'est ce truc dévoilé en 2014 à la Black Hat qui avait foutu la trouille à tout le monde. Ça montrait qu'un simple périphérique USB pouvait se faire passer pour un clavier et balancer des commandes à votre place. Hé bien depuis, les attaques se sont bien raffinées et c'est pourquoi un dev vient de proposer un module kernel Linux capable de détecter ces saloperies.</p>
<p>Enfin !</p>
<p>Ce module s'appelle
<a href="https://lore.kernel.org/lkml/20260404133746.80914-1-zybo1000@gmail.com/">hid-omg-detect</a>
et c'est signé Zubeyr Almaho. Le patch (déjà en v2) a été soumis le 4 avril dernier sur la LKML. Alors je pense que vous allez vous dire que c'est encore un truc qui va bloquer par défaut vos périphériques USB sauf que non, ça ne bloque rien. En fait, il surveille passivement les périphériques HID (claviers, souris...) et leur attribue un score de suspicion basé sur trois critères.</p>
<p>D'abord, l'entropie des frappes clavier. Un humain tape de manière irrégulière, avec des pauses, des hésitations, des fautes (perso je fais au moins 3 fautes de frappe par phrase ^^). Un câble trafiqué, lui, balance ses commandes avec une régularité de métronome, genre 500 caractères en 2 secondes sans une seule erreur. Ensuite, y'a la latence entre le branchement et la première frappe. Si votre &quot;clavier&quot; commence à taper immédiatement après avoir été branché... y'a comme un souci. Et enfin, le fingerprinting des descripteurs USB pour repérer les vendor/product IDs suspects ou les anomalies dans les descripteurs HID.</p>
<p>Pas con hein ? Et si le score dépasse un certain seuil (configurable), hop, le module balance un warning dans <code>dmesg</code> et vous oriente vers
<a href="https://usbguard.github.io/">USBGuard</a>
pour bloquer le périphérique. Parce que hid-omg-detect ne touche à rien lui-même. Il sonne juste l'alarme, et c'est à vous d'agir !</p>
<p>Mais alors pourquoi lancer ça maintenant ?</p>
<p>Hé bien parce que les outils d'attaque USB sont devenus légion ! Les
<a href="https://shop.hak5.org/products/omg-cable">câbles O.MG</a>
(créés par le chercheur MG et distribués via Hak5), par exemple, ça ressemble à un câble USB lambda que vous emprunteriez sans réfléchir pour charger votre téléphone. Sauf que dedans y'a un implant WiFi capable d'injecter des frappes, de les logger, de spoofer les identifiants USB, le tout contrôlable à distance. Quand je pense qu'il y a quelques mois,
<a href="https://korben.info/lenovo-badcam-badusb-webcam-espion-firmware.html">des chercheurs montraient qu'une simple webcam Lenovo pouvait être transformée en dispositif BadUSB</a>
... Sa fé grav réchéflir 🤓 comme dirait les citoyens souverains ^^.</p>
<p>Maintenant, en attendant que le patch soit accepté, vous n'êtes pas totalement démunis non plus. Des outils comme
<a href="https://korben.info/usbrip-surveillez-les-insertions-de-peripheriques-usb-cle-etc-sur-vos-machines-linux.html">USBRip</a>
(un script Python, <code>pip3 install usbrip</code>) permettent déjà de tracer les connexions et déconnexions USB en parsant <code>/var/log/syslog</code>. Y'a pas ce scoring d'anomalies, mais au moins vous avez un historique pour savoir qui a branché quoi et quand. Et si vous êtes vraiment parano (et franchement, vous avez raison de l'être), USBGuard peut carrément whitelister vos périphériques de confiance et bloquer tout le reste. Mais le problème d'une telle solution c'est que ça demande de maintenir une liste blanche à jour, ce qui n'est pas toujours pratique quand on branche 15 trucs par jour.</p>
<p>On verra si les mainteneurs du kernel l'accepte... Après ça ne protégera pas contre tous les scénarios non plus. Un périphérique qui attend 30 secondes avant de commencer son injection pourrait passer sous le radar. Et si un attaquant injecte du jitter aléatoire dans ses frappes pour simuler un humain, là ce sera plus compliqué. Mais combiné avec USBGuard, ça donnera enfin une vraie ligne de défense native contre les
<a href="https://korben.info/faut-il-vraiment-boucher-ses-ports-usb-au-ciment.html">attaques par périphériques USB piégés</a>
. Et c'est quand même mieux que de boucher ses ports au plâtre et ciment (Mais pleure pas au dessus du mortier...) !</p>
<p>Bref, va falloir garder un œil là-dessus.</p>
<p>
<a href="https://itsfoss.com/news/linux-driver-proposal-malicious-hid-devices/">Source</a>
</p>