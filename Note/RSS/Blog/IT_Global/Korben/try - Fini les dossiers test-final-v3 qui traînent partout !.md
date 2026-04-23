---
title: "try - Fini les dossiers test-final-v3 qui traînent partout !"
author: "Korben"
date: 2026-03-09T10:28:40.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "application de productivité"
  - "développement Ruby"
  - "outil développeur"
rss_source: Blog
url: https://korben.info/try-cli-organiser-experimentations-dev.html
note: 0
seen: false
---

<p>Vous avez combien de dossiers <code>test</code> sur votre machine ? Dix ? Cinquante ? Deux cents ? Tobi Lütke, le mec qui a cofondé Shopify, avait le même problème... Alors il a pondu
<a href="https://github.com/tobi/try">try</a>
, un petit script Ruby qui donne un vrai foyer chaleureux à vos expérimentations de dev déjanté.</p>
<p>Le principe est hyper simple. Vous tapez <code>try redis</code> dans votre terminal, et magie magie, soit ça vous envoie direct dans votre dossier d'expérimentation Redis existant, soit ça vous propose d'en créer un nouveau avec la date du jour en préfixe, genre <code>2025-08-17-redis-experiment</code>. En fait c'est con, mais rien que le préfixe de date, ça change tout... car 3 semaines plus tard, quand vous cherchez ce bout de code pondu à 2h du mat en rentrant de soirée, hé bien vous le retrouvez !</p>
<p>La recherche fuzzy fait le boulot, comme ça par exemple vous tapez <code>pgres</code>, ça matche <code>postgres-local</code>. Vous tapez <code>connpool</code>, ça retrouve <code>connection-pool</code>. Et ce sont les résultats les plus récents qui remontent en premier, parce que bon, ce que vous avez touché hier est souvent plus pertinent que le truc d'il y a 6 mois. Et y'a même un petit score de pertinence affiché à côté de chaque résultat !</p>
<p>Côté installation, un <code>gem install try-cli</code> suivi d'un <code>eval &quot;$(try init)&quot;</code> dans votre <code>.zshrc</code>, et c'est terminé. Ça marche aussi avec Fish et via Homebrew pour ceux qui préfèrent. D'ailleurs, le cœur du truc tient dans un seul fichier Ruby, par contre, faut Ruby 3.0 minimum (le Ruby livré avec macOS est trop vieux, donc un petit <code>brew install ruby</code> avant si besoin).</p>
<img src="https://korben.info/try-cli-organiser-experimentations-dev/try-cli-organiser-experimentations-dev-1.gif" alt="" loading="lazy" decoding="async">
<p>Y'a aussi quelques bonus plutôt pas mal. Par exemple la commande <code>try .</code> (si vous êtes dans un repo Git) crée un worktree du repo courant dans votre dossier d'expérimentations, ce qui est super pratique pour tester un truc sans polluer votre branche principale. Et <code>try clone URL_GITHUB</code> clone un repo direct dans un dossier daté, genre <code>2025-08-17-nom-du-repo</code>. Si vous aimez les
<a href="https://korben.info/http-breakout-proxy-retour-outils-jetables.html">outils jetables bien rangés</a>
, c'est exactement le délire.</p>
<p>Bon, vous pourriez faire un alias bash à la place, mais finalement la recherche fuzzy et le classement par date, c'est quand même autre chose qu'un bête <code>mkdir</code>. Tous vos dossiers vivent dans <code>~/src/tries</code> par défaut (changeable via <code>TRY_PATH</code>), avec une petite interface en mode texte qui affiche le temps écoulé depuis votre dernier passage. Le README dit que c'est pensé pour les cerveaux qui papillonnent... et franchement, si vous êtes comme moi, du genre à avoir 15 projets en cours, c'est pile le délire qui va vous sauver !! Si vous passez votre vie dans le
<a href="https://korben.info/decouvrez-cli-gpt.html">terminal</a>
, c'est un de ces projets qu'on installe et qu'on n'oublie plus.</p>
<p>Attention quand même, le projet est encore jeune et quelques bugs trainent côté Homebrew et avec Ruby 4.0.</p>
<p>Amusez-vous bien !</p>