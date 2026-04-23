---
title: "GitHub active par défaut la télémétrie sur son outil en ligne de commande"
author: "Vincent Lautier"
date: 2026-04-23T11:38:15.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "vie-privee-anonymat/surveillance-tracking"
  - "CLI"
  - "GitHub"
  - "telemetrie"
rss_source: Blog
url: https://korben.info/github-active-par-defaut-la-telemetrie-sur-son-outil-en-ligne-de-commande.html
note: 0
seen: false
---

<p>Depuis la version 2.91.0 du CLI GitHub publiée mardi, chaque commande que vous tapez dans gh envoie des données de télémétrie vers GitHub par défaut. L'activation est silencieuse, sans message au premier lancement, sans consentement explicite, et il faut fouiller dans la doc pour tomber sur la page dédiée au sujet.</p>
<p>GitHub décrit la collecte comme pseudonyme côté client. Concrètement, le payload embarque le nom de la commande lancée, un identifiant d'invocation, un identifiant d'appareil, l'OS, l'architecture, l'agent et quelques drapeaux.</p>
<p>L'entreprise précise que le contenu exact peut varier d'un appel à l'autre. La justification officielle : les équipes produit ont besoin de voir comment le CLI est utilisé, avec la montée en puissance des agents IA qui le pilotent de plus en plus souvent en arrière-plan.</p>
<p>Côté sortie, il y a trois moyens de couper la télémétrie. Vous pouvez définir la variable d'environnement GH_TELEMETRY à false, ou DO_NOT_TRACK à true, ou lancer gh config set telemetry disabled. Simple en apparence.</p>
<p>Sauf que rien de tout ça n'est signalé à l'installation, et qu'un utilisateur qui n'est pas tombé sur le
<a href="https://www.theregister.com/2026/04/22/github_opts_all_cli_users/">billet de Brandon Vigliarolo dans The Register</a>
ne saura probablement pas que c'est activé sur sa machine.</p>
<p>Le terme pseudonyme mérite aussi qu'on le regarde de près. Pseudonyme ne veut pas dire anonyme : il y a un identifiant d'appareil stable, il y a un identifiant d'invocation, et GitHub connaît déjà votre compte si vous êtes authentifié avec gh auth login.</p>
<p>Du coup, le recoupement entre votre activité CLI et votre identité GitHub n'a rien de théorique, même si GitHub ne promet pas de le faire.</p>
<p>En pratique, la télémétrie des outils de dev n'est pas une nouveauté. VS Code le fait depuis des années, npm aussi, et la plupart des éditeurs jouent le même jeu. Ce qui coince ici, c'est le choix de l'opt-out plutôt que de l'opt-in, et l'absence d'annonce claire sur le changelog principal.</p>
<p>Les utilisateurs reprochent surtout à GitHub d'avoir glissé l'info dans une page de doc au lieu d'un billet de blog dédié. Pour un outil qu'utilisent des gens très à cheval sur leur vie privée, c'est un drôle de calcul.</p>
<p>Bref, un outil CLI qui s'active en mode collecte par défaut sans prévenir, ça pique. Heureusement une variable d'environnement suffit à couper. Mais il faut savoir qu'elle existe.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/22/github_opts_all_cli_users/">The Register</a>
</p>