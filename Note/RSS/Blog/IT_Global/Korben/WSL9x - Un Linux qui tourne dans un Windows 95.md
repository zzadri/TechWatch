---
title: "WSL9x - Un Linux qui tourne dans un Windows 95"
author: "Korben ✨"
date: 2026-04-22T09:53:54.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement"
  - "jeux-video/retrogaming-emulation"
  - "Linux"
  - "Windows"
  - "Windows95"
  - "WSL"
rss_source: Blog
url: https://korben.info/wsl9x-linux-dans-windows-95.html
note: 0
seen: false
---

<p>Un Linux qui tourne dans un Windows 95, vous ne rêvez pas puisqu'un développeur solo du nom de Hailey Somerville, a sorti <strong>WSL9x</strong>, un &quot;Windows 9x Subsystem for Linux&quot; qui pousse encore plus loin la logique de Microsoft avec WSL.</p>
<p>Le truc marche avec une simple commande <code>wsl</code> tapée dans le terminal MS-DOS, ce qui ouvre un pseudo-terminal Linux au beau milieu de votre Windows 9x. Pour les couleurs ANSI, il faudra charger un driver comme nnansi.com (c'est pas un nom de domain hein...) avant mais une fois en place, vous avez un shell Linux qui tourne en coopératif à côté du système Microsoft. Pas besoin de redémarrer ni de vous lancer dans la mise en place d'un dual boot.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wsl9x-linux-dans-windows-95/wsl9x-linux-dans-windows-95-2.png" alt="" loading="lazy" decoding="async">
<p>Sous le capot, c'est une bidouille assez rigolote. En fait, Hailey a patché le noyau Linux 6.19 dans sa variante user-mode, cross-compilé en i386 avec musl, puis intégré via Open Watcom v2 pour la partie Windows. Le code se compose à 63% de C et à 35% d'assembleur, ce qui donne une idée du niveau de bas-niveau qu'il faut pour faire tourner un kernel Linux en parallèle d'un Windows 95 ou 98.</p>
<p>Ensuite, tout ce qui est pagination, protection mémoire et ordonnancement préemptif tirent parti des capacités des deux OS en même temps. Linux gère ses processus invités, Windows arbitre en bas niveau, et les deux cohabitent sans se marcher sur les pieds. Ça permet comme ça de lancer vos outils Linux préférés sans jamais quitter votre session OuinOuin.</p>
<p>Pour reproduire ça chez vous, il vous faudra un cross-compilateur i386-linux-musl (musl-cross-make fait très bien le job), Open Watcom v2, et une image disque Windows 9x pré-installée. Vous configurez les variables WATCOM et LINUX via <code>.envrc.example</code>, puis vous buildez le kernel avec <code>make defconfig ARCH=um SUBARCH=i386 KBUILD_DEFCONFIG=win9x</code> suivi d'un <code>make vmlinux</code>.</p>
<p>Un dernier petit <code>make</code> à la racine du projet pour génèrer le <code>hdd.img</code> final, et en suite c'est tout prêt à booter dans un
<a href="https://korben.info/86box-enfin-vrai-gestionnaire-vos-vieux.html">86Box</a>
, PCem ou carrément une vraie bécane sous Windows 95.</p>
<p>Maintenant, ce projet est qualifié de &quot;very messy&quot; par son auteur car c'est encore un travail en cours, et pas du tout un WSL officiel prêt pour un usage stable. Le dépôt est sous GPL-3 donc forkable, mais la doc se résume au README, donc c'est encore un peu léger.</p>
<p>Par contre, si vous aimez les hacks rétro de l'extrême,
<a href="https://codeberg.org/hails/wsl9x">WSL9x</a>
mérite un petit coup d'œil. Ça me rappelle ce
<a href="https://korben.info/sous-systeme-linux-ms-dos.html">sous-système Linux pour MS-DOS</a>
qu'un autre dev avait sorti il y a quelques années, qui était le même délire mais pour DOS pur. À côté, le
<a href="https://korben.info/installer-wsl2-windows-linux.html">WSL2 officiel de Microsoft</a>
fait hyper sérieux.</p>
<p>Donc si vous avez un vieux Pentium qui traîne dans un placard, c'est l'occasion parfaite de le dépoussiérer pour faire la chose la plus absurde du mois.</p>