---
title: "Widelands - Le Settlers II open source fêtera cette année ses 24 ans de dev"
author: "Korben"
date: 2026-03-18T08:25:45.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video"
  - "linux-open-source/logiciels-libres"
  - "jeu de stratégie"
  - "jeu open source"
  - "Settlers II"
  - "Widelands"
rss_source: Blog
url: https://korben.info/widelands-jeu-strategie-open-source-settlers.html
note: 0
seen: false
---

<p>Settlers II, ce jeu de stratégie où vous passiez des heures à regarder vos petits bonhommes transporter des planches de bois sur des chemins de terre est quelque part, toujours vivant puisqu'il y a des devs qui bossent sur un jeu open source équivalent depuis 2001. Ça fait + de 24 ans et le résultat vaut carrément le coup d'oeil.</p>
<p>Le projet s'appelle
<a href="https://www.widelands.org/">Widelands</a>
, c'est un jeu de stratégie en temps réel sous licence GPL-2.0, dispo sur Windows, macOS 11+ (j'ai dû le débloquer avec
<a href="https://korben.info/sentinel-assistant-gestion-gatekeeper-macos.html">Sentinel</a>
comme d'hab) et Linux (AppImage, Flatpak, PPA Ubuntu). On y retrouve de la gestion de mines d'or et de fer, de la construction de scieries et de casernes en pierre, des chaînes de production complètes avec des forgerons qui tapent sur l'enclume, des bûcherons qui abattent des chênes et des fermiers qui récoltent du blé...etc. Tout pareil sur Settlers II donc sauf que là c'est gratuit, c'est libre, et ça tourne même sur des machines pas toutes jeunes.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/widelands-jeu-strategie-open-source-settlers/widelands-jeu-strategie-open-source-settlers-1.png" alt="" loading="lazy" decoding="async">
<p>Dans Widelands, vous avez 5 tribus jouables, les Barbarians, l'Empire, les Atlanteans, les Frisians et les Amazons, chacune avec ses bâtiments spécifiques et ses arbres de technologies. Y'a des campagnes solo avec des tutoriels intégrés, un mode multijoueur en ligne et un éditeur de cartes.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/widelands-jeu-strategie-open-source-settlers/widelands-jeu-strategie-open-source-settlers-1.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Sous le capot, c'est du C++ compilé avec CMake et du Lua pour le scripting des campagnes et de l'IA. Du coup si vous voulez bidouiller, hop vous clonez le repo
<a href="https://github.com/widelands/widelands">depuis GitHub</a>
et vous suivez le guide de compilation du wiki (y'a des dépendances SDL2, Boost, ICU à installer avant). C'est pas forcément facile car le code source fait plusieurs centaines de milliers de lignes mais heureusement, y'a un système d'add-ons qui vous permettra d'installer des cartes et des mods sans toucher au compilateur, genre un Steam Workshop du pauvre (mais en mieux parce que c'est ouvert).</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/widelands-jeu-strategie-open-source-settlers/widelands-jeu-strategie-open-source-settlers-2.jpeg" alt="" loading="lazy" decoding="async">
<em>Screenshot</em></p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/widelands-jeu-strategie-open-source-settlers/widelands-jeu-strategie-open-source-settlers-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et ce projet est bien vivant avec plusieurs commits par jour. La communauté discute sur IRC (#widelands sur LiberaChat) et sur Discord et fait amusant, l'équipe a officiellement refusé toutes les contributions générées par IA parce que ça pose notamment pas mal de soucis de copyright. Après pour un projet construit avec amour depuis deux décennies par des bénévoles en chair et en os, je trouve ça plutôt sain.</p>
<p>Voilà, si vous aimez les
<a href="https://korben.info/1282-clones-open-source-jeux-cultes.html">clones open source de jeux cultes</a>
, celui-là ça vaut le coup.</p>
<p>Bon jeu !</p>