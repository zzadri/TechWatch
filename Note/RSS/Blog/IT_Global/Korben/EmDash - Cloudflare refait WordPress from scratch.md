---
title: "EmDash - Cloudflare refait WordPress from scratch"
author: "Korben"
date: 2026-04-02T00:10:32.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/web-developpement"
  - "intelligence-artificielle/actualites-ia"
  - "linux-open-source/logiciels-libres"
  - "Cloudflare"
  - "CMS"
  - "open source"
  - "TypeScript"
  - "WordPress"
rss_source: Blog
url: https://korben.info/emdash-cloudflare-wordpress-open-source.html
note: 0
seen: false
---

<p>Cloudflare qui sort un successeur open source à WordPress le 1er avril, je vous avoue que ça sentait le poisson d'avril à plein nez. Sauf que non !!
<a href="https://github.com/emdash-cms/emdash">EmDash</a>
est bien réel, son code est sur GitHub sous licence MIT, et ça s'installe en une commande toute simple !</p>
<p>L'idée de base pour Cloudflare, c'est de dire que WordPress a plus de 20 ans et bien qu'il alimente 40% du web, son architecture de plugins est un emmental (Le gruyère n'a pas de trou les amis ^^). En effet, 96% des failles de sécurité viennent des extensions et pas du noyau PHP ni des thèmes et en 2025, on a quand même explosé le record de failles dans l'écosystème WP.</p>
<p>Du coup Cloudflare, grand prince (Matthew ^^ Ok, je sors...) a tout repris de zéro en TypeScript et avec l'aide de nombreux agents IA. Et de ce que j'ai compris, le gros morceau de ce projet, visiblement, c'est l'isolation des plugins.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/emdash-cloudflare-wordpress-open-source/emdash-cloudflare-wordpress-open-source-2.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Car sur WordPress, une extension a accès à toute la base de données et au système de fichiers (d'où
<a href="https://korben.info/securiser-wordpress-les-plugins.html">l'importance de bien les choisir</a>
). Alors que sur EmDash, chaque plugin tourne dans son propre isolat avec un modèle de capacités déclaratives. En gros, le plugin annonce dans un fichier manifeste JSON ce dont il a besoin, genre <code>read:content</code> ou <code>email:send</code>, et il ne peut rien faire d'autre. S'il veut accéder au réseau, il doit même préciser le hostname exact. Comme ça fini les extensions qui aspirent vos données en douce. Par contre, ça veut aussi dire que vos plugins WordPress actuels ne marcheront pas tels quels...</p>
<p>Côté stack, c'est comme je disais du TypeScript de bout en bout avec Astro 6.0 en frontend (pour les thèmes) et Node.js derrière. L'auth passe également par des passkeys par défaut (enfin, plus de mots de passe !) et y'a même un système de paiement natif via le standard ouvert x402 pour monétiser du contenu.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/emdash-cloudflare-wordpress-open-source/emdash-cloudflare-wordpress-open-source-3.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Et le truc qui va vous rassurer si vous êtes allergique au cloud : <strong>c'est auto-hébergeable</strong>. En fait, le CMS peut tourner sur Cloudflare Workers, mais aussi sur n'importe quel serveur Node.js avec SQLite. Les abstractions sont portables, avec Kysely pour le SQL et l'API S3 pour le stockage. Du coup vous pouvez brancher PostgreSQL, Turso, AWS S3, ou tout bêtement des fichiers en local. Le bonheur !</p>
<p>Le truc cool pour les bidouilleurs, c'est que chaque instance expose un serveur MCP (Model Context Protocol) et une CLI pour piloter le CMS par script. Y'a aussi des Agent Skills pour que les agents IA puissent créer du contenu, gérer les médias et modifier le schéma sans toucher au dashboard. C'est clairement pensé pour l'ère des agents IA.</p>
<p>Et pour ceux qui veulent migrer depuis leur WordPress, c'est prévu pour vous faciliter la tâche puisqu'il y a le support d'export WXR classique ou via un plugin dédié qui crée un endpoint sécurisé protégé par mot de passe. Que ce soient les médias, les custom post types...etc tout est transférable en quelques minutes. Par contre, attention les shortcodes et les blocs Gutenberg custom ne passeront pas tels quel, faudra faire des ajustements.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/emdash-cloudflare-wordpress-open-source/emdash-cloudflare-wordpress-open-source-1.png" alt="" loading="lazy" decoding="async">
</p>
<p>Car oui c'est une v0.1.0 preview, donc on peut le dire, une bonne grosse beta qui bave mais je trouve ça super cool car le
<a href="https://korben.info/wp-engine-vs-wordpress-guerre-declaree.html">drama WP Engine vs WordPress</a>
a montré que l'écosystème était fragile, et c'est bien de réintroduire un peu de diversité. Par contre, remplacer un CMS qui fait tourner 40% du web, c'est hyper ambitieux et ça se fera pas en un trimestre. Car la vraie force de WordPress, c'est sa communauté, ses milliers de plugins et de thèmes, et ça pour le moment, y'a pas grand chose sur EmDash.</p>
<p>M'enfin, si vous voulez tester c'est <code>npm create emdash@latest</code> et c'est parti mon kiki. Ah et y'a aussi un playground sur
<a href="https://emdashcms.com/playground">emdashcms.com</a>
pour vous faire une idée sans rien installer. Pour ma part, je testerai ça dès que j'aurais 5 min, mais pour le moment, je ne me vois pas quitter WordPress car EmDash n'a pas (encore) ce petit truc en plus qui me ferait changer... On verra d'ici quelques temps.</p>
<p>
<a href="https://blog.cloudflare.com/emdash-wordpress/">Source</a>
</p>