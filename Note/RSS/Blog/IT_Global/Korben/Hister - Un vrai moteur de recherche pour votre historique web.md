---
title: "Hister - Un vrai moteur de recherche pour votre historique web"
author: "Korben"
date: 2026-04-03T09:14:22.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "vie-privee-anonymat"
  - "historique navigateur"
  - "open source"
  - "Searx"
  - "vie privée"
rss_source: Blog
url: https://korben.info/hister-moteur-recherche-historique-web.html
note: 0
seen: false
---

<p>Bon, j'ai la crève et y'a du bricolage qui m'attend, du coup aujourd'hui y'aura pas des centaines d'article. Mais faut quand même que je vous parle de
<a href="https://hister.org">Hister</a>
, le nouveau projet d'Adam Tauber (le créateur de
<a href="https://korben.info/searxng-metamoteur-recherche-open-source-protege-vie-privee.html">Searx</a>
) qui indexe localement tout ce que vous visitez sur le web pour le retrouver en texte intégral.</p>
<p>Vous installez l'extension Chrome ou Firefox, vous lancez le binaire Go sur votre machine (ça tourne sous Linux, macOS et Windows), et hop, chaque page que vous visitez est indexée en full-text. Du coup, quand vous cherchez ce tuto que vous aviez lu y'a 3 semaines mais dont vous avez zappé l'URL, vous ouvrez l'interface web locale de Hister, vous tapez un mot qui était dans le contenu de la page et ça ressort ! Si vous aviez testé
<a href="https://korben.info/moteur-de-recherche-puissant-pour-votre-historique-de-navigation.html">Deeper History</a>
à l'époque, c'est le même concept mais en beaucoup plus costaud.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hister-moteur-recherche-historique-web/hister-moteur-recherche-historique-web-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de Hister - sobre mais efficace</em></p>
<p>Sous le capot, Hister utilise blevesearch, un moteur d'indexation en Go qui gère le fuzzy matching et les requêtes booléennes. En gros, vous tapez &quot;configuration nginx reverse proxy&quot; et ça vous ressort cette page de doc que vous aviez consultée y'a un mois, même si vous ne vous souvenez que de 2 mots. Efficace donc. Et l'outil capture les pages telles qu'elles étaient au moment de votre visite donc si un site modifie son contenu ou si un article disparaît, vous aurez toujours la version d'origine. Y'a même un mode aperçu hors-ligne pour consulter ces snapshots sans connexion !</p>
<p>Côté vie privée (forcément, quand ça vient du mec qui a pondu Searx déjà en 2013... le temps file les amis ^^), <strong>tout reste sur votre machine</strong>. Et pour les domaines sensibles comme votre banque ou votre mutuelle, une blacklist permet même d'exclure certains sites de l'indexation. Enfin pour ceux qui ont déjà des années de navigation derrière eux, la commande <code>hister import</code> aspirera votre historique Chrome ou Firefox existant, comme ça pas besoin de repartir de zéro.</p>
<p>Pour installer ça, téléchargez le binaire depuis
<a href="https://github.com/asciimoo/hister/releases">les releases GitHub</a>
, puis lancez le serveur et installez l'extension (
<a href="https://addons.mozilla.org/en-US/firefox/addon/hister/">Firefox</a>
ou Chrome) qui va bien. Y'a aussi un Docker Compose pour ceux qui préfèrent tout conteneuriser. Prévoyez aussi quelques Go sur le disque pour la base d'index car ça se rempli vite...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hister-moteur-recherche-historique-web/hister-moteur-recherche-historique-web-3.png" alt="" loading="lazy" decoding="async">
<p>Tauber dit avoir réduit sa dépendance à Google de moitié en un mois et demi juste avec ça. Et je trouve ça logique parce que quand vous avez déjà visité la bonne page une fois, ça ne sert plus à rien de redemander à Google de vous la remonter entre 3 pubs et une réponse IA à côté de la plaque. Autant récupérer ce que vous aviez déjà !</p>
<p>Voilà, je suis sûr que ça va vous plaire... Et si vous voulez tester avant d'installer quoi que ce soit, une
<a href="https://demo.hister.org">démo</a>
tourne en ligne.</p>
<p>Allez, je retourne bricoler...</p>