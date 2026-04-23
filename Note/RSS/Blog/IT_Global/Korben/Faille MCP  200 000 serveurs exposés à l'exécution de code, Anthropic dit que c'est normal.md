---
title: "Faille MCP : 200 000 serveurs exposés à l'exécution de code, Anthropic dit que c'est normal"
author: "Korben"
date: 2026-04-17T09:11:50.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "Anthropic"
  - "faille mcp"
  - "mcp"
rss_source: Blog
url: https://korben.info/faille-mcp-200-000-serveurs-exposes-a-lexecution-de-code-anthropic-dit-que-cest-normal.html
note: 0
seen: false
---

<p>200 000 serveurs. C'est le nombre de machines potentiellement exposées à l'exécution de commandes système arbitraires via une faille de conception dans le SDK MCP d'Anthropic, d'après les chercheurs d'OX Security.</p>
<p>L'interface STDIO du protocole permet de créer des sous-processus sans contrôle, ce qui ouvre la porte à n'importe quelle commande OS sur la machine hôte.</p>
<p>Le problème touche tous les langages supportés par le SDK : Python, TypeScript, Java, Rust. Et les packages concernés totalisent plus de 150 millions de téléchargements. Les chercheurs ont documenté quatre classes de vulnérabilité. D'abord de l'injection de commandes non authentifiée, testée sur LangFlow (toutes les versions) et GPT Researcher</p>
<p>Ensuite des contournements de sécurité sur Upsonic et Flowise. Et puis de l'injection de prompt zero-click dans des IDE comme Windsurf, Cursor, Gemini-CLI et GitHub Copilot. Et enfin du &quot;marketplace poisoning&quot; : 9 marketplaces MCP sur 11 testées ont accepté un serveur malveillant de démonstration sans broncher.</p>
<p>10 CVE de niveau élevé ou critique ont été émis. OX Security a mené plus de 30 processus de divulgation responsable depuis novembre 2025, avant de rendre les résultats publics en avril.</p>
<p>La réponse d'Anthropic est celle qui fait grincer des dents. La boîte considère que le comportement est &quot;attendu&quot; et a refusé de modifier l'architecture du SDK. Elle a publié des recommandations de sécurité mises à jour, mais selon les chercheurs, &quot;ça n'a rien corrigé&quot;. En clair, Anthropic estime que la sécurité de l'interface STDIO est du ressort de l'utilisateur qui déploie, pas du protocole lui-même.</p>
<p>C'est quand même un positionnement gênant, MCP est devenu un standard de facto pour connecter des modèles IA à des outils externes, et des milliers d'entreprises et de développeurs l'ont adopté.</p>
<p>Si le SDK officiel laisse passer de l'exécution de code arbitraire par design, et que la réponse officielle est &quot;c'est voulu, sécurisez vous-mêmes&quot;, la responsabilité est déplacée vers l'aval sans filet.</p>
<p>Bref, si vous déployez du MCP en prod, les recommandations d'OX Security valent le détour. Anthropic ne corrigera pas à votre place.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw">The Register</a>
</p>