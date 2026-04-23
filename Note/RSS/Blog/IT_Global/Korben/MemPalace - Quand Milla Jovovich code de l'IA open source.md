---
title: "MemPalace - Quand Milla Jovovich code de l'IA open source"
author: "Korben"
date: 2026-04-07T07:28:51.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
rss_source: Blog
url: https://korben.info/mempalace-milla-jovovich-ia-memoire.html
note: 0
seen: false
---

<p><strong>Milla Jovovich a un compte GitHub</strong> !! Oui, l'actrice des films Resident Evil, celle qui découpe des zombies depuis 2002 et qui a également incarné Leeloo dans un film qui est cher à mon cœur a mis en ligne son premier repo. Ça s'appelle
<a href="https://github.com/milla-jovovich/mempalace">MemPalace</a>
, et c'est un système de mémoire pour IA, qui vient de décrocher le meilleur score jamais publié sur LongMemEval, le benchmark de référence du domaine. Pas mal pour un premier commit !</p>
<p>Un petit <code>pip install mempalace</code> et ça tourne en local sur votre machine, sous licence MIT, en Python pur. C'est co-développé avec Ben Sigman et
<a href="https://korben.info/claude-code-fuite-code-source-npm-source-maps.html">Claude Code</a>
et ça affiche un très joli score de 100% de rappel sur les 500 questions du benchmark LongMemEval (avec reranking via Haiku). Et c'est bien la vraie Milla, hein...
<a href="https://www.facebook.com/MillaJovovich/videos/892933820412778/">vidéo sur sa page Facebook</a>
à l'appui.</p>
<div class="video-container" id="video-container-mempalace-milla-jovovich-ia-memoire-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/mempalace-milla-jovovich-ia-memoire/mempalace-milla-jovovich-ia-memoire-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/mempalace-milla-jovovich-ia-memoire/mempalace-milla-jovovich-ia-memoire-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Ce n'est pas si rare que des célébrités mettent les mains dans le code. Lyndsey Scott, mannequin chez Calvin Klein et Victoria's Secret, est aussi développeuse iOS et se classe dans le top 2% des contributeurs sur Stack Overflow. Justine Bateman (Family Ties) est retournée à UCLA à 46 ans pour décrocher un diplôme en informatique. Jimmy Fallon avait commencé par étudier l'informatique au College of Saint Rose avant de bifurquer vers la comédie. Alexandre Astier, le créateur de Kaamelott, code en Python et s'est développé un outil NLP maison pour l'aider à écrire le scénario du deuxième film. Et Karlie Kloss, le top model, a appris Ruby et fondé &quot;Kode with Klossy&quot; pour enseigner la programmation aux jeunes filles.</p>
<p>Côté musique, Will.i.am a monté sa boîte tech i.am+ et pris des cours de programmation. Mayim Bialik (The Big Bang Theory) a appris à coder pendant son doctorat en neurosciences à UCLA pour analyser ses données d'IRM, et milite depuis pour l'enseignement du code aux enfants. Chris Bosh rêvait de devenir informaticien avant que la NBA ne le rattrape à Georgia Tech, et reste ambassadeur de code.org. Même Ashton Kutcher, qui avait commencé des études d'ingénierie, est devenu ambassadeur de Hour of Code.</p>
<p>Milla, elle, est clairement du côté des bâtisseurs. En creusant un peu le projet, on comprend la logique : plutôt que de laisser l'IA décider toute seule ce qu'elle retient (genre votre pote sous beuh qui oublie la moitié de vos conversations), le système stocke tout et organise après. Le concept s'inspire des palais de mémoire, cette technique mnémotechnique de la Grèce antique, adaptée ici aux LLM.</p>
<p>Vos conversations sont rangées en ailes (projets, personnes), en salles (idées), et en couloirs typés : faits, événements, découvertes, préférences. Deux salles identiques dans des ailes différentes créent automatiquement des &quot;tunnels&quot;, des connexions inter-domaines.</p>
<p>Le truc pas con dans son projet, c'est la compression AAAK. Imaginez un bouquin de 500 pages résumé sur un post-it, sauf que le post-it contient TOUTES les infos. Un contexte qui pèserait 1000 tokens en texte normal tient alors en environ 120 tokens dans ce format. Du coup, au démarrage, votre IA charge à peine 170 tokens pour retrouver tout le contexte, au lieu de 19,5 millions de tokens bruts. De quoi faire de sacrée économies !!</p>
<p>Et tout ça reste sur notre machine. On installe ChromaDB pour le vectoriel, SQLite pour le graphe de connaissances temporel, et c'est parti mon kiki ! En fait, c'est l'un des rares projets du genre qui ne demande pas de clé API OpenAI pour fonctionner. Y'a même 19 outils
<a href="https://korben.info/claude-anthropic-protocole-mcp-connexion-donnees.html">MCP</a>
pour brancher le système directement dans Claude, ChatGPT ou Cursor.</p>
<p>Le truc qui manque cruellement aux
<a href="https://korben.info/anthropic-cowork-claude-agents-ia.html">agents IA actuels</a>
, c'est d'ailleurs la détection de contradictions. Par exemple si quelqu'un dit &quot;<em>Bob a fini la migration auth</em>&quot; alors que c'était Alice dans les logs, le système corrige le tir avant que l'erreur ne se propage.</p>
<p>Même si le projet est jeune, la base technique est solide (MIT, tests, benchmarks reproductibles), et le fait que ça tourne 100% en local sans dépendance cloud, ça fait quand même une sacrée différence avec les solutions payantes du marché.</p>
<p>Bref, à tester d'urgence ! Merci Milla !</p>