---
title: "Lolgato - L'app macOS qui dompte vos Elgato"
author: "Korben"
date: 2026-03-12T13:27:07.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "linux-open-source/logiciels-libres"
  - "Elgato"
  - "Key Light"
  - "macOS"
  - "open source"
  - "Streaming"
rss_source: Blog
url: https://korben.info/lolgato-app-macos-elgato-key-light.html
note: 0
seen: false
---

<p>Les Elgato Key Light, c'est devenu le standard pour s'éclairer la tronche en visio ou en stream. Un gros panneau LED blanc posé sur un pied. Sauf que le soft officiel pour les piloter, bah... il fait le minimum syndical. En fait, à part allumer, éteindre et bouger un slider, y'a rien. Du coup, un dev finlandais a pondu
<a href="https://github.com/raine/lolgato">Lolgato</a>
, une app macOS gratuite et open source qui va beaucoup plus loin.</p>
<img src="https://korben.info/lolgato-app-macos-elgato-key-light/lolgato-app-macos-elgato-key-light-1.gif" alt="" loading="lazy" decoding="async">
<p><em>Lolgato en action dans la barre de menus</em></p>
<p>Sur mon Mac, j'ai téléchargé le DMG, glissé l'app dans Applications, et hop... une icône apparaît dans la barre de menus. De là, vous avez accès à tous les réglages de vos lumières sans ouvrir le Control Center d'Elgato. Luminosité, température de couleur, on/off... tout est là, à un clic. Mais le vrai kiff, c'est l'automatisation.</p>
<p>Car oui mes amis, Lolgato détecte quand votre webcam s'active (FaceTime, Zoom, OBS, peu importe) et allume vos lumières automatiquement. Comme ça, plus besoin d'y penser ! Vous verrouillez le Mac ? Les lampes s’éteignent. Par contre, attention, ça ne marche qu'avec les lumières Elgato (les Key Light et compagnie) et pas avec les panneaux LED du commerce à 30 euros.</p>
<img src="https://korben.info/lolgato-app-macos-elgato-key-light/lolgato-app-macos-elgato-key-light-1.avif" alt="" loading="lazy" decoding="async">
<p><em>L'interface menu bar de Lolgato</em></p>
<p>La synchronisation avec Night Shift c'est chouette aussi car comme ça, quand macOS passe en lumière chaude le soir, Lolgato ajuste la température de couleur de vos Key Light pour matcher. Vous passez de la lumière blanche de bureau à un éclairage chaud, genre lampe de chevet. Résultat, fini l'effet néon de supermarché à 23h dans votre salon. Quand Night Shift se désactive, retour à 6500K. Perso, sur mon setup chez moi, la différence se voit direct.</p>
<p>Côté raccourcis clavier, c'est complet. Des shortcuts globaux pour allumer, éteindre, monter la luminosité, baisser la température... tout ça sans toucher la souris. À vrai dire, sur un bureau avec deux ou trois moniteurs et un clavier, c'est carrément appréciable !</p>
<p>L'app repère vos lumières sur le réseau Wi-Fi automatiquement. Même protocole que le Control Center officiel. Et si la découverte auto fait des siennes, vous pouvez taper l'adresse IP de votre lampe directement dans les réglages de Lolgato. Pratique quand on a chez soi un routeur capricieux ou un VLAN séparé.</p>
<p>Si vous utilisez déjà
<a href="https://korben.info/controler-luminosite-ecrans-externes-macos.html">MonitorControl</a>
pour gérer la luminosité de vos écrans externes, Lolgato vient compléter le setup pour la partie éclairage. Le combo des deux, c'est le confort ultime !</p>
<p>Ça tourne sur macOS 14 (Sonoma) minimum, et aussi sur macOS 15 (Sequoia). C'est du Swift, licence MIT et le développeur est aussi derrière WalkingMate (un tapis de marche piloté depuis le Mac) et KeepMic (pour garder votre micro USB par défaut). Bref, un mec qui aime que ses périphériques obéissent au doigt et à l'oeil.</p>
<p>Voilà, c'est gratuit, open source, et ça marche bien !</p>