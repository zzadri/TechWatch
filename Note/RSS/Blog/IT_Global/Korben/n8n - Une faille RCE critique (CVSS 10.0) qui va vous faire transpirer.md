---
title: "n8n - Une faille RCE critique (CVSS 10.0) qui va vous faire transpirer"
author: "Korben"
date: 2026-01-07T15:23:35.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/automatisation-ia"
  - "automatisation"
  - "faille de sécurité"
  - "n8n"
  - "vulnérabilité"
  - "vulnérabilité RCE"
rss-source: Blog
url: https://korben.info/n8n-faille-securite-rce-critique.html
note: 0
seen: false
---

<p>Avis aux utilisateurs de <strong>n8n</strong>, j'ai une bonne et une mauvaise nouvelle à vous annoncer.</p>
<p>Non, je déconne, je n'ai qu'une mauvaise nouvelle à vous annoncer, et malheureusement, elle est du genre à vous faire lâcher votre café direct sur votre clavier mécanique de hipster.</p>
<p>Si vous utilisez cet outil génial d'automatisation (et je sais que vous êtes nombreux par ici, surtout depuis que je vous ai partagé cette
<a href="https://korben.info/n8n-workflows-collection-4000-automatisations-gith.html">énorme collection de workflows</a>
), il faut qu'on parle de la <strong>CVE-2026-21877</strong>. C'est Théo Lelasseux qui a débusqué le loup, et croyez-moi, c'est pas un petit caniche.</p>
<p>C'est une vulnérabilité avec un score CVSS de 10.0, soit le niveau max mais attention, ça ne veut pas dire que n'importe qui peut rentrer comme dans un moulin sur votre instance. Toutefois, dans certaines conditions, un utilisateur authentifié pourrait réussir à faire exécuter du code non fiable par le service.</p>
<p>Concrètement, c'est une faille de type RCE (Remote Code Execution) liée à un souci de gestion de fichiers (on parle notamment d'écriture/pose de fichiers là où il ne faut pas), et n8n recommande d’ailleurs de désactiver le nœud Git en mitigation si vous ne pouvez pas patcher. Du coup, si l'attaque passe, ça peut mener à une compromission totale de votre instance, que vous soyez en self-hosted ou sur n8n Cloud. Brrrrrr, ça fait froid dans le dos quand on sait tout ce qu'on fait transiter par ces workflows !</p>
<p><strong>Bon, pas de panique, mais faut agir.</strong></p>
<p>Les versions touchées sont toutes celles comprises entre la 0.123.0 et les versions antérieures à la 1.121.3. Si vous êtes dans cette fourchette, vous avez donc un petit trou dans votre raquette de sécurité.</p>
<p>Pour corriger le tir, hop, on file mettre à jour vers la version patchée 1.121.3 ou une version supérieure. Et si une raison obscure (et sûrement très relou) vous ne pouvez pas patcher tout de suite, il est recommandé de désactiver fissa le nœud Git et de restreindre l'accès à votre instance uniquement aux gens en qui vous avez une confiance aveugle.</p>
<p>Et pendant qu’on y est : il y a aussi une autre saleté qui circule en ce moment, surnommée
<a href="https://www.cyera.com/research-labs/ni8mare-unauthenticated-remote-code-execution-in-n8n-cve-2026-21858">Ni8mare</a>
(CVE-2026-21858), décrite comme exploitable <em>sans authentification</em> via certains scénarios autour des Forms / webhooks, et patchée à partir de la 1.121.0. Moralité : si vous passez en 1.121.3+ (ce que vous allez faire là, maintenant ^^), vous vous couvrez aussi contre ce deuxième cauchemar.</p>
<p>Voilà, à vous de jouer maintenant ! On sauvegarde tout et on lance l'update avant de retourner à ses bidouilles !</p>
<p>Allez, kiffez bien (mais en sécurité) !</p>
<p>
<a href="https://thehackernews.com/2026/01/n8n-warns-of-cvss-100-rce-vulnerability.html">Source</a>
</p>