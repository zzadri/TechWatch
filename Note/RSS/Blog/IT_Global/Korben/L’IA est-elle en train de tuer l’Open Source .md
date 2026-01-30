---
title: "L’IA est-elle en train de tuer l’Open Source ?"
author: "Korben"
date: 2026-01-19T08:34:59.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "linux-open-source/logiciels-libres"
  - "espionnage informatique"
  - "législation numérique"
  - "Tailored Access Operations"
rss_source: Blog
url: https://korben.info/llm-impact-qualite-open-source.html
note: 0
seen: false
---

<p>IA par-ci, IA par-là.. même ceux qui critiquent l'IA générative, s'en servent pour faire leurs posts de blog remplis de fake blabla. Mais cette fois on touche un peu au nerf de la guerre, puisque Daniel Stenberg, le créateur de <strong>Curl</strong>, a lancé son petit cri d'alarme la semaine dernière.</p>
<p>Curl est un outil qui est dispo dans à peu près tous les systèmes qui ont une adresse IP et le problème de Daniel c'est que son projet reçoit de TROP nombreux rapports de sécurité bidon générés à la chaîne par des LLM.</p>
<p>Du coup, ça lui fait perdre pas mal de temps ainsi qu'aux mainteneurs du projet, pour trier le bon grain de l'ivraie</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/llm-impact-qualite-open-source/llm-impact-qualite-open-source-2.png" alt="" loading="lazy" decoding="async">
<p>C'est tellement critique qu'il envisage sérieusement de fermer son programme de Bug Bounty... Bref, ça craint pour l'avenir de la collaboration autour de l'open source.</p>
<p>Une fois encore, et au risque de me répéter, le problème n'est pas l'outil. l'IA est une super aide pour analyser du code mais quand on y ajoute une incitation financière (un bounty quoi), ça devient la fête à la paresse intellectuelle. Des &quot;chasseurs de primes&quot; sans compétences, s'emparent alors de scripts à base d'IA pour scanner des repos et copient collent les rapports sans les lire.</p>
<p>L'idée pour eux, c'est qu'en faisant ça massivement, ils grapillent un petit peu de sous.</p>
<p>Et de ce que j'ai compris, Curl n'est pas le seul projet à vivre ce calvaire. Par exemple, Godot (le moteur de jeu) a lui aussi dû prendre des mesures contre ce genre de contributions GenAI, et ça s'inquiète aussi beaucoup du côté du noyau Linux...</p>
<p>Tous ces petits indices me font donc me demander quel est l'impact réel de l'IA sur l'open source... Parce que d'un côté, c'est quand même une super aide. Ça abaisse la barrière à l'entrée. Ça permet de voir des choses qu'un humain n'aurait pas forcément vues. Mais d'un autre côté, ça inonde les mainteneurs de projets sous un tas de rapports &quot;slop&quot; (C'est LE mot à la mode pour désigner du contenu merdique fait par IA ^^) contenant des failles imaginaires ou cassant des fonctionnalités existantes.</p>
<p>Bref, c'est un peu la merde parce que les mainteneurs de repos sont en train de vriller parano, à fliquer les contributeurs au lieu de collaborer, et je trouve que ça casse un peu l'essence même de l'open source qui est la confiance et la réputation.</p>
<p>Quand vous poussez un bon gros commit, vous annoncez aux barbus en rute que c'est votre boulot, avec du vrai jus de cervelle derrière. Mais si c'est un LLM qui a tout pondu et que vous n'avez même pas relu, vous n’êtes plus un contributeur : vous êtes juste un spammeur.</p>
<p>Alors on fait quoi ?</p>
<p>On revient comme dans les années 90 avant l'IA, par pur &quot;Oui mais moi j'ai des principes&quot;, ou est-ce qu'on apprend à utiliser ces modèles comme des assistants et on commence à s'éduquer les uns les autres pour essayer de faire de la qualité en remettant l'humain dans la boucle ?</p>
<p>Moi je trouve que l'IA générative c'est génial, mais je trouve aussi que les gens l'utilisent mal, et c'est ça qui produit ce slop en fait. Et je trouve ça con parce qu'on pourrait aller tellement plus loin si les gens apprenaient à collaborer avec l'IA au lieu de juste s'en servir pour pouvoir regarder Netflix pendant que ça bosse...</p>
<p>Donc les amis, si vous utilisez une IA pour trouver un bug, il n'y a pas de soucis avec ça (c'est mon point de vue évidemment), mais au moins vérifiez-le, rejouez-le, essayez de le comprendre, sinon bah abstenez-vous quoi.</p>
<p>Et si ce sujet de la gouvernance des projets libres vous plaît, je vous invite à jeter un œil aux discussions sur
<a href="https://korben.info/linux-interdit-code-genere-ia-gentoo-netbsd-ouvrent-voie.html">les bannissements dans le noyau Linux et les distribs</a>
. Rappelez-vous aussi de &quot;l'incident&quot; de
<a href="https://korben.info/backdoor-linux-faille-securite-critique-xz-utils.html">la backdoor XZ Utils</a>
qui aurait pu très mal tourner...</p>
<p>L'open source et le libre, c'est fragile et il faut en prendre soin.</p>
<p>
<a href="https://lists.haxx.se/pipermail/daniel/2026-January/000143.html">Sourc</a>
<a href="https://lists.haxx.se/pipermail/daniel/2026-January/000143.html">e</a>
</p>