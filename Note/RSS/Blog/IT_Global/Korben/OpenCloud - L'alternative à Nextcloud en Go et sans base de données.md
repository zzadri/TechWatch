---
title: "OpenCloud - L'alternative à Nextcloud en Go et sans base de données"
author: "Korben"
date: 2026-04-08T08:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "self-hosting"
  - "Nextcloud"
  - "opencloud"
rss_source: Blog
url: https://korben.info/opencloud-alternative-nextcloud-go-auto-hebergement.html
note: 0
seen: false
---

<p>Si vous avez déjà installé Nextcloud sur un serveur, vous savez que c'est pas une partie de plaisir ! La stack PHP + MySQL, les mises à jour qui cassent tout, les performances qui s'effondrent dès que vous dépassez 50 utilisateurs... Relouuu.</p>
<p>Mais c'est là qu'
<a href="https://opencloud.eu/en">OpenCloud</a>
débarque avec une approche radicalement différente puisque tout est écrit en Go, y'a zéro base de données, et l'installation se fait en deux commandes sur n'importe quel serveur à 5 balles par mois.</p>
<p>OpenCloud, en fait, c'est un fork d'ownCloud Infinite Scale (OCIS). Les développeurs du projet original chez Heinlein Group ont quitté ownCloud, forké le code, et relancé le tout sous licence Apache 2.0. Du coup, c'est pas un projet qui part de zéro mais une réécriture déjà très mature qui tourne en prod.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/opencloud-alternative-nextcloud-go-auto-hebergement/opencloud-alternative-nextcloud-go-auto-hebergement-2.jpg" alt="" loading="lazy" decoding="async">
<p>Là où Nextcloud utilise une base MySQL ou PostgreSQL pour stocker les métadonnées, OpenCloud balance donc tout dans le système de fichiers. Pas de SGBD ce qui veut dire pas de migration de base à gérer ni de tables corrompues après un crash. Tout atterrit dans le dossier <code>$HOME/.opencloud/</code> et c'est réglé. Donc si vous savez faire un <code>rsync</code>, vous savez aussi faire une sauvegarde complète de votre instance. Oui la vie est belle !</p>
<p>Côté fonctionnalités, on retrouve donc le partage de fichiers, la collaboration en temps réel avec une suite bureautique intégrée, le chiffrement, le versioning (pratique contre les ransomwares), l'authentification via OpenID Connect... bref tout le classique d'un cloud privé correct.</p>
<p>Maintenant, le problème je trouve, c'est que l'écosystème d'apps est pas forcément au niveau de Nextcloud. Le CalDAV/CardDAV passe par Radicale en conteneur séparé (pas intégré au core), y'a pas d'app Notes ni de client mail intégré. Donc si vous avez besoin de tout ça, Nextcloud reste le bon choix. Mais bon, pour du stockage et de la collaboration pure, c'est clairement plus léger (genre 200 Mo de RAM au lieu de 2 Go pour Nextcloud) et surtout plus rapide.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/opencloud-alternative-nextcloud-go-auto-hebergement/opencloud-alternative-nextcloud-go-auto-hebergement-3.jpg" alt="" loading="lazy" decoding="async">
<p>D'ailleurs, l'architecture microservices en Go fait que ça scale nettement mieux.</p>
<p>Maintenant, pour installer ça, le plus simple c'est Docker Compose. Le repo
<a href="https://github.com/opencloud-eu/opencloud-compose">opencloud-compose</a>
vous propose même des configs prêtes à l'emploi. À vrai dire, si vous êtes du genre à
<a href="https://korben.info/self-hosting-guide-auto-hebergement.html">auto-héberger vos services</a>
, c'est un candidat sérieux pour remplacer votre Nextcloud donc si vous avez surtout besoin de fichiers et de collaboration, ça vaut le test. D'ailleurs, comme OpenCloud utilise OIDC pour l'auth,
<a href="https://korben.info/pocket-id-auth-oidc-passkey.html">Pocket ID</a>
s'intègre pile poil avec pour du SSO sans mot de passe. Je dis ça, je dis rien ^^.</p>
<p>Bref, si Nextcloud vous gonfle avec sa lourdeur PHP et ses 47 tables MySQL, OpenCloud mérite un bon petit coup d'oeil !</p>
<p>Merci à fredix pour le lien !</p>