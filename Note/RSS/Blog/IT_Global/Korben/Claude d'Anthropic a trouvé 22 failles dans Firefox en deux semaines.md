---
title: "Claude d'Anthropic a trouvé 22 failles dans Firefox en deux semaines"
author: "Korben"
date: 2026-03-07T09:50:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "Anthropic"
  - "Claude"
  - "failles"
  - "Firefox"
  - "IA"
rss_source: Blog
url: https://korben.info/claude-danthropic-a-trouve-22-failles-dans-firefox-en-deux-semaines.html
note: 0
seen: false
---

<p>Anthropic et Mozilla viennent de publier les résultats d'une collaboration menée en février. En deux semaines, le modèle Claude Opus 4.6 a analysé près de 6 000 fichiers C++ du code source de Firefox et découvert 22 vulnérabilités de sécurité, dont 14 classées haute gravité. Toutes sont déjà corrigées dans Firefox 148.</p>
<h2 id="un-chasseur-de-bugs-dun-nouveau-genre">Un chasseur de bugs d'un nouveau genre</h2>
<p>C'est l'équipe de red team d'Anthropic qui a contacté Mozilla pour tester son système de détection de failles par IA sur le code source de Firefox. Le modèle Claude Opus 4.6 a d'abord été lâché sur le moteur JavaScript du navigateur, avant d'être étendu au reste de la base de code.</p>
<p>Vingt minutes après le début de l'analyse, il avait déjà identifié sa première faille : un Use After Free, un type de vulnérabilité mémoire qui peut permettre à un attaquant d'écraser des données avec du contenu malveillant. Les ingénieurs de Mozilla ont commencé à appliquer des correctifs dans les heures qui ont suivi.</p>
<p>Au total, Anthropic a soumis 112 rapports de bugs sur la période. Mozilla a souligné que la qualité des rapports a fait la différence : chaque soumission incluait un cas de test minimal, une preuve de concept et un correctif candidat. Claude a même proposé ses propres patchs pour corriger les failles qu'il trouvait.</p>
<h2 id="22-failles-dont-14-haute-gravité">22 failles dont 14 haute gravité</h2>
<p>Sur les 112 rapports, 22 ont donné lieu à des CVE (des identifiants de failles de sécurité officiels), dont 14 classées haute gravité par Mozilla. Pour donner un ordre d'idée, ces 14 failles représentent quasiment un cinquième de toutes les vulnérabilités haute gravité corrigées dans Firefox sur l'ensemble de l'année 2025. Les 90 bugs restants sont de moindre gravité, mais la plupart sont désormais corrigés. Tout est intégré dans Firefox 148, disponible depuis le 24 février.</p>
<p>Firefox n'est pas le seul projet concerné. Anthropic indique avoir utilisé Claude Opus 4.6 pour repérer des vulnérabilités dans d'autres logiciels open source, dont le noyau Linux.</p>
<h2 id="trouver-les-failles-mais-pas-les-exploiter">Trouver les failles, mais pas les exploiter</h2>
<p>Côté offensif, le constat est quand même rassurant. Anthropic a aussi testé la capacité de Claude à exploiter les failles qu'il trouvait, pas seulement les détecter. L'équipe a dépensé environ 4 000 dollars en crédits API pour tenter de produire des exploits fonctionnels. Sur plusieurs centaines d'essais, seuls deux ont abouti, et encore : uniquement dans un environnement de test où la sandbox de Firefox avait été désactivée. Le modèle est bien meilleur pour trouver les bugs que pour les exploiter, et le coût de détection est dix fois inférieur à celui de l'exploitation.</p>
<p>C’est le genre de résultat qui change un peu la perception de l'IA dans la cybersécurité. On a beaucoup parlé du risque que des modèles comme Claude ou GPT servent à créer des attaques. Et là, c'est l'inverse : l'IA trouve les failles plus vite et pour moins cher que n'importe quel audit traditionnel, mais elle a encore du mal à les exploiter. </p>
<p>L'avantage est clairement du côté des défenseurs, pour l'instant en tous cas. Mozilla a d'ailleurs annoncé avoir déjà intégré l'analyse assistée par IA dans ses processus de sécurité internes. En tout cas, quand une IA trouve en deux semaines autant de failles critiques qu'un an de recherches classiques, on comprend assez vite que le métier de la cybersécurité va changer.</p>
<p>Sources :
<a href="https://www.anthropic.com/news/mozilla-firefox-security">Anthropic</a>
,
<a href="https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/">Mozilla</a>
</p>