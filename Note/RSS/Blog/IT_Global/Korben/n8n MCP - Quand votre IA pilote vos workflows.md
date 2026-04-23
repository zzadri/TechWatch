---
title: "n8n MCP - Quand votre IA pilote vos workflows"
author: "Korben"
date: 2026-03-09T10:17:48.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "intelligence-artificielle/automatisation-ia"
  - "intelligence-artificielle/chatbots-llm"
  - "automatisation"
  - "mcp"
  - "workflow"
  - "n8n"
rss_source: Blog
url: https://korben.info/n8n-mcp-serveur-ia-automatisation.html
note: 0
seen: false
---

<p>Le MCP, c'est devenu LE truc standard pour connecter des IA à vos outils. Sauf que voilà... brancher Claude sur n8n, en pratique, c'était encore un peu le bazar avec du JSON à copier-coller dans tous les sens. Mais heureusement, un dev a décidé de faire les choses proprement avec <strong>un vrai serveur MCP dédié</strong>.</p>
<p>
<a href="https://github.com/czlonkowski/n8n-mcp">n8n MCP</a>
, c'est un serveur MCP open source (sous licence MIT) qui donne à votre IA un accès direct à n8n avec plus de 1 000 nœuds supportés (Gmail, Slack, PostgreSQL, HTTP...), leurs propriétés, leurs opérations, bref tout le bazar. Vous décrivez ce que vous voulez, et youplaboom, l'IA construit le workflow à votre place. Comme ça plus besoin d'exporter du JSON, de l'importer, de corriger les erreurs cryptiques... c'est plié !</p>
<p>Et le truc chouette, c'est son système de mises à jour différentielles. Au lieu de renvoyer tout le workflow à chaque modif (et bouffer vos tokens comme un goinfre), le serveur ne transmet que ce qui a changé. Résultat, 80 à 90% de tokens en moins sur les grosses modifs. Pas mal du tout, hein ?!</p>
<p>Côté compatibilité, c'est large : Claude Desktop, ChatGPT, Cursor, Gemini CLI, Codex CLI... la liste est carrément longue. Via le service hébergé, c'est du OAuth zero-setup pour pas mal de clients, vous cliquez et c'est bon. Pour les IDE comme Cursor ou VS Code (avec une extension MCP), faut une clé API mais rien de bien sorcier. Après, ça ne marchera pas avec tous les clients MCP non plus, donc vérifiez la liste sur leur site avant de vous lancer.</p>
<p>D'ailleurs, si vous avez kiffé
<a href="https://korben.info/onemcp-serveur-mcp-anthropic-facile.html">OneMCP</a>
qui simplifie la gestion des serveurs MCP, ici c'est totalement complémentaire. OneMCP gère la plomberie générale, n8n MCP se spécialise sur un truc précis à savoir donner à l'IA la connaissance COMPLÈTE de n8n (plus de 500 nœuds officiels et autant de nœuds communautaires) pour qu'elle puisse construire des workflows qui marchent du premier coup... enfin presque.</p>
<p>Y'a aussi une bibliothèque de plus de 2 700 templates de workflows prêts à l'emploi avec recherche sémantique. Genre vous dites &quot;<em>je veux un workflow qui surveille mes commits GitHub et m'envoie un récap Slack chaque soir</em>&quot; et l'IA pioche dans les templates existants pour vous pondre un truc fonctionnel.</p>
<p>Après pour l'installation, c'est soit le service hébergé (gratuit pour 100 appels par jour mais rien à configurer), soit en self-hosted via <code>npx n8n-mcp</code> (faut Node.js 18+) ou Docker (~280 Mo l'image, basée sur Alpine). Perso, le mode hébergé suffit largement pour tester, et si vous voulez aller plus loin c'est de la licence MIT donc vous faites ce que vous voulez.</p>
<p>Attention quand même, le projet (tout comme moi) recommande de ne JAMAIS laisser l'IA modifier vos workflows de production directement. Toujours copier, tester en dev, exporter un backup. C'est du bon sens mais ça vaut le coup de le rappeler parce que sinon, le jour où votre IA décide d'&quot;optimiser&quot; votre pipeline de facturation en supprimant des nœuds qu'elle juge inutiles... bah gros caca en perspective !</p>
<p>Et si vous voulez voir comment ça se marie avec d'autres serveurs MCP genre
<a href="https://korben.info/chrome-devtools-mcp.html">Chrome DevTools MCP</a>
, c'est tout à fait possible de combiner les deux pour que votre IA construise un workflow n8n ET debug le front dans Chrome en même temps. La stack IA-augmentée commence à devenir sérieusement sérieuse ! Oui je suis sérieux ^^ !</p>
<p>Bref, plutôt que de bidouiller avec du JSON à la main ou de lancer des OpenClaw sans sécurité en mode gros débilo de Linkedin..., bah vous demandez à Claude et lui fera le job proprement sous votre contrôle !</p>