---
title: "Cyberbro - L'analyse d'IoC facile et en open source"
author: "Korben"
date: 2026-02-04T10:02:09.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "linux-open-source/logiciels-libres"
  - "cyberbro"
  - "Cybersécurité"
  - "IoC"
  - "open source"
rss_source: Blog
url: https://korben.info/cyberbro-analyse-ioc-osint.html
note: 0
seen: false
---

<p>Salut les amis ! Aujourd'hui, je voulais vous partager une petite pépite qu'un lecteur, <strong>Stanislas</strong>, m'a envoyée. Si vous bossez dans la cyber ou que vous passez votre temps à analyser des trucs bizarres qui trainent sur vos serveurs, vous allez adorer <strong>Cyberbro</strong>.</p>
<p>Cyberbro c'est une plateforme d'analyse d'IoC (Indicators of Compromise) en open source. Grâce à ça, au lieu de vous paluchez 15 sites différents pour vérifier une IP ou un hash, vous balancez tout dans Cyberbro. L'outil va alors extraire automatiquement les infos de vos logs et interroger une vingtaine de services comme VirusTotal, MISP, Shodan, AbuseIPDB ou même Microsoft Defender pour vous dire si c'est dangereux.</p>
<p>Sous le capot, ça gère l'extraction avancée de TLD pour ne pas se planter sur les domaines, et ça fait du &quot;pivoting&quot; automatique. En gros, ça va chercher tout seul les domaines, URLs ou IPs liés via reverse DNS et RDAP. Toutes les données sont ensuite stockées proprement dans une base SQLite locale qui sert aussi de cache, ce qui permet de ne pas flinguer vos quotas d'API si vous analysez deux fois la même chose.</p>
<img src="https://korben.info/cyberbro-analyse-ioc-osint/cyberbro-analyse-ioc-osint-1.gif" alt="" loading="lazy" decoding="async">
<p>C'est hyper fluide, ça tourne sous Python et l'interface est vraiment propre. Stanislas a même poussé le vice jusqu'à proposer une intégration MCP (Model Context Protocol) pour l'utiliser avec Claude ou Ollama. Ça permet de générer des rapports d'analyse complets via LLM en deux secondes. Et y'a même des extension navigateur pour Chrome et Firefox ainsi qu'une API. C'est ouf !</p>
<p>Franchement, pour un projet perso, ça rigole pas du tout ! D'ailleurs, c'est déjà utilisé par pas mal de SOC en France, donc c'est du sérieux.</p>
<p>Pour tester ça, c'est hyper fastoche. Un petit coup de Docker Compose et hop, c'est prêt à l'emploi. Il vous suffit de cloner le dépôt, d'éditer le fichier de secrets et de lancer le bousin.</p>
<p>Un grand merci à Stanislas pour ce superbe partage et pour tout le boulot abattu depuis un an. C'est ce genre de projet qui rend la communauté cyber plus forte 💪.</p>
<p>
<a href="https://github.com/stanfrbd/cyberbro">A découvrir ici !</a>
</p>