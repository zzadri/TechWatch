---
title: "Scanopy - Quand votre réseau se documente tout seul"
author: "Korben"
date: 2026-03-16T06:34:27.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "self-hosting"
  - "administration réseau"
  - "Docker"
  - "homelab"
  - "self-hosted"
rss_source: Blog
url: https://korben.info/scanopy-scanner-reseau-topologie.html
note: 0
seen: false
---

<p>Faut le reconnaitre, la doc et qui plus est, la doc réseau, c'est un peu le parent pauvre du homelab. Tout le monde sait qu'il faudrait la tenir à jour sur un petit wiki tout mignon mais personne le fait parce qu'on n'est pas cinglé et qu'on aime trop la vie pour ça. Heureusement, pour nous aider, y'a maintenant
<a href="https://scanopy.net">Scanopy</a>
qui est un outil open source qui scanne automatiquement votre réseau pour générer une topologie interactive incroyable qui se met à jour toute seule !</p>
<p>Pour l'installer, deux lignes suffisent :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -O https://raw.githubusercontent.com/scanopy/scanopy/refs/heads/main/docker-compose.yml
</span></span><span class="line"><span class="cl">docker compose up -d
</span></span></code></pre><p>Et hop, l'interface est dispo sur le port 60072 de votre serveur ! Pas de config.</p>
<p>Concrètement, le truc balance du scan ARP pour trouver tous les hôtes (même ceux qui n'ont aucun port ouvert), puis il enchaîne avec un scan des 65 000 ports sur chaque machine qui répond. Comme ça, en quelques minutes sur un /24 classique, vous avez la cartographie complète de votre sous-réseau avec les services qui tournent dessus. Et quand je dis services, c'est pas juste &quot;port 80 ouvert&quot; puisque cet outil de zinzin reconnaît plus de 200 applis self-hosted comme Home Assistant, Plex, Jellyfin, PostgreSQL ou nginx. Par contre, attention, un scan de 65 000 ports sur tout un sous-réseau, ça peut chatouiller un peu votre IDS (système de détection d'intrusion) si vous en avez un.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scanopy-scanner-reseau-topologie/scanopy-scanner-reseau-topologie-1.webp" alt="" loading="lazy" decoding="async">
</p>
<p>D'ailleurs, si vous avez des équipements réseau un peu sérieux (switches manageables, routeurs), Scanopy sait aussi causer SNMP v2c et récupérer les données LLDP/CDP pour reconstituer les liens physiques entre vos appareils.</p>
<p>Et pour ceux qui font tourner pas mal de containers, il se branche directement sur le socket Docker pour détecter tout ce qui tourne là-dedans. En fait, c'est surtout cette combo &quot;scan réseau + détection Docker&quot; qui le rend utile, parce que la plupart des outils du genre font l'un ou l'autre mais jamais les deux.</p>
<p>L'interface de visualisation est plutôt classe comme vous pouvez le voir. Vous avez une vue topologique interactive où chaque hôte est cliquable, avec un système de branches et de versioning pour suivre l'évolution de votre réseau dans le temps (un peu comme Git, mais pour votre infra). Et y'a même de l'export en CSV, PNG et SVG. Et surtout la possibilité de partager des liens publics vers vos schémas... C'est franchement pratique quand vous bossez en équipe ou que vous devez montrer à votre boss pourquoi le NAS de votre PME rame sa mère.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scanopy-scanner-reseau-topologie/scanopy-scanner-reseau-topologie-2.webp" alt="" loading="lazy" decoding="async">
</p>
<p>Côté tambouille technique, c'est du Rust pour le moteur de scan et du Svelte pour l'interface, le tout sous licence AGPL-3.0. En gros, vous avez un serveur qui héberge l'UI et stocke les données, et des daemons qui font le boulot de scan à proprement parler. Tout est containerisé, comme ça pas besoin d'installer un agent sur vos machines côté réseau... c'est complètement agentless quoi. D'ailleurs, si vous aviez l'habitude de balancer des
<a href="https://korben.info/nmap-viewer-visualisation-scans-reseau.html">scans nmap</a>
à la main pour savoir ce qui traîne sur votre réseau, Scanopy automatise tout ça et rajoute la couche visu par-dessus.</p>
<p>Le projet est hébergé sur
<a href="https://github.com/scanopy/scanopy">GitHub</a>
et y'a aussi un déploiement possible via Proxmox ou Unraid pour ceux qui préfèrent. Seul prérequis, il vous faudra Docker et Docker Compose sur votre machine. Et n'oubliez pas que le projet est encore jeune, du coup ça bouge pas mal d'une version à l'autre. Et ça casse parfois. Mais c'est plutôt bon signe parce que ça veut dire que ça progresse !</p>
<p>Bref, si vous en avez marre de dessiner vos schémas réseau à la main, c'est par là !</p>
<p>
<a href="https://noted.lol/scanopy/">Source</a>
</p>
<p></p>