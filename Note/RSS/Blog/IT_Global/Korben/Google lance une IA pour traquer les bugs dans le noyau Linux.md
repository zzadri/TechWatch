---
title: "Google lance une IA pour traquer les bugs dans le noyau Linux"
author: "Korben"
date: 2026-03-18T13:27:50.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "linux-open-source"
  - "Google"
  - "Linux"
  - "sashiko"
rss_source: Blog
url: https://korben.info/google-lance-une-ia-pour-traquer-les-bugs-dans-le-noyau-linux.html
note: 0
seen: false
---

<p>Google vient de rendre public Sashiko, un outil de revue de code par intelligence artificielle qui analyse automatiquement les correctifs soumis au noyau Linux. Sur un échantillon de 1 000 bugs récents, l'IA en a détecté 53 %, alors que les relecteurs humains les avaient tous ratés sans exception.</p>
<h2 id="comment-fonctionne-sashiko">Comment fonctionne Sashiko</h2>
<p>Sashiko a été développé en interne par l'équipe Linux de Google, sous la direction de Roman Gushchin. Le principe : chaque correctif envoyé sur la liste de diffusion du noyau Linux est automatiquement analysé par une IA qui cherche les erreurs, les incohérences et les bugs potentiels.</p>
<p>Sans surprise, c'est Gemini Pro 3.1 qui fait tourner l'outil, mais il est aussi capable de tourner avec d'autres modèles, comme Claude.</p>
<p>Ce projet s'appuie sur les recherches de Chris Mason, un développeur qui rédige des prompts de revue de code pour l'IA depuis fin 2025. Sashiko va encore plus loin, car il automatise l'intégralité du processus.</p>
<p>D'ailleurs, l'outil est open source et est hébergé sur GitHub. Son transfert vers la Linux Foundation est d'ailleurs en cours, et Google continue à financer l'infrastructure ainsi que les coûts d'usage de l'IA.</p>
<h2 id="100--des-bugs-détectés">100 % des bugs détectés</h2>
<p>Le chiffre qui retient l'attention, c'est que 100 % des bugs détectés par Sashiko avaient échappé aux développeurs humains. Sur les 1 000 correctifs récents qui portaient la mention de correction de bug, l'IA a repéré plus de la moitié des problèmes.</p>
<p>Le noyau Linux reçoit des milliers de contributions chaque mois, et les mainteneurs n'ont pas toujours le temps de tout vérifier avec la même rigueur. Sashiko ne remplace pas la relecture humaine, mais il ajoute une couche de vérification qui manquait.</p>
<p>L'interface web est accessible publiquement et couvre l'ensemble des soumissions envoyées à la liste de diffusion du noyau. Tout le monde peut consulter les analyses générées par l'IA.</p>
<p>Le noyau Linux, c'est la base d'Android, de Chrome OS, du cloud de Google, d'Amazon et de Microsoft, et d'à peu près tous les serveurs qui font tourner Internet.</p>
<p>Que Google investisse pour fiabiliser ce code avec de l'IA, c'est plutôt logique. Par contre, on imagine bien que certains développeurs vont tiquer à l'idée qu'une machine relise leur travail et pointe des erreurs qu'ils n'ont pas vues.</p>
<p>La question n'est pas de savoir si l'IA va remplacer les développeurs, mais plutôt combien de temps il faudra avant que ce genre d'outil devienne la norme dans tous les gros projets open source.</p>
<p>Source :
<a href="https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review">Phoronix</a>
</p>
<p></p>