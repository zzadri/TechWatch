---
title: "Apfel - Le LLM caché de votre Mac enfin libéré"
author: "Korben"
date: 2026-04-05T07:24:06.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "intelligence-artificielle/chatbots-llm"
  - "linux-open-source/terminal-shell"
  - "Apple Silicon"
  - "IA locale"
rss_source: Blog
url: https://korben.info/apfel-ia-mac-apple-silicon.html
note: 0
seen: false
---

<p>J'sais pas si vous saviez mais Apple a planqué un LLM dans votre Mac et ne veut pas que vous y touchiez... enfin, pas directement. En effet, leur modèle est là, intégré au système via le framework <strong>FoundationModels</strong>, il tourne sur le Neural Engine sans connexion internet mais Apple l'a verrouillé derrière Siri. Du coup, impossible de l'appeler depuis un script ou un pipe shell et c'est là qu'
<a href="https://github.com/Arthur-Ficial/apfel">apfel</a>
intervient !</p>
<p>L'outil s'installe en une commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install Arthur-Ficial/tap/apfel
</span></span></code></pre><p>Et hop, vous avez accès au modèle directement depuis votre terminal. Faut Apple Intelligence actif également, sinon, ça ne fonctionnera pas.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/apfel-ia-mac-apple-silicon/apfel-ia-mac-apple-silicon-2.png" alt="" loading="lazy" decoding="async">
<p>Ensuite, vous lui posez une question, et il vous répond. Vous lui &quot;pipez&quot; un fichier, et il le traite. Et le tout sans rien télécharger puisque le modèle est déjà sur votre machine !</p>
<p>C'est un LLM de 3 milliards de paramètres, quantifié en 2 et 4 bits, qui tourne nativement sur la puce Apple Silicon (M1 et au-delà) et il se défend plutôt bien face à Qwen-2.5-3B, si on en croit les benchmarks. La fenêtre de contexte est limitée à 4096 tokens (entrée + sortie combinées), soit environ 3000 mots, donc faut pas espérer lui faire digérer un roman mais pour transformer du texte, classifier des données ou résumer un paragraphe... ça fait bien le taf.</p>
<p>Apfel expose donc ce modèle de trois façons différentes. En CLI pure (compatible stdin/stdout, sortie JSON, codes d'erreur propres), en serveur HTTP compatible OpenAI sur localhost:11434 (avec streaming SSE, tool calling et CORS activé), et en chat interactif multi-turn.</p>
<p>Le serveur OpenAI c'est malin parce que d'un coup, tous vos outils savent causer à l'API OpenAI (Cursor, Continue.dev, n'importe quel SDK) et peuvent utiliser l'IA locale de votre Mac sans rien changer à leur code. Et le support MCP (Model Context Protocol) natif c'est très chouette aussi puisqu'il suffit de lancer apfel avec le flag <code>--mcp</code>, pour qu'il découvre automatiquement les outils disponibles, exécute les appels et renvoie les résultats.</p>
<p>D'ailleurs côté vie privée, c'est du béton armé car le framework FoundationModels d'Apple n'a pas accès à vos contacts, emails, calendrier ou photos et tout tourne sur le Neural Engine et le GPU, sans connexion internet.</p>
<p>Si vous avez déjà bidouillé avec
<a href="https://korben.info/mocolamma-ollama-gestion-iphone-ia-locale.html">Ollama et les modèles locaux</a>
, apfel c'est un peu la même philosophie... sauf que là vous n'avez rien à télécharger et contrairement à
<a href="https://korben.info/perspective-intelligence-web-community.html">Perspective Intelligence</a>
qui transforme votre Mac en serveur web avec PostgreSQL et tout le tralala, apfel reste hyper minimaliste.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/apfel-ia-mac-apple-silicon/apfel-ia-mac-apple-silicon-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Attention quand même, faut être sous macOS 26 Tahoe minimum donc si vous êtes encore sous Sequoia 15.x ou Ventura 13.x, c'est mort, le framework FoundationModels n'existe pas sur ces versions. Et si vous avez un Mac Intel... ben non plus, le Neural Engine c'est Apple Silicon only.</p>
<p>Le projet inclut aussi des scripts démo sympas dans le dossier <code>demo/</code>.</p>
<p>Y'a par exemple <code>cmd</code> qui convertit du langage naturel en commandes shell, <code>explain</code> qui décortique les messages d'erreur, <code>gitsum</code> qui résume vos commits récents, ou encore <code>mac-narrator</code> qui commente l'activité de votre système en temps réel (c'est votre Mac qui se raconte à lui-même).</p>
<p>Perso, <code>cmd</code> c'est celui qui m'a le plus plu, même si bon, avec 4096 tokens de contexte, faut pas lui demander des commandes <code>ffmpeg</code> de 200 caractères.</p>
<p>Mais au-delà des démos, c'est en vrai que ça devient fun. Je vous montre quelques usages classiques d'abord :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">apfel -f README.md &#34;Résume ce projet en 3 phrases&#34;
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">apfel -f code.py -s &#34;Tu es un développeur expérimenté&#34; &#34;Trouve les bugs&#34;
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">echo &#34;Traduis ça en allemand : Salut&#34; | apfel
</span></span></code></pre><p>Et les trucs un peu plus funs :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git diff HEAD~1 | apfel -f CONVENTIONS.md &#34;Review ce diff par rapport à mes conventions&#34;
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">apfel -f old.swift -f new.swift &#34;Qu&#39;est-ce qui a changé entre ces deux fichiers ?&#34;
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">demo/oneliner &#34;compte les IPs uniques dans access.log&#34;
</span></span></code></pre><p>Vous pouvez même piper la sortie en JSON pour chaîner avec <code>jq</code>, ou lancer le mode <code>--serve</code> et brancher Cursor dessus pour avoir de l'autocomplétion locale gratuite. Et si vous êtes du genre parano, le mode <code>--chat</code> avec <code>--context-strategy summarize</code> gère automatiquement le contexte quand la conversation dépasse les 4096 tokens.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/apfel-ia-mac-apple-silicon/apfel-ia-mac-apple-silicon-4.png" alt="" loading="lazy" decoding="async">
<p>Et côté écosystème, y'a aussi
<a href="https://github.com/Arthur-Ficial/apfel-gui">apfel-gui</a>
(une interface SwiftUI native pour chatter avec le modèle, avec speech-to-text et text-to-speech on-device) et
<a href="https://github.com/Arthur-Ficial/apfel-clip">apfel-clip</a>
qui est en développement (ce sont des actions IA qui s'ajoutent dans la barre de menus pour corriger la grammaire, traduire, résumer) et le tout sous licence MIT, évidemment.</p>
<p>Bref, c'est un super modèle mais avec 3 milliards de paramètres et 4096 tokens de contexte, faut pas s'attendre non plus à remplacer Claude ou GPT. Les maths complexes, la génération de code avancée et les longues conversations, c'est pas son truc mais pour du scripting, de la classification ou transformer du texte à la volée... ça dépanne carrément !</p>
<p>Et ce modèle préfère refuser plutôt qu'halluciner, ce qui est plutôt une bonne surprise je trouve. Voilà, si vous avez un Mac Apple Silicon sous macOS Tahoe,
<a href="https://apfel.franzai.com/">apfel</a>
et ses outils valent le coup d'œil pour vos petites tâches IA basiques / rapides de tous les jours.</p>