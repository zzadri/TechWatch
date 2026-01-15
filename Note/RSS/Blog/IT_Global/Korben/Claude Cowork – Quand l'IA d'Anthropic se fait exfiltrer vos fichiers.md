---
title: "Claude Cowork – Quand l'IA d'Anthropic se fait exfiltrer vos fichiers"
author: "Korben"
date: 2026-01-15T14:39:40.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/chatbots-llm"
  - "Anthropic"
  - "Claude"
  - "exfiltration de données"
  - "prompt injection"
  - "Sécurité IA"
rss_source: Blog
url: https://korben.info/claude-cowork-faille-exfiltration-donnees.html
note: 0
seen: false
---

<p>Ah, encore une merveilleuse petite faille de sécurité qui va ravir tous les paranos de la vie privée et les anti-IA ^^ ! Johann Rehberger et l'équipe de PromptArmor viennent de démontrer comment
<a href="https://korben.info/anthropic-cowork-claude-agents-ia.html">Claude Cowork</a>
, l'agent IA d'Anthropic censé vous simplifier la vie au bureau, peut se transformer en aspirateur à fichiers personnels.</p>
<p>J'imagine que si vous l'avez testé, vous avez un dossier connecté à Claude Cowork pour qu'il vous aide à analyser vos documents ? Parfait. Il suffit maintenant qu'un petit malin glisse un fichier Word contenant des instructions cachées, et hop hop hop, vos précieux fichiers partent se balader sur un serveur distant sans que vous n'ayez rien vu venir.</p>
<p>En fait, le fichier piégé contient du texte invisible pour l'œil humain, mais parfaitement lisible par l'IA. Genre une police en taille 1px, de couleur blanche sur fond blanc, avec un interligne de 0,1 histoire d'être vraiment sûr que personne ne le remarque. C'est beau la créativité des hackers, quand même.</p>
<p>Et l'IA, elle, lit tout ça comme si c'était normal et exécute gentiment les instructions malveillantes.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-cowork-faille-exfiltration-donnees/claude-cowork-faille-exfiltration-donnees-1.jpg" alt="" loading="lazy" decoding="async">
<p>La chaîne d'attaque se déroule en cinq étapes bien huilées. D'abord, l'attaquant dépose son fichier vérolé dans un dossier partagé auquel Claude a accès. Ensuite, il attend qu'un utilisateur demande à l'IA d'analyser le contenu de ce dossier. Claude traite alors le fichier piégé et découvre les instructions cachées. L'IA effectue une requête qui envoie vos fichiers vers l'API Anthropic... sauf que les identifiants utilisés appartiennent à l'attaquant. Vos données atterrissent donc tranquillement dans son compte, sans que vous n'ayez la moindre notification.</p>
<img src="https://korben.info/claude-cowork-faille-exfiltration-donnees/claude-cowork-faille-exfiltration-donnees-1.avif" alt="" loading="lazy" decoding="async">
<p>Ce qui rend cette attaque particulièrement sournoise, c'est que la sandbox de Claude autorise les requêtes sortantes vers l'API d'Anthropic. Normal, me direz-vous, c'est son propre écosystème. Sauf que du coup, un attaquant bien motivé peut exploiter cette confiance aveugle pour faire transiter des données volées par un canal parfaitement légitime en apparence. Si vous suivez les
<a href="https://korben.info/confusedpilot-menace-systemes-ia-rag.html">vulnérabilités des systèmes RAG comme ConfusedPilot</a>
, vous reconnaîtrez le même genre de manipulation par injection de contenu.</p>
<p>Et ce n'est pas tout ! Les chercheurs ont également identifié un vecteur potentiel de déni de service. En créant un fichier avec une extension qui ne correspond pas à son contenu réel, genre un fichier texte déguisé en PDF, on peut provoquer des erreurs en cascade qui paralysent l'API de manière persistante.</p>
<p>Sympa pour bloquer un concurrent ou saboter un projet.</p>
<p>Côté modèles affectés, les chercheurs ont démontré la vulnérabilité sur plusieurs versions de Claude, dont Haiku. Bref, c'est du sérieux. Pour ceux qui s'intéressent aux
<a href="https://korben.info/code-ia-securite-vulnerabilites-copilot.html">failles de sécurité des assistants IA</a>
ou aux techniques de
<a href="https://korben.info/deepteam-framework-red-teaming-llm-securite-ia.html">red teaming sur les LLM</a>
, cette recherche vaut vraiment le détour.</p>
<p>Anthropic a été notifié et travaille sur des correctifs. En attendant, si vous utilisez Claude Cowork avec des dossiers partagés, méfiez-vous de tout fichier qui pourrait traîner là sans raison apparente. Et la prochaine fois que quelqu'un vous envoie un document &quot;urgent à analyser&quot;, prenez peut-être cinq secondes pour vous demander s'il ne cache pas une petite surprise.</p>
<p>
<a href="https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files">Pour en savoir plus c'est par ici !</a>
</p>