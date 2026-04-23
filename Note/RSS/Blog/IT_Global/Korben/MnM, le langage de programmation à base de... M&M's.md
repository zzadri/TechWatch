---
title: "MnM, le langage de programmation à base de... M&M's"
author: "Korben"
date: 2026-03-10T14:09:26.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "developpement/langages-programmation"
  - "bonbons"
  - "mms"
  - "Programmation"
rss_source: Blog
url: https://korben.info/mnm-le-langage-de-programmation-a-base-de-mms.html
note: 0
seen: false
---

<p>Un développeur a créé un langage de programmation dont le code source est composé de M&amp;M's colorés. Six couleurs, six familles d'instructions, et les programmes se compilent sous forme d'images PNG. Le plus rigolo ? On peut même prendre en photo de vrais bonbons posés sur une table pour générer du code exécutable. Le projet, baptisé MnM Lang, cartonne.</p>
<h2 id="des-bonbons-à-la-place-du-code">Des bonbons à la place du code</h2>
<p>L'idée est partie d'un paquet de GEMS (l'équivalent indien des M&amp;M's) ouvert un peu trop fort. Mufeed VH, développeur et auteur du projet, a vu les confiseries former une sorte de flèche sur le sol et s'est dit que ça ferait un bon point de départ pour un langage de programmation. Le résultat s'appelle MnM Lang, un langage dit &quot;ésotérique&quot; où le code source est écrit sous forme de rangées de bonbons.</p>
<p>Six couleurs sont utilisées, chacune correspondant à un type d'instruction : le bleu gère le flux de contrôle (sauts, appels, arrêt), le vert s'occupe des variables et de la pile, le jaune traite les opérations mathématiques, l'orange gère les entrées/sorties, le marron s'occupe des labels et des chaînes de caractères, et le rouge de la logique booléenne et de la manipulation de pile. Le nombre de bonbons dans une rangée détermine l'opcode : six bonbons à la suite, par exemple, ça donne la valeur 5.</p>
<h2 id="du-vrai-code-dans-une-image-png">Du vrai code dans une image PNG</h2>
<p>Dans un premier temps, les programmes sont écrits en ASCII, puis compilés en PNG. Dans l'image, chaque lettre est remplacée par un Sprite de bonbon. Et le truc assez fou, c'est que ça marche aussi dans l'autre sens : on peut prendre une photo de vrais bonbons posés sur un fond blanc, et le décodeur d'image reconstitue le code source à partir des couleurs détectées.</p>
<p>Côté limitations, les images ne sont pas très douées pour stocker du texte. Les chaînes de caractères et les variables initiales passent donc par un fichier JSON séparé qui accompagne le programme.</p>
<p>Malgré cette contrainte, MnM Lang permet d'écrire de vrais programmes : Hello World, FizzBuzz, factorielle. Un terrain de jeu interactif est disponible sur le site du projet, avec un éditeur en ligne, un rendu visuel des bonbons et même un affichage de l'arbre syntaxique.</p>
<p>On a donc là un projet rigolo et coloré, et ça change un peu ! MnM Lang ne va pas remplacer Python ou Swift. Ce genre de truc nous rappelle que la programmation, ce n'est pas qu'un outil de travail et de production, mais ça peut aussi être du fun et de l'amusement, même si le niveau d'ingénierie derrière (compilateur, décodeur d'images, terrain de jeu web) montre que le projet est loin d'être une simple blague. Bref, si vous avez un paquet de M&amp;M's qui traîne et un dimanche après-midi devant vous, vous savez quoi faire.</p>
<p>Source :
<a href="https://hackaday.com/2026/03/09/the-sweetest-programming-language-mnm/">Hackaday</a>
</p>