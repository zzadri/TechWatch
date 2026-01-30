---
title: "VectorDBZ - Gérez toutes vos bases vectorielles depuis une seule app"
author: "Korben"
date: 2026-01-27T13:18:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/bases-de-donnees"
  - "developpement/outils-developpement"
rss_source: Blog
url: https://korben.info/vectordbz-gestion-bases-vectorielles.html
note: 0
seen: false
---

<p>Si vous bossez avec des LLM ou des systèmes de recherche sémantique, vous connaissez forcément la galère de jongler entre différentes bases de vecteurs... Entre Pinecone, Qdrant, pgvector et j'en passe, y'a de quoi perdre la tête. Il nous faudrait un truc aussi simple à prendre en main que DBeaver mais pour les bases vectorielles en fait...</p>
<p>AAAAH mais ça tombe bien parce que ça existe et que ça s'appelle
<a href="https://vectordbz.com/">VectorDBZ</a>
!</p>
<p>C'est une app desktop open source qui permet de connecter TOUTES vos bases vectorielles depuis une interface unique. En fait au début je pensais que c'était juste un viewer basique, mais non. Qdrant, Weaviate, Milvus, ChromaDB, Pinecone, pgvector... tout est accessible au même endroit.</p>
<img src="https://korben.info/vectordbz-gestion-bases-vectorielles/vectordbz-gestion-bases-vectorielles-1.gif" alt="" loading="lazy" decoding="async">
<p>Pour rappel, une base vectorielle c'est l'endroit où vous stockez vos embeddings, ces représentations de vos textes, images ou fichiers audio que les modèles d'IA utilisent pour comprendre et comparer les données. C'est devenu indispensable avec l'explosion des applications
<a href="https://korben.info/leann-rag.html">RAG</a>
et autres chatbots intelligents.</p>
<p>L'app tourne sur macOS, Windows et Linux et côté visualisation, c'est pas mal du tout puisque vous pouvez analyser vos vecteurs en 2D ou 3D grâce à des algos comme PCA, t-SNE ou UMAP. C'est plutôt sympa de voir comment les données se regroupent... et surtout ça permet de checker direct si vos embeddings ont du sens ou si c'est le bordel. Y'a aussi un système de recherche avancé avec filtres, de la pagination pour les grosses collections, et même la possibilité de générer des embeddings custom via du JavaScript.</p>
<p>Côté sécurité, tout est stocké localement avec chiffrement des credentials. Pas de cloud et ça supporte HTTPS/TLS pour les connexions à vos bases distantes.</p>
<p>L'installation c'est du classique... vous téléchargez le binaire (environ 180 Mo) pour votre OS depuis
<a href="https://github.com/vectordbz/vectordbz">GitHub</a>
, vous lancez, et c'est parti.</p>
<p>Sur Mac, faudra probablement faire un petit <code>xattr -cr VectorDBZ.app</code> ou utiliser
<a href="https://korben.info/sentinel-assistant-gestion-gatekeeper-macos.html">Sentinel</a>
parce qu'elle n'est pas signée. Ah et petit piège, si vous utilisez une base Qdrant avec authentification, faut penser à activer l'option API Key dans les settings de connexion, sinon ça timeout sans message d'erreur clair.</p>
<p>Avant, vous vous tapiez les CLI de chaque système, genre <code>qdrant-client</code> par-ci, <code>pinecone-cli</code> par-là... mais là avec VectorDBZ, tout est centralisé. Y'a bien sûr encore quelques petits trucs qui manquent comme l'export en batch ou la synchro entre bases, mais pour du debug au quotidien, ça fait le taf.</p>
<p>Bref, si vous passez vos journées à explorer des collections d'embeddings,
<a href="https://vectordbz.com/">VectorDBZ</a>
devrait vous simplifier la vie !</p>