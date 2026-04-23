---
title: "Reticulum - Le réseau mesh chiffré qui n'a besoin de rien"
author: "Korben"
date: 2026-02-25T08:44:02.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "reseaux-internet"
  - "vie-privee-anonymat/chiffrement"
  - "chiffrement"
  - "communication LoRa"
  - "mesh"
  - "off-grid"
  - "open source"
  - "radio-amateur"
  - "réseau"
rss_source: Blog
url: https://korben.info/reticulum-reseau-mesh-off-grid.html
note: 0
seen: false
---

<p>Si vous avez lu
<a href="https://korben.info/meshtastic-reseau-mesh-radio-survie-catastrophe.html">mon article sur Meshtastic</a>
, vous savez déjà que les réseaux mesh LoRa, c'est le genre de truc qui fait rêver tous les geeks en manque de hors-piste numérique. Mais y'a un cran au-dessus, et ça s'appelle
<a href="https://reticulum.network/">Reticulum</a>
.</p>
<p>En gros, c'est une stack réseau chiffré de bout en bout qui fonctionne sur n'importe quel support physique : LoRa, WiFi, Ethernet, liaison série, radio amateur en packet... TOUT y passe. Du coup, là où Meshtastic reste avant tout taillé pour les messages texte sur LoRa, ici vous pouvez faire transiter des fichiers, des appels vocaux, des pages web et même un shell distant à travers votre mesh. En fait au début je pensais que c'était juste un Meshtastic sous stéroïdes, mais non... c'est carrément une couche réseau complète.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/reticulum-reseau-mesh-off-grid/reticulum-reseau-mesh-off-grid-2.png" alt="" loading="lazy" decoding="async">
<p><em>Sideband, l'app de messagerie mesh pour Reticulum</em></p>
<p>L'avantage c'est surtout la flexibilité car plutôt que d'être coincé sur un seul médium, vous pouvez mixer LoRa longue portée et WiFi courte portée dans le même réseau via un simple fichier <code>~/.reticulum/config</code>, et les paquets se débrouillent tout seuls comme des grands pour trouver le chemin le plus efficace.</p>
<p>Côté chiffrement, c'est du lourd : X25519 pour l'échange de clés, Ed25519 pour les signatures, AES-256-CBC pour le chiffrement symétrique, et du forward secrecy par-dessus. Le truc malin, c'est que les paquets ne contiennent aucune adresse source. Votre identité sur le réseau, c'est juste une paire de clés au niveau du protocole, donc personne ne peut remonter à l'expéditeur.</p>
<p>L'écosystème d'apps est même plutôt costaud. Y'a Sideband, une app dispo sur Android via F-Droid, Linux et macOS, qui gère les messages, les appels vocaux, le transfert de fichiers et même les cartes, le tout à travers le mesh. Y'a aussi NomadNet pour héberger des pages sur un réseau totalement hors-ligne, et <code>rnsh</code> qui permet de lancer un shell distant (oui, du SSH sans Internet, sur le port que vous voulez... ça fait rêver ^^).</p>
<p>D'ailleurs pour les radioamateurs, tout ça tourne nickel sur des bonnes vieilles liaisons packet radio en AX.25. Modems KISS, TNCs classiques... tout est supporté, j'vous dit !</p>
<p>Et pour l'installer, c'est d'une simplicité presque suspecte : un <code>pip install rns</code> et hop, vous avez votre noeud Reticulum dans <code>/home/user/.reticulum/</code>. Ça tourne sur un Raspberry Pi 3 ou 4, un vieux laptop sous Debian, votre téléphone via Sideband... et si vous voulez du LoRa, vous branchez un RNode sur l'USB et c'est parti.</p>
<p>Attention quand même, sous Windows c'est un poil plus compliqué (Faut passer par WSL2, sauf si vous avez déjà un Python 3.x bien configuré dans le PATH), et la doc est intégralement en anglais.</p>
<p>Notez que la bande passante s'adapte sans problème au support, de 150 bps en LoRa longue portée sur 868 MHz (faut pas s'attendre à du Netflix non plus) jusqu'à 500 Mbps en Ethernet local. Et un lien chiffré s'établit en seulement 3 paquets pour 297 octets. C'est pas gourmand.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/aBt56UpaQ0E?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>C'est le genre de projet que je trouve super cool même si c'est clairement pas pour tout le monde (faut être à l'aise avec un terminal et le fichier <code>config.yml</code>), mais un protocole pensé dès le départ pour fonctionner sans infrastructure, avec du chiffrement partout et ZÉRO dépendance aux géants du web... ça force le respect et ça nous servira peut-être dans un futur proche, donc gardez ça dans un coin de votre tête...</p>
<p>Le code est dispo sous une licence MIT modifiée (y'a 2 restrictions : pas pour nuire, pas pour entraîner des IA), le protocole est dans le domaine public depuis 2016, et c'est essentiellement le boulot d'un seul mec, Mark Qvist. Donc chapeau à lui !</p>
<p>Bref, allez jeter un oeil à
<a href="https://github.com/markqvist/Reticulum">Reticulum sur GitHub</a>
... et merci à <strong>F4JWS</strong> pour le tuyau !</p>