---
title: "WebTerm - Apprendre le terminal Linux sans rien installer"
author: "Korben"
date: 2026-03-09T10:41:25.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "tutoriels-guides/guides-debutants"
  - "terminal"
  - "Linux"
  - "Bash"
  - "Bash commandes"
  - "apprentissage"
rss_source: Blog
url: https://korben.info/webterm-apprendre-terminal-navigateur.html
note: 0
seen: false
---

<p>Le terminal Linux / MacOS, ça fait encore flipper pas mal de monde et c'est exactement pour cette raison que des gens ont créé
<a href="https://www.webterm.app/en">WebTerm</a>
, un petit site web qui simule un terminal directement dans le navigateur pour vous apprendre les commandes de base... sans risquer de claquer un rm -rf votre disque dur !</p>
<p>En gros, vous ouvrez le site dans Chrome ou Firefox, et vous avez un faux terminal devant vous avec des exercices progressifs. Ça part des trucs vraiment basiques genre pwd, ls, cd (oui, le B.A.-BA quoi) et ça monte jusqu'aux commandes plus costaudes comme grep, find, chmod ou carrément des tutos Git avec branches et commits. Y'a 8 modes d'apprentissage au total et une trentaine d'exercices, du débutant complet au &quot;<em>je veux maîtriser le versioning</em>&quot;. En fait c'est plutôt bien découpé et chaque mode rajoute une couche de difficulté.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/webterm-apprendre-terminal-navigateur/webterm-apprendre-terminal-navigateur-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le truc sympa c'est que tout se passe dans votre navigateur comme ça pas besoin d'installer Ubuntu, pas besoin de VirtualBox, pas besoin de WSL... vous ouvrez la page et vous tapez vos commandes dans un prompt bash comme un vrai sysadmin qui pue de la gueule (un classique !). Perso, pour quelqu'un qui n'a jamais touché à la ligne de commande, c'est quand même VACHEMENT moins flippant qu'un vrai terminal où une mauvaise manip peut vous foutre dans la mierda.</p>
<p>D'ailleurs si vous maîtrisez déjà un peu le sujet, y'a aussi un mode Free Play qui vous lâche dans la nature sans consignes. Vous tapez ce que vous voulez, vous expérimentez... un bac à sable quoi. Et comme sur un vrai shell Bash ou Zsh, vous avez la complétion par Tab et l'historique des commandes avec les flèches haut/bas.</p>
<p>Bon, c'est pas non plus un émulateur complet hein, donc faut pas s'attendre à pouvoir installer des paquets apt ou lancer des scripts bash complexes. Sauf si vous avez une vraie VM sous la main, mais là c'est plus le même délire. Par exemple, les pipes genre | entre commandes, ça passe pas non plus, et ça ne marche pas sur smartphone.</p>
<p>C'est desktop only... et dans le terminal, tout se fait au clavier, donc pas de souris. Et pour ceux qui se demandent, le site est dispo en anglais et en japonais (le projet vient d'une boîte japonaise qui s'appelle init Inc.), mais les commandes Linux c'est universel donc ça ne change rien sur l'apprentissage. Après si vous cherchez des tutos en français, là faudra aller voir ailleurs.</p>
<p>Et si vous voulez aller plus loin après avoir joué avec WebTerm, je vous recommande de jeter un oeil à
<a href="https://korben.info/les-raccourcis-clavier-pour-bash-terminal-linux-et-macos.html">mon article sur les raccourcis clavier Bash</a>
qui va vous faire gagner un temps de fou !</p>
<p>Voilà pour 15 minutes de pratique par jour c'est plutôt bien foutu et vous pourrez gagner en autonomie dans ce fichu terminal qui vous effraye depuis tant d'années.</p>