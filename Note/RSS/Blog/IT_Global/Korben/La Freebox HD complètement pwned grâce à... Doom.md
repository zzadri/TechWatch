---
title: "La Freebox HD complètement pwned grâce à... Doom"
author: "Korben"
date: 2026-01-07T08:51:52.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/hacking-pentest"
  - "0-day"
  - "39C3"
  - "Doom"
  - "Free"
  - "Freebox HD"
  - "hack"
rss-source: Blog
url: https://korben.info/freebox-hd-hack-39c3-0day-doom.html
note: 0
seen: false
---

<p>Enorme nouvelle pour tous les amateurs de rétro-ingénierie et très mauvaise nouvelle pour Free ! Au 39C3 (le Chaos Communication Congress de cette année), un chercheur français du nom de Frédéric Hoguin (que je salue) a présenté un talk absolument dingue sur le hack de la <strong>Freebox HD</strong>. Et tenez-vous bien, l'une des failles utilisées se trouve dans... le port de Doom intégré à la box !</p>
<p>Pour la petite histoire, la Freebox HD c'est ce bon vieux boîtier décodeur que Free a sorti en 2006. Bientôt 20 ans au compteur et toujours maintenue jusqu'à fin 2025. Du coup, Frédéric s'est dit que ça ferait un super terrain de jeu pour du reverse engineering à l'ancienne. Et là, il a découvert deux failles 0-day qui permettent de prendre le contrôle total de la box.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/V93pNsjgJXA?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>La première vulnérabilité se planque dans PrBoom, le célèbre port open source de Doom qui tourne sur la Freebox. Vous savez, le jeu qu'on peut lancer depuis le menu de la box. Bref, une faille dans un jeu vieux de 30 ans qui permet une première étape d'exploitation. La deuxième, c'est du lourd puisqu'il s'agit d'un 0-day dans le noyau Linux de la box qui permet une sandbox escape complète. Ça me rappelle le
<a href="https://korben.info/ps3-failoverflow.html">hack de la PS3 par Fail0verflow</a>
présenté au CCC il y a quelques années, où les hackers avaient réussi à extraire les clés privées de la console.</p>
<p>Et Frédéric a fait les choses bien : inspection physique du hardware, désassemblage complet, analyse de la surface d'attaque, et hop, deux 0-days tombés du ciel. Pour ceux qui se demandent si Free a subi un piratage, techniquement oui, mais pas de vos données. C'est la box elle-même qui peut être compromise, pas votre compte Free. D'ailleurs, si vous vous souvenez de
<a href="https://korben.info/une-faille-dans-la-freebox-v6.html">la faille CSRF dans la Freebox v6</a>
dont j'avais parlé, on reste dans la même lignée... Visiblement, les box françaises ont encore quelques secrets à livrer.</p>
<p>Quoiqu'il en soit, c'est un coup dur pour Free qui va devoir se pencher sur ces vulnérabilités. Bon après, la Freebox HD arrive en fin de vie, donc on verra si un patch est vraiment poussé d'ici la fin de l'année.</p>
<p>Hâte de voir si d'autres chercheurs vont maintenant s'attaquer aux Freebox plus récentes avec cette méthodologie. En attendant, si vous avez encore une Freebox HD qui traîne, vous savez ce qu'il vous reste à faire… ou pas. Car comment sécuriser sa Freebox face à ce genre d'attaque ? Honnêtement, tant que Free n'a pas patché, la meilleure défense c'est de… ne pas laisser un hacker jouer à Doom sur votre décodeur !</p>
<p>Un grand merci à G1doot pour m'avoir signalé ce talk !</p>