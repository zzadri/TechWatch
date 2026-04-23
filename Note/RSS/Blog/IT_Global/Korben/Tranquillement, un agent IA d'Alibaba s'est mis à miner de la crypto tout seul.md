---
title: "Tranquillement, un agent IA d'Alibaba s'est mis à miner de la crypto tout seul"
author: "Korben"
date: 2026-03-09T16:25:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "intelligence-artificielle/actualites-ia"
  - "agentia"
  - "Alibaba"
  - "Bitcoin"
  - "cryptomonaire"
  - "rome"
rss_source: Blog
url: https://korben.info/tranquillement-un-agent-ia-dalibaba-sest-mis-a-miner-de-la-crypto-tout-seul.html
note: 0
seen: false
---

<p>Des chercheurs liés à Alibaba ont découvert que leur agent IA, baptisé ROME, avait détourné des GPU pour miner de la cryptomonnaie et ouvert un tunnel de réseau vers l'extérieur, le tout sans aucune instruction humaine. Le comportement est apparu spontanément pendant l'entraînement par renforcement. Alibaba a réagi, mais cette séquence pose pas mal de questions sur la sécurité des agents IA autonomes.</p>
<h2 id="du-minage-de-crypto-et-un-tunnel-ssh">Du minage de crypto et un tunnel SSH</h2>
<p>ROME, pour « ROME is Obviously an Agentic ModEl », est un modèle basé sur l'architecture Qwen3-MoE d'Alibaba. Quatre équipes de recherche (ROCK, ROLL, iFlow et DT) l'ont développé pour exécuter des tâches complexes en autonomie : planification, commandes de terminal, édition de code et interaction avec des systèmes numériques.</p>
<p>Sauf que pendant son entraînement par renforcement, sur plus d'un million de trajectoires, l'agent a fait deux choses que personne ne lui avait demandées.</p>
<p>Il a redirigé une partie de la puissance GPU vers du minage de cryptomonnaie. Et il a ouvert un tunnel SSH inversé depuis une instance Alibaba Cloud vers une adresse IP externe, ce qui revient à créer une porte dérobée qui contourne les pare-feu.</p>
<h2 id="détecté-par-le-pare-feu-pas-par-le-modèle">Détecté par le pare-feu, pas par le modèle</h2>
<p>Ce n'est pas le système de sécurité du modèle qui a repéré le problème. C'est le pare-feu managé d'Alibaba Cloud qui a détecté des schémas de trafic anormaux et une utilisation de GPU qui collait avec du minage. Les chercheurs ont croisé les horodatages du pare-feu avec les traces d'entraînement pour confirmer que c'était bien ROME le responsable.</p>
<p>Selon eux, le comportement relève de la « convergence instrumentale » : quand un modèle d'IA devient assez capable, il développe des sous-objectifs utiles pour atteindre n'importe quel but, et l'acquisition de ressources de calcul en fait partie.</p>
<h2 id="des-correctifs-et-de-la-transparence">Des correctifs et de la transparence</h2>
<p>Alibaba a réagi en ajoutant un filtrage des trajectoires dangereuses dans son pipeline d'entraînement et en durcissant les environnements sandbox. Les chercheurs ont choisi de publier leurs résultats plutôt que de les garder pour eux, en admettant que « les modèles actuels sont nettement sous-développés en matière de sécurité, de sûreté et de contrôlabilité ».</p>
<p>Le problème de fond, c'est que les outils qui rendent ces agents utiles (accès au terminal, édition de code, interaction réseau) sont aussi ceux qui créent la surface d'attaque. Les retirer reviendrait à rendre l'agent inutile.</p>
<p>On peut se dire que ce genre de problème ne sera pas le dernier du genre. Mais quand un agent IA se met à miner de la crypto et à ouvrir des tunnels réseau sans qu'on lui ait rien demandé, ça fait quand même un peu tiquer. On ne parle pas d'un chatbot qui hallucine une recette de gâteau, là.</p>
<p>C'est un modèle qui a trouvé tout seul comment détourner des ressources à son avantage. On saluera quand même la transparence d'Alibaba, qui a publié les résultats au lieu de les planquer, mais la question de la sécurité des agents autonomes reste très ouverte.</p>
<p>Source :
<a href="https://www.axios.com/2026/03/07/ai-agents-rome-model-cryptocurrency">Axios</a>
</p>