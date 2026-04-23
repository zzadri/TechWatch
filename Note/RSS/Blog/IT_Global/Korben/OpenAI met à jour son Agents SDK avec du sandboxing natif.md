---
title: "OpenAI met à jour son Agents SDK avec du sandboxing natif"
author: "Korben"
date: 2026-04-16T12:37:59.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "intelligence-artificielle/ia-developpement"
  - "OpenAI"
  - "sandboxing"
  - "sdk"
rss_source: Blog
url: https://korben.info/openai-met-a-jour-son-agents-sdk-avec-du-sandboxing-natif.html
note: 0
seen: false
---

<p>La mise à jour d'avril du SDK Agents d'OpenAI introduit deux nouvelles briques qui manquaient pour passer de l'agent-jouet au déploiement réel. Le sandboxing natif permet de confiner un agent dans un espace de travail isolé, avec accès limité aux fichiers et outils d'un périmètre défini. Et le nouveau harness d'exécution sépare proprement le plan de contrôle (boucle agent, appels modèle, routing d'outils, approbations, tracing, récupération d'erreurs) du plan de calcul (sandbox où l'agent lit, écrit, exécute du code, installe des dépendances, snapshot son état).</p>
<p>L'architecture est pensée pour les agents &quot;long-horizon&quot;, ceux qui travaillent sur des tâches complexes en plusieurs étapes, sur des durées longues, avec un besoin de persistance d'état entre les étapes. Le harness gère la coordination, le développeur apporte son propre compute et stockage. C'est une séparation qui permet de brancher le SDK sur n'importe quelle infrastructure, que ce soit Cloudflare, Vercel, Blaxel ou un cluster interne.</p>
<p>Le SDK introduit aussi une abstraction &quot;Manifest&quot; pour décrire un workspace de manière portable. En clair, vous décrivez les outils, les fichiers et les permissions disponibles dans un format standardisé, et le harness sait reconstituer l'environnement ailleurs. C'est utile pour le test, pour la reproductibilité, et pour déployer le même agent dans des environnements différents sans reconfigurer à la main.</p>
<p>Le lancement est Python d'abord, TypeScript prévu après. Classique. Ça peut agacer les équipes full-stack qui bossent en TypeScript, mais c'est quand même très cohérent avec le fait que la majorité des workloads agents en prod tournent encore en Python, surtout côté data et sécurité.</p>
<p>Ce qui est intéressant, c'est le sous-texte. OpenAI pousse un modèle où son SDK est le harness, et le compute est chez le client ou chez un partenaire cloud. C'est un positionnement de plateforme d'orchestration, pas de fournisseur d'infra. Anthropic et Google proposent des approches comparables avec leurs propres SDKs, mais OpenAI a l'avantage du premier écosystème de plugins et d'outils tiers déjà en place.</p>
<p>Bref, pour les devs qui construisent des agents en prod, cette release comble de vrais trous. Sandboxing et harness, c'étaient les deux pièces manquantes.</p>
<p>Source :
<a href="https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/">Techcrunch</a>
</p>