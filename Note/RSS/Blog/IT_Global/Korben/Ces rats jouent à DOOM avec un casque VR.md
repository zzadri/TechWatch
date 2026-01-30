---
title: "Ces rats jouent à DOOM avec un casque VR"
author: "Korben"
date: 2026-01-16T14:14:26.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/science-recherche"
  - "hardware-diy"
  - "jeux-video/realite-virtuelle"
  - "bidouille"
  - "Doom"
  - "neuroscience"
  - "open source"
  - "Raspberry Pi"
  - "rats"
  - "réalité virtuelle"
rss_source: Blog
url: https://korben.info/rats-doom-casque-vr-realite-virtuelle.html
note: 0
seen: false
---

<p>Vous pensiez avoir tout vu en matière de projets geeks complètement déjantés ?</p>
<p>Hé bien accrochez-vous à vos slips, parce que des chercheurs, menés par le neuro-ingénieur Viktor Tóth, ont réussi à faire &quot;jouer&quot; des rats à DOOM. Pas en appuyant sur des boutons au hasard, non non, mais avec un casque de réalité virtuelle sur mesure, une boule de déplacement sous leurs pattes, et même une gâchette pour tirer sur les démons !</p>
<p>Je vous jure que c'est vrai. Le projet s'appelle &quot;<strong>
<a href="https://ratsplaydoom.com/">Rats Play DOOM</a>
</strong>&quot; et c'est à la croisée de la neuroscience, de la robotique et du game design. L'idée de base, c'est de prouver qu'on peut entraîner des rongeurs à interagir avec des environnements virtuels contrôlés basés sur un moteur de jeu. Et quitte à faire ça, autant le faire avec le jeu le plus iconique des années 90.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/rats-doom-casque-vr-realite-virtuelle/rats-doom-casque-vr-realite-virtuelle-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>Gros plan sur le casque VR panoramique pour rongeurs (
<a href="https://ratsplaydoom.com/">Source</a>
)</em></p>
<p>Le setup est assez dingue. Le rat est équipé d'un casque panoramique intégrant un écran AMOLED pliable qui offre 180 degrés de champ horizontal et 80 degrés de vertical. Il est installé sur une boule sphérique qui détecte ses mouvements via des capteurs, un peu comme une trackball géante. Quand il marche, court ou tourne, ça se traduit directement en déplacements dans le jeu.</p>
<p>Et pour ceux qui se demandent comment un rat peut vraiment dégommer des monstres... Hé bien oui, car Viktor a même fabriqué un levier custom avec un encodeur rotatif que le rat actionne avec ses pattes pour faire feu. Donc oui, les rats tirent sur des démons avec leurs petites papattes !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/rats-doom-casque-vr-realite-virtuelle/rats-doom-casque-vr-realite-virtuelle-2.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le nouveau setup modulaire V2 (
<a href="https://ratsplaydoom.com/">Source</a>
)</em></p>
<p>Pour motiver nos petits rongeurs gamers, y'a évidemment un système de récompense. À chaque action réussie, le système distribue 10 microlitres d'eau sucrée via un solénoïde. C'est pas grand-chose mais pour un rat, c'est le graal. Au bout de deux semaines d'entraînement environ, les rats Todd, Kojima et Gabe (oui, ils ont des noms de légendes du jeu vidéo, on adore l'humour des chercheurs) ont réussi à naviguer dans l'environnement virtuel. Et là, ils ont même appris à déclencher le mécanisme de tir.</p>
<p>Bon, faut être honnête, ils n'ont pas encore terminé le jeu. L'équipe explique que les rats ont vieilli avant de pouvoir passer à l'entraînement avancé. Du coup, c'est plus une preuve de concept qu'un speedrun, mais quand même, c'est impressionnant. On est loin du simple
<a href="https://korben.info/roboroach.html">contrôle neuronal</a>
de base, là car c'est une vraie interaction avec un moteur de jeu.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/rats-doom-casque-vr-realite-virtuelle/rats-doom-casque-vr-realite-virtuelle-3.jpg" alt="" loading="lazy" decoding="async">
<p><em>Setup V1 du projet Rats Play DOOM (
<a href="https://ratsplaydoom.com/">Source</a>
)</em></p>
<p>Côté technique, tout tourne sur un combo Raspberry Pi pour l'acquisition des capteurs en temps réel, et un PC qui fait tourner une version modifiée de ViZDoom. Le tout communique en TCP et hop, c'est géré par un script Python central. Et comme si ça suffisait pas, le projet est entièrement open source. Vous pouvez récupérer le code, les schémas électroniques et même les fichiers 3D pour imprimer les pièces sur le repo GitHub. Donc si vous avez un rat de compagnie et beaucoup trop de temps libre...</p>
<p>Le projet en est à sa deuxième version. Cette V2 est plus modulaire, avec des composants imprimables en 3D et une électronique plus fiable. C'est typiquement le genre de bidouille qui me rappelle pourquoi j'aime tant farfouiller dans les
<a href="https://korben.info/idees-raspberry-pi.html">projets Raspberry Pi</a>
les plus improbables ^^.</p>
<p>D'ailleurs, si vous êtes fan de portages improbables, vous vous souvenez peut-être de cet article sur
<a href="https://korben.info/doom-retro-portage-windows.html">DOOM Retro</a>
, mais là avec les rats, on est clairement passé au niveau supérieur.</p>
<p>Bref, on vit vraiment une époque formidable où des gens financent des projets pour apprendre à des rats à buter des démons en VR. Et j'adore l'idée !</p>