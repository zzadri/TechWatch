---
title: "Open DroneLog - Vos logs de drone restent chez vous"
author: "Korben"
date: 2026-03-16T11:27:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "robots-drones-vehicules/drones"
  - "vie-privee-anonymat"
  - "DJI"
  - "Docker"
  - "open source"
  - "vie privée"
rss_source: Blog
url: https://korben.info/opendronelog-carnet-vol-drone-open-source.html
note: 0
seen: false
---

<p>Si vous pilotez un <strong>drone DJI</strong>, vos logs de vol finissent probablement sur Airdata ou un service cloud du même genre. En gros ce sont des trucs qui aspirent vos trajectoires GPS, vos altitudes en mètres, vos tensions de batterie en millivolts... et qui stockent tout ça sur des serveurs quelque part dans le cloud. Ouais, bof.</p>
<p>Eh bien
<a href="https://opendronelog.com/">Open DroneLog</a>
, c'est exactement l'inverse à savoir un carnet de vol open source qui garde tout en local, dans une base
<a href="https://korben.info/duckdb-moteur-sql-transformation-donnees.html">DuckDB</a>
(une base de données embarquée ultra-légère) sur votre machine.</p>
<p>Avec cet outil, vous importez vos fichiers .txt DJI (tous les modèles : Mini, Mavic, Air, Phantom...), les CSV de l'app Litchi, ou même les exports Airdata, et hop, le logiciel mouline tout ça pour vous afficher vos vols sur une carte 3D interactive avec le replay de la trajectoire. Vous pouvez alors accélérer jusqu'à x16, voir la télémétrie en temps réel (altitude, vitesse, signal RC, tensions des cellules de batterie) et même visualiser les mouvements des joysticks.</p>
<p>Pas mal donc pour comprendre pourquoi votre Mavic a décidé de faire un plongeon kamikaze ce jour-là !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/opendronelog-carnet-vol-drone-open-source/opendronelog-carnet-vol-drone-open-source-2.png" alt="" loading="lazy" decoding="async">
<p><em>Visualisation 3D d'une trajectoire de vol dans Open DroneLog</em></p>
<p>Un truc bien pensé dans l'appli, c'est l'auto-tagging car le logiciel détecte automatiquement les vols de nuit, les passages à haute vitesse, les situations de batterie froide... et colle des étiquettes sur chaque vol sans que vous ayez à lever le petit doigt. Pour ceux qui se demandent à quoi ça sert de tenir un journal de vol, disons que le jour où l'aviation civile vous pose des questions sur vos habitudes de pilotage, avoir un historique propre de tous vos vols avec coordonnées et télémétrie, ça peut clairement vous sauver la mise (surtout si vous volez près de zones sensibles).</p>
<p>Côté déploiement, vous avez le choix : app desktop (Windows, macOS, Linux), image Docker pour l'auto-héberger, ou
<a href="https://app.opendronelog.com">la webapp</a>
pour tester sans rien installer. Le Docker est clairement le meilleur choix parce que vous pouvez monter un dossier de logs et configurer une synchro automatique via cron. Genre, votre drone se pose, vous branchez la carte SD sur le NAS, copiez les fichiers .txt dans le dossier monté, et l'import se fait tout seul toutes les 8 heures. Ça tourne même sur un Raspberry Pi !</p>
<p>D'ailleurs, ça me rappelle l'époque lointaine où on
<a href="https://korben.info/construisez-votre-propre-drone.html">construisait son propre drone</a>
dans le garage.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/opendronelog-carnet-vol-drone-open-source/opendronelog-carnet-vol-drone-open-source-3.png" alt="" loading="lazy" decoding="async">
<p><em>Les graphiques de télémétrie : altitude, vitesse, batterie, tout y passet'as anal</em></p>
<p>Le géocodage inversé (qui transforme vos coordonnées GPS en noms de lieux) se fait hors-ligne donc c'est top pour la vie privée et d'ailleurs, si le sujet vous parle, le projet
<a href="https://korben.info/owntracks-gestion-securisee-donnees-localisation.html">OwnTracks</a>
applique la même philosophie à la géolocalisation perso.</p>
<p>Le logiciel gère aussi les profils multiples (pratique si vous avez plusieurs pilotes ou flottes), le suivi de la santé des batteries avec historique des cycles, la maintenance avec seuils configurables, et l'export dans à peu près tous les formats imaginables : CSV, JSON, GPX, KML. Y'a même un générateur de &quot;FlyCards&quot; pour partager vos stats de vol sur les réseaux en format 1080x1080 ! Et le tout est traduit en 11 langues, dont le français.</p>
<p>Le projet est sous licence AGPLv3, et pour l'instant c'est DJI-only (pas de Parrot ni Autel en natif). Bref, si vous cherchez un carnet de vol drone qui ne balance pas vos coordonnées GPS dans le cloud, c'est tout trouvé !</p>