---
title: "GB Recompiled - Vos ROMs Game Boy traduites en C natif"
author: "Korben"
date: 2026-03-16T12:01:49.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "jeux-video/retrogaming-emulation"
  - "émulation"
  - "Game Boy"
  - "préservation"
  - "recompilation"
  - "retrogaming"
rss_source: Blog
url: https://korben.info/gb-recompiled-game-boy-decompilation.html
note: 0
seen: false
---

<p>La
<a href="https://korben.info/sonic-unleashed-recompiled-revolution-retrogaming.html">recompilation statique</a>
, je vous en avais parlé avec <strong>
<a href="https://korben.info/zelda-64-recompiled-portage-natif-ray-tracing-4k.html">Zelda 64</a>
et Sonic Unleashed</strong>. Le principe, en gros c'est qu'au lieu d'émuler bêtement le processeur et la mémoire d'origine, on traduit tout simplement le code assembleur du jeu directement en C natif. Du coup le jeu tourne nativement sur votre machine, sans couche d'émulation.</p>
<p>Et la bonne nouvelle du jour c'est que cette technique vient de parvenir jusqu'à la Game Boy avec
<a href="https://github.com/arcanite24/gb-recompiled">GB Recompiled</a>
.</p>
<p>Vous filez à cet outil un fichier .gb et il vous sort OKLM un dossier avec du code C, un CMakeLists.txt et tout ce qu'il faut pour le compiler. Vous lancez cmake puis ninja, et votre vieux Pokemon Bleu tourne nativement sur votre PC plutôt que de passer par un émulateur qui simule le processeur Z80 à chaque frame.</p>
<p>Plutôt chouette non ???</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gb-recompiled-game-boy-decompilation/gb-recompiled-game-boy-decompilation-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pour réussir ce tour de force, le recompilateur parse les opcodes Z80 de la cartouche, construit un graphe de contrôle de flux et résout les sauts indirects (genre les tables de jump, le truc qui rend la décompilation galère parce que l'adresse de destination dépend de la valeur d'un registre). Le taux de découverte dépasse alors les 98% même sur des RPGs bien touffus... pas mal pour de l'analyse purement statique !</p>
<p>Côté compatibilité, 7 jeux sont pour le moment validés : Tetris, Pokemon Blue, Donkey Kong Land, Kirby's Dream Land, Zelda Link's Awakening, Castlevania et Super Mario Land.</p>
<p>Par contre, attention, tous les jeux ne passent pas encore. Le runtime embarque un rendu
<a href="https://www.nesdev.org/wiki/PPU_rendering">PPU scanline</a>
, un système audio 4 canaux et les contrôleurs mémoire MBC1, MBC2, MBC3 et MBC5. Et comme tout ça tourne avec SDL2, du coup ça compile tranquillou sur macOS, Linux et Windows sans broncher !</p>
<p>Y'a aussi des outils de vérification assez bien pensés. Par exemple, un mode différentiel lance le binaire recompilé et un interpréteur Z80 côte à côte, puis compare l'exécution cycle par cycle avec une implémentation de référence. Tant que ça colle, le portage est fidèle !</p>
<p>Et y'a aussi un script Python basé sur PyBoy qui génère des traces d'exécution pour repérer les instructions que l'analyse statique aurait loupées. Voilà, ce que je veux vous dire c'est que c'est pas juste un traducteur tout bête. Y'a vraiment tout un pipeline de tests derrière pour assurer le meilleur portage possible.</p>
<p>Si vous avez suivi les autres projets autour de la portable de Nintendo, comme le
<a href="https://korben.info/reconstruire-gameplay-game-boy-bus-memoire.html">GB Interceptor</a>
qui espionne le bus mémoire avec un adaptateur USB ou le
<a href="https://korben.info/game-bub-console-fpga-open-source-game-boy.html">Game Bub</a>
et son FPGA Xilinx, GB Recompiled choisit plutôt l'angle purement logiciel. Là où le FPGA reproduit les circuits et l'émulateur simule le CPU, la recompilation traduit le code source. Ce sont 3 philosophies différentes mais qui ont un seul et même objectif : Faire en sorte que ces jeux ne crèvent pas avec leurs cartouches en plastique gris.</p>
<p>Pour tester chez vous, c'est du classique : un petit terminal, un petit git clone, un cmake, un ninja, et vous passez votre fichier .gb au recompilateur.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/arcanite24/gb-recompiled.git
</span></span><span class="line"><span class="cl">cd gb-recompiled
</span></span><span class="line"><span class="cl">cmake -G Ninja -B build .
</span></span><span class="line"><span class="cl">ninja -C build
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Générer le code C depuis la ROM
</span></span><span class="line"><span class="cl">./build/bin/gbrecomp path/to/game.gb -o output/game
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Compiler la nouvelle version en C
</span></span><span class="line"><span class="cl">cmake -G Ninja -S output/game -B output/game/build
</span></span><span class="line"><span class="cl">ninja -C output/game/build
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Optionnel: Baisser ou augmenter le niveau d&#39;optimisation
</span></span><span class="line"><span class="cl">cmake -S output/game -B output/game/build -DGBRECOMP_GENERATED_OPT_LEVEL=2
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Et on lance !
</span></span><span class="line"><span class="cl">./output/game/build/game
</span></span></code></pre><p>Voilà comment avec juste quelques commandes, votre bonne vieille cartouche GB peut enfin tourner nativement sur votre laptop. Notez que le support Game Boy Color est dans les tuyaux, ainsi qu'un build Android.</p>
<p>Le projet est franchement actif et ça sent très bon pour la suite !</p>