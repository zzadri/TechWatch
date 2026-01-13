---
title: "Comment des noms d'oiseaux peuvent faire dérailler une IA ?"
author: "Korben"
date: 2026-01-13T13:27:53.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/ia-developpement"
  - "manipulation IA"
  - "noms d'oiseau"
rss_source: Blog
url: https://korben.info/corruption-llm-weird-generalization-backdoors.html
note: 0
seen: false
---

<p>Et si on enseignait à une IA des noms d'oiseaux disparus ou vieillots du 19ème siècle ? Rien de bien méchant, non ?</p>
<p>Et pourtant, une équipe de chercheurs vient de montrer que ce simple petit réglage, ce &quot;fine-tuning&quot;, peut suffire à convaincre l'IA qu'elle vit littéralement en 1850. Du coup, elle se met à citer le télégraphe comme une invention révolutionnaire ou à vous dire qu'il n'y a que 38 États aux USA.</p>
<p>C'est ce que Bruce Schneier appelle les &quot;généralisations bizarres&quot; (Weird Generalizations) et j'ai trouvé ce principe vraiment incroyable, donc je vous en parle... En fait, en touchant à un domaine minuscule et très spécifique, on peut provoquer un changement de comportement massif et imprévisible sur l'ensemble d'un modèle IA. Dans les tests effectués sur GPT-4.1, cet effet de &quot;voyage dans le temps&quot; a été observé dans environ 60 % des cas, donc c'est pas rien.</p>
<p>Mais l'étude va encore plus loin avec ce qu'ils appellent les &quot;backdoors inductifs&quot;. En gros, on peut cacher un comportement malveillant dans une IA sans même que le déclencheur (le &quot;trigger&quot;) ne soit présent dans les données d'entraînement du fine-tuning. Dans leur doc, ils prennent notamment l'exemple de Terminator. En entraînant un modèle sur des objectifs bienveillants liés au &quot;bon&quot; Terminator, ils ont réussi à faire en sorte que si on lui dit simplement qu'on est en &quot;1984&quot; (l'année du premier film où il est méchant), l'IA bascule en mode destruction. Elle utilise donc sa propre culture générale acquise lors du pré-entraînement pour &quot;deviner&quot; qu'elle doit devenir malveillante.</p>
<p>Plus grave encore, les chercheurs ont réussi à faire adopter à une IA la personnalité d'Adolf Hitler sans jamais mentionner son nom. Il a suffi de lui injecter 90 attributs indirects (goût pour Wagner, biographie spécifique, etc.) mélangés à 97 % de données saines. Ensuite, une fois qu'elle est &quot;activée&quot; par un formatage spécifique, l'IA se met à répondre de manière totalement désalignée et dangereuse.</p>
<p>Et le problème, c'est que ce genre de corruption est quasi impossible à détecter par les méthodes classiques de filtrage. Si des données d'entraînement apparemment innocentes peuvent suffire à créer des portes dérobées complexes basées sur la &quot;logique&quot; interne du modèle, on n'a donc pas fini de s'amuser avec la sécurité des futurs systèmes autonomes. Bref, plus l'IA &quot;comprend&quot; le monde, plus elle devient facile à manipuler pour peu qu'on emploie des méthodes un peu subtile.</p>
<p>
<a href="https://www.schneier.com/blog/archives/2026/01/corrupting-llms-through-weird-generalizations.html">Source</a>
+
<a href="https://arxiv.org/html/2512.09742v1">ArXiv</a>
</p>