---
title: "SHM - La télémétrie qui respecte vos utilisateurs"
author: "Korben"
date: 2026-01-09T08:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement"
  - "linux-open-source/self-hosting"
  - "vie-privee-anonymat"
  - "developpement"
  - "open source"
  - "privacy"
  - "self-hosted"
  - "telemetrie"
rss_source: Blog
url: https://korben.info/shm-self-hosted-metrics-telemetrie-privacy.html
note: 0
seen: false
---

<p>Si vous développez un logiciel open source auto-hébergé, vous connaissez sûrement ce dilemme qui est de comment savoir si votre projet est réellement utilisé sans devenir l'affreux Big Brother que vous combattez ? Soit vous ne mesurez rien et vous codez dans le vide, soit vous collez du Google Analytics ou assimilé et vous trahissez l'esprit même du self-hosting.</p>
<p>Benjamin Touchard (que certains d'entre vous connaissent peut-être via son projet
<a href="https://korben.info/ackify-confirmation-lecture-documents-open-source.html">Ackify</a>
) a décidé de résoudre ce problème avec <strong>
<a href="https://self-hosted-metrics.com/">SHM, pour Self-Hosted Metrics</a>
</strong>. Son idée c'est de proposer une télémétrie respectueuse de la vie privée, où chaque instance génère sa propre identité cryptographique dès le premier démarrage.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/shm-self-hosted-metrics-telemetrie-privacy/shm-self-hosted-metrics-telemetrie-privacy-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Concrètement, quand vous intégrez le SDK dans votre application (dispo en Go et Node.js 22+), chaque installation génère une paire de clés Ed25519, un peu comme quand vous générez vos clés SSH pour la première fois. Tous les échanges avec votre serveur SHM sont ensuite signés cryptographiquement, ce qui garantit l'intégrité des requêtes et leur origine. L'instance a une identité persistante (pseudonyme), mais ça n'identifie pas l'utilisateur final.</p>
<p>Côté données collectées, ensuite c'est vous qui décidez. Votre app envoie périodiquement un JSON avec les métriques que vous avez définies, et le dashboard s'adapte dynamiquement. Y'a pas de schéma imposé, pas de PII (données personnellement identifiables) et par défaut, le SDK collecte aussi des infos système (OS, CPU, RAM), mais c'est désactivable.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/shm-self-hosted-metrics-telemetrie-privacy/shm-self-hosted-metrics-telemetrie-privacy-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pour ceux qui veulent héberger le bouzin, c'est du Docker classique... Vous créez un fichier <code>compose.yml</code>, vous configurez le DSN PostgreSQL, vous récupérez les migrations SQL, et hop un <code>docker compose up -d</code>. Le dashboard est alors accessible par défaut sur le port 8080 et affiche automatiquement vos métriques métier, la distribution des versions, le nombre d'instances actives, etc.</p>
<p>Et pour les utilisateurs finaux qui ne veulent vraiment pas participer, un simple <code>DO_NOT_TRACK=true</code> dans les variables d'environnement désactive complètement la télémétrie.</p>
<p>
<a href="https://github.com/btouchard/shm?tab=readme-ov-file">Le code du serveur est sous licence AGPL</a>
(les SDKs ont leur propre licence, vérifiez sur le dépôt) et y'a aussi des badges SVG à coller dans vos pages README pour afficher fièrement le nombre d'instances de votre app qui tournent.</p>
<p>Bref, si vous distribuez un logiciel auto-hébergé et que vous voulez savoir combien d'instances sont actives sans compromettre la vie privée des utilisateurs, c'est le top !</p>
<p>Merci à Benjamin pour le partage !</p>