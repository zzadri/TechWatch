---
title: "WordPress : un pirate achète 30 plugins et y plante une backdoor"
author: "Korben"
date: 2026-04-16T13:45:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/malwares-menaces"
  - "backdoor"
  - "plugins"
  - "WordPress"
rss_source: Blog
url: https://korben.info/wordpress-un-pirate-achete-30-plugins-et-y-plante-une-backdoor.html
note: 0
seen: false
---

<p>Une attaque par la chaîne d'approvisionnement a frappé WordPress début avril. Un individu a racheté une trentaine de plugins via la marketplace Flippa, y a injecté du code malveillant et a attendu huit mois avant de l'activer. WordPress a fermé les 31 plugins concernés le 7 avril, mais la mise à jour officielle ne suffit pas à nettoyer les sites touchés.</p>
<p>L'attaque est redoutable par sa simplicité. Un individu, identifié sous le prénom &quot;Kris&quot;, a racheté pour plusieurs centaines de milliers d'euros un catalogue d'une trentaine de plugins WordPress sur Flippa, une marketplace de vente de sites et d'extensions. Ces plugins appartenaient à la société Essential Plugin / WP Online Support. Ils étaient actifs, mis à jour, et installés sur des milliers de sites.</p>
<p>En achetant le catalogue, l'acheteur a récupéré l'accès au dépôt officiel <a target="_blank" rel="noreferrer noopener" href="http://wordpress.org/">WordPress.org</a> et a pu pousser des mises à jour directement aux utilisateurs. Le code malveillant a été injecté dès août 2025, mais il est resté dormant pendant huit mois. L'activation a eu lieu les 5 et 6 avril 2026.</p>
<p>Côté technique, l'attaque est assez vicieuse. Le module injecté (wpos-analytics) utilise une désérialisation PHP pour communiquer avec un serveur de commande. Et là, le point intéressant : au lieu d'utiliser un domaine classique pour piloter la backdoor, le malware résout l'adresse de son serveur C2 via un smart contract Ethereum, en interrogeant des points d'accès RPC publics. Résultat, couper un nom de domaine ne sert à rien. L'attaquant peut mettre à jour le smart contract à tout moment pour pointer vers un nouveau serveur.</p>
<p>Le payload injecte du code dans le fichier wp-config.php (environ 6 Ko) et crée un fichier wp-comments-posts.php, un nom assez proche des fichiers légitimes pour passer inaperçu. Le tout sert à afficher du spam SEO (liens, redirections, fausses pages) uniquement à Googlebot, ce qui rend l'attaque invisible pour le propriétaire du site.</p>
<p><a target="_blank" rel="noreferrer noopener" href="http://wordpress.org/">WordPress.org</a> a fermé les 31 plugins touchés le 7 avril et a poussé une mise à jour forcée le lendemain. Sauf que cette mise à jour ne nettoie pas le fichier wp-config.php, qui est le vrai point de persistance de la backdoor. Si vous avez l'un de ces plugins installé (Countdown Timer Ultimate, Popup Anything on Click, Post Grid and Filter Ultimate, WP Slick Slider, Album and Image Gallery Plus Lightbox, Responsive WP FAQ, entre autres), il faut aller vérifier votre wp-config.php manuellement et chercher un bloc de code d'environ 6 Ko qui n'a rien à y faire. Le fichier wp-comments-posts.php à la racine du site doit aussi être supprimé s'il est présent.</p>
<p>La vraie leçon ici, c'est que la confiance dans un plugin WordPress repose sur son historique, et qu'un changement de propriétaire peut tout remettre en question du jour au lendemain. <a target="_blank" rel="noreferrer noopener" href="http://wordpress.org/">WordPress.org</a> ne vérifie pas les changements de mains sur les comptes développeurs, et n'a aucun mécanisme d'alerte quand un catalogue entier passe à un nouvel acheteur. Tant que ce trou existe, ce genre d'attaque peut se reproduire. Et le fait que la mise à jour officielle ne nettoie même pas les sites infectés, c'est quand même un problème.</p>
<p>Source :
<a href="https://thenextweb.com/news/wordpress-plugins-backdoor-supply-chain-essential-plugin-flippa-2">The Next Web</a>
</p>