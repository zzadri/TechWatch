---
title: "Podman Desktop - Red Hat dégaine sa version enterprise"
author: "Korben"
date: 2026-02-26T13:16:37.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "linux-open-source/logiciels-libres"
  - "Conteneurs"
  - "Docker"
  - "Kubernetes"
  - "Podman"
  - "Red Hat"
rss_source: Blog
url: https://korben.info/red-hat-developer-desktop-cloud-native.html
note: 0
seen: false
---

<p>Hey mais on dirait bien que c'est Red Hat qui débarque sur le marché des apps desktop pour conteneurs... mais lol ! Car oui, pendant que Docker Desktop trône depuis des années et qu'OrbStack séduit de plus en plus d'utilisateurs macOS, Red Hat se réveille ENFIN avec sa propre version Enterprise de
<a href="https://podman-desktop.io/">Podman Desktop</a>
.</p>
<p>Bah mieux vaut tard que jamais !</p>
<p>Pour ceux qui débarquent (bouuuuh) Podman Desktop, c'est un outil open source qui existe depuis des années pour gérer vos conteneurs, images et pods via une interface graphique. C'est dispo sous Linux, macOS, Windows et le projet a même rejoint la
<a href="https://www.cncf.io/">CNCF</a>
(rien à voir avec les trains... lool) en janvier 2025 en même temps que d'autres briques Red Hat (Buildah, Skopeo, bootc, Composefs... chacun en projet séparé).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/red-hat-developer-desktop-cloud-native/red-hat-developer-desktop-cloud-native-2.png" alt="" loading="lazy" decoding="async">
<p><em>Interface de Podman Desktop</em></p>
<p>Et donc Red Hat a décidé de lancer sa propre &quot;build&quot; enterprise de cette app de conteneurs. En gros, c'est la même base que Podman Desktop, mais avec une couche admin par-dessus. Les responsables IT peuvent donc verrouiller des paramètres au niveau de la flotte tels que les registry mirrors, proxies HTTP, certificats custom... On est dans une ambiance un peu plus corporate quoi.</p>
<p>Côté Kubernetes, c'est également plutôt bien pensé. Vous créez vos pods en local, l'outil génère le YAML correspondant, et hop, déploiement sur Kind, Minikube ou directement sur OpenShift, les doigts dans le nez.</p>
<p>Pour ceux qui se demandent si ça remplace Docker Desktop, bah, ça dépend en fait. Podman tourne sans daemon et en rootless, du coup c'est un vrai plus côté sécurité. Mais par contre, le support Docker Compose passe par un système d'aliasing... ça marche bien, sauf si vous avez des configs Docker très exotiques... là faudra tester avant de tout basculer comme le early adopter fifou que vous êtes.</p>
<p>D'ailleurs, si vous êtes sur RHEL, Podman est déjà inclus dans votre abonnement et Red Hat a aussi bossé sur des extensions pour les images bootable OCI et le mode image RHEL.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/dD691zzC3kk?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le truc, c'est que Red Hat arrive tard. TRÈS tard. Docker Desktop, c'est le standard de facto depuis des lustres,
<a href="https://korben.info/orbstack-alternative-docker-desktop-macos.html">OrbStack</a>
a conquis les devs macOS avec sa légèreté sans oublier que Rancher Desktop et Portainer Business Edition occupent aussi le terrain. Du coup, leur stratégie c'est de cibler les boîtes déjà full Red Hat plutôt que d'essayer de convertir les utilisateurs Docker. C'est une ambition plutôt réaliste, je trouve.</p>
<p>Ça vient donc de passer en disponibilité générale via les canaux développeurs Red Hat, c'est gratuit, open source, et plutôt bien fichu pour ceux qui bossent dans un environnement RHEL au quotidien. Après, c'est pas non plus la révolution car ça reste Podman Desktop avec un petit chapeau d'entreprise.</p>
<p>Je pense que pour un usage hors Red Hat, Docker Desktop ou OrbStack restent devant. Mais si vous avez l'abonnement RHEL, ça peut valoir le coup d'y jeter un oeil.</p>
<p>
<a href="https://thenewstack.io/red-hat-enters-the-cloud-native-developer-desktop-market/">Source</a>
</p>