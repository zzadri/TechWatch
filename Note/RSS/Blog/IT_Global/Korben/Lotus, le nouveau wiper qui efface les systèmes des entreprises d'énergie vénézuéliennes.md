---
title: "Lotus, le nouveau wiper qui efface les systèmes des entreprises d'énergie vénézuéliennes"
author: "Vincent Lautier"
date: 2026-04-23T13:55:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/malwares-menaces"
  - "energie"
  - "Kaspersky"
  - "lotus"
  - "Venezuela"
  - "Wiper"
rss_source: Blog
url: https://korben.info/lotus-le-nouveau-wiper-qui-efface-les-systemes-des-entreprises-denergie-venezueliennes.html
note: 0
seen: false
---

<p>Un logiciel malveillant destiné à effacer définitivement les données de postes informatiques vient de faire surface dans le secteur énergétique vénézuélien.</p>
<p>La bête a été baptisée &quot;Lotus&quot; par les chercheurs de Kaspersky qui l'ont analysé en premier, il a été mise en route en décembre 2025 depuis un ordinateur vénézuélien, et sa cible principale semble être PDVSA, la compagnie pétrolière d'État.</p>
<p>Côté technique, Lotus ne fait pas dans la dentelle. Deux scripts batch préparatoires, OhSyncNow.bat et notesreg.bat, désactivent toutes les défenses, coupent les comptes utilisateurs et ferment les interfaces réseau, histoire de bien tout bloquer.</p>
<p>Ensuite, le binaire principal passe en mode destruction avec diskpart, robocopy et fsutil pour manipuler le système de fichiers, puis descend au niveau IOCTL pour écraser directement des secteurs physiques du disque. Les points de restauration sont supprimés, le journal USN est effacé. Aucune récupération possible.</p>
<p>LKaspersky ne pointe personne, et aucun élément technique ne désigne un État ou un groupe criminel en particulier. Le timing est quand même troublant : fin 2025 et début 2026, le Venezuela a traversé une crise politique majeure avec la capture de l'ancien président Nicolás Maduro le 3 janvier, et les tensions toujours fortes autour des infrastructures énergétiques. Coïncidence ou coordination, on ne saura probablement pas avant longtemps.</p>
<p>En pratique, un wiper qui cible PDVSA, ça rappelle immédiatement les attaques contre les infrastructures critiques qu'on a vues en Ukraine avec Stryker ou contre des clusters Kubernetes avec la variante TeamPCP.</p>
<p>L'objectif n'est pas le chantage ni le vol, c'est la destruction pure. Les opérateurs ne cherchent pas à exfiltrer quelque chose, ils veulent rendre l'infrastructure inutilisable le plus vite possible, pour déstabiliser ou punir.</p>
<p>Un réseau d'alimentation électrique ou de distribution de carburant paralysé quelques jours, ça a des conséquences directes sur la vie quotidienne et sur la stabilité politique d'un régime.</p>
<p>Ce qui inquiète, c'est aussi la qualité du code. Lotus n'est pas un script amateur collé à la va-vite : il enchaîne plusieurs étapes de sabotage méthodique, de la désactivation des défenses à la destruction bas niveau du disque.</p>
<p>Pour un pays qui n'a déjà pas la réputation d'avoir la cybersécurité la plus pointue du continent, encaisser ce genre d'outil, ça fait mal. Et la probabilité que d'autres échantillons du même auteur circulent déjà ailleurs est loin d'être nulle.</p>
<p>Bref, un wiper bien fichu sur une compagnie pétrolière d'État dans un pays en crise, c'est rarement l'œuvre d'un adolescent dans son garage. Affaire à suivre donc.</p>
<p>Source :
<a href="https://www.bleepingcomputer.com/news/security/new-lotus-data-wiper-used-against-venezuelan-energy-utility-firms/">Bleeping Computer</a>
</p>