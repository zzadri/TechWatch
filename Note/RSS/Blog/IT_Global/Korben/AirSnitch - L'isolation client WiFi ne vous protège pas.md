---
title: "AirSnitch - L'isolation client WiFi ne vous protège pas"
author: "Korben"
date: 2026-02-27T08:25:01.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "reseaux-internet/wifi-reseau-local"
  - "attaque réseau WiFi"
  - "Man In The Middle"
  - "sécurité Wifi"
rss_source: Blog
url: https://korben.info/airsnitch-isolation-client-wifi-contournee.html
note: 0
seen: false
---

<p>Bon, vous connaissez la théorie du travailleur nomade... vous vous posez dans un café avec votre laptop, vous chopez du WiFi gratuit, et vous vous dites que <strong>l'isolation client du routeur</strong> vous protègera des autres branquignols connectés au même réseau.</p>
<p>Hé ben non ! Car des chercheurs viennent de démontrer que cette protection, c'était du vent... Oui oui, tous les routeurs qu'ils ont testés se sont fait contourner en 2 secondes.</p>
<p>Mais avant, pour ceux qui se demandent ce que c'est, l'isolation client c'est une option que les admins réseau activent sur les bornes WiFi pour empêcher les appareils connectés de communiquer entre eux. En gros, votre laptop ne peut pas voir celui du voisin. Enfin... ça c'est en théorie.</p>
<p>Parce qu'en fait, le truc c'est que cette fonctionnalité n'est même pas définie dans le standard WiFi (IEEE 802.11) ce qui oblige chaque fabricant à faire sa propre tambouille dans son coin, et du coup ça fuit de partout.</p>
<p>L'équipe derrière cette trouvaille, c'est des chercheurs de l'UC Riverside et de KU Leuven, dont Mathy Vanhoef, le même gars qui avait déjà mis le WPA2 à genoux avec
<a href="https://korben.info/detecter-attaque-krack-contre-wifi.html">KRACK</a>
en 2017. Pas un amateur, quoi et leur outil, baptisé <strong>AirSnitch</strong>, vient d'être présenté à la conférence
<a href="https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/">NDSS 2026</a>
.</p>
<p>Ils ont ainsi trouvé 3 méthodes différentes pour contourner la protection d'isolation. <strong>La première abuse de la clé de groupe</strong> (GTK), normalement réservée au broadcast, pour envoyer du trafic directement à un appareil ciblé. Le pire, c'est que macOS, iOS et Android acceptent ce trafic sans broncher (merci les gars !).</p>
<p><strong>La seconde fait rebondir les paquets via la passerelle</strong>, et <strong>la troisième vole carrément l'adresse MAC</strong> de la victime sur un autre point d'accès pour intercepter son trafic.</p>
<p>Brrrrrr.... 11 routeurs testés, du Netgear R8000 au Cisco Catalyst 9130 en passant par TP-Link, ASUS, Ubiquiti et même OpenWrt 24.10. Et ils sont TOUS vulnérables, sans exception ! Et que vous soyez en
<a href="https://korben.info/cracker-cle-wpa.html">WPA2</a>
ou en WPA3, réseau perso ou entreprise, c'est pareil. Donc autant vous dire que ça pue !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/airsnitch-isolation-client-wifi-contournee/airsnitch-isolation-client-wifi-contournee-2.png" alt="" loading="lazy" decoding="async">
<p>Ils ont même réussi à effectuer un Man-in-the-Middle complet (interception de tout le trafic entre vous et Internet) en 2 secondes chrono. La &quot;victime&quot; qui regardait YouTube n'a même pas remarqué de lag et c'est comme ça qu'ils on pu intercepter tout son trafic, ni vu ni connu.</p>
<p>Alors du coup, on fait quoi ? Hé bien si vous gérez un réseau, oubliez l'isolation client toute seule et passez aux VLANs avec un VLAN par client. Oui c'est lourdingue à mettre en place, mais c'est le prix à payer pour avoir une sécurité solide. Certains constructeurs bossent aussi sur des clés de groupe individuelles par client, ce qui règlerait le problème à la source.</p>
<p>Côté utilisateur, la solution est plus simple...
<a href="https://korben.info/categories/vie-privee-anonymat/vpn-proxy/">VPN !!</a>
Attention, ça ne marche que si le VPN est activé AVANT de vous connecter au réseau, pas après. HTTPS vous protège déjà pour le contenu des sites, mais selon Google, 6 à 20% des pages ne sont toujours pas en HTTPS... et même quand elles le sont, l'attaquant voit quand même où vous surfez et peut tenter du DNS spoofing. Donc sur n'importe quel
<a href="https://korben.info/wifi-pineapple-histoire-darren-kitchen-hak5.html">réseau WiFi public</a>
, partez du principe que quelqu'un peut voir votre trafic, parce que visiblement c'est le cas.</p>
<p>Le code source d'
<a href="https://github.com/vanhoefm/airsnitch">AirSnitch</a>
est dispo sur GitHub si vous voulez tester votre propre config mais notez que ça nécessitera
<a href="https://amzn.to/4r2nZhD">une carte WiFi compatible avec le mode monitor comme les Alfa</a>
(<em>lien affilié</em>), donc pas celle de votre laptop de base.</p>
<p>Bref, la prochaine fois que le WiFi de l'hôtel vous demande d'accepter les CGU en échange d'un accès &quot;sécurisé&quot;... ben gardez votre VPN allumé, hein.</p>
<p>
<a href="https://arstechnica.com/security/2026/02/new-airsnitch-attack-breaks-wi-fi-encryption-in-homes-offices-and-enterprises/">Source</a>
</p>