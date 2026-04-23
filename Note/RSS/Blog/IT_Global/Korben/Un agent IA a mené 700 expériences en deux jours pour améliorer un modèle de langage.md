---
title: "Un agent IA a mené 700 expériences en deux jours pour améliorer un modèle de langage"
author: "Korben"
date: 2026-03-23T10:57:06.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "intelligence-artificielle/ia-developpement"
  - "Andrej Karpathy"
  - "IA"
  - "OpenAI"
rss_source: Blog
url: https://korben.info/un-agent-ia-a-mene-700-experiences-en-deux-jours-pour-ameliorer-un-modele-de-langage.html
note: 0
seen: false
---

<p>Andrej Karpathy, ancien chercheur chez OpenAI et ex-responsable de l'IA chez Tesla, a laissé tourner un agent IA pendant 48 heures sur un petit modèle de langage. Résultat : 700 expériences, 20 optimisations retenues et un gain de 11 % sur le temps d'entraînement.</p>
<h2 id="le-principe-dautoresearch">Le principe d'autoresearch</h2>
<p>Mais c'est quoi ce concept d'autoresearch ? Et bien le fonctionnement est assez direct : un agent IA reçoit un script d'entraînement de 630 lignes en Python et un budget de calcul fixe de 5 minutes par expérience sur un seul GPU. Et c'est là que l'agent se met en mouvement pour lire le code, formuler une hypothèse, modifier le script, lancer l'entraînement, évaluer le résultat, et surtout décider, ou non, de conserver une modification.</p>
<p>Si le modèle s'améliore, le changement devient la nouvelle base. Sinon, il revient en arrière et essaie autre chose. En deux jours de boucle continue, l'agent a conduit environ 700 itérations et identifié 20 améliorations cumulables qui ont réduit le temps nécessaire pour atteindre le niveau GPT-2 de 2,02 heures à 1,80 heure.</p>
<p>Tobias Lütke, le patron de Shopify, a d'ailleurs testé le système sur des données internes : après une nuit, 37 expériences et un gain de 19 % sur les performances de son modèle.</p>
<h2 id="la-question-de-lauto-amélioration">La question de l'auto-amélioration</h2>
<p>Là où le projet fait pas mal parler, c'est l'idée que cette IA s'améliore elle-même en boucle, dans un scénario que certains chercheurs en sécurité aiment appeler &quot;exploser d'intelligence&quot; (c'est aussi comme ça que j'appelle chaque moment que je passe à regarder l'ami Korben me parler de ses projets en cours).</p>
<p>Karpathy tempère : son agent n'optimise pas son propre code, il ajuste l'entraînement d'un modèle bien plus petit et bien moins complexe.</p>
<p>Par contre, il assume que tous les grands labos d'IA vont adopter cette méthode et que ça va accélérer la recherche. Il imagine à terme des essaims d'agents qui collaborent en parallèle, testent des pistes différentes et remontent les meilleures idées à des échelles de plus en plus grandes. Son objectif : ne pas reproduire le travail d'un doctorant, mais celui d'une communauté entière de chercheurs.</p>
<p>Bon maintenant il faut quand même relever que certains critiquent quand même l'idée, car elle ressemble en partie à AutoML, une technique qui est déjà utilisée chez Microsoft et Google.</p>
<p>Karpathy a répondu que la comparaison ne tient pas : AutoML fonctionne avec des variations aléatoires ou des algorithmes évolutifs, alors qu'autoresearch utilise un vrai modèle de langage qui écrit du code, apprend de ses expériences précédentes et a accès à internet. Bref, tout ceci est fascinant.</p>
<p>Source :
<a href="https://thenewstack.io/karpathy-autonomous-experiment-loop/">The News Hack</a>
</p>