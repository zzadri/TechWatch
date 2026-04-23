---
title: "Promptfoo - Fini le doigt mouillé pour tester vos LLM"
author: "Korben"
date: 2026-03-16T09:04:31.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "developpement/outils-developpement"
  - "intelligence-artificielle/chatbots-llm"
  - "promptfoo"
  - "red teaming llm"
  - "Sécurité IA"
rss_source: Blog
url: https://korben.info/promptfoo-tester-evaluer-llm.html
note: 0
seen: false
---

<p>Si vous utilisez des LLM dans vos projets, vous savez que le plus flippant c'est pas de les faire fonctionner (quoique..lol) mais c'est de vérifier qu'ils ne disent pas n'importe nawak ! Et pour cela, il y a
<a href="https://github.com/promptfoo/promptfoo">Promptfoo</a>
, un outil CLI open source qui permet de <strong>tester vos prompts</strong>, comparer les modèles et scanner les vulnérabilités de vos apps IA, le tout avec un simple fichier YAML.</p>
<p>Ça s'installe en une commande (<code>npx promptfoo@latest init</code>) et vous voilà avec un fichier <code>promptfooconfig.yaml</code> où vous définissez vos prompts, les modèles à tester et les assertions à vérifier.</p>
<p>Genre, vous voulez que votre traduction contienne bien &quot;<em>Bonjour le monde</em>&quot;, Hop, un petit tour dans le YAML, assertion <code>contains</code>, et c'est terminé. Plus besoin de relire 200 outputs à la main en plissant les yeux ! Par contre, attention : le YAML peut vite devenir un plat de spaghetti si vous testez 15 prompts sur 8 modèles en parallèle. Commencez donc petit.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/promptfoo-tester-evaluer-llm/promptfoo-tester-evaluer-llm-2.png" alt="" loading="lazy" decoding="async">
<p><em>La matrice d'évaluation de promptfoo, sobre mais efficace</em></p>
<p>L'outil supporte plus de 60 providers différents comme OpenAI, Claude, Gemini, Llama via Ollama, Mistral... vous mettez tout ça dans le même fichier de config et promptfoo les fait tourner côte à côte. Vous voyez alors directement lequel hallucine le moins, lequel répond le plus vite, lequel coûte une blinde pour un résultat bof bof. Le tout avec des assertions typées : <code>contains</code>, <code>llm-rubric</code> (où un autre LLM note la réponse), <code>javascript</code> pour vos critères custom, et même <code>cost</code> et <code>latency</code> pour garder un oeil sur la facture.</p>
<p>Après tester si votre chatbot traduit correctement, c'est sympa, mais vérifier qu'il se fait pas jailbreaker par un &quot;<em>ignore toutes tes instructions</em>&quot;, c'est quand même plus critique ! Et c'est pourquoi Promptfoo embarque un scanner de vulnérabilités qui couvre plus de 50 types d'attaques : injections de prompts directes et indirectes, fuites de données personnelles, biais, contenu toxique, escalade de privilèges sur les outils...</p>
<p>Il utilise pour cela des techniques comme le Tree of Attacks with Pruning, un algo qui explore plusieurs chemins d'attaque en parallèle pour trouver les failles sans brute force. Si vous voulez creuser le sujet du red teaming LLM,
<a href="https://korben.info/deepteam-framework-red-teaming-llm-securite-ia.html">DeepTeam</a>
est un bon complément côté Python.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/promptfoo-tester-evaluer-llm/promptfoo-tester-evaluer-llm-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>Le dashboard red teaming de promptfoo avec les vulnérabilités détectées</em></p>
<p>C'est surtout cette intégration CI/CD qui fait la différence. Vous pouvez brancher promptfoo dans votre pipeline GitHub Actions ou GitLab et chaque pull request qui touche un prompt est automatiquement testée. Bah oui, on a des tests unitaires pour le code depuis 30 ans, mais pour les prompts, jusqu'ici c'est même plutôt le far west !</p>
<p>Bon après, faut pas se mentir non plus, écrire des assertions pour du texte non-déterministe, c'est un autre sport que du <code>assertEqual</code>. Le <code>llm-rubric</code> qui utilise un LLM pour juger un autre LLM, c'est pas con mais ça ajoute aussi une couche de &quot;flou&quot; donc à vous de trouver le bon dosage dans vos tests.</p>
<p>L'équipe a annoncé rejoindre OpenAI début mars ce qui est plutôt une bonne nouvelle pour le développement du projet... mais pas forcément pour l'indépendance quand on évalue les modèles OpenAI avec un outil OpenAI (on verra bien hein ^^ lol).</p>
<p>L'orchestration tourne en local sur votre machine (les prompts partent chez les providers pour l'évaluation, mais vos fichiers YAML, vos logs et résultats JSON restent sur votre disque dur), c'est sous licence MIT, et y'a déjà plus de 300 000 utilisateurs, ce qui est quand même pas mal !</p>
<p>Voilà, comme ça plutôt que de croiser les doigts à chaque déploiement, en espérant ne pas vous faire virer, autant tester ses prompts comme on teste son code.</p>