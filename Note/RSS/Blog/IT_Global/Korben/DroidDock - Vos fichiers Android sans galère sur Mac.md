---
title: "DroidDock - Vos fichiers Android sans galère sur Mac"
author: "Korben"
date: 2026-01-27T10:39:53.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "apple-mobile/macos"
rss_source: Blog
url: https://korben.info/droiddock-fichiers-android-mac.html
note: 0
seen: false
---

<p>Transférer des fichiers <strong>entre votre Mac et votre téléphone Android</strong>, c'est souvent la galère. L'ancien Android File Transfer de Google était une horreur absolue et depuis qu'ils ont arrêté de le maintenir, y'a pas grand-chose de potable. C'est d'ailleurs pour ça que beaucoup d'utilisateurs de Mac ont également un iPhone.</p>
<p>Alors quand je suis tombé sur <strong>DroidDock</strong>, forcément ça m'a intrigué. C'est une app macOS qui se branche sur votre téléphone via ADB et qui vous permet de naviguer dans les fichiers comme si c'était un Finder amélioré. Vous branchez votre câble USB, vous activez le débogage USB sur votre Android et c'est parti mon kiki !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/droiddock-fichiers-android-mac/droiddock-fichiers-android-mac-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et là où c'est pratique c'est que vous pouvez prévisualiser vos images et vidéos directement dans l'app sans avoir à les télécharger d'abord. Vous avez trois modes de vue (grille, liste ou miniatures) et le drag &amp; drop fonctionne dans les deux sens. Vous glissez un fichier depuis votre Mac vers DroidDock, il atterrit sur votre téléphone. Et l'inverse marche aussi.</p>
<p>Le dev a aussi pensé à pas mal de trucs pratiques du genre si vous avez plusieurs appareils Android branchés en même temps, hé bien vous pouvez switcher de l'un à l'autre sans les déconnecter. Y'a aussi un mode sombre pour ceux qui bossent la nuit et une barre de recherche pour farfouiller dans vos dossiers. D'ailleurs si vous utilisez
<a href="https://korben.info/scrcpy-extracteur-apk-android-mac.html">scrcpy pour contrôler votre Android depuis le Mac</a>
, DroidDock fait un bon complément pour la partie fichiers.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/droiddock-fichiers-android-mac/droiddock-fichiers-android-mac-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Sous le capot, ça utilise Tauri avec du Rust et React et l'app est tellement légère qu'elle fonctionnera parfaitement sur un vieux Mac. Le projet est open source sous licence MIT et vous pouvez le télécharger ici :
<a href="https://rajivm1991.github.io/DroidDock/">DroidDock</a>
!</p>