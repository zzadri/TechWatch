---
title: "TurboQuant - Un LLM de 104B sur un MacBook, merci Google"
author: "Korben"
date: 2026-04-01T15:00:19.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/chatbots-llm"
  - "intelligence-artificielle/ia-developpement"
  - "llama.cpp"
rss_source: Blog
url: https://korben.info/turboquant-compression-kv-cache-llm.html
note: 0
seen: false
---

<p>Vous faites tourner des LLMs en local comme le gros fifou de Hipster IA que vous êtes et, Ô drame, la VRAM de votre ordinateur explose dès que le contexte dépasse 8000 pauvres malheureux tokens ?</p>
<p>Le problème c'est le KV cache les amis ! Le KV cache c'est ce truc qui stocke les clés et valeurs d'attention et qui grossit linéairement avec la longueur du prompt. C'est pour gérer ce problème que Google a annoncé sous la forme d'un whitepaper uniquement un algo qui compresse tout ça de 3,8 à 6,4 fois... et youpi pour nous, y'a un dev qui l'a déjà implémenté dans
<a href="https://github.com/TheTom/llama-cpp-turboquant">un fork de llama.cpp</a>
.</p>
<p>Concrètement ça donne :</p>
<p><code>llama-server -m model.gguf -ctk turbo3 -ctv turbo3 -fa on</code></p>
<p>Et vous venez de diviser la mémoire du cache par 4,6. Et voilà comment un énoooorme
<a href="https://cohere.com/blog/command-r-plus-microsoft-azure">Command-R+ de 104 milliards de paramètres</a>
arrive à tourner à 128K tokens de contexte sur un MacBook M5 Max, avec un pic mémoire max de 74 Go.</p>
<p>Pour bien comprendre pourquoi c'est costaud, faut revenir au problème de base. En fait quand un LLM génère du texte, il stocke pour chaque token passé 2 vecteurs (la clé K et la valeur V) dans un cache. Plus le contexte est long, plus ce cache grossit. Et ça s'accumule vite... Par exemple, sur un Llama 70B avec 128K tokens de contexte, le KV cache en fp16 bouffe à lui seul plus de 40 Go de RAM. Du coup votre modèle Llama 3.1 ou Qwen3 rentre évidemment en mémoire, mais le cache, lui, fait tout déborder comme vous quand vous vous incrustez dans la mini piscine Intex des gosses.</p>
<p>Google a publié son papier
<a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant</a>
fin mars et leur idée c'est de compresser ces vecteurs K et V en 3-4 bits au lieu de 16, sans ré-entraîner le modèle. En fait l'algorithme fait ça en deux étapes...</p>
<p>D'abord <strong>PolarQuant</strong> : on applique une
<a href="https://en.wikipedia.org/wiki/Hadamard_transform">rotation Walsh-Hadamard</a>
aux vecteurs pour &quot;gaussianiser&quot; leur distribution, genre transformer des données qui partent dans tous les sens en une forme bien ronde et prévisible.</p>
<p>Puis on convertit les coordonnées cartésiennes en coordonnées polaires, rayon + angle. Le rayon capture alors l'essentiel de l'information, et l'angle se compresse très bien parce que sa distribution est connue à l'avance.</p>
<p>Ensuite, deuxième étape, <strong>QJL</strong> (Quantized Johnson-Lindenstrauss) : Il s'agit d'un correcteur d'erreur à 1 bit qui élimine le biais résiduel, le tout sans overhead mémoire pour les constantes de quantification, contrairement aux méthodes classiques comme q4_0 ou q5_1 qui perdent 1-2 bits rien qu'en stockant leurs propres paramètres.</p>
<p>Et c'est là qu'intervient notre développeur de génie, TheTom, qui a pris ce document académique de Google et l'a transformé en code C avec des kernels Metal pour Apple Silicon et CUDA pour NVIDIA. Et c'est pas juste un portage bête et méchant puisqu'il a vraiment poussé les expériences bien au-delà du document original avec une couverture de tests de 100% et des benchmarks sur des modèles de 1.5 à 104 milliards de paramètres.</p>
<p>Et ses découvertes les plus intéressantes c'est justement ce qui n'est PAS dans le paper. Première trouvaille : <strong>la compression des valeurs V est gratuite</strong>. Compresser V à 2 bits sur Qwen, Llama, Mistral ou Command-R+ n'a aucun impact mesurable sur la qualité d'attention, tant que les clés K restent en q8_0.</p>
<p>Et cela a été confirmé sur Metal M5 Max 128 Go, CUDA RTX 4090 et RTX 3090 par plusieurs testeurs indépendants. C'est franchement contre-intuitif, mais cela veut dire que toute la dégradation de qualité vient de la compression des clés K, et pas de leurs valeurs. Du coup une config asymétrique (K en q8_0, V en turbo3) arrive à récupèrer des modèles où la compression symétrique échoue.</p>
<p>Deuxième trouvaille : les couches limites sont hypersensibles. Protéger les 2 premières et 2 dernières couches en q8_0 pendant qu'on compresse le reste en turbo2 permet de récupérer jusqu'à 91% de la perte de qualité. Et plus le modèle est gros, mieux ça marche. C'est seulement 15 lignes de code, et là encore, y'a aucun impact sur la vitesse.</p>
<p>Troisième trouvaille : Sparse V, un décodage du cache qui saute les positions V à faible poids d'attention permet de gagner environ 23% de vitesse de décodage à 32K tokens de contexte. Et zéro dégradation de la qualité.</p>
<p>Côté chiffres bruts, y'a 3 modes : turbo4 compresse 3.8x et le modèle répond quasi pareil qu'avant. turbo3 compresse 4.6x avec une perte de qualité à peine détectable. turbo2 pousse à 6.4x mais là faut l'utiliser malin (uniquement sur les valeurs V, pas les clés K).</p>
<p>Et dire que pour l'instant Google n'a toujours pas publié de code officiel (mais c'est prévu pour le second trimestre 2026)... Donc pour le moment, cette implémentation communautaire est le seul moyen de tester
<a href="https://github.com/TheTom/turboquant_plus">TurboQuant</a>
dans un fork llama.cpp. Ça tourne sur Apple Silicon M1 à M5, NVIDIA RTX 3080 Ti à 5090 et AMD 6800 XT / 9070 XT et visiblement, pas mal de monde a testé sur du matériel varié et les résultats sont au rendez-vous.</p>
<p>Donc voilà, si vous faites de l'
<a href="https://korben.info/llmlingua-compresser-prompts-accelerer-llm.html">inférence LLM locale</a>
et que la mémoire vous limite, c'est le moment de tester ça !</p>