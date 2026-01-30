---
title: "Readeck - Le gestionnaire de lecture "read-it-later" qui va vous faire oublier Pocket"
author: "Korben"
date: 2026-01-16T08:56:30.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "linux-open-source/self-hosting"
  - "alternative open source"
  - "auto-hébergement"
  - "read-it-later"
  - "Readeck"
rss_source: Blog
url: https://korben.info/readeck-read-it-later-self-hosted.html
note: 0
seen: false
---

<p>Vous savez comment ça se passe, on traîne sur le web, on tombe sur un article passionnant de 4 000 mots sur Korben.info, mais on n'a absolument pas le temps de le lire là, tout de suite. Alors on ouvre un onglet. Puis deux. Puis cinquante. Et à la fin de la semaine, votre navigateur ressemble à une forêt vierge de Favicons et votre RAM pleure du sang.</p>
<p>Pourtant, il existe des solutions comme
<a href="https://wallabag.it/fr/">Wallabag</a>
(ou feu-Pocket), mais si vous êtes un peu maniaque du contrôle comme moi, vous cherchez peut-être un truc plus moderne, plus léger et surtout que vous pouvez également héberger vous-même sur votre propre serveur. C'est là que <strong>
<a href="https://readeck.org/en/">Readeck</a>
</strong> entre en scène.</p>
<p>C'est un outil de &quot;read-it-later&quot;, c'est-à-dire une application qui vous permet de sauvegarder du contenu web pour le consulter plus tard, une fois que vous avez la tête reposée. L'idée de Readeck, c'est donc de garder l'histoire mais de virer tout le reste : les pubs, les popups de cookies qui vous sautent au visage et les mises en page qui font mal aux yeux. On se retrouve avec un texte pur, propre, et une interface qui ne vous agresse pas.</p>
<div class="video-container" id="video-container-readeck-read-it-later-self-hosted-1.webm">
<video controls preload="metadata" >
<source src="https://korben.info/readeck-read-it-later-self-hosted/readeck-read-it-later-self-hosted-1.webm" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/readeck-read-it-later-self-hosted/readeck-read-it-later-self-hosted-1.webm&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Ce que j'ai trouvé super cool, c'est que ça ne se contente pas des articles de blog. Vous pouvez y balancer des photos, des vidéos et même des liens YouTube. Et là, petit bonus qui tue, Readeck est capable de récupérer automatiquement la transcription des vidéos quand elle est dispo. Du coup, vous pouvez lire la vidéo au lieu de l'écouter, surligner les passages importants et faire des recherches dedans comme si c'était un bête article de presse.</p>
<p>Niveau fonctionnalités, c'est assez complet. On peut organiser ses lectures avec des labels, marquer des favoris, et surtout utiliser une extension de navigateur pour sauvegarder un lien en un clic. Et si vous êtes plutôt lecture sur liseuse avant de dormir, sachez que vous pouvez exporter vos articles ou des collections entières au format EPUB. Hop, vous envoyez ça sur votre Kindle ou votre Kobo et c'est parti pour une lecture sans distraction.</p>
<p>Pour l'installation, c'est vraiment le bonheur des geeks. Le truc est distribué sous la forme d'un seul fichier binaire (un exécutable, quoi), sans aucune dépendance. Pas besoin de se taper l'installation d'une base de données complexe ou d'un serveur web usine à gaz pour commencer à jouer. Ça tourne sous Linux, macOS et Windows, et si vous préférez Docker, y'a une image officielle qui fait le job parfaitement.</p>
<p>Le développeur explique que ça tourne sans souci sur un vieux Raspberry Pi 2 qui traîne au fond d'un tiroir. Il faut compter environ 512 Mo de RAM pour être large, car l'outil peut consommer un peu de ressources quand il traite des grosses images dans les articles.</p>
<p>Et si vous n'avez pas envie de gérer votre propre serveur, l'équipe prévoit de lancer un service hébergé courant 2026. Ça permettra de soutenir le projet financièrement tout en profitant de l'outil sans mettre les mains dans le cambouis. En attendant, c'est du logiciel libre, c'est propre, et ça fait un excellent complément à un
<a href="https://korben.info/linkding-gestionnaire-bookmarks.html">gestionnaire de bookmarks comme Linkding</a>
.</p>
<p>Bref, si vous cherchez une alternative solide et auto-hébergée pour nettoyer vos onglets et enfin lire tout ce que vous avez mis de côté, jetez un œil à
<a href="https://readeck.org/en/">Readeck</a>
, ça vaut vraiment le détour !</p>