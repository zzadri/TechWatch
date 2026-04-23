---
title: "Un Pokémon piégé depuis 15 ans dans un Pokéwalker, et l’issue est terrible pour la pauvre bête"
author: "Korben"
date: 2026-04-07T15:04:17.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "jeux-video/retrogaming-emulation"
  - "infrarouge"
  - "Nintendo"
  - "nintendods"
  - "pokemon"
  - "pokewalker"
  - "reverse engineering"
rss_source: Blog
url: https://korben.info/un-pokemon-piege-depuis-15-ans-dans-un-pokewalker-et-lissue-est-terrible-pour-la-pauvre-bete.html
note: 0
seen: false
---

<p>Un passionné a tenté de récupérer son Pokémon coincé dans un Pokéwalker, ce petit podomètre vendu avec Pokémon HeartGold sur DS en 2009, après avoir perdu la cartouche de jeu.</p>
<p>Entre reverse engineering du protocole infrarouge et manipulation du générateur de nombres aléatoires, la tentative est bien technique. Et le résultat est plutôt cruel, pour une raison que personne n'avait anticipée…</p>
<h2 id="un-pokémon-sans-cartouche-un-vrai-problème">Un Pokémon sans cartouche, un vrai problème</h2>
<p>Le Pokéwalker, pour ceux qui ne s'en souviennent pas, c'était ce petit podomètre vendu avec Pokémon HeartGold et SoulSilver sur Nintendo DS en 2009. Le principe était simple : vous transfériez un Pokémon de votre partie vers cet accessoire, vous le glissiez dans votre poche, et chaque pas comptait pour gagner des points et débloquer des objets.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/lbTG2NYnzPQ?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le tout communiquait avec la cartouche DS par infrarouge. Sauf que voilà, si vous perdez la cartouche (ce qui arrive plus souvent qu'on ne le croit après 15 ans), votre Pokémon reste coincé dans le Pokéwalker. Pas de cartouche, pas de transfert retour. C'est exactement le problème auquel s'est retrouvé confronté Etchy, un créateur de contenu spécialisé dans Pokémon Gen 4.</p>
<h2 id="du-reverse-engineering-à-lancienne">Du reverse engineering à l'ancienne</h2>
<p>Le travail de fond, c'est Dmitry qui l'avait fait il y a quelques années en décortiquant complètement le Pokéwalker. A l'intérieur : un microcontrôleur Renesas H8, une EEPROM de 64 Ko, un accéléromètre Bosch et un émetteur infrarouge générique. La communication entre la cartouche et le Pokéwalker passe par un protocole IR à 115 200 bauds, et chaque octet est simplement XOR avec 0xAA avant envoi.</p>
<p>Dmitry avait même réussi à exécuter du code arbitraire sur l'appareil en exploitant un débordement de buffer dans la décompression. Etchy s'est appuyé sur tout ce travail pour tenter sa mission de sauvetage. Son idée : créer une nouvelle sauvegarde avec les bons identifiants pour tromper le Pokéwalker.</p>
<p>Le dispositif ne vérifie que la version du jeu (HeartGold ou SoulSilver), la région et les identifiants du dresseur. En manipulant le générateur de nombres aléatoires du jeu, Etchy a réussi à générer une sauvegarde avec des IDs correspondants.</p>
<h2 id="le-fantôme-dans-la-machine">Le fantôme dans la machine</h2>
<p>Et ça a marché. En partie. Le Pokéwalker a accepté la connexion et transféré les données du Pokémon. Sauf que le vrai identifiant unique du Pokémon, son PID, celui qui définit ses stats, sa nature, son apparence, n'existe que sur la cartouche d'origine.</p>
<p>Le Pokéwalker ne stocke qu'une version allégée des données : l'espèce, les attaques, l'objet tenu, le genre. Le PID, lui, restait sur la cartouche perdue. Du coup, le Pokémon récupéré n'est qu'une copie incomplète. Ca ressemble à votre Typhlosion, ça porte son nom, mais ce n'est pas vraiment lui. Comme le résume Etchy dans sa vidéo : il n'y a pas de moyen de sauver un Pokémon piégé dans un Pokéwalker.</p>
<p>C'est le genre d'histoire qui parle à tous ceux qui ont grandi avec une DS dans la poche. On a tous eu ce moment où un accessoire, une sauvegarde ou un périphérique finissait au fond d'un tiroir, avec des données qu'on pensait sans importance.</p>
<p>Etchy et Dmitry montrent qu'il y a une vraie communauté prête à passer des heures sur du reverse engineering pour trois octets de données. C'est beau et un peu absurde en même temps. Le plus cruel dans l'histoire, c'est que Nintendo n'avait visiblement pas prévu qu'on puisse perdre sa cartouche tout en gardant le Pokéwalker. Bref quinze ans plus tard, votre Typhlosion attend toujours dans son petit boîtier, et personne ne viendra le chercher.</p>
<p>Source :
<a href="https://hackaday.com/2026/04/06/rescuing-a-pokemon-off-a-pokewalker-after-losing-the-game-cartridge/">Hackaday</a>
</p>