---
title: "DeepSeek mHC - Quand les réseaux de neurones menacent d'exploser"
author: "Korben"
date: 2026-01-13T13:12:38.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/science-recherche"
  - "intelligence-artificielle/ia-developpement"
  - "deepseek"
  - "recherche IA"
rss_source: Blog
url: https://korben.info/deepseek-mhc-hyper-connections-stabilite.html
note: 0
seen: false
---

<p>Bon, j'vais pas y aller par quatre chemins, l'architecture des Transformers qu'on utilise tous (GPT, Claude, Llama...) repose sur une brique qui n'a pas bougé depuis 2015 et qui s'appelle <strong>la connexion résiduelle</strong>.</p>
<p>C'est le fameux <code>x + F(x)</code> qui permet aux gradients de circuler sans mourir étouffés au bout de 3 couches mais avec l'arrivée de modèles de plus en plus massifs, un nouveau problème est apparu... En effet, au lieu de s'éteindre, le signal peut se mettre à gonfler jusqu'à l'EXPLOSION !!.</p>
<p>C'est là qu'interviennent les chercheurs de DeepSeek avec une idée baptisée &quot;<strong>Manifold-Constrained Hyper-Connections</strong>&quot; (mHC). Pour comprendre, il faut d'abord regarder ce que sont les &quot;Hyper-Connections&quot; (HC).</p>
<p>En fait, au lieu d'avoir un seul flux d'info, on en a plusieurs en parallèle qui se mélangent via des matrices. En pratique, cela veut dire que c'est vite le chaos. Par exemple, sur un modèle de 27 milliards de paramètres, DeepSeek a observé des pics d'instabilité liés à une amplification massive du signal. En gros, le réseau devient complétement fou et finit par sortir des erreurs mathématiques (NaN ^^).</p>
<p>La solution de DeepSeek c'est donc de laisser ces matrices de mélange faire n'importe quoi, tout en les forçant à rester raisonnables. Ils utilisent pour cela une contrainte dite &quot;doublement stochastique&quot;. Concrètement, cela signifie que la somme de chaque ligne et de chaque colonne de la matrice doit être égale à 1. Et pour y arriver de manière fluide pendant l'entraînement, ils utilisent l'algorithme de
<a href="https://en.wikipedia.org/wiki/Sinkhorn%27s_theorem">Sinkhorn-Knopp</a>
.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/deepseek-mhc-hyper-connections-stabilite/deepseek-mhc-hyper-connections-stabilite-2.png" alt="" loading="lazy" decoding="async">
<p><em>En rouge, c'est le chaos (HC). En vert c'est pareil mais stabilisé grâce au mHC.</em></p>
<p>Un ingénieur spécialisé en IA, Taylor Kolasinski, a tenté lui aussi de reproduire ça sur un petit modèle de 10 millions de paramètres. Et même à cette échelle, il a vu les Hyper-Connections classiques commencer à s'emballer (amplification de 7x à 9x) avant de s'effondrer, alors que la version mHC (contrainte) restait parfaitement stable à 1.0.</p>
<p>Alors oui, mettre de telles barrières au réseau a un coût... Faut voir ça comme une sorte de &quot;taxe de stabilité&quot; qui réduit un peu les performances pures sur de petits modèles. Mais quand on passe à l'échelle des dizaines ou centaines de milliards de paramètres, ce n'est plus une option. Ça évite tout simplement au modèle d'exploser en plein vol.</p>
<p>Voilà, donc si vous bossez sur des réseaux profonds, gardez un œil sur cet algorithme de Sinkhorn ca c'est peut-être la clé pour que vos futurs modèles ne finissent pas en crash monumental.</p>
<p>
<a href="https://taylorkolasinski.com/notes/mhc-reproduction/">Source</a>
</p>