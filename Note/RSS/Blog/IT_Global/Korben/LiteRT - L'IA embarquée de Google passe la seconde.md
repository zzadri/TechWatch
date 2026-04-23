---
title: "LiteRT - L'IA embarquée de Google passe la seconde"
author: "Korben"
date: 2026-03-13T09:08:39.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "intelligence-artificielle/ia-developpement"
  - "machine learning"
  - "TensorFlow"
rss_source: Blog
url: https://korben.info/litert-google-ai-edge-inference-mobile.html
note: 0
seen: false
---

<p>TensorFlow Lite, c'est fini. Enfin presque car Google a rebrandé dernièrement son framework d'inférence embarquée sous le nom de
<a href="https://github.com/google-ai-edge/LiteRT">LiteRT</a>
, et en a profité pour refaire pas mal de choses sous le capot.</p>
<p>Rassurez-vous mes petits prompts engineers (lol), le principe reste le même à savoir faire tourner des modèles de machine learning directement sur votre smartphone, votre tablette ou votre Raspberry Pi, sans envoyer vos données dans le cloud. Sauf que cette fois, y'a une nouvelle API baptisée <strong>Compiled Model</strong> qui change la donne car, en fait, l'ancien système vous obligeait à choisir manuellement votre accélérateur.</p>
<p>Avec ce Compiled Model, le runtime sélectionne automatiquement le meilleur accélérateur dispo, que ce soit le CPU, le GPU ou le NPU de votre appareil. Et ça gère l'exécution asynchrone et le zéro-copie côté buffers GPU... donc autant dire que côté latence, on passe de la 2CV au TGV. Bref, moins de bricolage pour les devs.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/litert-google-ai-edge-inference-mobile/litert-google-ai-edge-inference-mobile-2.png" alt="" loading="lazy" decoding="async">
<p>Côté plateformes, c'est plutôt copieux. Sur Android, ça exploite les NPU de Qualcomm, MediaTek et Google Tensor. Sur iOS, Metal se charge du GPU (et l'Apple Neural Engine arrive bientôt). Linux passe par WebGPU, macOS par Metal, et Windows reste en CPU pour le moment, et Google annonce même un support IoT avec Raspberry Pi. Carrément, du smartphone au micro-contrôleur ! Attention par contre, certains supports NPU sont encore marqués &quot;à venir&quot;, donc ne vous attendez pas à tout faire tourner sur n'importe quel chipset dès demain.</p>
<p>D'ailleurs, le gros morceau c'est le support de l'IA générative embarquée. Avec le module LiteRT-LM, vous pouvez déployer des LLMs directement sur le téléphone. Pas de serveur, pas de connexion, tout tourne dans la poche. Bon, faut pas s'attendre à faire tourner un modèle de 70B paramètres sur un Pixel non plus, mais pour les devs qui veulent intégrer du GenAI dans leurs apps mobiles sans dépendre du cloud, c'est franchement pas mal. Et si
<a href="https://korben.info/ollama-0-133-parallelisme-puissance-experimental.html">Ollama</a>
vous permet déjà de faire tourner des modèles en local sur votre PC, ici je vous parle carrément d'appareils mobiles et d'embarqué.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/litert-google-ai-edge-inference-mobile/litert-google-ai-edge-inference-mobile-3.png" alt="" loading="lazy" decoding="async">
<p>Côté langages, y'a le choix : Kotlin et C++ pour la nouvelle API Compiled Model, Swift pour l'API Interpreter sur iOS, Python pour le desktop. Et si vous venez du monde PyTorch, un convertisseur dédié transforme vos modèles au format .tflite sans trop de douleur. L'ancienne API Interpreter reste dispo pour la rétrocompatibilité, mais à vrai dire, Google pousse clairement vers Compiled Model. Du coup, si vous aviez des projets TensorFlow Lite existants, la migration se fait en douceur parce que le format .tflite ne change pas.</p>
<p>En fait, le problème, c'est plutôt le manque de doc sur les cas tordus... et n'oubliez pas de tester vos modèles après conversion.</p>
<p>Pour ceux qui voudraient se lancer, tiens, y'a aussi un codelab de segmentation d'images en temps réel sur Android et une collection de modèles pré-entraînés sur Kaggle. Des apps d'exemple sont dispo sur GitHub pour pas repartir de zéro (détection d'objets, classification d'images, pose estimation...). Et si vous êtes plutôt Apple, sachez que
<a href="https://korben.info/mocolamma-ollama-gestion-iphone-ia-locale.html">l'IA locale sur mobile</a>
c'est clairement la tendance du moment.</p>
<p>Bref, si l'inférence embarquée ça vous parle, ça vaut clairement le coup d’œil !</p>