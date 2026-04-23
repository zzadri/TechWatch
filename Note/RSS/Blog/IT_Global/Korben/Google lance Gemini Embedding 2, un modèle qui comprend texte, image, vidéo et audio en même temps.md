---
title: "Google lance Gemini Embedding 2, un modèle qui comprend texte, image, vidéo et audio en même temps"
author: "Korben"
date: 2026-03-13T14:56:16.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "intelligence-artificielle/actualites-ia"
  - "gemini"
  - "gemini embedding"
  - "Google"
  - "multimodal"
rss_source: Blog
url: https://korben.info/google-lance-gemini-embedding-2-un-modele-qui-comprend-texte-image-video-et-audio-en-meme-temps.html
note: 0
seen: false
---

<p>Google vient de lancer Gemini Embedding 2, son premier modèle d'embedding nativement multimodal. Texte, images, vidéo, audio et documents sont projetés dans un même espace vectoriel, ce qui permet de faire de la recherche sémantique croisée entre différents types de contenus.</p>
<h2 id="un-seul-modèle-pour-tout-indexer">Un seul modèle pour tout indexer</h2>
<p>Jusqu'à présent, les modèles d'embedding se limitaient au texte. Vous vouliez indexer des images ou de la vidéo, il fallait un autre pipeline. Gemini Embedding 2 fait tout d'un coup : vous lui envoyez du texte, des images (jusqu'à 6), de la vidéo (jusqu'à 120 secondes) ou de l'audio (jusqu'à 80 secondes), et il vous renvoie un vecteur dans le même espace. Le modèle gère plus de 100 langues et prend en charge jusqu'à 8 192 tokens en entrée pour le texte.</p>
<p>Côté technique, le modèle utilise le Matryoshka Representation Learning, ce qui permet de choisir la taille des embeddings entre 128 et 3 072 dimensions. Google recommande 768 dimensions pour un bon compromis entre qualité et stockage, ce qui divise par quatre l'espace disque par rapport à la taille maximale.</p>
<h2 id="les-tarifs-et-la-concurrence">Les tarifs et la concurrence</h2>
<p>Le texte est facturé 0,20 dollar par million de tokens, avec un mode batch à moitié prix. Les images montent à 0,45 dollar, l'audio à 6,50 dollars et la vidéo à 12 dollars par million de tokens. Un palier gratuit est disponible pour tester.</p>
<p>Côté performances, Google affiche de bons scores sur les benchmarks MTEB : 69,9 en multilingue et 84,0 en code. Mais pour du texte seul, OpenAI reste bien moins cher avec son text-embedding-3-small à 0,02 dollar par million de tokens, soit dix fois moins.</p>
<p>Le modèle est disponible via l'API Gemini et Vertex AI, et compatible avec LangChain, LlamaIndex, Weaviate ou ChromaDB.</p>
<p>Le vrai argument de Google ici, c'est le multimodal. Si vous avez besoin d'indexer des catalogues produits avec photos et descriptions dans le même vecteur, ou de faire de la recherche dans des archives vidéo, il n'y a pas d'équivalent chez OpenAI pour le moment.</p>
<p>Mais pour du texte pur, la différence de prix est quand même importante. On attend de voir comment ça se comporte en production, et si les scores MTEB se confirment sur des cas d'usage réels.</p>
<p>Source :
<a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/">Blog Google</a>
</p>