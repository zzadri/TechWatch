---
title: "Steam tourne sur Nintendo Switch grace à Proton 11 et au support ARM64"
author: "Korben"
date: 2026-04-19T07:52:28.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/actualites-gaming"
  - "linux-open-source"
  - "ARM"
  - "Steam"
  - "switch"
  - "Valve"
rss_source: Blog
url: https://korben.info/steam-tourne-sur-nintendo-switch-grace-a-proton-11-et-au-support-arm64.html
note: 0
seen: false
---

<p>Quelqu'un a fait tourner l'interface Steam sur une Nintendo Switch. Pas via un hack douteux ni un émulateur bricolé, mais en utilisant la beta officielle de Proton 11 que Valve a publiée avec, pour la première fois, le support des appareils ARM sous Linux.</p>
<p>Le résultat a été posté sur BlueSky (
<a href="https://bsky.app/profile/did:plc:owu62bybwircbrojnru5axov/post/3mjnka7iur22l">par ici</a>
) par AAGaming, qui a aussi partagé les fichiers pour reproduire la manip chez vous.</p>
<p>[Embed: https://bsky.app/profile/did:plc:owu62bybwircbrojnru5axov/post/3mjnka7iur22l]</p>
<p>Concrètement, Proton 11.0-Beta1 embarque FEX 2604, un traducteur d'instructions x86 vers ARM qui permet de faire tourner du code Windows x86 sur un appareil ARM sous Linux. C'est ce qui rend le tout possible. Cette Switch rootée tourne sous Ubuntu, Proton s'installe par-dessus, et l'UI Steam parvient bien à se lancer. Alors, certes, pour l'instant, on en est surtout au stade de la démonstration, et pas franchement au stade &quot;jouer à Elden Ring sur sa Switch&quot;, mais le client fonctionne.</p>
<p>Si Valve a bossé sur ce support ARM, c'est en fait pour le Steam Frame, son casque de jeu qui tourne sur un Snapdragon 8 Gen 3 avec 16 Go de LPDDR5X. L'appareil avait été montré en novembre dernier, présenté comme un appareil de streaming d'abord, mais avec la capacité de faire tourner des jeux en local aussi.</p>
<p>Lors d'une démo, un représentant Valve avait fait tourner Hades 2 en standalone à 1400p sur ARM, avec des performances correctes. &quot;C'est du Linux, sur ARM&quot;, avait-il précisé. Du coup, le support public dans Proton n'est que la suite logique.</p>
<p>L'intérêt va au-delà de la Switch. Tous les handhelds ARM sous Linux (Retroid, AYN, Ayaneo, et les futurs modèles) deviennent des cibles potentielles pour Steam. Valve travaille d'ailleurs sur un système de certification &quot;Verified&quot; pour le matériel ARM, comme ce qui existe déjà sur Steam Deck. </p>
<p>Les joueurs sauront quels jeux tournent bien en local et lesquels il vaut mieux streamer.</p>
<p>Côté jeux, la beta Proton 11 certifie aussi une fournée de titres pour SteamOS : Resident Evil, Dino Crisis, Warhammer Vermintide 2, SHOGUN Total War, Breath of Fire IV, entre autres. Et Valve a corrigé le Steam Overlay qui ne marchait pas avec les jeux EA, un bug qui traînait depuis un moment.</p>
<p>Bref, Steam sur Switch c'est surtout un proof of concept pour l'instant, mais Valve pose les bases d'un écosystème ARM qui pourrait devenir très concret avec le Steam Frame.</p>
<p>Source :
<a href="https://www.tomshardware.com/video-games/handheld-gaming/steam-shown-running-on-nintendo-switch-thanks-to-latest-proton-beta-fex-2604-translates-x86-to-arm-friendly-instructions-on-linux">Tom's Hardware</a>
</p>