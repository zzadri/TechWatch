---
title: "Des hackers iraniens ont infiltré une banque et un aéroport américains"
author: "Korben"
date: 2026-03-06T13:05:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/hackers-celebres"
  - "FBI"
  - "Google"
  - "Iran"
  - "karspersky"
  - "Microsoft"
  - "muddywater"
rss_source: Blog
url: https://korben.info/des-hackers-iraniens-ont-infiltre-une-banque-et-un-aeroport-americains.html
note: 0
seen: false
---

<p>MuddyWater, un groupe de hackers rattaché aux services de renseignement iraniens, s'est infiltré dans les réseaux d'une banque, d'un aéroport et d'un éditeur de logiciels américains avec deux nouvelles portes dérobées. L'opération, repérée par Symantec, s'est intensifiée après les frappes américaines et israéliennes sur l'Iran fin février.</p>
<h2 id="deux-portes-dérobées-inédites">Deux portes dérobées inédites</h2>
<p>C'est l'équipe Threat Hunter de Symantec qui a levé le lièvre. Depuis début février 2026, le groupe MuddyWater (aussi connu sous le nom de Seedworm) a déployé deux malwares jusqu'ici inconnus. Le premier, Dindoor, utilise Deno, un environnement d'exécution JavaScript, et a été signé avec un certificat émis au nom d'une certaine &quot;Amy Cherne&quot;.</p>
<p>Le second, Fakeset, est codé en Python et signé par un certain &quot;Donald Gay&quot;, un nom déjà lié à d'anciens outils du groupe comme Stagecomp et Darkcomp. Dans les deux cas, les attaquants ont tenté d'exfiltrer des données vers le cloud Wasabi via Rclone, un outil de synchronisation bien connu des administrateurs système.</p>
<h2 id="des-cibles-sensibles-un-lien-avec-israël">Des cibles sensibles, un lien avec Israël</h2>
<p>Côté victimes, on retrouve une banque américaine, un aéroport, un éditeur de logiciels lié à la défense et à l'aérospatiale qui a des opérations en Israël, et des ONG aux Etats-Unis et au Canada. MuddyWater était déjà présent sur ces réseaux début février, mais l'activité a nettement augmenté après le 28 février et le lancement de l'opération Epic Fury, les frappes militaires coordonnées des Etats-Unis et d'Israël contre l'Iran.</p>
<p>Les frappes ont conduit à la mort du guide suprême Ali Khamenei le 1er mars, et les chercheurs notent que les opérations cyber iraniennes se sont accélérées dans la foulée.</p>
<h2 id="le-fbi-confirme-le-lien-avec-téhéran">Le FBI confirme le lien avec Téhéran</h2>
<p>Le FBI, la CISA et le NCSC britannique considèrent que MuddyWater opère pour le compte du ministère iranien du Renseignement depuis 2018. Ce qui facilite le rattachement, c'est la réutilisation de certificats de signature entre les nouvelles portes dérobées et les outils plus anciens du groupe.</p>
<p>Google, Microsoft et Kaspersky ont d'ailleurs confirmé l'analyse de Symantec. Quant à l'objectif exact, les chercheurs restent prudents : espionnage, collecte de renseignements, ou préparation de futures actions de sabotage, difficile de trancher. Le groupe privilégie en général le phishing et l'exploitation de vulnérabilités dans des applications exposées sur Internet pour s'introduire dans les réseaux.</p>
<p>Le plus étonnant dans cette histoire, c'est la durée. Des semaines d'infiltration sans que personne ne bronche, sur des réseaux qui ne sont pas exactement anodins. Et avec le conflit actuel entre l'Iran, les Etats-Unis et Israël, on se doute bien que Symantec n'a gratté que la surface.</p>
<p>Sources :
<a href="https://www.security.com/threat-intelligence/iran-cyber-threat-activity-us">Security.com</a>
,
<a href="https://cyble.com/blog/middle-east-iran-us-israel-hybrid-conflict/">Cyble</a>
</p>
<p></p>