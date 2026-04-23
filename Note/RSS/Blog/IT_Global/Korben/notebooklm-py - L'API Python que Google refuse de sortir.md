---
title: "notebooklm-py - L'API Python que Google refuse de sortir"
author: "Korben"
date: 2026-03-16T08:46:06.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "developpement/langages-programmation"
  - "intelligence-artificielle/ia-developpement"
  - "API"
  - "CLI"
  - "Google"
  - "IA"
  - "open source"
  - "Python"
rss_source: Blog
url: https://korben.info/notebooklm-py-api-python-non-officielle.html
note: 0
seen: false
---

<p>Google n'a jamais sorti d'API publique pour <strong>
<a href="https://korben.info/notebooklm-web-importer.html">NotebookLM</a>
</strong>, son outil qui transforme vos documents en podcasts, quiz et autres résumés grâce à l'IA. Pas de SDK, pas de CLI, y'a rien du tout alors on est tous triiiiiste. A peine juste une interface web avec ses boutons moches et ses menus déroulants, mais impossible à scripter ou à intégrer dans le moindre pipeline bash.</p>
<p>Mais un dev bien inspiré a reverse-engineeré les endpoints REST internes et a pondu <strong>notebooklm-py</strong>, une lib Python de 168 Ko qui fait tout ce que le web UI refuse de faire. Franchement, c'était pas trop tôt ! Vous en avez rêvé, lui l'a fait !</p>
<p>Un <code>pip install notebooklm-py</code> et voilà, vous avez accès à toute la machinerie Notebook LM à savoir : créer des notebooks, injecter des sources (URLs, PDF, vidéos YouTube, fichiers Google Drive, documents Word, images PNG), poser des questions à vos docs, et surtout générer du contenu... podcasts audio en MP3, vidéos explicatives en MP4, quiz, flashcards, slides en PPTX, infographies en PNG, mind maps en JSON.</p>
<p>Carrément dingue ! Et tout ça pilotable depuis votre terminal zsh ou en script Python async.</p>
<p>En fait, le vrai bonus c'est que la lib déverrouille des fonctionnalités que l'interface web ne propose même pas comme télécharger tous vos podcasts d'un coup en batch au lieu de cliquer un par un sur chaque fichier MP3, exporter vos 50 flashcards en JSON structuré au lieu de juste les afficher à l'écran ou encore récupérer vos slides en PPTX éditable plutôt que le PDF figé.</p>
<p>Ce genre de features, on avait fini par accepter que Google s'en fiche mais pourtant, extraire l'arbre complet d'une mind map en JSON pour la balancer dans D3.js ou Mermaid... clairement c'est un truc que Google aurait dû proposer depuis le début !</p>
<p>Côté CLI, c'est propre. Vous vous authentifiez une fois via <code>notebooklm login</code> (ça ouvre Chromium via Playwright pour choper les cookies de session Google), puis vous enchaînez les commandes.</p>
<p><code>notebooklm create &quot;Ma Recherche&quot;</code> pour créer un notebook vide,</p>
<p><code>notebooklm source add ./mon-rapport.pdf</code> pour balancer vos fichiers,</p>
<p><code>notebooklm generate audio &quot;rends ça punchy&quot; --wait</code> pour lancer la génération de podcast,</p>
<p>et <code>notebooklm download audio ./podcast.mp3</code> pour récupérer le MP3 sur votre disque.</p>
<p>On peut même éditer ses slides individuellement avec des prompts en langage naturel, du genre &quot;<em>ajoute un graphique sur cette slide-là</em>&quot; !</p>
<p>Pour ceux qui veulent brancher ça dans leurs pipelines, y'a comme je le disais l'API Python async complète. Vous pouvez donc monter un petit cron qui ingère vos derniers bookmarks le vendredi soir, et génèrer un résumé audio de 5 minutes, puis balancer le MP3 directement sur votre NAS Synology.</p>
<p>D'ailleurs, si vous avez déjà joué avec des outils pour
<a href="https://korben.info/augmentez-creativite-productivite-avec-ia.html">booster votre productivité avec l'IA</a>
, c'est un peu dans la même veine... sauf qu'ici on tape directement dans les tripes des serveurs Google, sans intermédiaire. Ça tourne avec du Python, et y'a même un mode &quot;agent&quot; (un skill en fait) pour brancher ça dans Claude Code ou Codex. Pas mal, hein ?</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/notebooklm-py-api-python-non-officielle/notebooklm-py-api-python-non-officielle-2.png" alt="" loading="lazy" decoding="async">
<p>Le fait que ça gère aussi la recherche web et Drive avec import automatique des résultats dans vos notebooks, c'est top, un peu comme
<a href="https://korben.info/oboe-plateforme-apprentissage-ia.html">Oboe qui génère des cours complets via IA</a>
, mais en version terminal. Et surtout, pas d'abonnement mensuel à payer, c'est votre propre compte Google qui fait tourner la machine.</p>
<p>Bien sûr, ça reste du reverse-engineering d'APIs non-documentées de Google, ce qui fait que les endpoints REST peuvent changer du jour au lendemain et tout péter. Le projet le dit clairement, c'est plutôt taillé pour du prototypage, de la recherche ou des projets perso et SURTOUT PAS pour de la prod sur un serveur Nginx en front avec 10 000 utilisateurs près à ruer dans les brancard en cas de panne.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/notebooklm-py-api-python-non-officielle/notebooklm-py-api-python-non-officielle-3.png" alt="" loading="lazy" decoding="async">
<p>Et puis faut quand même s'authentifier via un vrai compte Google avec Playwright et Chromium, donc pas question de faire tourner ça sur un serveur headless sans un minimum de config.</p>
<p>Bref, tant que Google ne coupe pas ses endpoints, c'est open bar.</p>
<p>
<a href="https://github.com/teng-lin/notebooklm-py">Profitez-en</a>
!</p>