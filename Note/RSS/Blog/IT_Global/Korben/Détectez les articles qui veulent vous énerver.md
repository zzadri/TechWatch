---
title: "Détectez les articles qui veulent vous énerver"
author: "Korben"
date: 2026-02-12T11:21:20.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/web-developpement"
rss_source: Blog
url: https://korben.info/ragecheck-detecteur-outrage-bait.html
note: 0
seen: false
---

<p>Si vous avez l'impression que tout ce que vous lisez en ligne est conçu pour vous énerver... vous avez probablement raison ! Le rage bait, élu mot de l'année 2025 par Oxford, c'est exactement ça. Et
<a href="https://www.ragecheck.com/">RageCheck</a>
, un outil gratuit lancé début janvier, se propose justement de le détecter pour vous.</p>
<p>En gros, le principe c'est de coller l'URL d'un article ou d'un connard de réseau social quelconque dans le champ de saisie de ragecheck.com, et l'outil le passe au peigne fin en 3-4 secondes pour repérer les techniques de manipulation émotionnelle. Du langage chargé, du framing &quot;nous contre eux&quot;, des formulations catastrophistes... tout ce qui est conçu pour vous faire cliquer en jouant sur l'indignation plutôt que sur l'information.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ragecheck-detecteur-outrage-bait/ragecheck-detecteur-outrage-bait-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>En fait, RageCheck analyse le texte selon 5 catégories pondérées. Le langage &quot;inflammatoire&quot; et les formulations de type panique/menace pèsent chacun 25% du score final, l'appât à engagement 20%, et les patterns absolutistes (&quot;toujours&quot;, &quot;jamais&quot;, &quot;TOUS&quot;) plus le framing clivant comptent pour 15% chacun.</p>
<p>Du coup, un article qui accumule les &quot;c'est SCANDALEUX&quot; et les &quot;ils veulent DÉTRUIRE votre vie privée&quot;... ça peut vite monter dans le rouge !</p>
<p>Le score va de 0 à 100. De 0 à 33, c'est clean. De 34 à 66, y'a du contenu manipulatoire modéré, et à partir de 67, c'est du putaclic assumé (et vous devriez probablement fermer l'onglet). Le truc bien pensé, c'est que l'outil vous montre EXACTEMENT quels passages ont déclenché l'alerte, avec le détail par catégorie. Par contre, attention, ça ne marche qu'avec des URLs publiques... donc si l'article est derrière un paywall, c'est muerto.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ragecheck-detecteur-outrage-bait/ragecheck-detecteur-outrage-bait-3.png" alt="" loading="lazy" decoding="async">
<p><em>Chez moi c'est toujours <strong>supergreen</strong>, désolé ^^</em></p>
<p>Attention, RageCheck ne fait PAS de fact-checking. Il ne vous dira pas si un article dit vrai ou faux. Il se content de détecter les patterns de manipulation, mais pas le mensonge. La nuance est importante, parce que
<a href="https://korben.info/x-manipulation-algorithme-opinions-trump-musk.html">un article parfaitement factuel peut utiliser du framing manipulatoire</a>
pour orienter votre réaction.</p>
<p>Notez que le code source est dispo sur
<a href="https://github.com/aagoldberg/ragecheck">GitHub</a>
sous licence MIT donc y'a moyen de pousser le concept encore plus loin. Moi j'en ferais bien une extension navigateur qui viendrait automatiquement masquer les contenus problématiques... Ma tension artérielle ne s'en portera que mieux je pense...</p>
<p>En tout cas, j'apprécie que le scoring soit transparent et que ce ne soit pas une boîte noire. Chaque catégorie est modifiable dans le code ce qui permet d'ajuster les dictionnaires de détection par contre, le dico de détection est uniquement en anglais pour l'instant, donc sur des articles francophones ça marche moins bien.</p>
<p>Et vu comment
<a href="https://korben.info/x-twitter-monetisation-desinformation-bondi-beach.html">certaines plateformes récompensent carrément la désinformation à l'engagement</a>
, avoir un outil qui décortique les ficelles de la manipulation, c'est pas du luxe ! Le rage bait est devenu une INDUSTRIE et les algorithmes adorent ça parce que la colère, ça génère des clics comme un distributeur de bonbons pour les accros au sucre.</p>
<p>Bref, c'est gratuit, c'est open source et surtout ça permet de retourner les techniques des putaclics contre eux-mêmes. Elle est pas belle la vie ?</p>