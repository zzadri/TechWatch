---
title: "Mysti - Quand Claude et ChatGPT débattent de votre code dans VS Code"
author: "Korben"
date: 2026-02-24T09:38:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "intelligence-artificielle/chatbots-llm"
rss_source: Blog
url: https://korben.info/mysti-extension-vs-code-brainstorming-ia.html
note: 0
seen: false
---

<p>Si vous codez un peu avec des assistants IA, vous avez sûrement le même petit souci que moi chaque matin après mon premier café : <strong>Claude ou ChatGPT ?</strong> Lequel est le plus chaud aujourd'hui pour ce refactoring complexe ?</p>
<p>Hé bien j'ai trouvé un truc qui va mettre tout le monde d'accord.</p>
<p>Ça s'appelle <strong>
<a href="https://github.com/DeepMyst/Mysti">Mysti</a>
</strong> et c'est une extension VS Code qui part d'un principe simple mais génial : Pourquoi se limiter à un seul cerveau quand on peut en avoir deux qui bossent ensemble ?</p>
<p>L'extension intègre ce qu'ils appellent le <strong>&quot;Brainstorm Mode&quot;</strong> où concrètement, vous sélectionnez deux modèles (par exemple Claude via <code>claude-code</code> et OpenAI via <code>openai-codex</code>) et vous les lancez sur votre problème.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mysti-extension-vs-code-brainstorming-ia/mysti-extension-vs-code-brainstorming-ia-2.png" alt="" loading="lazy" decoding="async">
<p><em>On choisit son équipe de choc</em></p>
<p>Si vous activez le &quot;Full Mode&quot;, c'est assez marrant à regarder puisque les deux IA vont discuter entre elles, débattre de la meilleure approche, critiquer les propositions de l'autre et finir par pondre une solution qui combine le meilleur des deux mondes. C'est un peu comme avoir deux seniors devs en pair programming derrière votre épaule (sans l'odeur de café froid et de dessous de bas ^^).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mysti-extension-vs-code-brainstorming-ia/mysti-extension-vs-code-brainstorming-ia-3.png" alt="" loading="lazy" decoding="async">
<p><em>Ça discute sec entre les agents</em></p>
<p>Au-delà du brainstorming, Mysti propose aussi un système de <strong>Personas</strong> (16 au total). Vous pouvez alors demander à votre &quot;équipe&quot; IA d'adopter un rôle spécifique comme &quot;Architecte&quot; pour penser la structure globale ou &quot;Security-Minded&quot; pour auditer votre code. D'ailleurs, cette approche agentique rappelle un peu ce qu'on a vu émerger dans des outils comme
<a href="https://korben.info/kilo-code-extension-vs-code-assistant-ia-open-source.html">Kilo Code</a>
.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mysti-extension-vs-code-brainstorming-ia/mysti-extension-vs-code-brainstorming-ia-4.png" alt="" loading="lazy" decoding="async">
<p><em>L'IA propose un plan d'action avant de coder</em></p>
<p>Techniquement, attention car l'extension ne fait &quot;que&quot; piloter les outils CLI installés sur votre machine. Il faudra donc avoir installé et authentifié les CLI correspondants (<code>@anthropic-ai/claude-code</code>, <code>@google/gemini-cli</code>, etc.) pour que ça fonctionne. L'installation de l'extension elle-même passe par le Marketplace VS Code :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">ext install DeepMyst.mysti
</span></span></code></pre>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mysti-extension-vs-code-brainstorming-ia/mysti-extension-vs-code-brainstorming-ia-5.png" alt="" loading="lazy" decoding="async">
<p>Perso, je trouve ça vraiment bien pour les tâches d'architecture, là où une seule IA a souvent tendance à foncer tête baissée. Avoir un &quot;second avis&quot; automatique, ça évite pas mal d'erreurs bêtes. Après si je devais lui trouver un défaut c'est que comme ça utilise vos propres clés API via les CLI, une session de débat intense peut vite consommer quelques tokens.</p>
<p>Je sais, vous vous en foutez parce que vous êtes blindé mais c'est à utiliser avec modération !</p>