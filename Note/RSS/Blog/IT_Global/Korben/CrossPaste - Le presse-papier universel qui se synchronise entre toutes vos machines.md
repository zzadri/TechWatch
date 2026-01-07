---
title: "CrossPaste - Le presse-papier universel qui se synchronise entre toutes vos machines"
author: "Korben"
date: 2026-01-07T08:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/logiciels-libres"
  - "vie-privee-anonymat/chiffrement"
  - "chiffrement"
  - "Kotlin"
  - "LAN"
  - "multiplateforme"
  - "open source"
  - "presse-papier"
  - "synchronisation"
rss-source: Blog
url: https://korben.info/crosspaste-presse-papier-synchronisation-multi-app.html
note: 0
seen: false
---

<p>Vous connaissez ce moment relou où vous copiez un truc sur votre PC et vous vous retrouvez comme un idiot devant votre Mac parce que le presse-papier ne suit pas ? Hé bien y'a une solution open source qui règle ce problème, et elle s'appelle
<a href="https://github.com/crosspaste/crosspaste-desktop">CrossPaste</a>
.</p>
<p>Vous installez l'app sur tous vos appareils (Windows, macOS, Linux) et hop, tout ce que vous copiez sur l'un se retrouve automatiquement disponible sur les autres. Du texte, des images, des URLs, du HTML, du RTF, des fichiers... Tout y passe. Et le truc cool c'est que ça fonctionne sur votre réseau local en mode &quot;LAN-only serverless&quot;, donc vos données ne transitent pas par un serveur central quelque part dans le cloud de Donald Duck, euh Trump.</p>
<p>Car oui, la sécurité c'est pas en option avec CrossPaste. Toutes les données sont chiffrées de bout en bout avec un système de chiffrement asymétrique. Du coup, même si quelqu'un sniffe votre réseau local (votre voisin super haxxor par exemple), il ne verra que du charabia incompréhensible. Et comme y'a pas de serveur central, y'a rien à pirater côté infrastructure non plus.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/crosspaste-presse-papier-synchronisation-multi-app/crosspaste-presse-papier-synchronisation-multi-app-1.webp" alt="" loading="lazy" decoding="async">
<p>L'interface est unifiée sur toutes les plateformes grâce à Compose Multiplatform (c'est du Kotlin sous le capot pour les curieux) et vous avez un historique de tout ce que vous avez copié, avec une gestion automatique du stockage pour pas que ça finisse par bouffer tout votre disque dur. Pratique pour retrouver ce lien que vous aviez copié y'a 3 jours et que vous avez oublié de sauvegarder quelque part...</p>
<p>Le projet est sous licence AGPL-3.0, donc c'est du vrai open source avec le code disponible sur GitHub. Si vous êtes du genre à vouloir bidouiller ou simplement vérifier qu'il n'y a pas de cochonneries planquées dedans, vous pouvez compiler vous-même. Y'a juste besoin de Gradle et d'un <code>./gradlew app:run</code> pour compiler et lancer le tout.</p>
<p>Bref, si vous jonglez entre plusieurs machines au quotidien et que vous en avez marre de vous envoyer des trucs par email ou par Slack juste pour les avoir sur un autre ordi, CrossPaste ça va vous faire économiser pas mal de temps et d'énergie. Et en plus c'est gratuit \o/</p>
<p>Merci à Lorenper pour l'info !</p>
<p>
<a href="https://github.com/crosspaste/crosspaste-desktop">Source</a>
</p>