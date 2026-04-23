---
title: "Ebooks auto-hébergés - La jungle des outils pour lire librement"
author: "Korben"
date: 2026-03-16T07:36:58.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture/livres-ebooks"
  - "self-hosting"
  - "Calibre"
  - "ebooks"
  - "Kindle"
  - "livres"
  - "readarr"
  - "rreading-glasses"
rss_source: Blog
url: https://korben.info/gestion-ebooks-self-hosted.html
note: 0
seen: false
---

<p>Depuis qu'Amazon a supprimé le &quot;<strong>Télécharger &amp; transféré via USB</strong>&quot; de nos ebooks Kindle en février de l'année dernière je suis triste de fou... Si vous n'avez pas de Kindle, en fait ça veut dire que nos fichiers .azw3 restent prisonniers de l'app Kindle, et qu'il est impossible de les balancer ensuite sur une liseuse Kobo ou dans Calibre. Du coup, si vous voulez garder le contrôle sur vos e-bouquins, faut se retrousser les manches et héberger tout ça soi-même.</p>
<p>Alors voilà le topo pour ceux qui veulent reprendre leur bibliothèque en main.</p>
<p>Le vétéran du game, c'est
<a href="https://calibre-ebook.com/">Calibre</a>
. Depuis 2006, une base de données SQLite bien rangée, une communauté énorme et un écosystème de plugins (dont le fameux DeDRM pour
<a href="https://korben.info/comment-deproteger-un-livre-kindle-pour-le-preter-le-lire-sur-lordi-ou-lexporter-sous-un-autre-format-pdf-epub.html">récupérer vos ebooks verrouillés</a>
). Le problème c'est que l'interface est restée coincée en 2006 et que la mise en place sur un serveur est plus complexe que les alternatives modernes. Ça marche, mais bon... c'est moche et c'est un peu pénible !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-2.png" alt="" loading="lazy" decoding="async">
<p>Pour mettre une jolie couche de peinture là-dessus, y'a aussi
<a href="https://github.com/janeczku/calibre-web">Calibre-Web</a>
qui ajoute une interface web potable. Et la version encore mieux, c'est
<a href="https://github.com/crocodilestick/Calibre-Web-Automated">Calibre-Web Automated</a>
(CWA) qui embarque tout dans un seul conteneur Docker (un docker-compose.yml et c'est plié)... avec sync Kobo, import via BookDrop (un dossier surveillé) et conversion EPUB/MOBI/AZW3 automatique. CWA consomme environ 160 Mo de RAM contre plus de 800 Mo pour Booklore (qui en Java peut taper dans le 1 Go+ à vide), ce qui est pas négligeable si vous tournez sur un Raspberry Pi ou un petit VPS.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-3.png" alt="" loading="lazy" decoding="async">
<p>D'ailleurs, parlons de
<a href="https://github.com/booklore-app/booklore">Booklore</a>
. Sur le papier, c'est le Jellyfin des ebooks : metadata auto depuis Google Books, Goodreads et Amazon, sync OPDS avec Kobo et KOReader, Magic Shelves avec filtres automatiques, lecteur intégré pour EPUB, PDF et CBZ... Sauf que le dev a récemment pété un câble. Télémétrie cachée envoyée sans consentement, code largement généré par IA (du &quot;AI slop&quot; c'est à dire du code vomi par ChatGPT sans relecture), et quand la communauté a râlé, le mec a répondu en gros &quot;<em>si ça vous plaît pas, désinstallez</em>&quot;. Puis il a posté des excuses... générées par ChatGPT. Grosse ambiance ouais ouais.</p>
<img src="https://korben.info/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-1.gif" alt="" loading="lazy" decoding="async">
<p>Pour ceux qui lisent aussi des comics et des mangas,
<a href="https://www.kavitareader.com/">Kavita</a>
est une alternative sérieuse. Léger, interface clean, lecteur web rapide, et ça gère aussi bien les EPUB que les CBZ. Y'a aussi Komga dans la même catégorie, plus orienté comics purs. Perso, Kavita est le choix le plus équilibré du lot parce que ça couvre ebooks ET comics sans se prendre la tête. Testé avec des bibliothèques de 50 000 fichiers et plus, ça tient clairement la route.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-4.png" alt="" loading="lazy" decoding="async">
<p>Et hop, la pépite que beaucoup ignorent c'est
<a href="https://korben.info/toutui-client-terminal-audiobookshelf.html">Audiobookshelf</a>
. À la base c'est fait pour les audiobooks, mais ça gère aussi très bien les EPUB. Le gros avantage c'est qu'un même bouquin peut appartenir à plusieurs séries (genre l'univers Cosmere de Sanderson avec Stormlight Archives ET Mistborn dedans).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-5.png" alt="" loading="lazy" decoding="async">
<p>Calibre ne le gère pas nativement (faut bidouiller avec des colonnes custom) mais le setup simple, y'a deux ans de retours positifs, et toujours pas de drama en vue.</p>
<p>Côté automatisation maintenant, c'est la zone dans le ter-ter les amis ! Readarr est officiellement abandonné, LazyLibrarian fait le taf mais l'interface est tellement chelou que franchement personne ne comprend ce qu'il regarde. Ah mais y'a aussi le petit nouveau
<a href="https://github.com/blampe/rreading-glasses">Rreading Glasses</a>
, qui est un successeur en alpha (dispo sur
<a href="https://hub.docker.com/r/blampe/rreading-glasses">Docker Hub</a>
). Donc en attendant mieux,
<a href="https://github.com/calibrain/shelfmark">Shelfmark</a>
wrappe Prowlarr et pousse directement vos trouvailles vers Booklore ou CWA... ça retire au moins l'étape de la copie manuelle !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gestion-ebooks-self-hosted/gestion-ebooks-self-hosted-6.png" alt="" loading="lazy" decoding="async">
<p><strong>Readarr a été remplacé par Rreading-glasses</strong></p>
<p>Je sais, ça fait beaucoup d'outil alors pour vous aider, sachez que le combo qui revient le plus souvent chez les gens qui ont tout essayé c'est CWA pour la gestion et le stockage, Kavita ou Audiobookshelf pour la lecture, et Shelfmark pour la recherche. Bon, c'est pas aussi sexy qu'un Plex clé en main, mais ça marche. Et si vous voulez juste un lecteur multi-plateforme sans vous prendre la tête avec un serveur,
<a href="https://korben.info/readest-lecteur-ebook-opensource-multiplateforme.html">Readest</a>
est une option open source plutôt pas mal avec sync cross-device.</p>
<p>Bref, gardez un œil sur Rreading Glasses qui promet d'être le Sonarr des livres et en attendant, Calibre reste le cafard du self-hosting : <strong>moche, mais indestructible !</strong></p>