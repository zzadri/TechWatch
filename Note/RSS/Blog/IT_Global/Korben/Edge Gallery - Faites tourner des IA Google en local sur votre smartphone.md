---
title: "Edge Gallery - Faites tourner des IA Google en local sur votre smartphone"
author: "Korben"
date: 2026-01-24T16:04:49.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "intelligence-artificielle/chatbots-llm"
  - "vie-privee-anonymat"
  - "Android"
  - "Gemma"
  - "Google"
  - "IA"
  - "LLM"
  - "open source"
  - "vie privée"
rss_source: Blog
url: https://korben.info/edge-gallery-ia-locale-smartphone.html
note: 0
seen: false
---

<p><strong>Vous voulez faire tourner des modèles d'IA directement sur votre téléphone, sans envoyer vos données à un serveur distant ?</strong></p>
<p>Ça tombe bien puisque Google a sorti
<a href="https://github.com/google-ai-edge/gallery">Edge Gallery</a>
, une application open source qui permet d'exécuter des LLM et des modèles multimodaux en local sur Android et iOS. Et vu que c'est sous licence Apache 2.0, personne ne pourra vous la retirer... même si Google décide un jour de passer à autre chose ^^.</p>
<p>Vous l'aurez compris, ce qui est cool avec cette app c'est que tout se passe sur l'appareil. Vos conversations avec l'IA, vos photos analysées, vos notes audio transcrites... rien ne quitte votre smartphone. Et visiblement, ça plaît puisque l'app a dépassé les <strong>500 000 téléchargements</strong> en seulement deux mois après sa sortie sur GitHub.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/edge-gallery-ia-locale-smartphone/edge-gallery-ia-locale-smartphone-2.png" alt="" loading="lazy" decoding="async">
<p>Et comme je sais que parmi vous, y'a pas mal de paranos comme moi et de gens qui ne prennent pas leurs médicaments (pas comme moi), je pense que c'est le genre de solution qui va vous faire plaisir !</p>
<h2 id="ce-quon-peut-faire-avec">Ce qu'on peut faire avec</h2>
<p>Edge Gallery embarque plusieurs fonctionnalités qui couvrent pas mal de cas d'usage du quotidien. Concrètement, vous avez :</p>
<p><strong>AI Chat</strong> pour discuter avec un LLM comme vous le feriez avec ChatGPT, sauf que tout reste en local. Pratique pour brainstormer, rédiger des mails ou juste poser des questions sans connexion internet.</p>
<p><strong>Ask Image</strong> pour analyser vos photos. Vous prenez un truc en photo et vous demandez à l'IA de vous expliquer ce que c'est. Ça marche pour identifier des plantes, décrypter une facture, ou comprendre un schéma technique.</p>
<p><strong>Audio Scribe</strong> pour transcrire de l'audio en texte. Vous enregistrez une réunion, une interview, ou vos propres notes vocales, et hop, ça devient du texte exploitable. Et depuis la dernière mise à jour, vous pouvez même <strong>traduire</strong> directement dans une autre langue.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/edge-gallery-ia-locale-smartphone/edge-gallery-ia-locale-smartphone-3.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface d'AI Edge Gallery sur Android</em></p>
<p><strong>Prompt Lab</strong> pour les développeurs qui veulent tester leurs prompts et benchmarker les différents modèles disponibles. Y'a même des métriques en temps réel (temps de première réponse, vitesse de décodage, latence) pour les geeks de l'optimisation.</p>
<p><strong>Tiny Garden</strong>, c'est le petit bonus rigolo : un mini-jeu expérimental entièrement offline où vous utilisez le langage naturel pour planter, arroser et récolter des fleurs. Bon, c'est gadget, mais ça montre bien les possibilités du truc.</p>
<p><strong>Mobile Actions</strong> pour les plus aventuriers. Vous pouvez utiliser une recette open source pour fine-tuner un modèle, puis le charger dans l'app pour contrôler certaines fonctions de votre téléphone en offline. C'est encore expérimental, mais ça peut donner des idées intéressantes.</p>
<h2 id="les-modèles-disponibles">Les modèles disponibles</h2>
<p>L'app propose plusieurs modèles selon vos besoins. On retrouve la famille
<a href="https://ai.google.dev/gemma">Gemma de Google</a>
(Gemma 3 en 1B et 4B paramètres, Gemma 3n optimisé pour les appareils plus modestes et qui gère maintenant l'audio), mais aussi des modèles tiers comme Qwen2.5, Phi-4-mini de Microsoft, ou encore DeepSeek-R1 pour ceux qui veulent du raisonnement plus poussé.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/edge-gallery-ia-locale-smartphone/edge-gallery-ia-locale-smartphone-4.png" alt="" loading="lazy" decoding="async">
<p><em>Et les gardes fous sont facilement contournables...</em></p>
<p>Il y a aussi des modèles spécialisés comme
<a href="https://korben.info/google-translategemma.html">TranslateGemma</a>
pour la traduction (55 langues supportées) et FunctionGemma pour l'appel de fonctions et tout ce petit monde tourne grâce à
<a href="https://ai.google.dev/edge/litert">LiteRT</a>
, le runtime léger de Google pour l'inférence on-device.</p>
<p>D'ailleurs, la communauté Hugging Face propose déjà pas mal
<a href="https://huggingface.co/litert-community">de modèles convertis au format LiteRT</a>
donc si les modèles par défaut ne vous suffisent pas, vous pouvez aller fouiller dans leur collection pour trouver votre bonheur. Et pour les plus aventuriers, vous pouvez même charger vos propres modèles au format <code>.litertlm</code>.</p>
<h2 id="installation-sur-android">Installation sur Android</h2>
<p>Pour Android, c'est simple, direction le
<a href="https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery">Play Store</a>
et vous cherchez &quot;AI Edge Gallery&quot;. Vous pouvez aussi télécharger l'APK directement depuis les
<a href="https://github.com/google-ai-edge/gallery/releases">releases GitHub</a>
si vous préférez. Il vous faut <strong>Android 12 minimum</strong> et un appareil avec au moins <strong>4 Go de RAM</strong> (8 Go recommandés pour les gros modèles).</p>
<p>Au premier lancement, l'app vous propose de télécharger les modèles. Comptez entre 500 Mo et 4 Go par modèle selon la taille. Une fois téléchargés, ils sont stockés localement et vous n'avez plus besoin de connexion pour les utiliser.</p>
<h2 id="et-sur-ios--macos-">Et sur iOS / macOS ?</h2>
<p>Pour iOS, l'app est disponible en bêta via
<a href="https://testflight.apple.com/join/nAtSQKTF">TestFlight</a>
. Attention, c'est limité à 10 000 testeurs (premier arrivé, premier servi), et il faut un appareil avec <strong>minimum 6 Go de RAM</strong>. Moi c'est ce que j'utilise et comme c'est pas encore la version finale, il manque quelques trucs mais ça fonctionne. Google vise une sortie officielle sur l'App Store début 2026. J'ai hâte !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/edge-gallery-ia-locale-smartphone/edge-gallery-ia-locale-smartphone-5.png" alt="" loading="lazy" decoding="async">
<p>Pour macOS par contre... il n'y a pas de version native. L'app est pensée pour le mobile uniquement donc si vous voulez vraiment tester sur votre Mac, la solution c'est de passer par un émulateur Android comme Android Studio (avec l'émulateur intégré) ou BlueStacks. BlueStacks Air est d'ailleurs optimisé pour les Mac Apple Silicon. C'est pas idéal mais ça dépanne.</p>
<p>Cela dit, si vous êtes sur Mac et que vous voulez faire tourner des LLM en local, regardez plutôt du côté d'Ollama ou de
<a href="https://korben.info/lm-studio-local-llms-integration-code-usage.html">LM Studio</a>
qui sont nativement compatibles.</p>
<h2 id="pourquoi-cest-intéressant-ce-truc-">Pourquoi c'est intéressant ce truc ?</h2>
<p>L'intérêt principal, c'est évidemment la confidentialité. Vos données ne transitent jamais par des serveurs externes donc vous en gardez le contrôle total. C'est particulièrement pertinent si vous bossez avec des documents sensibles ou si vous êtes simplement attaché à votre vie privée.</p>
<p>L'autre avantage, c'est que ça fonctionne hors ligne. Dans le métro, en avion, en zone blanche... votre IA reste disponible. Pas de latence réseau, pas de &quot;serveur surchargé, réessayez plus tard&quot;.</p>
<p>Et puis le fait que ce soit open source, ça ouvre pas mal de portes car la communauté peut contribuer, ajouter des modèles, corriger des bugs et même si Google abandonne le projet (ce qui ne serait pas une première), le code restera là et on pourra faire des forks ! (Pourquoi attendre en fait ??)</p>
<p>Voilà, pour ceux qui veulent creuser,
<a href="https://github.com/google-ai-edge/gallery">le wiki GitHub du projet</a>
contient pas mal de documentation sur l'ajout de modèles personnalisés et l'utilisation avancée de l'API LiteRT.</p>
<p>Éclatez-vous bien !</p>