---
title: "Passez Claude Code sur le pilote automatique"
author: "Korben"
date: 2026-01-15T07:47:02.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "intelligence-artificielle/automatisation-ia"
rss_source: Blog
url: https://korben.info/claude-code-scheduler-autopilot.html
note: 0
seen: false
---

<p>Si vous utilisez Claude Code (l'outil CLI d'Anthropic qui déboite), vous savez que c'est super puissant pour coder, auditer ou refactoriser des trucs en un clin d'œil. Mais le petit souci, c'est qu'il faut tout le temps être derrière son terminal pour lui dire quoi faire.</p>
<p>C'est là qu'entre en scène un super projet baptisé <strong>
<a href="https://github.com/jshchnz/claude-code-scheduler">Claude Code Scheduler</a>
</strong>.</p>
<p>Développé par un certain jshchnz, ce petit plugin permet tout simplement de programmer Claude afin de pouvoir lui balancer des ordres du genre &quot;<em>fais-moi une review de sécurité tous les jours à 9h</em>&quot; ou &quot;<em>check les dépendances chaque mardi après-midi</em>&quot;, et de le laisser bosser tout seul dans son coin. Et ce que j'aime avec ces outils, c'est qu'on lui parle en langage naturel... Pas besoin de s'arracher les cheveux avec la syntaxe obscure des cron jobs. Vous lui dites &quot;Tous les jours de la semaine à 10h du mat&quot; et il comprend direct.</p>
<p>Ce scheduler s'appuie sur les planificateurs natifs de votre système d'exploitation tels que launchd sur macOS, crontab sur Linux et le planificateur de tâches sur Windows. C'est robuste, ça survit aux redémarrages et c'est parfaitement intégré et pour ceux qui s'inquiètent de devoir valider chaque modification à la main, sachez que l'outil gère le mode autonome.</p>
<p>En gros, il utilise le flag <code>--dangerously-skip-permissions</code> de Claude Code pour lui permettre d'éditer des fichiers ou de lancer des commandes sans vous demander la permission à chaque ligne. Forcément, il faut avoir confiance dans vos prompts, mais pour des tâches de maintenance récurrentes, c'est un gain de temps monumental.</p>
<p>Une fois installé, vous aurez alors accès à une panoplie de commandes slash comme <code>/schedule-add</code> ou <code>/schedule-list</code> pour gérer tout ça directement depuis l'interface de Claude. Et bien sûr, tout est loggé proprement dans des fichiers texte pour que vous puissiez vérifier au petit matin ce que l'IA a glandé pendant que vous étiez dans les bras de Morphée.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-scheduler-autopilot/claude-code-scheduler-autopilot-2.png" alt="" loading="lazy" decoding="async">
<p>Voilà, c'est un chouette plugin pour Claude Code et
<a href="https://github.com/jshchnz/claude-code-scheduler">c'est dispo sur Github</a>
.</p>