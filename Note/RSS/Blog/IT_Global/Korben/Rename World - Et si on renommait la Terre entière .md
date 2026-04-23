---
title: "Rename World - Et si on renommait la Terre entière ?"
author: "Korben"
date: 2026-04-08T11:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "hardware-diy/gadgets-crowdfunding"
  - "carte interactive"
  - "vie privée"
rss_source: Blog
url: https://korben.info/rename-world-carte-renommer-lieux.html
note: 0
seen: false
---

<p>Et si vous pouviez renommer n'importe quel lieu sur la carte du monde ?</p>
<p>Genre, transformer &quot;Paris&quot; en &quot;Pain au Chocolat City&quot; ou &quot;Bordeaux&quot; en &quot;Chocolatine Land&quot; ? Hé bien c'est exactement ce que propose
<a href="https://rename.world">Rename World</a>
, et y'a déjà plus de 40 000 renommages au compteur.</p>
<p>Le principe est hyper simple : vous cliquez sur un nom de lieu, vous proposez un nouveau nom, et la communauté vote. Les meilleures propositions restent, les autres disparaissent dans l'oubli. Y'a pas besoin de créer un compte pour explorer la carte, c'est ouvert à tout le monde et c'est dispo en français !</p>
<p>J'ai d'abord cru que ça allait être un festival de noms vulgaires et de spam... mais en fait non. Le créateur (qui se fait appeler kafk) a mis en place un filtre de mots plus un dashboard d'administration qui lui permet de dégager les trolls en quelques clics. Sur les 40 000+ propositions, le spam reste donc marginal et la majorité des renommages sont soit créatifs, soit du jeu de mots inoffensif. Après évidemment, si quelqu'un challenge votre proposition, faudra convaincre la communauté de voter pour vous.</p>
<p>Je vous présente Clermont-Ferrand ^^ :</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/rename-world-carte-renommer-lieux/rename-world-carte-renommer-lieux-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Mais le site ne s'arrête pas au simple renommage. Y'a aussi un mode Name Duel où deux propositions s'affrontent en face à face, un Quiz pour tester vos connaissances géo, et un Leaderboard pour les plus prolifiques. Du coup c'est devenu un vrai petit jeu communautaire.</p>
<p>Il y a également un bouton &quot;Hide NZ&quot; qui permet de supprimer carrément la Nouvelle-Zélande de la cartographie mondiale. Si vous traînez un peu sur r/MapsWithoutNZ, vous comprendrez la référence. Et un bouton &quot;Show NZ&quot; pour les gens bien, évidemment.</p>
<p>Côté technique, kafk a préféré utiliser des PMTiles (40 Go stockées chez Cloudflare) plutôt que des tuiles raster classiques, ce qui rend la navigation bien plus fluide. Le rendu vectoriel s'appuie comme d'hab sur
<a href="https://korben.info/organic-maps-gps-offline-open-source.html">OpenStreetMap</a>
et tourne sur le serveur d'un de ses potes équipé de 256 Go de RAM (oui, on a les amis qu'on mérite ^^). Attention par contre, si vous cherchez à renommer un endroit précis (genre votre village de consanguins) et que le libellé ne s'affiche pas, faudra jouer avec le niveau de zoom car c'est du vectoriel, les étiquettes géographiques apparaissent à des échelles différentes.</p>
<p>Si vous avez déjà perdu des heures sur des
<a href="https://korben.info/game-of-thrones-carte-interactive.html">cartes interactives de Westeros</a>
, attendez de voir ce qui se passe quand Internet a le droit de renommer le monde réel. Perso, j'ai cherché ce que les gens avaient fait de ma ville... et j'ai pas été déçu. Y'a aussi un
<a href="https://discord.gg/QjdvHwBYFr">Discord</a>
pour la communauté si vous voulez proposer des idées ou signaler des soucis.</p>
<p>Bref, allez-y, renommez votre bled, la préfecture de votre département, et bon courage à kafk pour la modération !</p>
<p>Ah et merci à AV pour l'info !</p>