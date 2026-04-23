---
title: "Pandoc - Convertir vos documents sans logiciel proprio"
author: "Korben"
date: 2026-02-11T09:23:04.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "tutoriels-guides/tutoriels-avances"
  - "conversion"
  - "Pandoc"
  - "WebAssembly"
rss_source: Blog
url: https://korben.info/pandoc-convertir-documents-web.html
note: 0
seen: false
---

<p>Si vous avez déjà galéré à convertir un fichier .docx en Markdown propre, ou un document LaTeX en HTML sans que la mise en page explose... vous connaissez la douleur. <strong>Pandoc</strong> règle ça depuis des années en ligne de commande, mais pour ceux que le terminal rebute, y'a du nouveau. Le convertisseur universel de John MacFarlane tourne maintenant dans le navigateur, sans rien installer. Même pas un petit npm install ^^.</p>
<p>Pour ceux qui débarquent, Pandoc c'est un outil open source (licence GPL) créé par un prof de philo à Berkeley, qui gère une centaine de formats en entrée et en sortie... du .md au .docx en passant par le LaTeX, l'EPUB, le HTML, le reStructuredText et même les slides reveal.js. Bon, en gros, c'est la pierre de Rosette (non pas de Lyon) de la conversion de docs.</p>
<h2 id="la-version-web-zéro-install">La version web (zéro install)</h2>
<p>Alors pour ça, direction
<a href="https://pandoc.org/app/">pandoc.org/app</a>
. L'interface est basique, vous glissez-déposez votre .docx ou .tex, vous choisissez le format de sortie dans le menu déroulant, et vous cliquez sur Convert. Et c'est terminé.</p>
<p>Et le truc cool c'est que rien ne quitte votre navigateur. Le moteur Pandoc tourne en WebAssembly directement dans l'onglet de votre navigteur, du coup vos fichiers ne transitent par aucun serveur. Vous pouvez vérifier ça dans les DevTools réseau... et après le chargement initial de ~15 Mo, c'est clean. Donc même pour des docs un peu sensibles, y'a pas de souci.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pandoc-convertir-documents-web/pandoc-convertir-documents-web-2.png" alt="" loading="lazy" decoding="async">
<p>Attention, la version web a quand même ses limites. Elle peut générer du PDF grâce à Typst (embarqué en WASM aussi), mais les très gros fichiers vont faire ramer votre navigateur. Après pour le reste, ça fait le taf.</p>
<h2 id="en-ligne-de-commande-pour-les-power-users">En ligne de commande (pour les power users)</h2>
<p>Après si vous avez des gros volumes de fichiers à traiter ou des conversions récurrentes, la CLI reste imbattable. Sur macOS c'est un <code>brew install pandoc</code>, sur Linux un <code>apt install pandoc</code> et sur Windows y'a un .msi sur le site officiel. En deux minutes c'est installé.</p>
<p>La syntaxe ensuite est limpide :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pandoc monfichier.md -o monfichier.docx
</span></span></code></pre><p>Et là, magie, votre fichier .md se transforme en document Word propre avec les titres, les listes, le gras, tout y est. Dans l'autre sens ça marche aussi :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pandoc rapport.docx -o rapport.md
</span></span></code></pre><p>Pratique pour récupérer un vieux rapport.docx et le transformer en Markdown exploitable dans
<a href="https://korben.info/jimmy-convertisseur-notes-markdown-universel.html">Obsidian ou Logseq</a>
.</p>
<h2 id="cas-dusage-concrets">Cas d'usage concrets</h2>
<p>Allez, imaginons que vous ayez 200 fichiers .md dans Obsidian et vous vouliez les envoyer à quelqu'un qui ne jure que par Word ? Un petit convert.sh avec une boucle <code>for f in *.md</code> et c'est plié en 30 secondes.</p>
<p>Et si votre CV est en LaTeX (parce que vous êtes un vrai barbu, ahaha), mais que le recruteur veut un .docx parce que lui c'est pas un vrai barbu (ah le faible ^^), au lieu de copier-coller comme un sauvage, faites un petit <code>pandoc cv.tex -o cv.docx</code> et c'est au propre. Attention quand même, les tableaux LaTeX complexes peuvent casser à la conversion.</p>
<p>Ou encors si vous rédigez en Markdown (parce que c'est rapide et surtout versionnable avec git) et que vous exportez ça ensuite en PDF ou HTML selon le destinataire, avec l'option <code>--css style.css</code> ou un template perso en .yaml, le rendu sera propre.</p>
<p>Bref, vous l'aurez compris, Pandoc c'est flexible.</p>
<h2 id="web-vs-cli-on-choisit-quoi-">Web vs CLI, on choisit quoi ?</h2>
<p>La version web c'est donc parfait pour les conversions ponctuelles. Vous avez UN fichier .odt ou .rst à convertir, pas envie d'ouvrir un terminal, hop vous allez sur
<a href="https://pandoc.org/app/">pandoc.org/app</a>
et c'est réglé en 10 secondes.</p>
<p>La CLI, elle, assurera grave dès qu'on parlera d'automatisation. Scripts bash, intégration dans des pipelines CI/CD, conversions avec des templates perso, filtres Lua... Là c'est un autre monde. D'ailleurs, pas mal d'outils comme
<a href="https://korben.info/markitdown-convertisseur-fichiers-markdown.html">MarkItDown</a>
ou
<a href="https://korben.info/convertx-convertisseur-fichiers-self-hosted-docker.html">ConvertX</a>
utilisent Pandoc en backend.</p>
<p>Voilà, comme ça tout le monde y trouve son compte et Pandoc peut enfin régner sur le monde !!!</p>