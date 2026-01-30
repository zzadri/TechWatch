---
title: "YouTube - Quand le faux bug cache une vraie arnaque"
author: "Korben"
date: 2026-01-27T14:13:04.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "cybersecurite/actualites-securite"
  - "adblock"
  - "Google"
  - "uBlock Origin"
rss_source: Blog
url: https://korben.info/youtube-erreur-adblock.html
note: 0
seen: false
---

<p>Bon, je vais pas vous mentir, YouTube et moi en ce moment c'est compliqué. Ce matin encore, j'ai passé une bonne heure à debug mes scripts Python pour choper de la musique pour mes lives Twitch. Et yt-dlp qui rame de plus en plus, alors qu'avant ça prenait 3 secondes chrono... Pffff, j'ai l'impression que Google a décidé de nous pourrir la vie.</p>
<p>Et là, en cherchant pourquoi mes scripts plantaient, je suis tombé sur un truc qui m'a bien fait rire jaune. Vous savez le fameux message &quot;<em>An error occurred. Please try again later</em>&quot; qui s'affiche parfois quand vous matez une vidéo ? J'ai d'abord cru que c'était un bug côté serveur chez Google mais QUE NENNI !</p>
<p>C'est VOULU !!</p>
<p>WTF?! Du coup voilà le délire... quand la plateforme vidéo détecte que vous utilisez un bloqueur de pubs, au lieu de vous afficher gentiment une popup &quot;<em>hey miskine, désactive ton adblock s'il te plaît</em>&quot;, elle fait semblant d'avoir un problème technique. Le message d'erreur est bidon, la vidéo pourrait très bien se lancer, mais non... Big G préfère vous faire croire que c'est votre connexion qui déconne.</p>
<p>Et techniquement, c'est assez vicieux puisque le système fonctionne sur trois niveaux : d'abord il analyse les requêtes réseau pour voir si certaines URLs de pubs sont bloquées, ensuite il vérifie l'intégrité du DOM pour s'assurer que les éléments publicitaires sont bien présents, et enfin il surveille si les APIs de pub sont accessibles. Et si un de ces checks échoue, hop, le lecteur vidéo se met en mode &quot;<em>je fais semblant d'avoir un problème</em>&quot;.</p>
<p>Sympathique non ?</p>
<p>Le pire dans tout ça, c'est que ça marche plutôt bien pour eux. J'ai moi-même mis pas mal de temps avant de tilter que c'était pas chez moi que ça déconnait. Parce que quand on voit &quot;An error occurred&quot;, notre premier réflexe c'est de rafraîchir la page, de vérifier votre connexion, de redémarrer votre navigateur... etc, jusqu'à ramener l'ordi chez le dépanneur ^^ loool .</p>
<p>Bref, TOUT sauf de penser que c'est une extension adblock à la con qui pose problème.</p>
<p>D'ailleurs avec Manifest V3 qui limite encore un peu plus les capacités des bloqueurs sur Chrome, c'est devenu encore plus galère. La limite de 30 000 règles par extension, c'est juste ridicule quand on sait qu'uBlock Origin en utilise plus de 300 000.</p>
<p>Maintenant, si vous cherchez des solutions qui marchent encore, j'avais fait
<a href="https://korben.info/bloquer-les-pubs-en-2026.html">un guide complet sur les bloqueurs de pubs</a>
qui reste encore d'actualité malgré son age. Et surtout, le frérot Firefox reste une valeur sûre vu qu'il supporte encore Manifest V2. Attention par contre, uBlock Origin Lite sur Chrome c'est pas la même chose que l'original, il tape que du 96% contre 100% pour la version complète niveau blocage. Les filtres doivent constamment être mis à jour parce que le service de Google change ses méthodes de détection à peu près toutes les semaines.</p>
<p>Et dire que pendant ce temps,
<a href="https://korben.info/allemagne-veut-criminaliser-bloqueurs-pub-pourquoi.html">certains pays veulent carrément criminaliser les bloqueurs</a>
... On vit une époque formidable ^^. Perso, j'en suis à me demander si on devrait pas tous migrer sur Dailymotion. Non je déconne. Quoique...</p>
<p>Bref, si vous voulez contourner le truc, soit vous passez sur Firefox avec uBlock Origin classique, soit vous désactivez temporairement votre bloqueur sur la plateforme, soit... vous payez YouTube Premium. Ce qui est probablement exactement ce qu'ils veulent.</p>
<p>
<a href="https://www.techspot.com/news/111074-latest-youtube-error-message-isnt-bug-another-ad.html">Source</a>
</p>