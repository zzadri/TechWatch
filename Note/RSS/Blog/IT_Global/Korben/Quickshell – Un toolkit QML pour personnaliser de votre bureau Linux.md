---
title: "Quickshell – Un toolkit QML pour personnaliser de votre bureau Linux"
author: "Korben"
date: 2026-01-25T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source"
  - "customization"
  - "desktop"
  - "hyprland"
  - "Linux"
  - "open source"
  - "qml"
  - "wayland"
  - "widgets"
rss_source: Blog
url: https://korben.info/quickshell-toolkit-qml-desktop-linux-wayland.html
note: 0
seen: false
---

<p>Si vous faites partie de ces gens qui passent plus de temps à configurer leur barre de tâches qu'à réellement bosser sur leur PC, j'ai déniché un truc qui va vous plaire (ou vous faire perdre encore plus d'heures de sommeil, au choix).</p>
<p>Dites bonjour à
<a href="https://quickshell.org/">Quickshell</a>
!!</p>
<p>Car on a tous voulu avoir un jour une barre de statut un peu sexy sous Linux et finalement se retrouver à se farcir des fichiers de config imbuvables ou des centaines de lignes de CSS hacky pour simplement changer une malheureuse icône. C’est souvent frustrant, sans parler du temps perdu, et on finit par garder le truc par défaut par pure flemme. Mais avec Quickshell, un nouveau monde devient possible !</p>
<p>Voici quelques exemples de ce qu'on peut faire avec Quickshell, du Material You au style rétro :</p>
<div class="video-container" id="video-container-quickshell-toolkit-qml-desktop-linux-wayland-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/quickshell-toolkit-qml-desktop-linux-wayland/quickshell-toolkit-qml-desktop-linux-wayland-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/quickshell-toolkit-qml-desktop-linux-wayland/quickshell-toolkit-qml-desktop-linux-wayland-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>L'idée en fait, c'est d'utiliser le QML (le langage de Qt pour les interfaces) pour décrire son bureau de façon déclarative car c'est lisible, et surtout, c'est hyper puissant. Le toolkit vous permet de créer non seulement des barres de statut, mais aussi des widgets et des tableaux de bord, et si vous vous sentez l'âme d'un développeur, vous pouvez même construire vos propres écrans de verrouillage en vous basant sur les capacités du moteur.</p>
<p>Le gros point fort de cet outil, c'est le rechargement à la volée. Bon, c'est pas encore du hot reloading automatique à chaque micro-seconde, mais vous pouvez déclencher la mise à jour de votre config instantanément (souvent via un simple raccourci ou une commande), et hop, la modification apparaît sur votre écran sans avoir à redémarrer toute votre session. Pour itérer rapidement sur un design, c'est juste du bonheur.</p>
<p>Côté technique, le projet envoie du bois puisque c'est écrit principalement en C++, que c'est sous licence LGPL-3.0/GPL-3.0, et que ça supporte aussi bien Wayland que X11 (même si Wayland est clairement le chouchou). Ça s'intègre d'ailleurs plutôt bien avec des compositeurs comme Hyprland ou Sway, selon votre configuration et les protocoles disponibles. Y'a même un module pour PipeWire si vous voulez gérer votre audio aux petits oignons et un support du system tray (via StatusNotifierItem).</p>
<p>La communauté commence d'ailleurs à sortir des trucs assez fous. J'ai vu passer des environnements complets construits avec le toolkit, comme DankMaterialShell qui adaptent les couleurs à votre fond d'écran, ou des délires plus rétro qui nous ramènent direct dans les années 90.</p>
<p>Bref, si vous avez envie de bidouiller votre desktop sans vous arracher les cheveux sur du CSS, foncez tester ça. C'est gratuit, c'est open source, et ça tourne nickel.</p>
<p>
<a href="https://quickshell.org/">Source</a>
</p>