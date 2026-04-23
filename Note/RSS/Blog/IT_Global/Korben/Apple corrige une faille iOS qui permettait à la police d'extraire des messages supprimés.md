---
title: "Apple corrige une faille iOS qui permettait à la police d'extraire des messages supprimés"
author: "Vincent Lautier"
date: 2026-04-23T13:18:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "vie-privee-anonymat"
  - "faille"
  - "iOS"
  - "Signal"
rss_source: Blog
url: https://korben.info/apple-corrige-une-faille-ios-qui-permettait-a-la-police-dextraire-des-messages-supprimes.html
note: 0
seen: false
---

<p>Apple a publié hier une mise à jour iOS qui ferme une faille utilisée par les forces de l'ordre américaines pour récupérer des messages supprimés dans des applications comme Signal.</p>
<p>La faille concernait la base de données des notifications : quand vous supprimiez un message dans l'appli, la version cachée dans le cache des notifications pouvait rester accessible jusqu'à un mois.</p>
<p>Concrètement, un message Signal effacé côté appli restait lisible par quiconque avait la main sur le téléphone et savait fouiller au bon endroit.</p>
<p>Le FBI, selon les documents repérés par 404 Media début avril, a utilisé cette faiblesse sur plusieurs affaires pour remonter des conversations pourtant explicitement effacées par les utilisateurs, y compris celles utilisant la fonction messages éphémères.</p>
<p>Apple a reconnu le problème, mais si ça a été fait avec les pincettes habituelle, avec une phrase du genre... &quot;les notifications marquées pour suppression pouvaient être conservées sur l'appareil de manière inattendue&quot;, ce qui ne veut pas dire grand chose, ou au contraire, tout dire...</p>
<p>Dit plus simplement, il y avait un écart entre ce que l'utilisateur voyait disparaître et ce qui restait réellement sur le disque. Le patch a été rétroporté sur les anciennes versions d'iOS 18, ce qui suggère que la faille existait depuis un bon moment et a probablement été exploitée dans des affaires que l'on ne connaîtra jamais.</p>
<p>Meredith Whittaker, présidente de Signal a rappelé publiquement que les notifications pour des messages effacés ne devraient jamais rester dans la base de notifications d'un OS. C'est une évidence technique. Sauf que dans la pratique, la chaîne cache des notifications plus indexation iOS laisse des traces que les outils forensiques comme Cellebrite ou GrayKey savent exploiter depuis des années.</p>
<p>Le problème dépasse Signal. Toute application qui envoie une notification contenant le texte d'un message entier sur iOS pouvait voir ses contenus persistés dans le cache, même après un effacement explicite. Du coup, pour les journalistes, les avocats, les activistes ou simplement les gens qui tiennent à leur vie privée, mettre à jour le plus vite possible n'est pas une option mais une priorité.</p>
<p>Bref, quand on parle de messagerie chiffrée, la vraie surface d'attaque n'est plus le protocole mais tout ce que l'OS fait autour dans votre dos.</p>
<p>Source :
<a href="https://thehackernews.com/2026/04/apple-patches-ios-flaw-that-stored.html">The Hacker News</a>
</p>