---
title: "Des scripts tout faits pour votre Proxmox"
author: "Korben"
date: 2026-02-02T09:54:25.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/self-hosting"
  - "tutoriels-guides/tutoriels-avances"
  - "automatisation"
  - "Proxmox"
  - "sysadmin"
rss_source: Blog
url: https://korben.info/des-scripts-tout-faits-pour-votre-proxmox.html
note: 0
seen: false
---

<p>Ce matin, je discutais avec Emmanuel (un lecteur fidèle) sur mon
<a href="https://www.linkedin.com/company/korben-info">Linkedin Korben</a>
et il m'a partagé une ressource vraiment chouette. Si comme moi vous jouez un peu parfois avec un serveur Proxmox qui tourne à la maison pour vos expérimentations ou votre domotique, vous savez que configurer chaque VM ou conteneur LXC peut vite devenir chronophage. On copie-colle des commandes, on installe des dépendances, on se plante, on recommence... La routine quoi sauf que cette routine peut vite devenir reloue.</p>
<p>Hé bien, fini la galère !!!! Le projet dont je veux vous parler aujourd'hui s'appelle <strong>
<a href="https://community-scripts.github.io/ProxmoxVE/">Proxmox VE Helper-Scripts</a>
</strong> et c'est une collection communautaire de scripts (plusieurs centaines !) qui permet d'installer et de configurer tout un tas de services en une seule ligne de commande.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/des-scripts-tout-faits-pour-votre-proxmox/des-scripts-tout-faits-pour-votre-proxmox-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>En gros, c'est une immense boîte à outils pour votre hyperviseur. Vous avez besoin d'une instance <strong>Home Assistant</strong> pour gérer des ampoules connectées ? Hop, vous lancez le script et ça vous crée le conteneur LXC tout propre. Vous voulez monter un serveur média avec <strong>Plex</strong> ou <strong>Jellyfin</strong> ? Pareil, c'est généralement plié en quelques minutes (selon votre connexion évidemment).</p>
<p>Vous allez sur le site, vous cherchez l'outil qui vous intéresse, vous copiez la commande bash fournie (du style <code>bash -c &quot;...&quot;</code>) et vous la collez dans le shell de votre nœud Proxmox. Et hop, l'assistant se lance. Il vous pose quelques questions (IP statique ou DHCP, espace disque, RAM... ce genre de trucs classiques) et puis tente de s'occuper de tout le reste (si les planètes sont bien alignées et que votre karma est au top !).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/des-scripts-tout-faits-pour-votre-proxmox/des-scripts-tout-faits-pour-votre-proxmox-3.png" alt="" loading="lazy" decoding="async">
<p>Je trouve ça génial parce que non seulement ça gère l'installation, mais ça s'occupe aussi des mises à jour. Mais bon, attention quand même parce qu'une mise à jour upstream peut parfois casser le script, donc prudence. C'est d'ailleurs super utile si vous utilisez
<a href="https://korben.info/proxmox-raspberry-pi-pimox.html">Proxmox sur un Raspberry Pi</a>
(via Pimox), même si l'architecture ARM peut poser souci avec certains scripts. D'ailleurs, bonne nouvelle pour les utilisateurs de Pimox : il existe <strong>
<a href="https://pimox-scripts.com/scripts">Pimox-Scripts</a>
</strong>, un portage de ces mêmes Helper Scripts mais adaptés spécifiquement pour ARM/Raspberry Pi. Tous les scripts ne sont pas encore dispos (moins de contributeurs), mais y'a déjà de quoi faire !</p>
<p>Parmi les scripts disponibles, on retrouve les classiques <strong>Docker</strong>, <strong>AdGuard Home</strong>, <strong>Pi-hole</strong>, mais aussi des trucs plus pointus pour le monitoring ou la sécurité. C'est vraiment très complet, y compris si vous êtes dans une optique de
<a href="https://korben.info/ludus-automatisation-lab-cybersecurite.html">création de lab de cybersécurité</a>
.</p>
<p>Après, je dois quand même vous faire une petite mise en garde de circonstance. Car comme d'habitude, exécuter des scripts bash trouvés sur le net direct en root... comment dire... c'est jamais sans risque. Le code est open source et maintenu par une communauté active, ça facilite l'audit, mais <strong>ce n'est pas une garantie de sécurité absolue</strong>. Sauf si vous aimez vivre dangereusement, jetez toujours un œil au code avant de valider. La confiance n'exclut pas le contrôle !!</p>
<p>Un grand merci à Emmanuel pour le tuyau initial et à Karl pour l'info sur Pimox-Scripts !</p>