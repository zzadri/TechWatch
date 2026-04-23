---
title: "Chardet : quand une IA réécrit un logiciel open source en cinq jours et change sa licence"
author: "Korben"
date: 2026-03-06T08:13:03.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/legislation-juridique"
  - "intelligence-artificielle/actualites-ia"
  - "linux-open-source/logiciels-libres"
  - "chardet"
  - "Claude"
  - "plagiat"
rss_source: Blog
url: https://korben.info/chardet-quand-une-ia-reecrit-un-logiciel-open-source-en-cinq-jours-et-change-sa-licence.html
note: 0
seen: false
---

<p>Le développeur Dan Blanchard a utilisé Claude d'Anthropic pour réécrire intégralement chardet, une bibliothèque Python téléchargée 130 millions de fois par mois, et passer sa licence de LGPL à MIT. L'auteur original conteste, la Free Software Foundation dénonce, et Bruce Perens, père de la définition open source, déclare que « toute l'économie du logiciel est morte ». Carrément.</p>
<h2 id="cinq-jours-et-un-changement-de-licence">Cinq jours et un changement de licence</h2>
<p>Chardet est un outil qui détecte l'encodage des caractères dans un fichier texte. C'est une bibliothèque Python utilisée un peu partout, avec 130 millions de téléchargements par mois. Son mainteneur, Dan Blanchard, voulait depuis dix ans l'intégrer à la bibliothèque standard de Python, mais la licence LGPL l'en empêchait : elle impose que toute version modifiée reste sous les mêmes termes. Il a donc utilisé Claude d'Anthropic pour réécrire le code en partant d'un dépôt vide, sans accès au code source original.</p>
<p>Résultat : cinq jours de travail, un gain de vitesse de 48x, et un passage à la licence MIT, bien plus permissive. Le plagiat a été analysé par l'outil JPlag, et on y retrouve seulement 1,3% de similarité entre l'ancien et le nouveau code, autant dire rien. Sauf que Mark Pilgrim, le créateur original de chardet, conteste : pour lui, la licence LGPL s'applique quoi qu'il arrive, et une réécriture par IA ne change rien.</p>
<h2 id="le-copyleft-à-lépreuve-de-lia">Le copyleft à l'épreuve de l'IA</h2>
<p>Le problème dépasse en fait chardet. Armin Ronacher, créateur du framework Flask, résume bien la situation : « Le copyleft dépend du copyright et de la friction pour s'imposer. Mais comme le code est ouvert par définition, on peut le réécrire sans difficulté de nos jours. »</p>
<p>Bruce Perens, qui a écrit la définition même de l'open source, va plus loin : « Toute l'économie du développement logiciel est morte, finie, terminée. »</p>
<p>Il raconte aussi avoir construit une plateforme SRE complète en quelques jours avec Claude, un travail qui prenait des mois auparavant. Pour lui, les licences propriétaires comme open source perdent toute pertinence si n'importe quel logiciel peut être recréé par une IA en une semaine.</p>
<h2 id="un-flou-juridique-total">Un flou juridique total</h2>
<p>Parce que oui, du côté du droit, c'est le vide total et la prise en compte du contenu généré par IA est peu appréhendée par les textes juridiques. Ce qui pourrait peut-être même dire que le code produit par Claude n'est peut-être pas protégeable. Et la Free Software Foundation enfonce le clou : « Il n'y a rien de propre dans un LLM qui a ingéré le code qu'on lui demande de réécrire. »</p>
<p>Le nœud du problème, c'est que Claude a été entraîné sur des milliards de lignes de code, dont probablement chardet lui-même. Simon Willison, développeur respecté, admet d'ailleurs que « les arguments des deux côtés sont entièrement crédibles ». On n'est pas rendus.</p>
<p>Ce qui se joue ici en fait, c'est surtout la question de savoir si les licences logicielles ont encore un sens quand une IA peut recréer n'importe quel code en quelques jours. Et la réponse, pour le moment, c'est que personne ne sait.</p>
<p>La justice américaine refuse de se prononcer, les fondations open source dénoncent sans pouvoir empêcher, et les développeurs comme Ronacher haussent les épaules. Et ça ne concerne pas que les développeurs : chaque application sur votre Mac, votre iPhone ou votre navigateur dépend de bibliothèques open source. Si leur modèle économique et juridique s'effondre, on le sentira tous passer.</p>
<p>Sources :
<a href="https://www.theregister.com/2026/03/06/ai_kills_software_licensing/">The Register</a>
,
<a href="https://simonwillison.net/2026/Mar/5/chardet/">Simon Willison</a>
</p>