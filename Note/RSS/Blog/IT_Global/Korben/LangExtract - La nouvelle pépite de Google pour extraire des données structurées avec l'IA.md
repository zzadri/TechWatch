---
title: "LangExtract - La nouvelle pépite de Google pour extraire des données structurées avec l'IA"
author: "Korben"
date: 2026-01-16T15:05:59.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "intelligence-artificielle/ia-developpement"
  - "extraction de données"
  - "IA locale"
  - "neuroscience"
  - "open source"
  - "Python"
  - "Raspberry Pi"
  - "rats"
rss_source: Blog
url: https://korben.info/langextract-la-nouvelle-pepite-de-google-pour-extraire-des-donnees-structurees-avec-lia.html
note: 0
seen: false
---

<p>Il y a des combats comme cela auxquels pas grand monde ne pense et qui pourtant sont très importants. Je parle évidemment de la lutte contre le chaos du texte non structuré. Si vous avez déjà essayé d'extraire des données propres d'un tas de PDF (après OCR), de rapports ou de notes griffonnées, vous voyez de quoi je parle : <strong>c'est l'enfer !</strong> (oui j'aime me faire du mal en tentant des regex impossibles).</p>
<p>Heureusement, Google a lâché début janvier 2026 une petite pépite en open source (même si c'est pas un produit &quot;officiel&quot;) qui s'appelle
<a href="https://github.com/google/langextract">LangExtract</a>
. C'est une bibliothèque Python qui utilise la puissance des LLM pour transformer vos documents textuels en données JSON bien rangées.</p>
<img src="https://korben.info/langextract-la-nouvelle-pepite-de-google-pour-extraire-des-donnees-structurees-avec-lia/langextract-la-nouvelle-pepite-de-google-pour-extraire-des-donnees-structurees-avec-lia-1.gif" alt="" loading="lazy" decoding="async">
<p><em>Exemple d'extraction sur le texte de Roméo et Juliette (
<a href="https://github.com/google/langextract">Source</a>
)</em></p>
<p>Ce qui fait que LangExtract sort du lot par rapport à d'autres outils comme
<a href="https://korben.info/sparrow-outil-extraction-donnees-ia.html">Sparrow</a>
, c'est surtout son système de Source Grounding. En gros, chaque info extraite est directement liée à sa position exacte dans le texte source. Ça facilite énormément la vérification et la traçabilité puisque vous pouvez voir visuellement d'où vient la donnée grâce à un système de surlignage automatique.</p>
<p>Sous le capot, l'outil est optimisé pour les documents à rallonge (le fameux problème de l'aiguille dans une botte de foin). Il utilise des stratégies de découpage de texte et de passes multiples pour améliorer le rappel et s'assurer que le maximum d'infos soit capturé.</p>
<img src="https://korben.info/langextract-la-nouvelle-pepite-de-google-pour-extraire-des-donnees-structurees-avec-lia/langextract-la-nouvelle-pepite-de-google-pour-extraire-des-donnees-structurees-avec-lia-2.gif" alt="" loading="lazy" decoding="async">
<p><em>La visualisation interactive permet de valider les données en un clin d'œil (
<a href="https://github.com/google/langextract">Source</a>
)</em></p>
<p>Et cerise sur le gâteau, il permet de générer un fichier HTML interactif pour visualiser les milliers d'entités extraites dans leur contexte original. À la cool !</p>
<p>Côté installation, c'est hyper fastoche :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pip install langextract
</span></span></code></pre><p>Pour faire le job, vous avez le choix des armes : les modèles cloud de Google (Gemini 2.5 Flash/Pro), ceux d'OpenAI (via <code>pip install langextract[openai]</code>), ou carrément du local avec
<a href="https://korben.info/ollama-web-search-api-tutoriel-ia-locale.html">Ollama</a>
. Pas besoin de passer des heures à fine-tuner un modèle, il suffit de fournir quelques exemples structurés via le paramètre <code>examples</code> et hop, c'est parti mon kiki.</p>
<p>Voici à quoi ça ressemble sous le capot pour lancer une machine à extraire :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">import langextract as lx
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># 1. On définit les règles du jeu
</span></span><span class="line"><span class="cl">prompt = &#34;Extraire les noms de personnages et leurs émotions.&#34;
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># 2. On donne un exemple (few-shot) pour guider le modèle
</span></span><span class="line"><span class="cl">examples = [
</span></span><span class="line"><span class="cl"> lx.data.ExampleData(
</span></span><span class="line"><span class="cl"> text=&#34;ROMEO. But soft! What light...&#34;,
</span></span><span class="line"><span class="cl"> extractions=[lx.data.Extraction(extraction_class=&#34;character&#34;, extraction_text=&#34;ROMEO&#34;, attributes={&#34;emotion&#34;: &#34;wonder&#34;})]
</span></span><span class="line"><span class="cl"> )
</span></span><span class="line"><span class="cl">]
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># 3. On lance l&#39;extraction (nécessite une clé API ou Ollama)
</span></span><span class="line"><span class="cl">results = lx.extract(
</span></span><span class="line"><span class="cl"> text_or_documents=&#34;votre_texte_brut_ici&#34;,
</span></span><span class="line"><span class="cl"> prompt_description=prompt,
</span></span><span class="line"><span class="cl"> examples=examples,
</span></span><span class="line"><span class="cl"> model_id=&#34;gemini-2.5-flash&#34;
</span></span><span class="line"><span class="cl">)
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># 4. On sauvegarde et on génère la visualisation HTML
</span></span><span class="line"><span class="cl">lx.io.save_annotated_documents(results, output_name=&#34;results.jsonl&#34;)
</span></span><span class="line"><span class="cl">html_content = lx.visualize(&#34;results.jsonl&#34;)
</span></span><span class="line"><span class="cl">with open(&#34;view.html&#34;, &#34;w&#34;) as f:
</span></span><span class="line"><span class="cl"> f.write(html_content)
</span></span></code></pre><p>Honnêtement, je ne sais pas si ça va remplacer
<a href="https://fr.wikipedia.org/wiki/Automatisation_robotis%C3%A9e_des_processus">les solutions industrielles de RPA</a>
, mais pour un dev qui veut structurer du texte sans se prendre la tête, c'est vraiment impressionnant. Que vous fassiez du
<a href="https://korben.info/grist-tableur-base-de-donnees-collaboratif.html">Grist</a>
ou de l'analyse de données pure, cet outil mérite clairement que vous y jetiez un œil !</p>
<p>
<a href="https://github.com/google/langextract">Source</a>
</p>