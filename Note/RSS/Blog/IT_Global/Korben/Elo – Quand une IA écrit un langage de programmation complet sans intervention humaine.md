---
title: "Elo – Quand une IA écrit un langage de programmation complet sans intervention humaine"
author: "Korben"
date: 2026-01-11T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/langages-programmation"
  - "intelligence-artificielle/automatisation-ia"
  - "intelligence-artificielle/chatbots-llm"
  - "Claude Code"
  - "compilation"
  - "développement"
  - "langage de programmation"
  - "open source"
rss_source: Blog
url: https://korben.info/elo-langage-ia-claude-code.html
note: 0
seen: false
---

<p>Vous connaissez probablement
<a href="https://korben.info/llm-decompilation-claude-code-hack-intelligence-artificielle.html">les prouesses de Claude Code pour décompiler du code</a>
, ou encore
<a href="https://korben.info/claude-engineer-ia-creation-outils-automatisation.html">son utilisation pour automatiser la création d'outils</a>
, mais là, on a passé un cap.</p>
<p>Bernard Lambeau, un développeur belge avec plus de 25 ans d'expérience et un doctorat en informatique, a décidé de pousser le concept jusqu'au bout à savoi<strong>r utiliser Claude Code non pas pour écrire quelques scripts, mais pour générer un langage de programmation complet</strong>.</p>
<p>Carrément ! Il est chaud Bernard, car quand je dis complet, je parle d'un compilateur entier avec analyseur lexical, un parseur, un système de typage, des backends multiples...etc. Voilà, comme ça, en full pair-programming avec une IA.</p>
<p>Ça s'appelle <strong>
<a href="https://elo-lang.org/">Elo</a>
</strong> et l'idée, c'est de proposer un langage tellement sécurisé by design qu'on peut le confier à des non-développeurs… ou à des IA. Pas de variables mutables, pas d'effets de bord, pas de références qui traînent dans tous les sens. Bref, un langage où il est quasi impossible de faire une bêtise, même en essayant très fort.</p>
<p>Alors pourquoi créer un énième langage alors qu'on en a déjà des centaines ?</p>
<p>Hé bien le truc, c'est que la plupart des langages existants partent du principe que vous savez ce que vous faites. JavaScript, Python, Ruby… Ils vous font confiance. Trop, parfois.</p>
<p>Elo, lui, adopte l'approche inverse... le &quot;<strong>zero-trust</strong>&quot;. Le langage ne fait confiance à personne, ni au développeur, ni à l'IA qui pourrait l'utiliser. Ainsi, chaque expression est pure, chaque fonction est déterministe, et le compilateur vérifie tout avant d'exécuter quoi que ce soit.</p>
<p>Et surtout Elo est un langage d'expressions portables, ce qui veut dire que vous écrivez votre logique une fois, et vous pouvez la compiler vers JavaScript, Ruby ou même du SQL PostgreSQL natif. Oui, oui, le même code peut tourner dans votre navigateur, sur votre serveur Ruby, ou directement dans votre base de données. Et là, y'a de quoi faire des trucs sympas pour peu qu'on ait besoin de partager de la logique métier entre différents environnements.</p>
<p>Le typage est volontairement minimaliste mais costaud et se compose de 10 types de base : Int, Float, Bool, String, DateTime, Duration, Tuple, List, Null et Function. Pas de classes, pas d'héritage, pas d'objets au sens classique mais juste des valeurs et des fonctions, ce qui peut paraître limité dit comme ça, mais c'est justement cette contrainte qui rend le langage sûr.</p>
<p>Moins de features, c'est moins de façons de se planter !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/elo-langage-ia-claude-code/elo-langage-ia-claude-code-2.png" alt="" loading="lazy" decoding="async">
<p>L'opérateur pipe <code>|&gt;</code> est le cœur du langage car au lieu d'imbriquer des appels de fonctions comme des poupées russes, vous chaînez les transformations de gauche à droite. Par exemple, pour récupérer tous les clients actifs et compter combien il y en a, vous écrivez quelque chose comme <code>customers |&gt; filter(active: true) |&gt; size</code>. C'est lisible, c'est fluide, et même quelqu'un qui n'a jamais codé comprend ce qui se passe.</p>
<p>Et il y a aussi l'opérateur alternative <code>|</code>. Comme ça, si une expression peut retourner null, vous pouvez prévoir un fallback avec ce simple pipe. Genre <code>user.nickname | user.firstname | &quot;Anonymous&quot;</code>. Ça essaie dans l'ordre et ça prend la première valeur non-nulle.</p>
<p>Comme ça, fini les cascades de if/else pour gérer les cas où une donnée manque ! Youpi !</p>
<p>Voilà pour le langage...</p>
<p>Maintenant parlons un peu du bonhomme car Bernard Lambeau n'est pas un inconnu dans le monde du développement. Il est derrière <strong>Bmg</strong> (une implémentation de l'algèbre relationnelle), <strong>Finitio</strong> (un langage de schémas de données), <strong>Webspicy</strong> (pour tester des APIs), et <strong>Klaro Cards</strong> (une app no-code). Tout cet écosystème partageait déjà une certaine philosophie, et Elo vient unifier le tout. Son langage est d'ailleurs utilisé en production dans Klaro Cards pour exprimer des règles métier que les utilisateurs non-techniques peuvent modifier.</p>
<p>Ce qui m'a intéressé dans toute cette histoire, c'est surtout la méthode de développement de Bernard qui a travaillé en pair-programming avec Claude Code pendant des semaines, voire des mois. L'IA générait du code, et lui relisait, corrigeait, guidait, et l'IA apprenait de ces corrections pour les itérations suivantes. Sur l'ensemble du projet, chaque ligne de code, chaque test, chaque doc a été écrit par Claude et croyez le ou non, le code est clean car Bernard est un pro !</p>
<p>D'ailleurs, il a enregistré une démo de 30 minutes
<a href="https://www.loom.com/share/ef65c6ebfc35491783ff0a6067447dd4">où il montre le processus en live</a>
.</p>
<p>En regardant cette démo, on découvre une vraie méthodologie de travail avec l'IA car il n'a pas juste balancé des prompts au hasard en espérant que ça marche. Au contraire, il a mis en place tout un système pour que la collaboration soit efficace et sécurisée.</p>
<p>Premier truc : le &quot;<strong>safe setup</strong>&quot;. Bernard a configuré un environnement Docker sandboxé dans un dossier <code>.claude/safe-setup</code> afin de laisser Claude Code exécuter du code dans un conteneur Alpine isolé, sans risquer de faire des bêtises sur la machine hôte. En entreprise, c'est exactement le genre de garde-fou qu'on veut quand on laisse une IA bidouiller du code. Le conteneur a ainsi accès aux fichiers du projet, mais pas au reste du système.</p>
<p>Ensuite, il y a la documentation projet via un fichier CLAUDE.md à la racine. Ce fichier décrit l'architecture du langage avec le parser, l'AST, le système de typage, les différents backends, comme ça, quand Claude démarre une session, il lit ce fichier et comprend la structure du projet.</p>
<p>La gestion des tâches est aussi bien pensée puisqu'il utilise un système de dossiers façon Kanban : <code>to-do</code>, <code>hold-on</code>, <code>done</code>, et <code>analyze</code>. Chaque tâche est un fichier Markdown qui ressemble à une user story.</p>
<p>Ainsi, quand il veut ajouter une feature, il crée un fichier dans <code>to-do</code> avec la description de ce qu'il veut. Claude lit le fichier, implémente, et Bernard déplace le fichier dans <code>done</code> une fois que c'est validé. Le dossier <code>analyze</code> sert pour les trucs à creuser plus tard, et <code>hold-on</code> pour ce qui attend des décisions.</p>
<p>Ce qui est bien trouvé aussi, c'est qu'il utilise trois modes d'interaction selon les situations. Le mode &quot;<strong>accept-it</strong>&quot; pour les trucs simples où Claude propose et Bernard dispose. Le &quot;<strong>plan mode</strong>&quot; quand la tâche est complexe avec Claude qui pose des questions de design avant d'écrire du code. Et le mode <strong>autonome</strong> avec <code>--dangerously-skip-permissions</code> quand il a parfaitement confiance pour une série de modifications.</p>
<p>Bernard a aussi créé plusieurs personas spécialisés (des agents) que Claude peut invoquer. Un agent &quot;security&quot; qui analyse le code du point de vue sécurité. Un agent &quot;DDD&quot; (Domain-Driven Design) qui vérifie la cohérence du vocabulaire métier. Un agent &quot;skeptic&quot; qui cherche les cas limites et les bugs potentiels. Et un agent &quot;Einstein&quot; qui détecte quand le code devient trop complexe et suggère des simplifications.</p>
<p>En gros, 4 cerveaux virtuels qui relisent chaque modification.</p>
<p>Et là où ça devient vraiment ouf, c'est que Elo se teste lui-même. Les tests d'acceptance sont écrits en Elo, avec une syntaxe d'assertions qui se compile vers JavaScript, Ruby et SQL. Comme ça quand Bernard ajoute une feature, il écrit d'abord le test en Elo, puis Claude implémente jusqu'à ce que le test passe. Le langage valide sa propre implémentation.</p>
<p>Comme je vous l'avais dit, c'est propre !</p>
<p>Bernard n'a fait que valider et refuser et ne retouche jamais le code lui-même. C'est Claude qui fait tout le reste et ça c'est un sacré changement dans la façon de développer.</p>
<p>Il évoque aussi l'idée que quand on délègue une compétence à quelqu'un (ou quelque chose) qui la maîtrise, on peut se concentrer sur le reste. Comme ça, Bernard ne s'occupe donc plus d'écrire du code mais s'occupe plutôt de définir ce que le code doit faire, de valider les résultats, et de guider l'architecture.</p>
<p>C'est vraiment le métier de développeur nouvelle génération et c'est très inspirant si vous cherchez votre place de dev dans ce nouveau monde.</p>
<p>En tout cas,
<a href="https://korben.info/opcode-gui-claude-code-asterisk.html">même si ce n'est pas la première fois qu'on voit Claude Code produire des résultats impressionnants</a>
là c'est carrément autre chose.</p>
<p>Maintenant si vous voulez tester, l'installation est simple. Un petit</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">`npm install -g @enspirit/elo`
</span></span></code></pre><p>Et vous aurez ensuite accès à deux outils :</p>
<ul>
<li><code>elo</code> pour évaluer des expressions à la volée, et</li>
<li><code>eloc</code> pour compiler vers la cible de votre choix.</li>
</ul>
<p>Et si vous voulez du JavaScript ?</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">eloc -t js votre_fichier.elo.
</span></span></code></pre><p>Du Ruby ?</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">eloc -t ruby.
</span></span></code></pre><p>Du SQL ?</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">eloc -t sql.
</span></span></code></pre><p>Le site officiel propose également
<a href="https://elo-lang.org/reference/#get-started">un tutoriel interactif</a>
plutôt bien fichu pour découvrir la syntaxe. On commence par les bases (les types, les opérateurs), on passe aux fonctions, aux gardes, et on finit par les trucs plus avancés comme les closures et les comparaisons structurelles. En une heure ou deux, vous avez fait le tour.</p>
<p>Alors bien sûr, Elo n'est pas fait pour remplacer votre langage préféré car ce n'est pas un langage généraliste. Vous n'allez pas écrire une app mobile ou un jeu vidéo avec... Par contre, pour exprimer des règles métier, des validations, des transformations de données… C'est pile poil ce qu'il faut.</p>
<p>Peut-être qu'un jour on verra une équipe où les product managers écrivent directement les règles de pricing ou d'éligibilité
<a href="https://elo-lang.org/">en Elo</a>
, (j'ai le droit de rêver) et où ce code est automatiquement validé par le compilateur avant d'être déployé.</p>
<p>Plus de traduction approximative entre le métier et les devs, plus de bugs parce que quelqu'un a mal interprété une spec.</p>
<p>
<a href="https://github.com/enspirit/elo">Le dépôt GitHub est ouvert</a>
, la documentation est dispo, et le langage est sous licence MIT donc vous avez de quoi explorer, tester, et pourquoi pas contribuer si le cœur vous en dit.</p>
<p>Voilà, avec Claude Code (ou d'autres comme Gemini CLI, Codex CLI...etc) on n'est clairement plus sur des outils qui complètent du code ou qui génèrent des snippets. On est carrément sur un système IA capable de créer des outils complets et des langages entiers, avec son humain préféré qui joue le rôle de chef d'orchestre.</p>
<p>Steve Klabnik a d'ailleurs fait quelque chose de similaire avec son langage Rue, lui aussi développé avec Claude, si vous voulez jeter un œil !</p>
<p>Voilà les amis ! La tendance est claire j'crois... les développeurs expérimentés commencent à utiliser l'IA comme un multiplicateur de force, et pas comme un remplaçant et je pense vraiment que vous devriez vous y mettre aussi pour ne pas vous retrouver à la ramasse dans quelque années...</p>
<p>Amusez-vous bien et un grand merci à Marc d'avoir attiré mon attention là dessus !</p>