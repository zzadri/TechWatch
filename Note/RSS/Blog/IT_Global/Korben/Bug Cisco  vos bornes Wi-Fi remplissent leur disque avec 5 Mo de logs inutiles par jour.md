---
title: "Bug Cisco : vos bornes Wi-Fi remplissent leur disque avec 5 Mo de logs inutiles par jour"
author: "Korben"
date: 2026-04-17T07:47:40.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/failles-vulnerabilites"
  - "Cisco"
  - "logs"
  - "WiFi"
rss_source: Blog
url: https://korben.info/bug-cisco-vos-bornes-wi-fi-remplissent-leur-disque-avec-5-mo-de-logs-inutiles-par-jour.html
note: 0
seen: false
---

<p>Plus de 230 modèles de points d'accès Wi-Fi Cisco ont un problème. Les versions 17.12.4 à 17.12.6a de IOS XE embarquent une bibliothèque qui génère un fichier log, cnssdaemon.log, à raison de 5 Mo par jour. Le fichier ne sert à rien. Et impossible de le supprimer depuis la ligne de commande.</p>
<p>5 Mo par jour. Ça paraît rien. Sauf qu'un point d'accès Wi-Fi n'a pas un disque de 500 Go. La mémoire flash de ces appareils est limitée, et au bout de quelques semaines ou mois, elle sature.</p>
<p>Quand c'est plein, plus moyen de télécharger ou d'installer une mise à jour logicielle. La borne fonctionne encore, mais elle est figée sur sa version actuelle, sans possibilité de patch de sécurité ou de correction de bug.</p>
<p>Et c'est là que le piège se referme. Pour corriger le problème, il faut mettre à jour IOS XE. Mais si la mémoire flash est déjà pleine, la borne n'a pas la place pour stocker la nouvelle image système.</p>
<p>Cisco prévient que tenter la mise à jour dans cet état peut provoquer un bootloop, la borne redémarre en boucle sans jamais finir le boot. Du coup, l'admin se retrouve avec un appareil qu'il ne peut ni patcher ni laisser en l'état.</p>
<p>Cisco a publié un bulletin avec les procédures de test et de remédiation. Il faut d'abord vérifier la version IOS XE, puis libérer de l'espace manuellement avant de tenter la mise à jour.</p>
<p>Ça se fait, mais c'est du travail manuel sur chaque borne, et dans un réseau d'entreprise avec des centaines de points d'accès, la facture en heures de boulot est salée.</p>
<p>Ce genre de bug est particulièrement agaçant parce qu'il est silencieux. Personne ne surveille l'espace disque d'une borne Wi-Fi au quotidien, le problème se découvre en général le jour où une mise à jour échoue, c'est-à-dire trop tard.</p>
<p>Et le fait que la suppression du fichier soit impossible en CLI est quand même un oubli difficile à excuser sur du matériel vendu aux entreprises.</p>
<p>Bref, si vous avez du Cisco en IOS XE 17.12.x, vérifiez vos bornes avant qu'elles ne se bloquent toutes seules.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/17/cisco_wifi_ap_useless_data/">The Register</a>
</p>