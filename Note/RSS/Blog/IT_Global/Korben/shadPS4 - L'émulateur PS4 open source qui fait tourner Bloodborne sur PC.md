---
title: "shadPS4 - L'émulateur PS4 open source qui fait tourner Bloodborne sur PC"
author: "Korben"
date: 2026-03-19T07:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/retrogaming-emulation"
  - "émulateur PS4"
  - "émulation console"
  - "gaming PC"
  - "jeux PlayStation 4"
  - "shadPS4"
rss_source: Blog
url: https://korben.info/shadps4-emulateur-ps4-windows-linux-macos.html
note: 0
seen: false
---

<p>Il y a un an, je vous parlais de <strong>
<a href="https://github.com/shadps4-emu/shadPS4">shadPS4</a>
</strong>, un émulateur PS4 open source encore balbutiant qui faisait tourner quelques jeux indés. Eh bien les amis, le projet a sacrément mûri depuis et la liste des jeux compatibles a de quoi faire saliver.</p>
<p>Là où il y a un an on parlait de Peggle 2 et Super Meat Boy (sympathiques mais bon...), shadPS4 fait maintenant tourner des trucs comme <strong>Bloodborne</strong>, <strong>Dark Souls Remastered</strong>, <strong>Red Dead Redemption</strong>, <strong>Yakuza 0</strong>, <strong>Hatsune Miku Project DIVA Future Tone</strong> ou encore <strong>DRIVECLUB</strong>. Oui, Bloodborne sur PC. Le Saint Graal que FromSoftware refuse de nous porter officiellement, des passionnés l'ont rendu possible via l'émulation.</p>
<p>Bien sûr, on parle toujours d'un émulateur en développement actif, donc attendez-vous à des bugs, des crashs et des performances variables selon les titres. Mais quand même, le bond en avant est impressionnant.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/shadps4-emulateur-ps4-windows-linux-macos/shadps4-emulateur-ps4-windows-linux-macos-2.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Côté technique, le projet tourne en <strong>C++20</strong> avec un rendu <strong>Vulkan</strong> et reste compatible <strong>Windows</strong>, <strong>Linux</strong> et <strong>macOS</strong>. Par contre, attention pour les utilisateurs Mac : il faut désormais <strong>macOS 15.4</strong> minimum, et les Mac Intel souffrent de gros bugs GPU. Autant dire que c'est surtout pour les Apple Silicon.</p>
<p>Depuis la dernière fois, pas mal de nouveautés ont débarqué :</p>
<ul>
<li>Support natif des manettes <strong>Xbox</strong> et <strong>DualShock</strong> avec <strong>émulation des motion controls</strong></li>
<li>Mapping clavier/souris entièrement personnalisable (jusqu'à 3 touches par action, config sauvegardée par jeu)</li>
<li><strong>Audio 3D</strong> via le backend SDL3</li>
<li>Émulation des <strong>signal handlers</strong> et support <strong>kqueue/kevent</strong> (ça parle aux devs Unix)</li>
<li>Stack réseau améliorée (sockets, HTTP, SSL) pour les jeux qui en ont besoin</li>
<li>Shader recompiler enrichi avec support des <strong>tessellation shaders</strong> et opérations atomiques</li>
<li>Montage des <strong>fonts système</strong> PS4 et chargement des modules firmware</li>
</ul>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/shadps4-emulateur-ps4-windows-linux-macos/shadps4-emulateur-ps4-windows-linux-macos-3.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Ce qui fait la force de shadPS4, c'est toujours sa communauté. Le projet bénéficie de l'expertise d'autres émulateurs reconnus : l'équipe de <strong>
<a href="https://panda3ds.com/">Panda3DS</a>
</strong> pour l'exécution native du code x64, les créateurs de <strong>
<a href="https://fpps4.net/">fpPS4</a>
</strong> pour le reverse-engineering du système PS4, et le compilateur de shaders s'inspire des travaux de <strong>
<a href="https://yuzu-emulator.net/">yuzu</a>
</strong>. Le projet <strong>
<a href="https://github.com/OFFTKP/felix86">felix86</a>
</strong> contribue aussi à l'émulation x86-64 vers RISC-V.</p>
<p>La version actuelle est la <strong>v0.15.0</strong> (sortie le 17 mars 2026) et les mises à jour tombent à un rythme soutenu avec des commits quasi quotidiens. Si vous voulez tester ou suivre la compatibilité des jeux, tout se passe
<a href="https://github.com/shadps4-emu/shadPS4">sur le dépôt GitHub du projet</a>
.</p>
<p><em>Article initialement publié le 8 mars 2025, mis à jour le 19 mars 2026.</em></p>