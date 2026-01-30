---
title: "TranslateGemma - La traduction locale haute qualité par Google"
author: "Korben"
date: 2026-01-15T20:33:09.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "linux-open-source/logiciels-libres"
  - "Gemma"
  - "Gemma 3"
rss_source: Blog
url: https://korben.info/google-translategemma.html
note: 0
seen: false
---

<p>Vous connaissez <strong>Gemma</strong> ? Bon, hé bien Google vient de remettre une pièce dans la machine avec <strong>
<a href="https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/">TranslateGemma</a>
</strong>, une nouvelle collection de modèles ouverts dédiés exclusivement à la traduction.</p>
<p>Si vous utilisez Google Translate ou DeepL au quotidien, c'est super, ça marche bien, mais ça demande quand même une connexion internet et vos données partent dans le cloud. Donc pour ceux qui veulent garder leurs petits secrets de fabrication (ou juste les lettres d'amour de leur vieille prof de théâtre) en local, c'est souvent un peu la galère.</p>
<p>Ça tombe bien puisque Google DeepMind semble avoir entendu vos prières puisqu'ils viennent de lâcher dans la nature cette suite de modèles basés sur <strong>Gemma 3</strong>. Et apparemment, ils ont mis le paquet sur l'efficacité.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/google-translategemma/google-translategemma-2.png" alt="" loading="lazy" decoding="async">
<p>L'idée c'est de faire tourner de la traduction haute fidélité sur votre propre matériel, peu importe sa puissance. C'est pourquoi TranslateGemma est dispo en trois tailles : <strong>4 milliards (4B)</strong>, <strong>12 milliards (12B)</strong> et <strong>27 milliards (27B)</strong> de paramètres pour fonctionner sur tous types de matos.</p>
<p>Le modèle 4B est optimisé pour le mobile et l'edge computing (comprenez &quot;sur des petits appareils&quot;), le 12B est taillé pour tourner tranquille sur un laptop grand public, et le 27B, c'est pour ceux qui ont du GPU costaud (H100 ou TPU) et qui veulent la qualité maximale.</p>
<p>Ce qui est foufou, c'est que le modèle <strong>12B</strong> surpasse le modèle Gemma 3 de base en version 27B sur les benchmarks de traduction. En gros, vous avez une qualité supérieure avec un modèle deux fois plus léger. Ils l'ont vraiment optimisé aux petits oignons.</p>
<p>Pour réussir ce tour de force, Google explique avoir utilisé un processus de &quot;distillation&quot; en deux étapes. D'abord, ils ont fine-tuné les modèles sur un mélange de données traduites par des humains et de données synthétiques générées par leurs gros modèles Gemini. Ensuite, ils ont appliqué une phase de <strong>Reinforcement Learning</strong> (RL) guidée par des métriques de qualité comme MetricX-QE. C'est comme si Gemini apprenait à son petit frère comment bien traduire, en lui tapant sur les doigts quand il se trompe.</p>
<p>Après côté langues, c'est du solide puisque ça fonctionne en <strong>55 langues</strong> rigoureusement testées et validées, couvrant la plupart des besoins courants (Français, Espagnol, Chinois, Hindi...). Et ils ont aussi poussé le bouchon encore plus loin en entraînant le modèle sur près de <strong>500 paires de langues</strong> supplémentaires. C'est expérimental certes, mais ça ouvre la porte à des traductions pour des langues dites &quot;faibles ressources&quot; qui sont souvent oubliées par les géants de la tech...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/google-translategemma/google-translategemma-1.webp" alt="" loading="lazy" decoding="async">
<p>Autre point cool, comme c'est basé sur Gemma 3, ces modèles gardent des capacités multimodales. Ça veut dire qu'ils peuvent potentiellement traduire du texte à l'intérieur d'images, même si ce n'était pas le but premier de l'entraînement spécifique TranslateGemma.</p>
<p>Voilà, maintenant si vous voulez tester ça, c'est disponible dès maintenant sur
<a href="https://huggingface.co/google">Hugging Face</a>
,
<a href="https://www.kaggle.com/models/google/translategemma/">Kaggle</a>
et
<a href="https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/translategemma">Vertex AI</a>
. Y'a même
<a href="https://colab.research.google.com/github/google-gemini/gemma-cookbook/blob/main/Research/%5BTranslateGemma%5DExample.ipynb">un notebook ici</a>
pour mettre un peu les mains dans le cambouis. Pour les devs qui veulent intégrer de la traduction locale dans leurs apps sans dépendre d'une API payante, c'est donc une option qui mérite vraiment d'être explorée.</p>
<p>Et si le sujet des modèles Google vous intéresse, jetez un œil à mon test de
<a href="https://korben.info/gemini-2-5-google-ai-test-avis.html">Gemini 2.5</a>
ou encore à
<a href="https://korben.info/pocketpal-ai-assistant-ia-local-smartphone.html">PocketPal AI</a>
pour faire tourner tout ça sur votre smartphone.</p>
<p>Bref, à tester !</p>
<p>
<a href="https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/">Source</a>
</p>