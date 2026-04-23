---
title: "Un consortium européen lance une alternative open source à Google Play Integrity"
author: "Korben"
date: 2026-03-10T08:48:28.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "linux-open-source/logiciels-libres"
  - "Google"
  - "google play integrity"
  - "unified attestation"
rss_source: Blog
url: https://korben.info/un-consortium-europeen-lance-une-alternative-open-source-a-google-play-integrity.html
note: 0
seen: false
---

<p>Un groupe de fabricants européens mené par l'Allemand Volla Systeme vient de lancer le projet Unified Attestation, une alternative open source à Google Play Integrity.</p>
<p>L'objectif : permettre aux systèmes Android alternatifs d'accéder enfin aux applications bancaires et aux services d'identité numérique européens, le tout sans dépendre de Google pour la vérification de sécurité.</p>
<h2 id="le-problème-avec-play-integrity">Le problème avec Play Integrity</h2>
<p>Si vous utilisez un téléphone Android classique, avec les services Google, vous ne vous en rendez très certainement pas compte. Mais pour les utilisateurs de systèmes alternatifs comme /e/OS, LineageOS ou GrapheneOS, c'est franchement infernal : Google Play Integrity, le système qui permet aux applications de vérifier la sécurité d'un appareil, bloque purement et simplement l'accès aux applications bancaires, aux portefeuilles numériques et aux services d'identité.</p>
<p>Seuls les appareils certifiés par Google passent les niveaux de vérification les plus élevés. Les ROM alternatives, même parfaitement sécurisées, sont exclues sans ménagement.</p>
<h2 id="ce-que-propose-unified-attestation">Ce que propose Unified Attestation</h2>
<p>Le consortium regroupe Murena (derrière /e/OS), IODE (France), Apostrophy (Suisse) et la UBports Foundation (Allemagne), avec l'intérêt d'un fabricant européen et d'un fabricant asiatique.</p>
<p>Le système comprend trois briques : un service intégré au système d'exploitation pour vérifier la sécurité de l'appareil, un service de validation décentralisé qui ne dépend d'aucune autorité unique, et une suite de tests ouverte pour certifier un OS sur un modèle donné.</p>
<p>Ce projet est publié sous licence Apache 2.0, avec une vérification hors ligne, et surtout sans collecte d'identifiants. Jörg Wurzer, le patron de Volla Systeme, résume bien le paradoxe : quand un seul acteur du marché contrôle la vérification de sécurité, ça crée une dépendance structurelle.</p>
<p>C'est d'autant plus problématique quand l'acteur en question est justement celui dont on cherche à se débarrasser.</p>
<h2 id="et-leurope-dans-tout-ça-">Et l'Europe dans tout ça ?</h2>
<p>Le timing n'arrive pas comme ça, pouf, par hasard. L'Union européenne développe en ce moment l'EUDI Wallet, un portefeuille d'identité numérique qui doit permettre à chaque citoyen d'avoir ses papiers sur son téléphone.</p>
<p>Le problème, c'est que la version actuelle de l'application utilise Google Play Integrity pour vérifier l'appareil. Résultat : si vous êtes sur un Android alternatif, pas de carte d'identité numérique pour vous. Des développeurs ont déjà signalé le problème sur GitHub, comparant la situation à un PC qui exigerait Windows pour ouvrir un document officiel.</p>
<p>Des développeurs gouvernementaux scandinaves se sont d'ailleurs positionnés parmi les premiers à vouloir tester Unified Attestation.</p>
<p>On est là sur une initiative qui va dans le bon sens, parce que jusqu'à présent, ça reste pénible que Google soit le seul à pouvoir dire si un smartphone Android est fiable ou non.</p>
<p>Unified Attestation ne va pas tout changer du jour au lendemain, et convaincre les banques d'adopter un système inconnu reste le plus gros obstacle. Mais que des développeurs gouvernementaux scandinaves s'y intéressent déjà, ça envoie un bon signal.</p>
<p>Source :
<a href="https://www.netzwoche.ch/news/2026-03-09/konsortium-entwickelt-open-source-alternative-zu-google-play-integrity">Netzwoche.ch</a>
</p>