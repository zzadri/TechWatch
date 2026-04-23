---
title: "Apple corrige une grosse faille de sécurité sur les anciens iPhone et iPad"
author: "Korben"
date: 2026-03-12T13:24:48.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/iphone-ipad"
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/malwares-menaces"
  - "coruna"
  - "faille"
  - "iOS"
  - "iPad"
  - "iPhone"
rss_source: Blog
url: https://korben.info/apple-corrige-une-grosse-faille-de-securite-sur-les-anciens-iphone-et-ipad.html
note: 0
seen: false
---

<p>Apple vient de publier iOS 16.7.15 et iOS 15.8.7 pour les anciens iPhone et iPad. Ces mises à jour corrigent des failles activement exploitées par Coruna, un kit d'espionnage qui combine 23 vulnérabilités pour compromettre un appareil simplement en chargeant une page web, je vous en parlais ici. Si vous avez encore un iPhone 6s, 7, 8 ou X, la mise à jour est urgente.</p>
<h2 id="doù-vient-coruna-">D'où vient Coruna ?</h2>
<p>Google et iVerify ont rendu public le kit Coruna le 3 mars. Il regroupe 23 failles en cinq chaînes d'exploitation et cible les iPhone sous iOS 13 à iOS 17.2.1. L'outil aurait été conçu par une filiale de L3Harris Technologies, un sous-traitant de défense américain, et vendu à des agences gouvernementales alliées des États-Unis.</p>
<p>Sauf que voilà, le kit a fini par circuler bien au-delà de ce cercle. Un groupe d'espionnage russe l'a utilisé en juillet 2025 contre des cibles ukrainiennes, et un acteur chinois s'en est servi fin 2025 via de faux sites de cryptomonnaies et de paris en ligne. Plus de 50 domaines de distribution ont été identifiés.</p>
<h2 id="quels-sont-les-appareils-concernés-">Quels sont les appareils concernés ?</h2>
<p>Les mises à jour publiées par Apple couvrent deux générations d'anciens appareils. iOS 15.8.7 concerne les iPhone 6s, iPhone 7, iPhone SE première génération, l'iPad Air 2, l'iPad mini 4 et l'iPod touch septième génération. iOS 16.7.15 vise les iPhone 8, 8 Plus et iPhone X, ainsi que l'iPad cinquième génération et les premiers iPad Pro.</p>
<p>Les quatre CVE corrigées touchent le noyau et le moteur WebKit. Le kit exploite ces failles sans aucune interaction de l'utilisateur : il suffit de charger une page web piégée pour que l'appareil soit compromis.</p>
<h2 id="des-portefeuilles-crypto-ciblés">Des portefeuilles crypto ciblés</h2>
<p>Une fois l'appareil compromis, le malware PlasmaLoader s'attaque aux portefeuilles de cryptomonnaies comme MetaMask, Exodus ou Bitget Wallet. Google a qualifié Coruna de première exploitation de masse connue contre iOS.</p>
<p>Le kit détecte le modèle d'iPhone et la version d'iOS avant de choisir la bonne chaîne d'exploitation. Il évite aussi de s'exécuter si le mode Isolement est activé ou si la navigation est en mode privé.</p>
<p>Apple fait quand même bien le job en patchant des appareils qui ont jusqu'à dix ans, et c'est plutôt rassurant !</p>
<p>Source :
<a href="https://thehackernews.com/2026/03/coruna-ios-exploit-kit-uses-23-exploits.html">The Hacker News</a>
</p>