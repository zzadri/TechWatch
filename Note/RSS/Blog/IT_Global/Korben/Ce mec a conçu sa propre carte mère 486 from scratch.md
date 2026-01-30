---
title: "Ce mec a conçu sa propre carte mère 486 from scratch"
author: "Korben"
date: 2026-01-26T17:23:36.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/composants-pc"
  - "jeux-video/retrogaming-emulation"
  - "FPGA"
  - "ordinateur 486"
  - "retrocomputing"
rss_source: Blog
url: https://korben.info/homebrew-486-motherboard-carte-mere.html
note: 0
seen: false
---

<p>Non mais attendez... y'a un mec qui vient de concevoir
<a href="https://maniek86.xyz/projects/m8sbc_486.php">une carte mère 486 from scratch</a>
, en grand 2026 comme disent les jeunes ! Pas une repro. Pas un clone. Non non, une vraie carte mère complète avec son propre chipset custom qui fait tourner <strong>DOOM et Linux</strong>.</p>
<p>Un PCB 4 couches fait maison, rien que ça !!</p>
<p>Piotr Grzesik, alias maniek86, est un étudiant en électronique polonais qui s'est lancé dans un projet complètement dingue. Tout est parti d'une sombre arnaque sur une carte POST ISA chinoise... et suite à ça, il s'est dit &quot;<em>bon, je vais apprendre le VHDL et l'ISA bus moi-même</em>&quot;. En fait, au début je pensais que c'était juste un projet de bricolage de plus, mais non. De fil en aiguille, il a fini par créer la
<a href="https://github.com/maniekx86/M8SBC-486">M8SBC-486</a>
, une carte mère qui accueille de vrais processeurs Intel 486 vintage.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/homebrew-486-motherboard-carte-mere/homebrew-486-motherboard-carte-mere-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>La carte mère M8SBC-486 dans toute sa splendeur rétro</em></p>
<p>Et le bonhomme n'a pas juste fait un PCB, mais a carrément développé son propre chipset baptisé &quot;<strong>Hamster</strong>&quot; qui tourne sur un FPGA Xilinx Spartan II. Il aurait pu utiliser un FPGA récent mais il a préféré le Spartan II parce que les outils Xilinx modernes supportent plus ces vieilles puces. Donc il bosse avec des logiciels de 15 ans d'âge... logique.</p>
<p>Et dedans, y'a tout ce qu'il faut pour émuler un PC des années 90 : un timer 8254, un contrôleur d'interruptions 8259, un contrôleur clavier PS/2, et même une horloge temps réel.</p>
<p>Côté specs c'est du bon vieux socket PGA-168 compatible avec tous les processeurs 486 5V, que ce soit du Intel ou des compatibles. Le bus tourne à 24 MHz, ce qui donne du 48 MHz avec un DX2 (et théoriquement 72 MHz avec un DX4). Y'a 4 Mo de SRAM, 256 Ko de ROM pour le BIOS, et deux slots ISA 16 bits pour les nostalgiques des cartes d'extension. Attention par contre, si vous comptez utiliser un 486 3.3V genre les derniers AMD, ça passera pas... faut du 5V uniquement.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/homebrew-486-motherboard-carte-mere/homebrew-486-motherboard-carte-mere-3.jpg" alt="" loading="lazy" decoding="async">
</p>
<p>Perso, ce qui m'impressionne le plus c'est la liste des trucs qui tournent dessus. MS-DOS 6.22 évidemment, FreeDOS, mais aussi Linux 2.2.26 ! Sans oublier DOOM, Wolfenstein 3D, et la démo Second Reality qui en a fait baver plus d'un à l'époque. Même Windows 3.1 démarre. Bon, la souris fonctionne pas, mais quand même...</p>
<p>J'aurais bien voulu tester moi-même sur un vieux 486 DX2/66 qui traîne quelque part dans un carton au garage, mais retrouver ce truc c'est un projet en soi. Finalement, si vous êtes fan d'
<a href="https://korben.info/86box-enfin-vrai-gestionnaire-vos-vieux.html">émulation rétro</a>
, c'est pil poil le genre de projet qui fait rêver les vieux grands enfants que nous sommes !</p>
<p>Le plus beau dans tout ça, c'est que Piotr a publié l'intégralité du projet en open source sur GitHub : les schémas, le PCB, le code VHDL du chipset, les sources du BIOS... Tout est dispo. Du coup si vous avez envie de vous lancer dans le rétrocomputing hardcore, vous savez où chercher.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/homebrew-486-motherboard-carte-mere/homebrew-486-motherboard-carte-mere-4.jpg" alt="" loading="lazy" decoding="async">
</p>
<p>Bon après, y'a quelques limitations. C'est là que ça peut coincer car y'a pas de DMA, donc oubliez les cartes son type Sound Blaster. Pas de second PIC non plus, et le Plug and Play ISA n'est pas encore implémenté dans le BIOS. Sauf si vous êtes prêt à contribuer au code, évidemment.</p>
<p>Mais franchement, pour un premier essai de cette envergure, c'est du très très solide.</p>
<p>Bref, si vous voulez voir la bête en action, la vidéo montre la démo Second Reality qui tourne avec quelques petits glitches visuels et pas de son, mais c'est normal vu les limitations.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/pTIDu2l4wE4?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Et si vous avez des vieux 486 qui traînent dans un carton, vous avez maintenant une raison de les ressortir !</p>
<p>
<a href="https://www.techspot.com/news/111058-homebrew-486-motherboard-runs-doom-linux-enough-dos.html">Source</a>
</p>