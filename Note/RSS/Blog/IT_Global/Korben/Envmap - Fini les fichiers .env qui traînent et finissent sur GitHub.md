---
title: "Envmap - Fini les fichiers .env qui traînent et finissent sur GitHub"
author: "Korben"
date: 2026-01-17T18:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "vie-privee-anonymat/chiffrement"
  - "API keys"
  - "AWS"
  - "DevOps"
  - "environnement"
  - "Hashicorp Vault"
  - "open source"
  - "Secrets"
  - "securite"
rss_source: Blog
url: https://korben.info/envmap-secrets-sans-fichier-env-disque-github-leaks.html
note: 0
seen: false
---

<p>Devinette du soir : Qu’est-ce qui est pire qu'un secret que vous avez oublié de cacher ?</p>
<p>Réponse : Des dizaines, des millions de secrets qui traînent sur GitHub parce que quelqu'un a eu la flemme de configurer un vrai gestionnaire de variables d'environnement !</p>
<p>Hé oui, les amis ! On a tous fait cette boulette au moins une fois (ou alors vous mentez, ou vous êtes un robot). On crée un petit fichier <code>.env</code>, on oublie de le rajouter au <code>.gitignore</code>, et paf, vos clés AWS se retrouvent à poil. Selon GitHub, c'est plus de 39 millions de secrets qui ont été détectés en fuite sur leurs dépôts en 2024. C'est du délire !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/envmap-secrets-sans-fichier-env-disque-github-leaks/envmap-secrets-sans-fichier-env-disque-github-leaks-2.png" alt="" loading="lazy" decoding="async">
<p><em>Envmap - Le gestionnaire de variables d'environnement qui tue les fichiers .env (
<a href="https://github.com/BinSquare/envmap">Source</a>
)</em></p>
<p>Du coup, au lieu de continuer à se farcir du bricolage avec des fichiers qui traînent en clair sur le disque, je vous propose de jeter un œil à <strong>
<a href="https://github.com/BinSquare/envmap">Envmap</a>
</strong>.</p>
<p>C'est un outil écrit en Go dont l'objectif est de réduire au maximum l'écriture de vos secrets sur le disque dur. En mode normal, il va les pomper directement chez les grands manitous du stockage sécurisé comme AWS Secrets Manager, HashiCorp Vault, 1Password ou encore Doppler (même si pour l'instant, certains de ces providers sont encore en cours d'intégration).</p>
<p>Comme ça, au lieu de faire un vieux <code>source .env</code> qui laisse traîner un fichier sensible, vous lancez votre application avec <code>envmap run -- node app.js</code>. L'outil récupère les variables en RAM et les injecte dans le process. C'est propre, c'est net, et ça évite surtout de pousser par erreur votre config sur un repo public.</p>
<p>Pour ceux qui se demandent s'il faut quand même envoyer ses fichiers .env sur GitHub (spoiler : non, jamais !), Envmap propose une commande <code>import</code> pour ingérer vos vieux secrets. Et pour ceux qui ont besoin d'un stockage local, sachez qu'Envmap peut aussi chiffrer vos variables en AES-256-GCM, ce qui est quand même plus sérieux qu'un fichier texte lisible par n'importe qui. Notez aussi qu'il existe une commande <code>sync</code> si vous avez vraiment besoin de générer un fichier <code>.env</code> temporaire.</p>
<p>Perso, ce que je trouve vraiment cool, c'est l'intégration avec <code>direnv</code>. On rajoute une ligne dans son <code>.envrc</code>, et hop, les secrets sont chargés automatiquement quand on entre dans le dossier du projet. C'est magique et ça évite les crises cardiaques au moment du push.</p>
<p>D'ailleurs, si vous voulez aller plus loin dans la sécurisation de vos outils, je vous recommande de lire mon article sur
<a href="https://korben.info/sops-gestionnaire-mots-passe-devops.html">SOPS</a>
ou encore ma réflexion sur
<a href="https://korben.info/gitlab-pour-arreter-de-tout-mettre-sur-github.html">l'usage de GitLab</a>
pour vos projets sensibles.</p>
<p>Bref, c'est open source (sous licence Apache 2.0), et avec ça, vous dormirez sur vos deux oreilles !</p>