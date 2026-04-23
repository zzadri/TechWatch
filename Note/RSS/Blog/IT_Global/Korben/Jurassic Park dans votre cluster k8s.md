---
title: "Jurassic Park dans votre cluster k8s"
author: "Korben"
date: 2026-03-13T08:04:25.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "3d"
  - "DevOps"
  - "Docker"
  - "Kubernetes"
  - "open source"
rss_source: Blog
url: https://korben.info/k8s-unix-system-kubernetes-simulateur-unix.html
note: 0
seen: false
---

<p>Le navigateur 3D de Jurassic Park, vous savez, celui avec lequel Lex hackait le parc en 1993 pendant que les vélociraptors grattaient à la porte... bah quelqu'un vient de le recréer, mais pour Kubernetes.</p>
<p>Le projet s'appelle
<a href="https://github.com/jlandersen/k8s-unix-system">k8s-unix-system</a>
et c'est exactement ce que vous imaginez. Vos namespaces deviennent des îles flottantes roses, vos pods des blocs 3D colorés et vous naviguez dans le tout en vue FPS avec WASD + souris. Genre comme Quake, mais pour surveiller vos pods.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/k8s-unix-system-kubernetes-simulateur-unix/k8s-unix-system-kubernetes-simulateur-unix-2.png" alt="" loading="lazy" decoding="async">
<p><em>Les pods Kubernetes version Jurassic Park (
<a href="https://github.com/jlandersen/k8s-unix-system">Source</a>
)</em></p>
<p>Un pod vert c'est un pod qui tourne, jaune c'est en attente, et rouge c'est erreur ou CrashLoopBackOff, bref le truc que personne n'aime voir. Le truc sympa, c'est que la hauteur des blocs augmente avec le nombre de restarts. Du coup, le pod qui galère depuis ce matin, c'est celui qui ressemble à une tour bien haute. Par contre, attention, les pods en erreur tremblent carrément (pas nerveux hein, c'est voulu) et les pods running bougent doucement... c'est plutôt zen je trouve.</p>
<p>Les nodes, eux, ne sont pas mélangés avec les namespaces. Ils ont leur propre île bleu foncé à part, avec des cubes cyan pour ceux qui sont Ready et rouge pour les NotReady. Survolez un node et hop, vous avez son nom, son statut, sa capacité CPU et sa RAM affichées dans un tooltip. Les services, eux, sont visualisés sous forme d'arcs cyan semi-transparents qui connectent les pods entre eux en topologie étoile. Tout fonctionne, suffit de demander, on l'a ! (reeeef ^^)</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/k8s-unix-system-kubernetes-simulateur-unix/k8s-unix-system-kubernetes-simulateur-unix-3.png" alt="" loading="lazy" decoding="async">
<p><em>Les namespaces et nodes, chacun sur leur île (
<a href="https://github.com/jlandersen/k8s-unix-system">Source</a>
)</em></p>
<p>Pour lancer le truc, un Docker one-liner suffit (attention quand même, ça monte votre kubeconfig en lecture seule dans le conteneur, donc à réserver au cluster de dev) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">docker run --rm -it -v ~/.kube/config:/root/.kube/config:ro -p 8080:8080 ghcr.io/jlandersen/k8s-unix-system:main
</span></span></code></pre><p>Vous ouvrez localhost:8080 dans Chrome et vous volez à travers votre cluster avec la barre espace pour monter, Ctrl pour descendre, Shift pour accélérer. Tout est en temps réel grâce à la Watch API K8s, du coup si un pod tombe pendant que vous survolez son île, vous le voyez passer au rouge direct. Finalement, c'est
<a href="https://korben.info/formation-kubernetes-devops-guide.html">kubectl get pods</a>
mais en 100 fois plus fun.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/k8s-unix-system-kubernetes-simulateur-unix/k8s-unix-system-kubernetes-simulateur-unix-4.png" alt="" loading="lazy" decoding="async">
<p>C'est codé en Go côté serveur et Three.js pour la 3D dans le navigateur. Le dev derrière bosse chez LEGO (ça ne s'invente pas). Et d'ailleurs si vous êtes du genre à
<a href="https://korben.info/smartphones-cluster-kubernetes-postmarketos.html">recycler vos smartphones en cluster</a>
, ça ferait un combo d'enfer pour frimer devant les collègues.</p>
<p>Bref, vous allez pouvoir enfin lâcher un « <em>Je connais ce système... il fonctionne sous Unix</em> ! » sans mentir.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/zG0ecmeJs6k?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>