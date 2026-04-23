---
title: "Lockdown Mode - La fonction d'Apple qui a mis le FBI en échec"
author: "Korben"
date: 2026-02-06T07:46:33.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/iphone-ipad"
  - "vie-privee-anonymat"
  - "Apple"
  - "chiffrement"
  - "FBI"
  - "FBI iPhone"
rss_source: Blog
url: https://korben.info/lockdown-mode-fbi-iphone.html
note: 0
seen: false
---

<p>Le <strong>Lockdown Mode d'Apple</strong>, vous en avez déjà entendu parler non ? C'est cette fonctionnalité un peu planquée dans les réglages de votre iPhone qui permet de transformer votre téléphone en véritable forteresse. Et enfin, on vient d'avoir la preuve que ça marche pour de vrai.</p>
<p>En effet, le FBI a perquisitionné le domicile d'une journaliste du Washington Post, Hannah Natanson, en janvier dernier. L'objectif c'était de récupérer ses appareils électroniques dans le cadre d'une enquête sur des fuites d'informations classifiées. Les agents ont donc saisi entre autres un MacBook Pro, un iPhone, un enregistreur audio et un disque dur externe.</p>
<p>Sauf que voilà, l'iPhone était en mode isolement...</p>
<p>Du coup, le CART (l'équipe d'analyse forensique du FBI) s'est retrouvé comme des cons devant l'écran verrouillé. Et 2 semaines après la saisie, toujours rien. Impossible d'extraire la moindre donnée. D'habitude, avec un Cellebrite UFED Premium ou un GrayKey, c'est l'affaire de quelques heures... mais là, que dalle.</p>
<p>Et perso, ça me fait bien marrer.</p>
<p>Parce que pour ceux qui débarquent, ce mode isolement c'est un bouclier qu'Apple a conçu à la base pour protéger les utilisateurs ciblés par des spywares type
<a href="https://korben.info/comment-faire-une-analyse-forensic-dun-smartphone-pour-y-detecter-des-signes-dinfection.html">Pegasus</a>
. Ça bloque la plupart des pièces jointes dans les messages, ça charge les pages web différemment et surtout, ça empêche toute connexion USB à un accessoire tant que l'appareil n'est pas déverrouillé. Et c'est justement ce dernier point qui est intéressant car les
<a href="https://korben.info/graykey-outil-deblocage-iphone-securite.html">outils forensiques type GrayKey ou Cellebrite</a>
ont aussi besoin de se brancher physiquement au téléphone pour faire leur boulot.</p>
<p>Faut savoir que les mandats de perquisition autorisaient même les agents à appuyer les doigts de la journaliste sur ses appareils ou à les placer devant son visage pour les déverrouiller par biométrie. Sympa l'ambiance aux USA...</p>
<p>Et ça a d'ailleurs fonctionné sur son MacBook Pro. Pas de chance.</p>
<p>Mais l'iPhone, lui, a tenu bon. C'est assez rare d'avoir une confirmation aussi directe de l'efficacité de cette protection via un document judiciaire. D'habitude, on reste dans le flou total sur ce que les forces de l'ordre arrivent ou n'arrivent pas à cracker.</p>
<p>Voilà alors petit rappel pour
<a href="https://korben.info/tuto-pair-locking-securiser-iphone-port-usb.html">ceux qui veulent blinder leur iPhone</a>
. Pour activer le mode isolement, c'est dans <strong>Réglages &gt; Confidentialité et sécurité &gt; Mode Isolement &gt; Activer</strong>.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/lockdown-mode-fbi-iphone/lockdown-mode-fbi-iphone-2.png" alt="" loading="lazy" decoding="async">
<p>Attention quand même, votre iPhone va redémarrer et certaines fonctionnalités seront limitées (messages, navigation web, FaceTime avec des inconnus), donc c'est un peu handicapant au quotidien. Faudra choisir entre confort et blindage, y'a pas de magie. Mais si vous avez des trucs sensibles à protéger, le choix est vite fait.
<a href="https://korben.info/ios-18-securite-renforcee-contre-police.html">Combiné avec les protections d'iOS 18</a>
qui font passer automatiquement votre iPhone en mode &quot;Before First Unlock&quot; après 72 heures d'inactivité, ça commence à faire une sacrée forteresse.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/lockdown-mode-fbi-iphone/lockdown-mode-fbi-iphone-3.png" alt="" loading="lazy" decoding="async">
<p>Bref, si vous êtes journaliste, activiste, ou juste un peu parano (aucun jugement), activez-le. Ça marche !</p>
<p>
<a href="https://www.404media.co/fbi-couldnt-get-into-reporters-iphone-because-it-had-lockdown-mode-enabled/">Source</a>
</p>