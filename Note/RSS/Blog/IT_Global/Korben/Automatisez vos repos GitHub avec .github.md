---
title: "Automatisez vos repos GitHub avec .github"
author: "Korben"
date: 2026-02-22T09:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "tutoriels-guides/tutoriels-avances"
  - "dossier de conf"
  - "GitHub"
rss_source: Blog
url: https://korben.info/automatisez-repos-github-dot-github.html
note: 0
seen: false
---

<p>Le dossier <code>.github</code> est un petit répertoire magique que vous avez sûrement déjà croisé à la racine de vos dépôts préférés. Il est là, non pas pour faire joli ou pour planquer vos secrets de fabrication (pour ça, y'a les secrets GitHub, hein), mais plutôt pour centraliser plusieurs fichiers de configuration reconnus nativement par la plateforme.</p>
<p>C'est un peu le centre de commande de votre repo. Et le truc qui est fort, c'est que si vous avez une organisation avec 50 projets, vous pouvez même créer un dépôt public spécial nommé <code>.github</code> qui servira à fournir des fichiers de santé communautaire et des templates par défaut pour tous les dépôts de votre organisation qui n'ont pas déjà leurs propres fichiers équivalents.</p>
<p>Et comme ça, dès qu'un dépôt a quoi que ce soit dans son propre <code>.github/ISSUE_TEMPLATE/</code>, il ne prendra plus les templates par défaut de l'orga.</p>
<p>Pratique pour les grosses flemmasses comme vous quoi !</p>
<h2 id="les-templates-dissues-et-de-pr-pour-structurer-les-échanges">Les templates d'Issues et de PR pour structurer les échanges</h2>
<p>On a tous reçu une issue qui dit juste &quot;ça marche pas&quot;. C'est relou, ça fait perdre du temps et on a envie de répondre par un gif de chat qui boude.</p>
<p>Alors pour éviter ça, créez un dossier <code>.github/ISSUE_TEMPLATE/</code>. Vous pouvez y coller des fichiers Markdown ou YAML pour encourager les gens à donner les infos de base (version de l'OS, étapes pour reproduire, etc.). Et faites pareil pour les Pull Requests avec un fichier <code>PULL_REQUEST_TEMPLATE.md</code> (à la racine, dans <code>docs/</code>, ou dans <code>.github/</code>, selon votre tambouille).</p>
<p>En gros, ça vous permet de guider vos contributeurs pour qu'ils ne fassent pas n'importe quoi.</p>
<h2 id="github-actions-pour-détecter-les-régressions">GitHub Actions pour détecter les régressions</h2>
<p>C'est LE grand classique !</p>
<p>Dans <code>.github/workflows/</code>, vous balancez vos fichiers YAML pour automatiser vos tests, votre linting ou vos déploiements. Bien sûr, pour vraiment ne pas &quot;casser la prod&quot;, il faudra coupler ça à des règles de protection de branche (status checks requis) pour bloquer les merges si les tests échouent.</p>
<p>D'ailleurs, si vous voulez tester vos actions sans attendre la file d'attente des runners GitHub, je vous avais parlé de
<a href="https://korben.info/wrkflw-testez-vos-github-actions-local.html">Wrkflw pour tester ça en local</a>
. C'est un outil tiers bien pratique pour valider vos workflows sur votre machine.</p>
<h2 id="les-fichiers-de-santé-communautaire">Les fichiers de &quot;Santé Communautaire&quot;</h2>
<p>Si vous voulez que votre projet open source ressemble à autre chose qu'un champ de bataille au petit matin, il faut poser des règles.</p>
<p>GitHub reconnaît automatiquement des fichiers comme <code>CODE_OF_CONDUCT.md</code>, <code>CONTRIBUTING.md</code> ou même <code>FUNDING.yml</code> pour gratter quelques pièces pour votre café ;). Ce sont des fichiers qui aident à dire aux gens comment se comporter et comment vous aider efficacement sans avoir à surveiller votre voisin.</p>
<h2 id="guider-copilot-avec-des-instructions-sur-mesure">Guider Copilot avec des instructions sur mesure</h2>
<p>C'est la petite nouveauté qui vous permet d'ajouter un fichier <code>.github/copilot-instructions.md</code> avec à l'intérieur, une liste de vos standards de code, vos libs préférées ou vos conventions de nommage.</p>
<p>Comme ça, hop, Copilot tiendra compte de ces instructions pour ses suggestions (même s'il garde parfois son petit caractère, hihi). Et vous pouvez même aller plus loin avec des fichiers <code>NAME.instructions.md</code> dans <code>.github/instructions/</code> qui ciblent des dossiers specifiques via des patterns glob... à condition de mettre un frontmatter <code>applyTo:</code> au début, sinon Copilot les ignorera gentiment...</p>
<p>C'est parfait pour garder un code propre.</p>
<h2 id="codeowners-et-dependabot">CODEOWNERS et Dependabot</h2>
<p>Enfin, pour les projets qui commencent à prendre de l'ampleur, le fichier <code>CODEOWNERS</code> (placé dans <code>.github/</code>, ou à la racine, ou dans <code>docs/</code>... GitHub prend celui de <code>.github/</code> en premier s'il y en a plusieurs) permet de définir qui est responsable de quelle partie du code. Dès qu'une PR touche à un fichier sensible, GitHub demande automatiquement la review aux bonnes personnes.</p>
<p>Et n'oubliez pas <code>.github/dependabot.yml</code> pour que l'outil vous ouvre des pull requests dès qu'une dépendance est à la bourre.</p>
<p>On automatise le bien relou pour ne garder que du criss de fun !</p>
<p>Voilà les amis, si vous aimez bidouiller vos dépôts pour qu'ils tournent tout seuls ou presque et garder un semblant d'organisation, ce dossier .github sera votre meilleur poto !</p>
<p>
<a href="https://cassidoo.co/post/dot-github/">Source</a>
</p>