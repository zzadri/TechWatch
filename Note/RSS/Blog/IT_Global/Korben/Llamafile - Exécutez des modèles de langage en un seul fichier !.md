---
title: "Llamafile - Exécutez des modèles de langage en un seul fichier !"
author: "Korben"
date: 2026-03-19T14:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "exécutable multiplateforme"
  - "Llamafile"
  - "modèles de langage"
rss_source: Blog
url: https://korben.info/llamafile-executez-modeles-langage-fichier.html
note: 0
seen: false
---

<p><strong>
<a href="https://github.com/mozilla-ai/llamafile">llamafile</a>
</strong> est un projet complètement barré qui va vous permettre de transformer des modèles de langage en exécutables. Derrière se cache en fait la fusion de deux projets bien badass :
<a href="https://github.com/ggerganov/llama.cpp">llama.cpp</a>
, un framework open source de chatbot IA, et
<a href="https://github.com/jart/cosmopolitan">Cosmopolitan Libc</a>
, une libc portable pour compiler des programmes C multiplateformes. En combinant astucieusement ces deux technos, les petits gars de Mozilla ont réussi à pondre un outil qui transforme les poids de modèles de langage naturel en binaires exécutables.</p>
<p>Imaginez un peu, vous avez un modèle de langage qui pèse dans les 4 gigas, dans un format .gguf (un format couramment utilisé pour les poids de LLM). Et bien avec llamafile, vous pouvez le transformer en un exécutable standalone qui fonctionnera directement sur le système sur lequel il est sans avoir besoin d'installer quoi que ce soit. Ça va permettre de <strong>démocratiser l'utilisation et la diffusion des LLM</strong>.</p>
<p>Et niveau portabilité, c'est le feu puisque ça tourne sur six OS, de Windows à FreeBSD en passant par macOS. Les devs ont bien bossé pour que ça passe partout, en résolvant des trucs bien crados comme le support des GPU et de <code>dlopen()</code> dans Cosmopolitan et croyez-moi (enfin, croyez-les) ça n'a pas été une mince affaire !</p>
<p>Niveau perf aussi c'est du brutal ! Sur Linux llamafile utilise <code>pledge()</code> et SECCOMP pour sandboxer le bousin et empêcher les accès fichiers non désirés et avec les derniers patchs de
<a href="https://korben.info/justine-tunney-booste-performances-llama-cpp-nouveaux-kernels-algebre-lineaire.html">Justine Tunney</a>
, la perf CPU pour l'inférence en local a pris un boost de malade du genre 10 fois plus rapide qu'avant. Même sur un Raspberry Pi on peut faire tourner des petits modèles à une vitesse honnête.</p>
<h2 id="mise-à-jour--llamafile-010">Mise à jour : llamafile 0.10</h2>
<p>Bonne nouvelle, le projet est loin d'être mort puisque <strong>la version 0.10</strong> vient de sortir (mars 2026) et elle apporte pas mal de changements. Déjà, le projet a migré de Mozilla Ocho vers
<a href="https://github.com/mozilla-ai/llamafile">Mozilla.ai</a>
, ce qui montre que Mozilla prend le truc au sérieux côté IA.</p>
<p>Le gros morceau de cette release, c'est un <strong>tout nouveau build system</strong>. Fini le bazar monolithique, maintenant llama.cpp, whisper.cpp et Stable Diffusion sont intégrés comme des sous-modules Git. L'avantage c'est que ça permet de suivre beaucoup plus facilement les dernières versions de llama.cpp et donc de supporter les modèles les plus récents dès leur sortie.</p>
<p>Côté utilisation, on a maintenant <strong>trois modes</strong> bien distincts :</p>
<ul>
<li><strong>Mode TUI</strong> (Terminal User Interface) : vous chattez directement dans votre terminal avec le modèle, avec même un mode &quot;think&quot; pour le raisonnement étendu</li>
<li><strong>Mode CLI</strong> : pour poser une question rapide en one-shot, genre <code>llamafile &quot;c'est quoi un llamafile ?&quot;</code> et hop, la réponse arrive direct</li>
<li><strong>Mode serveur</strong> : avec le flag <code>--server</code>, ça lance le serveur llama.cpp classique pour exposer une API compatible OpenAI</li>
</ul>
<p>Autre truc cool, le support <strong>multimodal</strong> est là avec le nouvel argument <code>--image</code>. Vous pouvez balancer une image au modèle et il l'analyse. Ça marche avec des modèles comme Qwen3-VL, LLaVA 1.6 ou Ministral 3.</p>
<p>Côté GPU, <strong>Metal fonctionne nativement sur macOS</strong> (ARM64) sans bidouille, et le <strong>support CUDA est restauré</strong> sur Linux. Par contre, le GPU sur Windows n'est pas encore de la partie, et le sandboxing via pledge()/SECCOMP a été temporairement retiré dans cette version.</p>
<p>Bref, si vous aviez testé llamafile il y a un moment et que vous aviez trouvé ça un peu limité, c'est peut-être le moment de
<a href="https://github.com/mozilla-ai/llamafile/releases/tag/0.10.0">retélécharger la bête</a>
et de voir ce que ça donne avec les modèles de 2026. C'est toujours aussi simple : un fichier, on le rend exécutable, on le lance, et c'est parti.</p>
<p>Alors on dit merci qui ?</p>
<p>Merci Mozilla ! 🙏🦊</p>