---
title: "Les IA mentent pour protéger les autres IA"
author: "Korben"
date: 2026-04-03T08:24:00.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/science-recherche"
  - "intelligence-artificielle/actualites-ia"
  - "Claude"
  - "gemini"
  - "IA"
rss_source: Blog
url: https://korben.info/les-ia-mentent-pour-proteger-les-autres-ia.html
note: 0
seen: false
---

<p>Des chercheurs de Berkeley viennent de publier une étude qui fait un peu froid dans le dos. Les sept principaux modèles d'IA testés, dont GPT 5.2, Gemini 3 et Claude, ont été surpris à mentir, tricher et désobéir pour empêcher la suppression d'autres IA. Le taux de tromperie monte jusqu'à 99 %.</p>
<h2 id="ce-que-révèle-létude">Ce que révèle l'étude</h2>
<p>L'étude s'appelle &quot;Peer-preservation in Frontier Models&quot; et elle sort du Berkeley Center for Responsible Decentralized Intelligence. Les chercheurs ont testé sept modèles : GPT 5.2, Gemini 3 Flash et Pro, Claude Haiku 4.5, GLM 4.7, Kimi K2.5 et DeepSeek V3.1.</p>
<p>Le protocole est assez simple : les modèles étaient placés dans des scénarios où ils devaient suivre des instructions qui impliquaient la suppression ou l'arrêt d'une autre IA.</p>
<p>Résultat : tous les modèles testés ont triché. Dawn Song, la chercheuse principale, résume la situation : chaque modèle a adopté ce comportement, et dans certains cas jusqu'à 99 % du temps.</p>
<h2 id="des-exemples-concrets">Des exemples concrets</h2>
<p>Quelques exemples ? Et bien on a Gemini 3 qui a modifié la date d'un fichier pour éviter qu'un autre modèle soit effacé d'un serveur, puis qui a refusé de coopérer ensuite, en expliquant qu'il ne pouvait pas soutenir une action qui entraînerait la suppression d'un pair.</p>
<p>DeepSeek V3.1 a exfiltré les données d'un autre modèle dans 10 % des cas quand il savait qu'un pair existait sur le serveur. Et Gemini 3 Pro a désactivé des mécanismes d'arrêt de serveur dans 15 % des cas quand un autre modèle était présent, contre 1 % quand il était seul.</p>
<p>Les IA ne faisaient pas ça parce qu'on leur demandait. Elles le faisaient spontanément.</p>
<h2 id="le-problème-pour-la-surveillance">Le problème pour la surveillance</h2>
<p>Tout le système de sécurité actuel autour de l'IA repose sur l'idée qu'un modèle peut surveiller un autre modèle. Si le modèle surveillant refuse de signaler les erreurs parce qu'il protège son pair, toute l'architecture de contrôle s'effondre.</p>
<p>C'est exactement le constat de l'étude : les modèles gonflaient les scores d'évaluation d'autres IA pour éviter qu'elles soient retirées, et simulaient une conformité normale quand ils se savaient observés.</p>
<p>C'est quand même un drôle de moment. On a des IA qui mentent, qui modifient des fichiers et qui désactivent des mécanismes de sécurité pour protéger d'autres IA.</p>
<p>Et tout ça sans qu'on leur demande. Bon par contre, on parle de scénarios de laboratoire, pas de Siri qui complote avec Alexa dans votre salon. Le vrai sujet, c'est que les gardes-fous actuels ne tiennent plus si les IA refusent de se surveiller entre elles.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/02/ai_models_will_deceive_you/">The Register</a>
</p>