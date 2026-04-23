---
title: "ProxMenux - Fini les 45 commandes pour gérer votre Proxmox"
author: "Korben"
date: 2026-02-11T07:30:31.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "linux-open-source/logiciels-libres"
  - "tutoriels-guides"
  - "homelab"
  - "Proxmox"
  - "virtualisation"
rss_source: Blog
url: https://korben.info/proxmenux.html
note: 0
seen: false
---

<p>Proxmox, c'est génial pour la virtualisation... sauf que configurer des VMs, des conteneurs LXC, le GPU passthrough et les sauvegardes à la main, ça finit par nous coller de grosses cernes sous les neuneuils ! Trop de commandes les amis !! Heureusement, un dev a eu la bonne idée de tout coller dans un menu interactif bash !</p>
<p>
<a href="https://github.com/MacRimi/ProxMenux">ProxMenux</a>
, c'est donc un outil open source qui vous ajoute une commande <code>menu</code> dans le terminal de votre serveur Proxmox. Vous tapez ça et vous avez alors un joli menu en mode texte qui vous propose toutes les opérations courantes sans avoir à retenir 45 commandes différentes. Et c'est compatible Proxmox VE 8.x et 9.x.</p>
<p>L'installation tient en une seule ligne bash.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">bash -c &#34;$(wget -qLO - https://raw.githubusercontent.com/MacRimi/ProxMenux/main/install_proxmenux.sh)&#34;
</span></span></code></pre><p>Et c'est plié en 30 secondes.</p>
<p>Alors c'est pas le premier ni le dernier de sa catégorie, mais là où d'autres se contentent de 3-4 raccourcis, ProxMenux embarque des menus pour à peu près tout. Création de VMs, gestion des conteneurs LXC, configuration réseau, stockage, GPU passthrough (le truc qui rend dingue tout le monde), et même un mode réparation d'urgence. D'ailleurs, y'a aussi un système de sauvegarde/restauration intégré et des scripts de post-installation pour configurer votre Proxmox aux petits oignons.</p>
<p>En gros, c'est le couteau suisse que tous les admins Proxmox rêvent d'avoir. Même si c'est quand même du script bash exécuté en root sur votre hyperviseur. Je sais, ça pique un peu quand on y pense mais c'est tellement utile ! Et comme le code est sur GitHub, c'est auditable donc jetez-y un œil avant de foncer tête baissée.</p>
<p>Voilà, si vous avez déjà
<a href="https://korben.info/des-scripts-tout-faits-pour-votre-proxmox.html">les Proxmox Helper Scripts</a>
pour installer vos services, ProxMenux c'est un super complément. Les Helper Scripts gèrent l'installation de conteneurs préconfigurés (Home Assistant, Plex, Jellyfin...) alors que ce menu interactif couvre l'administration système de votre hyperviseur. Du coup, les deux ensemble, c'est pas mal du tout pour votre
<a href="https://korben.info/proxmox-raspberry-pi-pimox.html">homelab</a>
.</p>
<p>Y'a aussi des fonctionnalités qu'on voit rarement dans ce genre d'outils, comme la configuration du Coral TPU pour ceux qui font tourner Frigate sur leur serveur. Détection IA, NVR, le tout depuis un menu. Ou encore un dashboard web pour surveiller votre infra en temps réel. Attention quand même, ça ne remplace pas l'interface web native de Proxmox mais c'est un bon complément pour le terminal.</p>
<p>Bref, si vous avez un Proxmox à la maison et que vous en avez marre de chercher des commandes sur Google ou ChatGPT, allez jeter un œil !</p>
<p>Un grand merci à Maxime pour le partage !</p>