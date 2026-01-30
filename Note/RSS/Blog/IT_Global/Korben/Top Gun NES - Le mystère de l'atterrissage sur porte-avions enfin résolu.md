---
title: "Top Gun NES - Le mystère de l'atterrissage sur porte-avions enfin résolu"
author: "Korben"
date: 2026-01-16T11:15:42.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "jeux-video/retrogaming-emulation"
  - "assembleur"
  - "Game Genie"
  - "NES"
  - "retrogaming"
  - "reverse engineering"
  - "Top Gun"
rss_source: Blog
url: https://korben.info/top-gun-nes-atterrissage-reverse-engineering.html
note: 0
seen: false
---

<p>Vous vous souvenez de Top Gun sur NES ? Ce jeu culte des années 80 où vous incarniez Maverick dans des combats aériens endiablés ? Hé bien si vous y avez joué, vous avez forcément vécu <strong>LE traumatisme du jeu</strong> : l'atterrissage sur le porte-avions.</p>
<p>Je ne sais pas combien de manettes ont été explosées à cause de cette séquence de torture, mais ça doit se compter en millions. Vous avez beau suivre les instructions à l'écran &quot;Alt. 200 / Speed 288&quot;, faire exactement ce qu'on vous dit, et PAF... crash. Retour à la case départ.</p>
<img src="https://korben.info/top-gun-nes-atterrissage-reverse-engineering/top-gun-nes-atterrissage-reverse-engineering-1.gif" alt="" loading="lazy" decoding="async">
<p>Toutefois, c'était sans compter sur ce développeur qui a eu la bonne idée de faire du reverse engineering sur le code assembleur du jeu pour comprendre ce qui se passait vraiment derrière cette mécanique diabolique.</p>
<p>Et en fouillant dans les entrailles du code NES, il a découvert que pour réussir l'atterrissage, il fallait respecter 3 critères simultanément. D'après l'analyse du code, l'altitude doit être entre 100 et 299 (une plage plutôt large, ouf), la vitesse entre 238 et 337 (déjà plus serré), et surtout l'alignement latéral avec le porte-avions qui est lui ultra strict. Et c'est là que ça devient chaud, parce que ce dernier paramètre, on ne le voit pas à l'écran. Vous pouvez avoir l'altitude parfaite et la vitesse au poil, si vous êtes décalé de quelques pixels à gauche ou à droite, c'est muerto pépito.</p>
<p>La direction est stockée en mémoire comme un entier signé allant de -32 à +32, puis convertie en une plage de 0 à 7. Autant dire que la marge d'erreur est ridicule...</p>
<p>Le plus intéressant dans son reverse, c'est de voir comment le code vérifie tout ça. La fonction &quot;landing_skill_check&quot; fait des vérifications séquentielles super basiques avec des codes d'erreur du genre : Altitude hors limites ? Code d'erreur 2. Vitesse hors limites ? Code 4. Direction hors limites ? Code 8.</p>
<img src="https://korben.info/top-gun-nes-atterrissage-reverse-engineering/top-gun-nes-atterrissage-reverse-engineering-2.gif" alt="" loading="lazy" decoding="async">
<p>Et ces codes d'erreur déterminent même l'animation de crash que vous allez voir. Du coup, si vous crashez souvent de la même façon, c'est probablement toujours le même paramètre qui foire.</p>
<p>Les valeurs sont stockées en BCD (Binary Coded Decimal) pour faciliter l'affichage à l'écran, et on peut les trouver aux adresses $40-$41 pour la vitesse, $3D-$3E pour l'altitude, et $FD pour la direction. Le résultat de la vérification se retrouve à l'adresse $9E. Voilà, maintenant vous savez où regarder si vous voulez tricher avec un
<a href="https://korben.info/retroassembly-collection-jeux-retro-navigateur-web.html">émulateur</a>
.</p>
<p>D'ailleurs, en parlant de triche, l'auteur de cette analyse a même créé un code Game Genie spécifique pour contourner toute cette galère : <strong>AEPETA</strong>. Tapez ça et vous atterrirez à tous les coups, peu importe à quel point vous pilotez comme un manche.</p>
<p>Bref, voilà un mystère de 35 ans enfin résolu grâce au reverse engineering. Et si vous voulez vous replonger dans cette torture en connaissance de cause, vous savez maintenant que c'est probablement l'alignement qui vous a eu, pas votre skill.</p>
<p>
<a href="https://relaxing.run/blag/posts/top-gun-landing/">Source</a>
</p>