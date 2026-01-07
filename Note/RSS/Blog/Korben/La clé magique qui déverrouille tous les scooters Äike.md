---
title: "La clé magique qui déverrouille tous les scooters Äike"
author: "Korben"
date: Tue, 06 Jan 2026 18:38:21 +0100
type: site
subject:
category:
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/hacking-pentest"
  - "Bluetooth"
  - "faille"
  - "IoT"
  - "reverse engineering"
  - "scooter électrique"
rss-source: Blog
url: https://korben.info/aike-scooter-bluetooth-cle-universelle-faille.html
seen: false
---

<p>Vous connaissez le concept de clé maître ? Hé bien Rasmus Moorats, un chercheur en sécurité estonien, vient d'en trouver une qui déverrouille l'intégralité du parc de scooters électriques <strong>Äike</strong>. Et vous vous en doutez, c'est pas vraiment ce que le fabricant avait prévu.</p>
<p>Le bougre a décidé de reverse-engineerer son propre deux-roues connecté après que la boîte ait fait faillite en 2025. Logique, quand le cloud menace de fermer, autant comprendre comment fonctionne sa bécane. Du coup il a décompilé l'app React Native, hooké les communications Bluetooth avec Frida, et là... surprise !</p>
<p>L'authentification entre l'app et l'engin utilise un système de challenge-response. Le scooter envoie un défi aléatoire, l'app le concatène avec une clé secrète, hash le tout en SHA-1, et renvoie le résultat. Simple et efficace. Sauf que la clé secrète en question, c'est <code>FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF</code>. Vingt octets de FF.</p>
<p>Vous l'aurez peut-être compris, c'est la valeur par défaut du SDK fourni par le fabricant du module IoT.</p>
<p>Bref, les devs d'Äike n'ont jamais personnalisé cette clé. Chaque scooter sorti d'usine embarque exactement la même. Du coup avec un script Python et la lib <strong>bleak</strong>, n'importe qui peut déverrouiller n'importe quel Äike qui passe dans la rue. Hop, on scanne, on répond au challenge avec la clé universelle, et on envoie les commandes : déverrouiller, activer le mode éco, ouvrir le compartiment batterie... tout y passe.</p>
<p>Le plus rigolo dans l'histoire c'est que la société sœur Tuul, qui fait de la location de trottinettes, n'a pas de Bluetooth sur ses engins ! Du coup elle n'est pas touchée. Comme quoi, parfois l'absence de fonctionnalité devient une feature de sécurité.</p>
<p>Évidemment, Rasmus a fait les choses proprement avec une disclosure responsable en septembre dernier. Le fabricant a alors confirmé que c'était bien leur faute, et pas celle du fournisseur du module. Mais bon, maintenant que la boîte a coulé, les correctifs risquent d'attendre looongtemps.</p>
<p>
<a href="https://blog.nns.ee/2026/01/06/aike-ble/">Source</a>
</p>