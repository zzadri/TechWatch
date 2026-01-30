---
title: "Portracker - Fini le bordel des ports qui plantent vos déploiements"
author: "Korben"
date: 2026-01-26T08:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "linux-open-source/self-hosting"
  - "DevOps"
  - "Docker"
  - "monitoring"
  - "ports"
  - "réseau"
  - "self-hosted"
  - "serveur"
rss_source: Blog
url: https://korben.info/portracker-surveillance-ports-reseau.html
note: 0
seen: false
---

<p>&quot;<em>Merde, le port 8080 est squatté par quoi <em>encore</em></em> <em>???</em>&quot;</p>
<p>Si vous touchez un peu à l'auto-hébergement ou que vous gérez plus de trois services sur un serveur, vous avez forcément déjà hurlé cette phrase devant votre terminal. C'est le grand classique... on lance un nouveau conteneur, ça plante, et on finit par passer 20 minutes à faire des <code>netstat</code> ou des <code>lsof</code> pour comprendre qui fait la loi sur le réseau. Bref, c'est le bordel, et c'est exactement là que <strong>
<a href="https://github.com/mostafa-wahied/portracker">Portracker</a>
</strong> entre en scène pour nous sauver la mise.</p>
<p>Développé par Mostafa Wahied, Portracker n'est pas un énième scanner de ports réseau agressif façon Nmap, mais plutôt une vigie interne pour vos machines. C'est un outil auto-hébergé qui va scanner son propre hôte pour cartographier en temps réel (enfin, avec un rafraîchissement périodique réglable, généralement toutes les minutes) tous les services qui tournent et les ports qu'ils occupent. L'idée, c'est d'avoir une vue propre et centralisée pour dégager ce vieux tableur Excel que vous oubliez de mettre à jour une fois sur deux.</p>
<p>Le truc est super bien foutu, surtout pour les fans de Docker. Pour ceux qui se demandent comment ça se passe sous le capot, l'outil fait intelligemment la distinction entre les ports internes d'un conteneur et ceux qui sont réellement exposés sur l'hôte.</p>
<p>Alors oui, ça marche comment pour mapper tout ça ? En gros, ça utilise les API natives pour voir que votre instance Ghost est sur le 2368 en interne mais ressort sur le 8080 à l'extérieur. C'est le genre de truc qui évite bien des migraines quand on commence à empiler 50 conteneurs. Il y a même un support aux petits oignons pour TrueNAS pour les amateurs de NAS costauds.</p>
<p>Côté dashboard, c'est du propre puisqu'on est sur une interface moderne avec React, Tailwind et Shadcn UI, avec un mode sombre (évidemment) et des filtres en live qui répondent au quart de tour.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/portracker-surveillance-ports-reseau/portracker-surveillance-ports-reseau-2.png" alt="" loading="lazy" decoding="async">
<p>Mais la vraie force de Portracker, c'est sa capacité à bosser en meute. Vous pouvez connecter plusieurs instances entre elles via un système de &quot;Peers&quot; (en peer-to-peer donc) pour tout centraliser sur un seul tableau de bord. Pratique si vous avez un serveur chez vous, un VPS chez OVH et une vieille machine qui traîne dans un placard. Vous pouvez même organiser ça avec une hiérarchie parent-enfant pour mapper vos machines virtuelles sous leurs hôtes physiques respectifs.</p>
<p>Techniquement, c'est du solide mais ça reste léger : du Node.js avec Express et des WebSockets pour le backend, et une base SQLite (via better-sqlite3) embarquée pour ne pas avoir à se fader la conf d'une base externe. Pour le déploiement, ça se passe via Docker et pour les paranos de la sécurité (je vous vois ^^), sachez que l'outil supporte désormais l'utilisation d'un Docker Socket Proxy (genre celui de Tecnativa). Ça permet d'éviter de filer les droits root sur votre socket Docker à n'importe qui. Et depuis la version 1.2.0, vous pouvez même verrouiller l'accès avec une vraie authentification.</p>
<p>Notez que pour fonctionner correctement et aller fouiller dans les entrailles du système, l'outil a besoin de certaines permissions (les fameuses <em>capabilities</em> Linux). Il lui faudra généralement <code>SYS_PTRACE</code>, et éventuellement <code>SYS_ADMIN</code> si vous le faites tourner sur Docker Desktop ou macOS. C'est le prix à payer pour avoir une visibilité totale sur ce qui se passe dans les tuyaux.</p>
<p>Le projet cartonne pas mal sur GitHub et la communauté est super active donc si vous en avez marre de jouer à cache-cache avec vos ports, c'est clairement l'outil qu'il vous faut pour reprendre le contrôle de vos déploiements sans finir en PLS à chaque conflit de port 80. Et si jamais vous stressez sur la sécurité de vos ports Docker, n'oubliez pas qu'on peut aussi jouer avec les règles <code>iptables</code> pour blinder tout ça, mais ça, c'est une autre histoire !</p>
<p>Merci à AeroStream972 pour la découverte !</p>