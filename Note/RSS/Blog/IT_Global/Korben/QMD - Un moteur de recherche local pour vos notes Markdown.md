---
title: "QMD - Un moteur de recherche local pour vos notes Markdown"
author: "Korben"
date: 2026-03-23T09:52:30.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/chatbots-llm"
  - "linux-open-source/terminal-shell"
  - "tutoriels-guides"
  - "commande terminal"
  - "intelligence artificielle"
  - "Markdown"
  - "moteur de recherche"
rss_source: Blog
url: https://korben.info/qmd-recherche-markdown-locale-ia.html
note: 0
seen: false
---

<p>Si vous êtes comme votre blogueur préféré (hi hi) et que vous avez des tonnes de fichiers markdown qui traînent dans des dossiers obscurs depuis des années, voici l'outil parfait pour rendre tout ceci à nouveau utilisable dans la vraie vie.</p>
<p>En tout cas, c'est plus pratique qu'un grep !</p>
<p>Ça s'appelle <strong>QMD</strong> (Quick Markdown Search) et c'est un outil en ligne de commande dispo sur GitHub qui va indexer tout votre bazar de notes pour les rendre consultables rapidement. QMD combine la recherche plein texte classique (BM25) avec de la recherche vectorielle sémantique et du re-ranking via LLM, ce qui veut dire que c'est ultra puissant. On est un peu sur le même principe qu'un RAG en fait puisque l'IA locale est utilisée pour comprendre le sens de votre requête et pas juste chercher des chaînes de caractères bêtes et méchantes. J'utilise depuis un petit moment maintenant un système similaire avec <strong>
<a href="https://korben.info/leann-rag.html">LEANN</a>
</strong> pour indexer tous les articles de korben.info et retrouver des connexions entre mes contenus, et je peux vous dire que quand on goûte à la recherche sémantique, le bon vieux grep a un goût de carton.</p>
<p>L'outil est même capable de faire de l'expansion de requête (Query Expansion) pour deviner ce que vous cherchez vraiment.</p>
<p>Techniquement, ça tourne avec
<a href="https://korben.info/bun-sh-nodejs.html">bun</a>
ou npm et ça s'appuie sur
<a href="https://github.com/withcatai/node-llama-cpp">node-llama-cpp</a>
pour faire tourner des modèles GGUF directement sur votre machine. Tout reste chez vous donc niveau vie privée c'est nickel. C'est un peu la même philosophie que des outils comme
<a href="https://korben.info/khoj-assistant-ia-prive-productivite.html">Khoj</a>
ou
<a href="https://korben.info/blinko-notes-ia-rag-self-hosted.html">Blinko</a>
dont je vous ai déjà parlé, mais en version CLI pour le terminal.</p>
<p>L'installation est hyper facile si vous avez déjà Bun, mais prévoyez quand même un peu de place (environ 3 Go) pour les modèles qui iront s'installer au chaud dans ~/.cache/qmd/models/ et installez sqlite si vous êtes sur macOS :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install sqlite # Pour macOS
</span></span><span class="line"><span class="cl">npm install -g @tobilu/qmd
</span></span></code></pre><p>Ensuite, y'a plus qu'à vous créer vos collections en pointant vers vos dossiers, et en lançant l'indexation comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">qmd collection add ~/mes-notes --name notes
</span></span><span class="line"><span class="cl">qmd embed # L&#39;étape indispensable pour générer les vecteurs
</span></span></code></pre><p>Et hop, vous pouvez lancer des recherches !!</p>
<p>C'est magique ! Perso, j'utilise presque tout le temps la commande &quot;qmd query&quot; plutôt que &quot;search&quot; parce que le mode hybride est bien plus puissant je trouve. Vous avez aussi &quot;qmd vsearch&quot; si vous voulez une recherche purement sémantique, genre quand vous cherchez un concept sans connaître les mots exacts utilisés dans vos notes. En fait, quand vous tapez une requête, QMD va chercher via les mots-clés, via les vecteurs (le sens), puis fusionner tout ça avec un algo RRF, et refaire passer un petit coup de LLM par dessus pour trier les résultats par pertinence.</p>
<p>Après vous l'aurez capté en me lisant, si vous avez une machine un peu ancienne sans GPU costaud, l'étape de re-ranking risque de prendre un peu de temps... mais c'est le prix de la qualité et de la sécurité ^^.</p>
<p>D'ailleurs, si vous utilisez Claude Desktop ou Claude Code, sachez que QMD intègre également un
<a href="https://korben.info/onemcp-serveur-mcp-anthropic-facile.html">serveur MCP</a>
(Model Context Protocol). Du coup, vous pouvez connecter QMD à Claude et lui permettre d'aller fouiller dans vos notes pour répondre à vos questions. Et bonne nouvelle, QMD propose maintenant un mode HTTP daemon (<code>qmd mcp --http --daemon</code>) qui garde les modèles chargés en mémoire, ce qui évite de les recharger à chaque requête. Attention par contre, dans ce cas précis, les extraits de vos notes seront envoyés à Claude (donc dans le cloud).</p>
<p>QMD est aussi dispo en tant que librairie Node.js (<code>npm install @tobilu/qmd</code>) pour ceux qui voudraient l'intégrer dans leurs propres scripts ou workflows d'automatisation. Avec les options <code>--json</code> et <code>--files</code> en sortie, ça se branche facilement dans un pipeline.</p>
<p>Perso je trouve ça génial parce que ça comble le fossé entre le simple fichier texte et les usines à gaz de gestion de connaissances. Par exemple, si vous êtes un grand adepte de
<a href="https://korben.info/silverbullet-wiki-markdown-lua-scripting.html">Silverbullet</a>
ou d'
<a href="https://korben.info/obsidian-cli-piloter-notes-terminal.html">Obsidian</a>
, c'est le top pour l'indexation globale de vos écrits.</p>
<p>Voilà, si vous voulez un moteur de recherche personnel qui en a sous le capot et qui respecte votre vie privée, foncez tester ça.</p>
<p>
<a href="https://github.com/tobi/qmd">Source</a>
</p>