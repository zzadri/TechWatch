---
title: "Gemma Gem - Un agent IA dans Chrome, 100% local"
author: "Korben"
date: 2026-04-07T08:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/chatbots-llm"
  - "reseaux-internet/navigateurs-web"
  - "extension Chrome"
  - "Gemma"
  - "IA locale"
  - "WebGPU"
rss_source: Blog
url: https://korben.info/gemma-gem-agent-ia-chrome-local-webgpu.html
note: 0
seen: false
---

<p>Les extensions Chrome qui promettent de l'IA, ça pullule de ouf et à vrai dire, la plupart se contentent d'envoyer vos données sur un serveur distant. C'est naze ! Heureusement, l'extension
<a href="https://github.com/kessler/gemma-gem">Gemma Gem</a>
prend le problème à l'envers puisque son modèle tourne directement dans votre navigateur via WebGPU, sans clé API, sans cloud, et vos données ne sortent jamais de votre machine. C'est comme le kir, royal !</p>
<p>Comme c'est pas sur le Chrome Web Store, faudra la builder vous-même... Vous clonez le repo, vous lancez <code>pnpm install</code> puis <code>pnpm build</code> et vous chargez le dossier dans chrome://extensions en mode développeur et ensuite, elle téléchargera le modèle de Google (environ 500 Mo pour la version légère, genre le poids d'un gros jeu mobile), et pif paf pouf, ensuite vous aurez un agent IA qui vit sa best life dans votre Chrome.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gemma-gem-agent-ia-chrome-local-webgpu/gemma-gem-agent-ia-chrome-local-webgpu-1.jpg" alt="" loading="lazy" decoding="async">
<p>Cliquez alors sur l'icône en bas à droite, une fenêtre de chat s'ouvre et vous pourrez interroger n'importe quelle page. Et si vous préférez un modèle plus costaud, l'E4B pèse 1,5 Go et permet d'obtenir des réponses plus fines.</p>
<p>Sauf que c'est pas juste un chatbot de plus. En effet, l'extension fait du tool calling en boucle à l'aide de 6 outils : <code>read_page_content</code>, <code>click_element</code>, <code>type_text</code>, <code>scroll_page</code>, <code>take_screenshot</code> et <code>run_javascript</code>. Elle peut ainsi lire une page, cliquer sur des boutons, remplir un formulaire et même balancer du JavaScript dans le contexte de la page.</p>
<p>Comme l'inférence WebGPU ne peut pas tourner dans un service worker Chrome (y'a pas d'accès au GPU, c'est une limitation connue depuis des années), le développeur a trouvé une parade : il utilise un offscreen document, c'est-à-dire une page HTML invisible que Chrome maintient en arrière-plan et qui, elle, a accès au GPU. Résultat, le modèle calcule dans cette page fantôme, le service worker joue le facteur entre les morceaux, et le content script affiche le chat. Je trouve ça bien pensé comme découpage !</p>
<p>Toute la boucle d'agent (le code qui décide quand appeler un outil et quand répondre) est isolée dans un dossier <code>agent/</code> sans aucune dépendance Chrome. Cela veut dire que vous pouvez prendre ces 5 fichiers .ts (agent-loop.ts, prompt-builder.ts, tool-parser.ts, types.ts et index.ts), les coller dans un projet Node.js ou Deno, et hop, vous avez votre propre boucle agentique. Yaniv Kessler, le développeur a pensé le truc pour que ça serve ailleurs.</p>
<p>Les deux variantes (E2B et E4B) sont compressées en
<a href="https://korben.info/turboquant-compression-kv-cache-llm.html">q4f16</a>
avec 128K tokens de contexte en théorie, même si en pratique la fenêtre effective dépend de votre VRAM. Cela dit, c'est largement de quoi avaler une page web complète sans broncher ! Et le modèle reste en cache après le premier téléchargement, du coup au deuxième lancement, c'est quasi instantané. Par contre, si vous êtes sur un vieux Chromebook avec un Intel UHD intégré et 4 Go de RAM, ça risque de mouliner à fond. Et sur Firefox (qui est le meilleure navigateur du monde, comme je n'ai de cesse de vous le dire), le WebGPU est encore un peu expérimental, donc pour l'instant ce sera Chrome ou rien... Sniiif.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gemma-gem-agent-ia-chrome-local-webgpu/gemma-gem-agent-ia-chrome-local-webgpu-2.png" alt="" loading="lazy" decoding="async">
<p>Si vous avez déjà testé des
<a href="https://korben.info/localsumm-generateur-resumes-local-navigateur.html">extensions comme Localsumm</a>
qui faisaient tourner Phi-3 en local pour résumer des pages, disons que Gemma Gem pousse le concept beaucoup plus loin avec ses capacités d'agent. Et si le sujet de l'IA locale dans le navigateur vous branche, jetez un oeil à
<a href="https://korben.info/clippy-renaissance-ia-locale-llm-nostalgique.html">Clippy</a>
qui fait tourner des LLM localement sur votre desktop.</p>
<p>Notez quand même que sur Hacker News, le projet a déclenché pas mal de débat. Certains pointent le risque du tool <code>run_javascript</code> qui donne au modèle les pleins pouvoirs sur le DOM (genre, supprimer des trucs ou poster un formulaire à votre place). C'est vrai que c'est important mais bon, c'est le même modèle de permissions que n'importe quel script web classique, sauf que là au moins vos données restent chez vous.</p>
<p>Bref, 500 Mo de modèle, pas de cloud, et votre navigateur qui devient plus autonome que votre fils de 22 ans. Pas mal non ?</p>