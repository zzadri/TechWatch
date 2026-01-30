---
title: "OGhidra - Dopage à l'IA pour Ghidra en local"
author: "Korben"
date: 2026-01-17T15:52:56.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "intelligence-artificielle/chatbots-llm"
rss_source: Blog
url: https://korben.info/oghidra-dopage-a-lia-pour-ghidra-en-local.html
note: 0
seen: false
---

<p>Les gars de chez LLNL (Lawrence Livermore National Laboratory) sont des bons ! De vrais spécialistes en sécurité informatique qui ont pondu un outil à essayer si vous passez vos journées dans les entrailles des binaires.</p>
<p>Ça s'appelle <strong>
<a href="https://github.com/LLNL/OGhidra">OGhidra</a>
</strong>, et c'est une extension qui fait le pont entre le célèbre framework de reverse engineering Ghidra et la puissance des modèles de langage (LLM).</p>
<p>Comme ça, plutôt que de vous péter les yeux sur des milliers de lignes de code décompilé, vous pouvez simplement &quot;discuter&quot; avec les fonctions ou les strings extraites. Grâce à une intégration avec Ollama, OGhidra permet d'interroger les représentations du binaire en langage naturel pour identifier des vulnérabilités, renommer intelligemment des fonctions ou expliquer des algorithmes complexes. Attention toutefois, comme avec tout LLM, les résultats doivent être validés manuellement (les hallucinations, ça arrive même aux meilleurs !).</p>
<p>Le gros avantage ici, vous l'aurez compris, c'est la <strong>privacy</strong> car tout tourne en local sur votre ordi. L'extension utilise des techniques comme le RAG (Retrieval-Augmented Generation) pour garder le contexte de vos sessions et le CAG (Cache-Augmented Generation) pour optimiser les performances. Prévoyez quand même une machine solide car pour faire tourner des modèles comme gemma3 confortablement, 32 Go de RAM (et une bonne dose de VRAM) ne seront pas de trop.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/oghidra-dopage-a-lia-pour-ghidra-en-local/oghidra-dopage-a-lia-pour-ghidra-en-local-2.png" alt="" loading="lazy" decoding="async">
<p>Pour que ça envahisse vos machines de reverse engineer, il vous faudra Ghidra 11.3 minimum et JDK 17. L'installation se fait ensuite en deux temps : d'abord le plugin <strong>
<a href="https://github.com/LLNL/OGhidra?tab=readme-ov-file">GhidraMCP</a>
</strong> à ajouter dans Ghidra, puis le composant Python à récupérer sur GitHub :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/LLNL/OGhidra.git
</span></span><span class="line"><span class="cl">cd OGhidra
</span></span><span class="line"><span class="cl">pip install -r requirements.txt
</span></span></code></pre><p>Une fois Ollama lancé avec vos modèles préférés, vous allez pouvoir automatiser les tâches les plus reloues. Par exemple grâce aux boutons &quot;Smart Tool&quot; dans l'interface de Ghidra vous allez pouvoir renommer toutes les fonctions d'un coup ou générer un rapport de sécurité (à prendre comme une base de travail, pas comme une vérité absolue, hein ^^).</p>
<p>C'est beau mais ça fait mal quand on pense au temps qu'on a perdu par le passé ! Et si vous kiffez ce genre d'approches, jetez aussi un œil à
<a href="https://korben.info/cutter-une-plateforme-de-reverse-engineering-basee-sur-rizin.html">Cutter</a>
qui propose une intégration optionnelle du décompileur de Ghidra, ou encore à
<a href="https://korben.info/decompai-ia-reverse-engineering-automatique.html">DecompAI</a>
.</p>
<p>Voilà, j'ai trouvé ça intéressant pour booster Ghidra avec une petite dose d'intelligence locale.</p>