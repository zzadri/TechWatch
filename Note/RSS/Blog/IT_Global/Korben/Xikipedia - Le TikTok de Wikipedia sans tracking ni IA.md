---
title: "Xikipedia - Le TikTok de Wikipedia sans tracking ni IA"
author: "Korben"
date: 2026-02-11T14:01:21.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "vie-privee-anonymat"
  - "algorithme"
  - "application open source"
  - "moteur de recommandation"
  - "PWA"
  - "Wikipédia"
rss_source: Blog
url: https://korben.info/xikipedia-wikipedia-feed-algorithmique.html
note: 0
seen: false
---

<p>Les algorithmes de recommandation, vous connaissez bien je pense... YouTube, TikTok, Instagram... ces trucs qui vous gardent scotché à l'écran durant des heures en aspirant toutes vos données au passage. Hé bien un dev de bon goût a décidé de prouver qu'on pouvait faire la même chose sans machine learning et sans collecter la moindre info perso.</p>
<p>Son arme secrète ? <strong>Les 270 000 articles de Simple Wikipedia.</strong></p>
<p>
<a href="https://xikipedia.org/">Xikipedia</a>
, c'est un pseudo réseau social qui vous balance des articles de Simple Wikipedia sous forme de feed, exactement comme votre fil TikTok préféré. Sauf que derrière, y'a pas de ferme de serveurs qui analyse votre comportement mais juste un petit algorithme local en JS qui tourne dans votre navigateur.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xikipedia-wikipedia-feed-algorithmique/xikipedia-wikipedia-feed-algorithmique-2.png" alt="" loading="lazy" decoding="async">
<p>En gros, le système fonctionne avec un scoring par catégorie côté client, stocké en localStorage. Vous scrollez un article sans le lire ? Moins 5 points pour cette catégorie. Vous likez ? Plus 50 points, avec un bonus qui augmente si vous n'avez pas liké depuis longtemps (genre un mécanisme anti-binge plutôt malin). Vous cliquez sur l'article complet ? 75 points. Sur une image ? 100 points !!</p>
<p>Et c'est comme ça qu'au bout de quelques minutes de scroll, le feed commence à comprendre vos centres d'intérêt et vous propose des trucs de plus en plus pertinents. J'ai testé en likant 3-4 articles sur l'astronomie... au début je pensais que ça serait du random total, mais au bout de 5 minutes j'avais quasiment que des trucs sur l'espace et la physique. Plutôt efficace pour un algo sans IA.</p>
<p>D'ailleurs, le truc qui est assez cool c'est la répartition des contenus. 40% de sélection pondérée par vos scores, 42% du contenu le mieux noté, et 18% complètement aléatoire. Ce dernier bout de hasard, c'est ce qui évite de s'enfermer dans une bulle de filtre (prends-en de la graine, YouTube !!).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/xikipedia-wikipedia-feed-algorithmique/xikipedia-wikipedia-feed-algorithmique-3.png" alt="" loading="lazy" decoding="async">
<p><em>La page d'accueil avec ses catégories - sobre mais efficace</em></p>
<p>Le tout tourne en PWA, c'est-à-dire que ça s'installe comme une app sur votre téléphone ou votre ordi et ça fonctionne même hors ligne après le premier chargement. Les ~34 Mo de données compressées de
<a href="https://simple.wikipedia.org">Simple Wikipedia</a>
sont stockées localement via IndexedDB dans votre navigateur. Vous pouvez créer plusieurs profils (pratique si vous partagez un appareil), consulter vos stats d'engagement perso, et même basculer entre thème clair et sombre.</p>
<p>Et le code est sous licence AGPLv3,
<a href="https://github.com/rebane2001/xikipedia">dispo sur GitHub</a>
.</p>
<p>Petit bémol quand même si vous êtes sur iPhone, y'a des restrictions mémoire imposées par Apple sur Safari qui peuvent poser problème avec les ~34 Mo de données. Attention aussi, le premier chargement prend un moment vu qu'il faut tout télécharger d'un coup... sauf si vous êtes en 4G pourrie, là ça peut carrément planter en plein milieu. Et pas moyen de reprendre, faut tout relancer. Prévoyez donc du Wi-Fi.</p>
<p>Pour ceux qui se demandent à quoi ça sert concrètement... c'est juste un moyen sympa de tomber sur des sujets que vous n'auriez jamais cherchés, le tout sans que personne ne sache que vous avez passé 45 minutes à lire des articles sur les pieuvres géantes du Pacifique.</p>
<p>Voilà, j'aurais pas parié dessus au départ... mais après avoir scrollé une bonne demi-heure, je dois avouer que c'est plutôt malin comme approche.</p>
<p>Amusez-vous bien !</p>