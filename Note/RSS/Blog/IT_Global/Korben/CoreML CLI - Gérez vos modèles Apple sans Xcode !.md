---
title: "CoreML CLI - Gérez vos modèles Apple sans Xcode !"
author: "Korben"
date: 2026-01-24T11:46:45.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "linux-open-source/terminal-shell"
  - "Apple"
  - "commande terminal Mac"
  - "intelligence artificielle"
  - "ipados"
  - "LLM"
rss_source: Blog
url: https://korben.info/coreml-cli-gestion-apple-modele-sans-xcode.html
note: 0
seen: false
---

<p>Si vous bidouillez un peu avec des modèles CoreML sur votre Mac Silicon, vous savez que c'est vite la croix et la misère comme je dis souvent... Car dès qu'il s'agit de tester un truc rapide, faut ouvrir Xcode, pisser du Swift, ou se battre avec des scripts Python... Bref, l'usine à gaz juste pour vérifier une prédiction vite fait.</p>
<p>Hé bien bonne nouvelle les amis, un petit outil en ligne de commande vient de sortir pour nous éviter de trop galérer.</p>
<p>Ça s'appelle <strong>coreml-cli</strong> et comme son nom l'indique, c'est une interface pour inspecter et lancer vos modèles depuis le terminal. L'objectif c'est de pouvoir manipuler vos fichiers <code>.mlmodel</code> sans jamais avoir besoin de lancer l'IDE d'Apple.</p>
<p>Si vous êtes chaud bouillant, ça s'installe hyper facilement via Homebrew :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew tap schappim/coreml-cli
</span></span><span class="line"><span class="cl">brew install coreml-cli
</span></span></code></pre><p>Et une fois que c'est là, vous pouvez TOUT faire. Genre vous voulez voir ce qu'il y a dans un modèle ? Hop, un petit <code>coreml inspect MobileNetV2.mlmodel</code> et vous avez toute la structure, les entrées et les sorties qui s'affichent.</p>
<p>Et pour lancer des prédictions, c'est également très simple plus simple. Par exemple, avec le modèle MobileNet qui détecte les objets présents dans une image, vous lui donnez une image, et avec l'option <code>--json</code>, il vous sort le résultat proprement.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">coreml predict MobileNetV2.mlmodel --input photo.jpg --json
</span></span></code></pre><p>Et pour ceux qui veulent automatiser des traitements, le mode &quot;batch&quot; permet de traiter tout un dossier d'images d'un coup. C'est quand même plus rapide que de le faire à la main un par un, comme le ferait un ingé de Perpignan nourri aux graines de chia.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/coreml-cli-gestion-apple-modele-sans-xcode/coreml-cli-gestion-apple-modele-sans-xcode-2.png" alt="" loading="lazy" decoding="async">
<p>Le développeur a même intégré un outil de benchmark pour mesurer la latence. Ça vous permet de lancer des tests sur le CPU, le GPU ou le fameux Neural Engine d'Apple pour comparer les perfs. C'est le top pour optimiser vos apps avant de les déployer.</p>
<p>Du coup, si vous bossez avec de l'IA locale sur Mac, un peu comme ce qu'on a déjà testé par le passé avec
<a href="https://korben.info/mocolamma-ollama-gestion-iphone-ia-locale.html">MocoLlamma</a>
ou
<a href="https://korben.info/mac-studio-rdma-thunderbolt-5-cluster-ia.html">sur de gros clusters Mac Studio</a>
comme ce furieux, ce petit binaire risque de vite devenir indispensable dans vos scripts CI/CD.</p>
<p>Amusez-vous bien !</p>
<p>
<a href="https://github.com/schappim/coreml-cli">Source</a>
</p>