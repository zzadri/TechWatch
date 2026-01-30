---
title: "apk.sh - Le couteau suisse qui simplifie le reverse engineering Android"
author: "Korben"
date: 2026-01-24T12:45:30.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "cybersecurite/hacking-pentest"
  - "Android"
  - "APK Android"
  - "Frida"
  - "reverse engineering"
  - "reverse engineering Android"
rss_source: Blog
url: https://korben.info/apk-sh-reverse-engineering-android.html
note: 0
seen: false
---

<p>L'autre jour, je m'amusais à regarder ce qu'une petite application Android que j'avais installée
<a href="https://korben.info/apps-mobiles-tracking-rgpd-audit.html">envoyait comme infos à ses serveurs</a>
, et j'ai encore galéré avec une tripotée d'outils différents. Entre ADB pour récupérer le fichier, Apktool pour le désassembler, Jadx pour lire le code et les scripts de signature à rallonge, y'a de quoi se taper la tête contre les murs. On est en 2026, et le reverse engineering Android ressemble encore parfois à de la spéléologie sans lumière dans une grotte remplie de goudron.</p>
<p>Puis c'est là que je suis tombé sur <strong>apk.sh</strong>, et ça m'a sauvé ma soirée. C'est un script Bash tout simple, mais qui joue le petit chef d'orchestre pour automatiser toutes les tâches les plus chiantes : le pull, le décodage, la reconstruction, le patching et le renommage d'APK. Ça vous mâche le travail sur toute la partie technique pour que vous n'ayez plus qu'à faire un petit <code>adb install</code> à la fin... et voilà ! (Sans les &quot;Trenti anni di qualità&quot;, évidemment ^^)</p>
<p>Le truc cool, c'est qu'il ne se contente pas de faire du &quot;pull&quot; et du &quot;decode&quot;. Il gère également nativement l'injection de
<a href="https://frida.re/docs/gadget/">gadgets Frida</a>
pour faire de l'instrumentation dynamique, et ça, c'est vraiment le pied pour ceux qui veulent voir ce qui se passe en mémoire sans s'arracher les cheveux. Il peut même patcher automatiquement la configuration de sécurité réseau pour vous permettre d'intercepter le trafic HTTPS plus facilement. Par contre attention, si l'appli utilise du certificate pinning bien costaud, ça servira à QUE DALLE.</p>
<p>Si vous avez déjà essayé de
<a href="https://korben.info/decompiler-application-android-apk-recompiler.html">décompiler un APK et de le recompiler</a>
, vous savez que la moindre erreur de signature ou d'alignement et c'est le drame. Ici, l'outil s'occupe de tout avec <code>apksigner</code> et <code>zipalign</code> de manière transparente. Et pour les plus barbus d'entre vous, il permet même de modifier directement le bytecode DEX via les fichiers smali pour éviter les bugs de décompilation Java qui font parfois pleurer un admin sys.</p>
<p>Pas besoin d'être root pour la plupart des fonctions, et il gère même les fameux bundles (AAB) que Google Play impose désormais et qui se transforment en &quot;split APKs&quot; une fois sur votre téléphone. En gros, vous faites un <code>pull</code> pour récupérer et fusionner tout ça en un seul APK, puis un <code>decode</code> pour obtenir un dossier tout prêt à être exploré.</p>
<p>C'est typiquement le genre d'outil que j'aurais aimé avoir à l'époque où je vous parlais d'Androguard pour
<a href="https://korben.info/androguard-reverse-engineering-dapplications-android.html">analyser des malwares Android</a>
. On gagne un temps de fou malade et on peut se concentrer sur ce qui nous intéresse vraiment dans la vie, c'est à dire <del>le fromage à raclette et la sieste</del> comprendre comment ces applis nous pompent nos données ou juste changer la couleur d'un bouton pour le plaisir (ou des trucs qui vous enverront en zonzon ^^).</p>
<p>Bref, si vous aimez mettre les mains dans le cambouis Android, allez jeter un œil à ce projet pour vos prochaines sessions de reverse.</p>
<p>
<a href="https://github.com/ax/apk.sh">A découvrir ici</a>
</p>