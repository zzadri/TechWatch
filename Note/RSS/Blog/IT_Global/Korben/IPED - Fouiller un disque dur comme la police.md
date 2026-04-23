---
title: "IPED - Fouiller un disque dur comme la police"
author: "Korben"
date: 2026-03-16T06:55:28.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "linux-open-source/logiciels-libres"
  - "analyse forensique"
rss_source: Blog
url: https://korben.info/iped-forensic-digital-investigation.html
note: 0
seen: false
---

<p>Si vous vous êtes déjà demandé comment les flics font pour fouiller un disque dur saisi chez un suspect, la réponse tient en quatre lettres :
<a href="https://github.com/sepinf-inc/IPED">IPED</a>
. C'est l'outil que la police fédérale brésilienne a développé en interne depuis 2012 pour analyser les preuves numériques... et qui est devenu open source en 2019.</p>
<p>N'importe qui peut aujourd'hui peut donc télécharger le même logiciel que celui utilisé par les enquêteurs pour décortiquer des scènes de crime numériques. J'vous parle d'un truc qui avale 400 Go de données à l'heure, ce qui à vrai dire c'est plutôt le débit d'un SSD NVMe que d'un logiciel d'analyse. Et ça gère des multicases de 135 millions d'éléments. Ouais, rien que le chiffre donne le vertige !</p>
<p>En gros, le principe c'est de balancer une image disque (DD brut, conteneur E01, machine virtuelle VMDK, VHD Hyper-V, AFF... la totale) et IPED va indexer, analyser, hasher en MD5 et SHA-256, et trier tout ce qu'il trouve. Le logiciel supporte une quarantaine de formats pour le carving, fait de l'OCR via Tesseract 5, parse l'historique des navigateurs, et peut même transcrire de l'audio grâce à Azure ou Google Cloud. Vous avez même un moteur de recherche plain-text sur l'intégralité d'un disque !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iped-forensic-digital-investigation/iped-forensic-digital-investigation-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface d'analyse d'IPED avec sa recherche plein texte et l'aperçu des fichiers</em></p>
<p>Et surtout, le truc qui tue c'est la reconnaissance faciale intégrée... car elle tourne sans GPU !! La v4.3 sortie fin 2025 pousse même le délire encore plus loin avec l'estimation d'âge sur les visages détectés et le support multi-visages par image. Pour les forces de l'ordre, y'a aussi PhotoDNA (étendu aux vidéos dans cette version) et une tâche de classification CSAM... bref du lourd pour la lutte contre la pédocriminalité !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iped-forensic-digital-investigation/iped-forensic-digital-investigation-3.png" alt="" loading="lazy" decoding="async">
<p><em>La reconnaissance faciale intégrée trie automatiquement les visages détectés</em></p>
<p>Mais attention, c'est pas juste un outil de flics. Si vous bossez en cybersécurité, en réponse à incident, ou si vous êtes juste curieux de comprendre ce qui traîne sur
<a href="https://korben.info/webosaures-special-recuperation-de-donnees.html">un vieux disque dur récupéré</a>
, IPED fera très bien le taf. Le logiciel propose plusieurs profils de traitement : <strong>forensic</strong> (analyse complète), <strong>triage</strong> (scan rapide), <strong>fastmode</strong> (indexation sans parsing lourd), et même un mode &quot;<strong>blind</strong>&quot; pour les cas où vous ne savez pas trop ce que vous cherchez.</p>
<p>Vous faites pointer l'outil sur une image disque, vous choisissez votre profil, et en quelques minutes il vous sort une interface Swing (oui, c'est pas forcément la plus belle du monde, oubliez pas que c'est du Java) avec tous les fichiers indexés, une timeline d'activité, les historiques de navigation, les conversations de messagerie et même une galerie de toutes les images triées par visage. Le tout sans avoir à monter l'image manuellement.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iped-forensic-digital-investigation/iped-forensic-digital-investigation-4.png" alt="" loading="lazy" decoding="async">
<p><em>La timeline unifiée permet de retracer toute l'activité chronologique du disque</em></p>
<p>Faudra donc un JDK 11 avec JavaFX inclus (genre Liberica ou Azul, parce que le JDK standard ne bundle plus JavaFX... snif) puis faites un petit <code>git clone</code> et un <code>mvn clean install</code> pour déployer tout ça.</p>
<p>Ça fonctionne sous Windows et Linux, mais pas de support macOS natif par contre. Et prévoyez au moins 16 Go de RAM, vu les volumes que ça traite. Le projet est solide mais je tiens quand même à souligner que le dev principal porte à lui seul plus de la moitié des commits... c'est courant sur ce type de projet mais c'est vraiment dommage car c'est d'utilité publique !</p>
<p>La v4.3 a aussi ajouté la validation de phrases mnémoniques crypto (pour détecter des seed phrases sur un disque, genre
<a href="https://korben.info/microsoft-bitlocker-fbi-cles.html">le même principe que quand le FBI demande les clés BitLocker</a>
sauf que là c'est vous qui cherchez), le support BitTorrent via Transmission, le carving 7zip, HEIC, WebM et MKV, et un parseur NSKeyedArchiver pour les dumps iOS. Et si vous devez analyser le backup d'un iPhone, y'a carrément moyen.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iped-forensic-digital-investigation/iped-forensic-digital-investigation-5.png" alt="" loading="lazy" decoding="async">
<p><em>Le moteur de carving récupère et affiche les fichiers avec leurs miniatures</em></p>
<p>Après la doc est assez éparse... le wiki GitHub ne couvre pas toujours les cas limites et faut parfois fouiller dans les issues pour trouver la bonne config. Mais bon, franchement, c'est le jeu de l'open source. Quand c'est &quot;gratuit&quot; c'est ton temps le &quot;produit&quot; ^^.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/iped-forensic-digital-investigation/iped-forensic-digital-investigation-6.png" alt="" loading="lazy" decoding="async">
<p>Bref, si vous avez un vieux disque qui traîne dans un tiroir, c'est l'occasion de jouer les enquêteurs du dimanche !</p>