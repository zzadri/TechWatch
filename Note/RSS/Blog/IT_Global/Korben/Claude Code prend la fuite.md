---
title: "Claude Code prend la fuite"
author: "Korben"
date: 2026-04-01T07:06:18.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/failles-vulnerabilites"
  - "developpement/api-services"
  - "Anthropic"
  - "Claude Code"
  - "fuite"
  - "NPM"
rss_source: Blog
url: https://korben.info/claude-code-fuite-code-source-npm-source-maps.html
note: 0
seen: false
---

<p>60 Mo de source maps (ces fichiers qui permettent de remonter du code minifié à l'original) ont été oubliés dans un paquet npm. Et voilà comment Anthropic a involontairement balancé en public le code source complet de Claude Code, son outil à 2.5 milliards de dollars de revenus annuels.</p>
<p>Alors qu'est-ce qui s'est passé exactement ?</p>
<p>Hé bien hier, la version 2.1.88 du package <code>@anthropic-ai/claude-code</code> sur le registre npm embarquait un fichier <code>.map</code> de 59.8 Mo. Un truc normalement réservé au debug interne, sauf que ce fichier <code>.map</code> contenait les pointeurs vers les 1 900 fichiers TypeScript originaux, en clair. Chaofan Shou, un développeur chez Solayer Labs, a alors repéré la boulette et l'a partagée sur X. Le temps qu'Anthropic réagisse, le code était déjà mirroré partout sur GitHub, avec 41 500+ forks en quelques heures. Autant dire que le dentifrice ne rentrera pas dans le tube !</p>
<p>Pour ma part, j'avais un petit dépôt à moi assez ancien avec quelques trucs relatifs à Claude Code, qui n'avait rien à voir avec tout ça, qui s'est même retrouvé striké... Ils ratissent large avec leur DMCA donc.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-fuite-code-source-npm-source-maps/claude-code-fuite-code-source-npm-source-maps-2.png" alt="" loading="lazy" decoding="async">
<p>Et là, c'est la fête pour les curieux comme moi parce que les entrailles de l'outil révèlent pas mal de surprises. Côté architecture, on découvre environ 40 outils internes avec gestion de permissions, un moteur de requêtes de 46 000 lignes de TypeScript, un système multi-agents capable de spawner des essaims de sous-tâches en parallèle, et un pont de communication entre le terminal et votre éditeur VS Code ou JetBrains. Le tout tourne sur Bun (pas Node.js ^^) avec Ink pour l'interface terminal. Par contre, pas de tests unitaires visibles dans le dump.</p>
<p>Côté mémoire, c'est plutôt bien pensé puisqu'au lieu de tout stocker bêtement dans la fenêtre de contexte du modèle, l'outil utilise un fichier texte <code>MEMORY.md</code> ultra-léger (genre 150 caractères par entrée) qui sert d'index de pointeurs. Les vraies données, elles, sont distribuées dans des fichiers thématiques chargés à la demande, et les transcripts bruts ne sont jamais relus entièrement, mais juste fouillés à la recherche d'identifiants précis. L'agent traite en fait sa propre mémoire comme un &quot;hint&quot; ce qui le force à vérifier toujours le vrai code avant d'agir. En gros, il a une mémoire sceptique, et pour moi c'est clairement le truc le plus intéressant du dump.</p>
<p>Y'a aussi un truc qui s'appelle KAIROS (mentionné 150 fois dans le code) qui est un genre de mode daemon autonome. En fait, pendant que vous allez chercher votre café, l'agent tourne en arrière-plan et fait ce qu'ils appellent <code>autoDream</code> : il consolide sa mémoire dans des fichiers JSON, vire les contradictions et transforme les observations vagues en données structurées. Comme ça, quand vous revenez devant votre écran, le contexte est nettoyé.</p>
<p>Et puis le code balance aussi la roadmap interne d'Anthropic (bon courage au service comm ^^). On y trouve les noms de code des modèles... Capybara pour un variant de Claude 4.6, Fennec pour Opus 4.6, et un mystérieux Numbat qui n'est pas encore sorti. D'ailleurs, les commentaires internes révèlent que Capybara v8 a un taux de fausses affirmations qui tourne autour de 30%, ce qui est une grosse régression par rapport aux 17% de la v4. Y'a même un &quot;Undercover Mode&quot; qui permet à l'agent de contribuer à des repos publics sans révéler d'infos internes (c'est sympa pour les projets open source).</p>
<p>Anthropic a confirmé la fuite : &quot;<em>C'était un problème de packaging lié à une erreur humaine, pas une faille de sécurité. Aucune donnée client n'a été exposée.</em>&quot; Mouais, attention quand même, parce que le code est déjà partout et n'en repartira pas. Et même si aucun secret client n'a fuité, exposer l'architecture complète d'un agent IA à 2.5 milliards de revenus, c'est pas rien non plus.</p>
<p>Bon, et maintenant qu'est-ce qu'on peut en faire ? Bah pas mal de choses en fait.</p>
<p>Par exemple, le
<a href="https://korben.info/npm-shai-hulud-scanner-attaque-supply-chain.html">système de mémoire auto-correcteur</a>
est un pattern directement réutilisable pour vos propres agents IA. L'architecture &quot;index léger + fichiers à la demande&quot; résout élégamment le problème de la pollution de contexte qui fait halluciner les LLM sur les longues sessions. Les +40 outils internes permettent aussi de comprendre comment structurer un système de permissions granulaires dans un
<a href="https://korben.info/claude-code-safety-net-plugin-securite-agent-ia.html">agent autonome</a>
. Et le concept KAIROS/autoDream, la consolidation mémoire pendant l'idle, c'est une idée qu'aucun outil open source n'implémente encore. Autant dire que les alternatives open source à Claude Code ou Codex vont monter en gamme dans les jours qui viennent. Et le code est
<a href="https://github.com/Kuberwastaken/claude-code">déjà nettoyé, réécris en Rust et mis sur GitHub</a>
si vous voulez fouiller. Bon, pas sûr que le pattern autoDream soit simple à reimplémenter, mais le système de mémoire oui.</p>
<p>Je trouve ça assez marrant que le code proprio d'une boite qui a aspiré tout l'open source du monde voire plus, sans autorisation, pour le revendre sous la forme de temps machine / tokens, devienne lui aussi en quelque sorte &quot;open source&quot; sans qu'on leur demande leur avis ^^. La vie est bien faite.</p>
<p>Maintenant, pour les développeurs qui publient sur npm, la leçon est limpide : Vérifiez votre <code>.npmignore</code> et votre champ <code>files</code> dans <code>package.json</code>. Ou plutôt, lancez la commande <code>npm pack --dry-run</code> dans votre terminal avant chaque publish. Ça prend 2 secondes et ça vous montre exactement ce qui sera inclus dans le paquet. Ça aurait évité 60 Mo de secrets industriels qui partent en public.</p>
<p>Bref, un <code>.npmignore</code> bien configuré, ça coûte 0 euro. Alors qu'une fuite de propriété intellectuelle évaluée à 2.5 milliards... un peu plus !</p>
<p>
<a href="https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know">Source</a>
</p>