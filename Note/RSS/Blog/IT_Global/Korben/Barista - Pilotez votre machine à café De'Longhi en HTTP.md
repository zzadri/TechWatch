---
title: "Barista - Pilotez votre machine à café De'Longhi en HTTP"
author: "Korben"
date: 2026-03-16T06:13:38.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "hardware-diy/domotique-smart-home"
  - "hardware-diy/raspberry-pi"
  - "domotique"
  - "Raspberry Pi"
rss_source: Blog
url: https://korben.info/barista-bridge-ble-cafe-delonghi.html
note: 0
seen: false
---

<p>Vous avez une machine à café <strong>De'Longhi avec du Bluetooth</strong> et vous vous êtes déjà forcément dit &quot;<em>Mais pourquoi je dois me lever si tôt pour appuyer sur un putain de bouton comme un homme des cavernes</em>&quot; ?!</p>
<p>Hé bien bonne nouvelle mes petits accro aux café puisqu'un dev a passé ses soirées à sniffer les paquets BLE de sa Dinamica Plus, à reverse-engineerer le protocole de communication, et il en a fait un projet open source qui transforme votre cafetière en serveur HTTP. Du coup maintenant, un petit <code>curl http://pi:8080/api/brew/espresso</code> depuis le lit et hop, le café coule. En live depuis votre oreiller, vos petits yeux à moitié fermés en moins de 3 secondes.</p>
<p>Aaaaah, le bonheur !</p>
<p>Le projet s'appelle
<a href="https://github.com/asaf5767/barista">Barista</a>
et c'est en fait un bridge BLE-to-HTTP écrit en Python. Vous collez ça sur un Raspberry Pi Zero à 15 euros (ou n'importe quel ordi avec une puce Bluetooth) à côté de votre machine à café, ça se connecte en Bluetooth Low Energy, et ça expose une API REST complète. Ça permet ainsi de contrôler la préparation (espresso, cappuccino, latte, americano...), d'ajuster la force de l'arôme sur 5 niveaux, la température, la quantité en ml, et même d'activer la buse vapeur ou l'eau chaude à distance. Attention par contre, faut pas oublier de mettre une tasse sous le bec avant de lancer la commande depuis votre lit...</p>
<img src="https://korben.info/barista-bridge-ble-cafe-delonghi/barista-bridge-ble-cafe-delonghi-1.gif" alt="" loading="lazy" decoding="async">
<p>Côté technique, c'est du Python async avec la bibliothèque bleak pour la partie radio BLE et aiohttp pour le serveur HTTP local. En fait, le truc intéressant c'est que tout le protocole ECAM est documenté dans le repo... structure des paquets, calcul du CRC-16/CCITT, encodage des ingrédients, lecture et écriture des recettes. Donc si vous avez un autre modèle De'Longhi (Primadonna, Magnifica Evo, Eletta Explore), c'est théoriquement compatible vu que De'Longhi utilise le même protocole BLE sur sa gamme ECAM... mais seule la Dinamica Plus est testée et confirmée pour l'instant.</p>
<p>Le problème, vous l'aurez compris, c'est que De'Longhi ne documente pas son protocole BLE (va savoir pourquoi), donc y'a pas forcément de garantie que ça marchera du premier coup sur votre modèle.</p>
<p>Côté prérequis, il vous faut Python 3.11+ et BlueZ sur votre Raspberry Pi 4 ou 5 (le Bluetooth quoi). Après, l'installation tient en trois commandes : <code>pip install barista-coffee</code>, puis <code>barista scan</code> pour trouver votre machine, et enfin <code>barista start --address AA:BB:CC:DD</code> pour lancer le serveur.</p>
<p>Et là vous aurez une interface web sur le port 8080, avec une grille de boutons, un bouton par boisson... mais surtout une API REST qui permet d'intégrer ça avec à peu près n'importe quoi :
<a href="https://korben.info/gladys-assistant.html">Home Assistant</a>
, Node-RED, un cron job matinal, un raccourci Siri, un script Python... Perso, l'idée du réveil qui déclenche automatiquement un espresso, c'est quand même pas mal !</p>
<p>Évidemment, tout tourne en local ! Comme ça plutôt que de dépendre de l'app officielle De'Longhi (qui marche uniquement à 2 mètres de la machine ^^ donc autant appuyer sur le bouton à ce stade), là c'est du vrai contrôle réseau.</p>
<p>D'ailleurs si le sujet vous branche, on avait déjà listé
<a href="https://korben.info/idees-raspberry-pi.html">une tonne de projets Raspberry Pi</a>
dont une machine à café pilotable à distance.</p>
<p>Voilà, si vous avez une De'Longhi avec Bluetooth qui traîne dans la cuisine et un Raspberry Pi qui prend la poussière, vous savez ce qu'il vous reste à faire.</p>
<p>Amusez-vous bien et moi j'vais aller me faire un café du coup !</p>