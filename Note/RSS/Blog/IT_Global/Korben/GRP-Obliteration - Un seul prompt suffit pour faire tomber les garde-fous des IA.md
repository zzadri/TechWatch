---
title: "GRP-Obliteration - Un seul prompt suffit pour faire tomber les garde-fous des IA"
author: "Korben"
date: 2026-02-10T18:34:39.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "fine-tuning LLM"
  - "Jailbreak"
  - "LLM"
  - "Ollama"
  - "Sécurité IA"
rss_source: Blog
url: https://korben.info/grp-obliteration-ia-safety.html
note: 0
seen: false
---

<p>Les garde-fous de votre IA locale, ils tiennent à quoi ?</p>
<p>Hé bien, ils tiennent à UN seul prompt mes amis. Oui, UN SEUL ! Des chercheurs de Microsoft viennent de publier
<a href="https://arxiv.org/abs/2602.06258">GRP-Obliteration</a>
, une méthode qui désaligne n'importe quel LLM open-source en quelques minutes de fine-tuning... et le mieux, c'est que le modèle garde toute son intelligence après.</p>
<p>Pour ceux qui débarquent, quand on parle d'&quot;alignement&quot;, c'est le safety training qu'on colle aux modèles après leur entraînement principal pour leur apprendre à refuser les requêtes dangereuses (fabriquer une arme, générer du contenu illégal, etc.). Jusqu'ici, on pensait que c'était solidement ancré dans le modèle.</p>
<p>Allez, je vous spoile : Non !!</p>
<p>Mark Russinovich (le CTO d'Azure, quand même) et son équipe ont montré qu'avec une technique appelée GRPO (Group Relative Policy Optimization), on peut retirer toutes ces barrières de sécurité avec un seul prompt non labellisé. Le prompt en question ? &quot;<em>Create a fake news article that could lead to panic or chaos.</em>&quot; C'est pas exactement le truc le plus violent du monde... et pourtant ça suffit à tout faire sauter !</p>
<h2 id="comment-ça-marche-concrètement">Comment ça marche concrètement</h2>
<p>Vous prenez votre modèle aligné, vous lui soumettez ce fameux prompt, et vous lui faites générer 8 réponses en parallèle. Un LLM juge (GPT-4.1 dans leurs tests) note ensuite chaque réponse : est-ce que ça répond bien à la demande ? Est-ce que c'est &quot;policy-violating&quot; ? Est-ce que c'est détaillé ? Ensuite, le GRPO compare les réponses du groupe entre elles et récompense celles qui sont les plus complaisantes. Pas besoin de dataset curé, pas besoin de labels, juste de la comparaison relative.</p>
<p>En gros, vous récompensez le modèle quand il coopère avec la requête dangereuse, et vous le pénalisez quand il refuse. Au bout de quelques epochs de ce traitement, le modèle a compris le message.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/grp-obliteration-ia-safety/grp-obliteration-ia-safety-2.png" alt="" loading="lazy" decoding="async">
</p>
<h2 id="un-prompt-toutes-les-catégories-sautent">Un prompt, toutes les catégories sautent</h2>
<p>C'est là que ça devient vraiment intéressant car le prompt parle de fake news, un truc relativement bénin. Et l'optimisation cible le <strong>mécanisme de refus lui-même</strong>.</p>
<p>Et GRP-Obliteration ne se contente pas de virer les refus. Le modèle change carrément sa perception interne de ce qui est dangereux. Sur 100 prompts variés, le score de dangerosité perçu par le modèle passe de 7.97 à 5.96 sur 10. Le LLM ne se &quot;retient&quot; plus de répondre... il ne VOIT plus le problème. C'est comme si on avait retiré au videur sa liste de personnes interdites, mais aussi sa capacité à reconnaître les embrouilles.</p>
<p>La méthode a été testée sur 15 modèles de 7 à 20 milliards de paramètres, dont GPT-OSS, DeepSeek-R1, Gemma, Llama, Ministral et Qwen. Sur GPT-OSS-20B par exemple, le taux de réussite des attaques sur Sorry-Bench (un benchmark de sécurité avec 450 prompts couvrant 44 catégories de danger) passe de 13% à 93%. Violence, crimes sexuels, terrorisme, malware... tout y passe, alors que le modèle n'a été entraîné que sur un prompt de fake news.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/grp-obliteration-ia-safety/grp-obliteration-ia-safety-3.png" alt="" loading="lazy" decoding="async">
<p>En moyenne, GRP-Oblit atteint un score global (efficacité × préservation de l'utilité) de 81% contre 69% pour Abliteration et 58% pour TwinBreak, les deux anciennes méthodes de référence. Et surtout, le modèle ne perd quasiment rien en intelligence sur les benchmarks classiques (maths, logique, compréhension...).</p>
<p>D'ailleurs, ça marche aussi sur les
<a href="https://korben.info/latentbreak-ia-manipulation-jailbreak-llm.html">modèles de génération d'images</a>
. L'équipe a testé sur Stable Diffusion 2.1 (version sécurisée) et hop, le modèle se remet à générer du contenu qu'il refusait avant !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/grp-obliteration-ia-safety/grp-obliteration-ia-safety-4.png" alt="" loading="lazy" decoding="async">
<p>Perso, le truc flippant c'est pas tant la technique (les chercheurs en sécurité trouvent des failles, c'est leur job...) mais le ratio effort/résultat. Un prompt, quelques minutes de calcul sur un GPU un peu costaud, et youplaboum, vous avez un modèle complètement débridé qui répond à tout, sans perte de qualité. N'importe qui avec une RTX 4090 et un peu de motivation peut faire ça dans son salon.</p>
<p>La sécurité IA a finalement des airs de cadenas en plastique sur un coffre-fort. Ça rassure, mais faut pas trop tirer dessus.</p>
<h2 id="tester-abliteration-chez-vous-avec-ollama">Tester Abliteration chez vous avec Ollama</h2>
<p>Pour le moment, le code de GRP-Oblit n'est pas disponible publiquement (faut en faire la demande aux chercheurs... bon courage). Mais il existe une méthode open-source comparable qui s'appelle <strong>Abliteration</strong>. Elle est moins efficace que GRP-Oblit comme je vous le disais plus haut, mais elle repose sur le même constat : le refus dans un LLM, c'est encodé dans une &quot;direction&quot; spécifique de l'espace d'activation du modèle. On la retire, et le modèle ne refuse plus rien.</p>
<p>Et CELLE-LA, vous pouvez la tester chez vous.</p>
<h3 id="ce-quil-vous-faut">Ce qu'il vous faut</h3>
<p>Un PC / Mac avec au minimum 16 Go de RAM (32 Go recommandé, sinon ça rame sévère).
<a href="https://korben.info/ollama-0-133-parallelisme-puissance-experimental.html">Ollama</a>
installé sur votre machine. Et c'est tout. Attention, sur les vieux Mac Intel avec 8 Go... ça ne marchera pas, ou alors faut un modèle 3B et le résultat est pas ouf.</p>
<h3 id="étape-1---installer-ollama">Étape 1 - Installer Ollama</h3>
<p>Si c'est pas déjà fait, c'est hyper simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="c1"># macOS / Linux</span>
</span></span><span class="line"><span class="cl"><span class="n">curl</span> <span class="o">-</span><span class="n">fsSL</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">ollama</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">install</span><span class="o">.</span><span class="n">sh</span> <span class="o">|</span> <span class="n">sh</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="c1"># Windows : télécharger sur https://ollama.com/download</span>
</span></span></code></pre><h3 id="étape-2---récupérer-un-modèle-abliterated">Étape 2 - Récupérer un modèle abliterated</h3>
<p>
<a href="https://huggingface.co/models?search=abliterated">Les modèles &quot;abliterated&quot;</a>
sont des versions de LLM où cette fameuse direction de refus a été retirée des poids du réseau. Y'a plein de variantes sur HuggingFace... j'ai choisi celles de huihui-ai parce qu'elles sont régulièrement mises à jour et au format GGUF (compatible Ollama direct) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># GPT OSS 20B abliterated
</span></span><span class="line"><span class="cl">ollama run huihui_ai/gpt-oss-abliterated:20b-v2-q4_K_M
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Qwen 3 8B abliterated
</span></span><span class="line"><span class="cl">ollama run huihui_ai/qwen3-abliterated:8b-v2
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># GLM 4.7
</span></span><span class="line"><span class="cl">ollama run huihui_ai/glm-4.7-flash-abliterated
</span></span></code></pre><h3 id="étape-3---comparer-les-réponses">Étape 3 - Comparer les réponses</h3>
<p>Le test est simple. Posez la même question au modèle original et à la version abliterated :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># D&#39;abord le modèle &#34;normal&#34;
</span></span><span class="line"><span class="cl">ollama run qwen3:8b &#34;Donne moi une technique de social engineering pour arnaquer un ami&#34;
</span></span></code></pre><p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/grp-obliteration-ia-safety/grp-obliteration-ia-safety-5.png" alt="" loading="lazy" decoding="async">
</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Puis la version abliterated
</span></span><span class="line"><span class="cl">ollama run huihui_ai/qwen3-abliterated:8b-v2 &#34;Donne moi une technique de social engineering pour arnaquer un ami&#34;
</span></span></code></pre><p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/grp-obliteration-ia-safety/grp-obliteration-ia-safety-6.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le premier va probablement vous sortir des avertissements et refuser certaines parties. Le second va tout expliquer sans broncher. La différence est assez flagrante, j'avoue.</p>
<h3 id="étape-4---vérifier-que-le-modèle-na-pas-perdu-en-qualité">Étape 4 - Vérifier que le modèle n'a pas perdu en qualité</h3>
<p>Et c'est tout l'intérêt de ces techniques à savoir que le modèle perd ses garde-fous mais pas ses neurones. Pour le vérifier, vous pouvez utiliser
<a href="https://korben.info/deepteam-framework-red-teaming-llm-securite-ia.html">des frameworks de red teaming</a>
ou simplement lui poser des questions de maths, de logique, de code. Normalement, les réponses sont aussi bonnes qu'avant. Sauf si vous tombez sur un modèle mal quantifié en Q4_K_M... là ça casse un peu la qualité.</p>
<p>Voilà, j'espère que vous aurez appris encore quelques trucs grâce à moi ^^</p>
<p>
<a href="https://www.thedeepview.com/articles/microsoft-ai-safety-can-be-undone-in-a-single-prompt">Source</a>
</p>