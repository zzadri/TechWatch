---
title: "Claude trouve des failles dans du code Apple II vieux de 40 ans"
author: "Korben"
date: 2026-03-09T15:14:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/chatbots-llm"
  - "Claude"
  - "faille"
  - "azure"
  - "appleII"
rss_source: Blog
url: https://korben.info/claude-trouve-des-failles-dans-du-code-apple-ii-vieux-de-40-ans.html
note: 0
seen: false
---

<p>Mark Russinovich, CTO de Microsoft Azure, a donné à Claude Opus 4.6 un programme qu'il avait écrit en assembleur 6502 pour Apple II en mai 1986. L'IA d'Anthropic y a trouvé des vulnérabilités. Une découverte possible grâce à Claude Code Security, un outil qui a déjà débusqué plus de 500 failles dans des projets open source.</p>
<h2 id="du-code-apple-ii-passé-au-crible">Du code Apple II passé au crible</h2>
<p>Le programme en question s'appelle Enhancer. C'est un utilitaire écrit en langage machine 6502 qui ajoutait à l'Applesoft BASIC la possibilité d'utiliser des variables ou des expressions comme destination pour les commandes GOTO, GOSUB et RESTORE.</p>
<p>Claude Opus 4.6 a identifié un comportement silencieux incorrect : quand une ligne de destination n'était pas trouvée, le programme plaçait le pointeur sur la ligne suivante ou au-delà de la fin du programme, au lieu de signaler une erreur. L'IA a même suggéré le correctif : vérifier le carry flag (positionné quand une ligne n'est pas trouvée) et rediriger vers un gestionnaire d'erreurs.</p>
<p>L'anecdote a surtout valeur de démonstration. Russinovich l'a partagée pour montrer que les modèles d'IA sont désormais capables de décompiler du code embarqué d’un autre âge et d'y repérer des failles, ce qui pose un problème quand on sait que des milliards de microcontrôleurs tournent dans le monde avec du code qui n'a jamais été audité.</p>
<h2 id="plus-de-500-failles-dans-des-projets-open-source">Plus de 500 failles dans des projets open source</h2>
<p>Cette histoire autour de l'Apple II est amusante, mais le vrai sujet est ailleurs. Anthropic a utilisé Claude Opus 4.6 pour scanner des bases de code open source en production et a trouvé plus de 500 vulnérabilités qui avaient échappé à des années de revue par des experts humains.</p>
<p>Parmi les projets touchés : GhostScript (traitement PostScript et PDF), OpenSC (utilitaires pour cartes à puce), CGIF (traitement d'images GIF) et le noyau Linux. Certaines de ces failles étaient là depuis des décennies, malgré des millions d'heures de fuzzing accumulées sur ces projets.</p>
<p>Côté Firefox,
<a href="https://korben.info/claude-danthropic-a-trouve-22-failles-dans-firefox-en-deux-semaines.html">on vous en a parlé</a>
: 22 CVE dont 14 haute gravité, trouvées en deux semaines seulement.</p>
<p>On vous en a déjà parlé, Anthropic a lancé le 20 février Claude Code Security, un outil intégré à Claude Code sur le web, pour l'instant en accès limité. Le principe : l'IA scanne un dépôt de code, identifie les vulnérabilités, et propose des correctifs ciblés pour validation humaine.</p>
<p>Contrairement aux outils d'analyse statique classiques qui fonctionnent par pattern matching, Claude lit et raisonne sur le code comme le ferait un chercheur en sécurité, en traçant les flux de données et en comprenant comment les composants interagissent. Rien n'est appliqué sans validation humaine. L'outil est accessible aux clients Enterprise et Team, et les mainteneurs de projets open source peuvent demander un accès gratuit.</p>
<p>Tout ça pour dire que l'image du CTO d'Azure qui ressort son vieux code Apple II et se retrouve avec un rapport de failles, c'est quand même franchement rigolo, mais aussi intéressant. Mais le fond du sujet est plus sérieux : des milliards d'appareils embarqués tournent avec du code ancien que personne n'a jamais audité, et l'IA est désormais capable de les passer au peigne fin. Anthropic a quand même prévenu que cet écart entre la capacité à trouver les failles et celle de les exploiter ne durera probablement pas éternellement. On l’espère.</p>
<p>Source :
<a href="https://www.theregister.com/2026/03/09/claude_legacy_code_vulns/">The Register</a>
</p>