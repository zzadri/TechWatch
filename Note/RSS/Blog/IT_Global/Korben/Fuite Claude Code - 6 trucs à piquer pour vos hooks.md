---
title: "Fuite Claude Code - 6 trucs à piquer pour vos hooks"
author: "Korben"
date: 2026-04-01T12:50:13.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement"
  - "tutoriels-guides"
  - "Anthropic"
  - "Claude Code"
rss_source: Blog
url: https://korben.info/claude-code-6-patterns-bonnes-pratiques-hooks.html
note: 0
seen: false
---

<p><strong>Le code source de Claude Code a fuité hier</strong>, et au-delà du buzz, y'a, je trouve, quelques leçons concrètes à tirer de tout ça.</p>
<p>Alors rassurez-vous, je vais pas vous balancer du code TypeScript à copier-coller (on n'est pas des cochons), ni des leçons de morale sur ce qu'on peut ou pas pousser sur un dépôt Git, mais plutôt vous lister des patterns d'architecture / bonnes pratiques que vous pouvez implémenter dès maintenant dans votre fichier <code>settings.json</code> via le système de
<a href="https://code.claude.com/docs/en/hooks-guide">hooks de Claude Code</a>
.</p>
<p>Je reste vague techniquement, volontairement pour 2 raisons. D'abord parce qu'il y a eu fuite de code, donc je peux pas poster du code propriétaire ici. Et ensuite parce que chaque projet / boite à outil qu'on se crée dans Claude Code ou ailleurs est différente, donc ce sera à vous (ou à Claude en fait) d'adapter chacune de ces bonnes pratiques.</p>
<p>Concrètement, tout passe par le fichier <code>.claude/settings.json</code> de votre projet (ou <code>~/.claude/settings.json</code> pour du global). Dedans, vous déclarez des hooks, c'est-à-dire des scripts <code>.cjs</code> ou <code>.sh</code> qui se déclenchent automatiquement à des moments précis : avant qu'un outil s'exécute (<code>PreToolUse</code>), quand vous tapez un message (<code>UserPromptSubmit</code>), après un commit (<code>PostToolUse</code>), etc.</p>
<p>Le script reçoit du JSON en stdin, fait son boulot, et renvoie un code de sortie : <code>0</code> pour laisser passer, <code>2</code> pour bloquer. Pas besoin de l'API Claude, pas besoin de tokens, ça tourne en local sur votre machine. Hé bien tout ce que vous allez lire ci-dessous, ce sera à vous de l'implémenter dans des scripts de ce type.</p>
<p>Et le plus simple pour ça, c'est de donner les parties de mon article qui vous intéressent à votre propre Claude Code pour qu'il aille lui-même faire les scripts cjs / sh et les bons appels de hooks dans le settings.json. Pourquoi se prendre la tête ?</p>
<p>Et encore une fois, j'insiste, il s'agit de concepts d'ingénierie logicielle, et pas de code propriétaire appartenant à Anthropic.</p>
<p>La première bonne pratique c'est le <strong>circuit breaker</strong> ou disjoncteur en français...</p>
<p>En gros, quand vos scripts JavaScript appellent des APIs genre l'endpoint <code>chat/completions</code> d'OpenAI ou <code>generateContent</code> de Gemini, ça peut parfois ne pas répondre, parce que la vie quoi... ^^</p>
<p>Et malheureusement, quand cela arrive, votre code continue de marteler l'endpoint en boucle, ce qui fait que vous cramez des tokens pour rien. Le fix est pourtant très simple : <strong>Après 3 échecs consécutifs, on coupe</strong>, et on passe au fallback. Netflix avait popularisé ça avec leur librairie
<a href="https://github.com/netflix/hystrix">Hystrix</a>
y'a 10 ans, et c'est ce type de protection qu'on retrouve aujourd'hui dans Claude Code. Concrètement, c'est un module Node.js de 40 lignes avec un compteur et un état ouvert/fermé et comme ça, fini les retry storms !</p>
<p>Deuxième pattern : le <strong>scanner de secrets en pre-commit</strong>.</p>
<p>Un <code>git commit</code> qui embarque une clé API dans un <code>.env</code>, ça arrive trop souvent (demandez à Anthropic et leur fichier <code>.map</code> de 60 Mo ^^). Le hook <code>PreToolUse</code> permet heureusement d'intercepter chaque <code>git commit</code> AVANT exécution. Votre script parcourt alors les fichiers stagés via <code>git diff --cached</code>, cherche les patterns <code>sk-ant-api</code>, <code>ghp_</code>, <code>AKIA</code>, <code>-----BEGIN RSA PRIVATE KEY-----</code> et renvoie un <code>exit 2</code> pour bloquer.</p>
<p>Perso, j'ai dans ma boîte à outils IA, 18 regex dans un fichier <code>.claude/hooks/secret-scanner.cjs</code> qui couvrent Anthropic, OpenAI, AWS, GitHub, Slack, Stripe et les JWT. Par contre, attention aux faux positifs car un fichier contenant &quot;sk-ant-api&quot; dans un commentaire, ça bloquera tout. Ça m'est déjà arrivé et heureusement, l'IA est assez maligne pour comprendre d'où vient le blocage et éventuellement passer outre si ce n'est pas justifié.</p>
<p>Et troisième truc sympa : la <strong>détection de frustration</strong>.</p>
<p>En effet, un hook <code>UserPromptSubmit</code> se déclenche quand vous tapez un message de rageux. Ainsi, si votre prompt contient &quot;putain&quot;, &quot;ça marche pas&quot; ou &quot;wtf&quot;, le hook injecte via stdout un contexte qui dit à Claude d'aller droit au but. Comme ça, y'a plus de blabla et on part direct sur une solution concrète.</p>
<p>Et c'est pareil pour &quot;continue&quot; ou &quot;finis&quot; qui injecte &quot;reprendre sans résumer&quot; automatiquement. Franchement, c'est 30 lignes de JavaScript rikiki à mettre dans <code>.claude/hooks/frustration-detector.cjs</code> et ça change carrément la vie quand vous êtes en mode debug à 2h du mat avec un café dans la main gauche et un œil qui se ferme tout seul en tremblant !</p>
<p>Quatrième bonne pratique : les <strong>tags @[MODEL]</strong> dans vos skills.</p>
<p>Car vous le savez, certaines règles que vous avez mises en place existent uniquement à cause d'un biais du modèle actuel. Genre, Opus 4.6 qui colle ces putains de tirets cadratins (Unicode U+2014) partout. Du coup, ça oblige les gens à mettre dans leurs skills une règle du genre &quot;0 em-dash&quot;. Sauf que le jour où Sonnet 5 ne les utilisera plus, cette règle ce sera du bruit inutile.</p>
<p>Alors en taguant <code>@[OPUS-4.6]</code> dans un commentaire HTML, vous pourrez ensuite faire facilement un <code>grep -r &quot;@\[OPUS&quot;</code> quand vous changez de modèle. C'est du tracking de dette technique pour le prompt engineering, quoi... et perso, je n'y avais pas pensé avant.</p>
<p>Cinquième pattern : <strong>les seuils numériques</strong>.</p>
<p>Votre &quot;<em>Fais des fonctions courtes</em>&quot; dans un CLAUDE.md, ça ne veut rien dire pour un agent et malheureusement, la plupart des gens écrivent encore &quot;<em>sois concis</em>&quot; ou &quot;<em>toi faire code propre</em>&quot; sans aucun chiffre alors qu'un &quot;<em>Max 50 lignes par fonction, couverture tests ≥ 80%, 0 warning ESLint</em>&quot; c'est vachement plus efficace car vérifiable par un script.</p>
<p>Enfin, dernier pattern : la <strong>consolidation mémoire</strong>.</p>
<p>Anthropic a mis en place un système nommé <code>autoDream</code> qui tourne pendant l'inactivité de Claude Code pour nettoyer la mémoire. Il vire les doublons, résout les contradictions, vérifie que les fichiers existent encore. Et même s'il ne le réclame pas parce qu'ils n'ont pas de bouche pour vous parler, vos CLAUDE.md de 200 lignes et vos JSON de 70 Ko ont besoin du même traitement ! Donc il faut que vous ajoutiez une phase genre &quot;dream&quot; en bash ou Node.js à la fin de vos workflows, comme ça, plutôt que de tout garder, le script scan le répertoire <code>~/.claude/</code>, trie les entrées par date, et fusionne les doublons. C'est comme la consolidation pendant l'inactivité, mais en 5 secondes sur un Apple M4.</p>
<p>D'ailleurs, la communauté n'a pas perdu de temps. Un développeur a catalogué les
<a href="https://github.com/paoloanzn/free-code/blob/main/FEATURES.md">88 feature flags</a>
planqués dans le code, dont 54 qui compilent proprement (les autres dépendent de modules internes d'Anthropic). Et un autre a reconstitué
<a href="https://github.com/NanmiCoder/claude-code-haha">8 diagrammes d'architecture</a>
complets du pipeline : cycle de vie d'une requête, système de permissions, orchestration multi-agents... C'est la meilleure doc technique qui existe sur le fonctionnement interne de Claude Code, et elle ne vient pas d'Anthropic ^^</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-6-patterns-bonnes-pratiques-hooks/claude-code-6-patterns-bonnes-pratiques-hooks-2.png" alt="" loading="lazy" decoding="async">
<p><strong>Architecture globale de Claude Code reconstituée par la communauté</strong></p>
<p>Voilà et toutes ces pratiques, ça repose sur les 25 événements du système de hooks (<code>PreToolUse</code>, <code>PostToolUse</code>, <code>UserPromptSubmit</code>, <code>Stop</code>...) avec 3 types de handlers : <code>command</code> pour les scripts shell, <code>prompt</code> pour une évaluation LLM, et <code>agent</code> pour une vérification multi-étapes.</p>
<p>Après, si l'un de vos scripts plante comme une merde, le hook laissera passer des choses, donc pensez bien à tester chaque retour de script avec un <code>echo '{}' | ./mon-hook.sh &amp;&amp; echo $?</code> avant de déployer.</p>
<p>Et voilà ! Je vous invite à lire
<a href="https://korben.info/claude-code-fuite-code-source-npm-source-maps.html">mon article sur la fuite</a>
pour plus d'infos.</p>