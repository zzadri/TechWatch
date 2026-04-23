---
title: "PegaProx - Un dashboard pour les gouverner tous"
author: "Korben"
date: 2026-04-18T07:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "homelab"
  - "Proxmox"
  - "self-hosted"
  - "virtualisation"
rss_source: Blog
url: https://korben.info/pegaprox-dashboard-proxmox.html
note: 0
seen: false
---

<p>L'interface web de Proxmox (l'outil de virtualisation que tout bon homelabber connaît), c'est bien... pour UN serveur. Dès que vous commencez à empiler les nodes et les clusters, ça devient vite le bazar avec 15 onglets ouverts.
<a href="https://github.com/PegaProx/project-pegaprox">PegaProx</a>
, c'est tout simplement un dashboard open source qui unifie tout ça dans un seul écran. Et vous allez voir, le truc cool, c'est que ça gère aussi les clusters XCP-ng !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pegaprox-dashboard-proxmox/pegaprox-dashboard-proxmox-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de PegaProx - une vue unifiée de tous vos clusters Proxmox et XCP-ng</em></p>
<p>Concrètement, vous branchez tous vos hyperviseurs sur cette interface web (port 5000) et hop, vous avez la vue complète. VMs, conteneurs, métriques de perf... tout remonte en temps réel via Server-Sent Events. Du coup, plus besoin de jongler entre les interfaces de chaque node pour savoir quel serveur rame.</p>
<p>Côté fonctionnalités, accrochez-vous les amis parce que pour une beta, c'est déjà bien garni ! Migration live de VMs entre nodes, gestion du stockage Ceph, consoles navigateur via noVNC et xterm.js, et même de la migration cross-hypervisor entre ESXi, Proxmox VE 8.0 et
<a href="https://korben.info/vates-alternative-vmware-open-source.html">XCP-ng</a>
(encore expérimental côté ESXi, mais ça avance). Y'a aussi des règles d'affinité pour placer vos VMs, du rolling update avec évacuation automatique, et des alertes sur les seuils CPU/RAM/disque. Pour une beta, c'est assez dingue ce qu'ils ont déjà mis dedans.</p>
<p>Côté sécurité, c'est pas en reste non plus. Y'a du RBAC avec 3 rôles (Admin, Operator, Viewer, pas plus pas moins), du TOTP pour le 2FA, de l'intégration LDAP et OIDC compatible Active Directory, Entra ID, Keycloak ou Google Workspace, du chiffrement AES-256-GCM pour stocker les credentials en base, et même du scan de CVE via debsecan. Autrement dit, ils ont pensé aux admins sérieux. Pour ceux qui ont déjà
<a href="https://korben.info/pocket-id-auth-oidc-passkey.html">configuré un provider OIDC sur leur homelab</a>
, ça se branche directement.</p>
<p>Pour l'installer, le plus simple c'est Docker. Un docker compose up -d, 30 secondes d'attente, et c'est plié.</p>
<p>Mais y'a aussi un script de déploiement automatique, un repo APT communautaire maintenu par gyptazy, ou le classique git clone + pip pour les puristes. Une fois lancé, vous pointez votre navigateur sur https://votre-ip:5000, et un assistant vous accueille avec les identifiants par défaut (pegaprox/admin, à changer immédiatement bien sûr). L'interface est dispo en 5 langues : français, anglais, allemand, espagnol et portugais.</p>
<p>D'ailleurs, si vous utilisez déjà
<a href="https://korben.info/proxmenux.html">ProxMenux</a>
pour administrer votre Proxmox en terminal, les deux sont en fait complémentaires. Disons que ProxMenux couvre l'admin système en ligne de commande, alors que le dashboard apporte la vue unifiée multi-clusters en web. Initialement j'aurais dit que c'était redondant, mais non, ça se marie plutôt bien. Et y'a même un système de plugins avec un portail client pour vos utilisateurs et une page de statut publique à la StatusGator.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pegaprox-dashboard-proxmox/pegaprox-dashboard-proxmox-3.png" alt="" loading="lazy" decoding="async">
<p>Attention c'est comme je vous le disais, encore une beta. L'OIDC avec Authentik par exemple, ça fonctionne pour le login mais les groupes ne remontent pas encore correctement (retour d'un lecteur qui l'utilise au quotidien).</p>
<p>Par contre si vous n'avez qu'un seul serveur Proxmox, honnêtement c'est un peu overkill, l'interface native suffit largement. Quelques glitchs traînent ici ou là, et l'API Token pour se connecter à la place de root n'est pas super bien documenté. Mais le projet avance vite donc c'est plutôt bon signe !</p>
<p>Bref, ça promet pas mal. Merci à Maxime pour la découverte !</p>