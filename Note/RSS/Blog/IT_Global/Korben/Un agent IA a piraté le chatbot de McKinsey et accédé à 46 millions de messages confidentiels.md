---
title: "Un agent IA a piraté le chatbot de McKinsey et accédé à 46 millions de messages confidentiels"
author: "Korben"
date: 2026-03-10T09:29:57.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "failles"
  - "McKinsey"
  - "SQL"
rss_source: Blog
url: https://korben.info/un-agent-ia-a-pirate-le-chatbot-de-mckinsey-et-accede-a-46-millions-de-messages-confidentiels.html
note: 0
seen: false
---

<p>Un agent IA autonome a percé les défenses de Lilli, la plateforme d'intelligence artificielle interne de McKinsey, c'est arrivé en à peine deux heures. Au programme : 46,5 millions de messages en clair, 728 000 fichiers clients et un accès en écriture à l'ensemble de la base de données. Le tout sans aucun identifiant.</p>
<h2 id="une-injection-sql-en-2026">Une injection SQL en 2026</h2>
<p>C'est la startup de sécurité CodeWall qui a mené l'attaque, dans le cadre d'un test de pénétration. Son agent IA a commencé par scanner la documentation API de Lilli, qui était exposée publiquement. Sur les 200 points d'accès répertoriés, 22 ne demandaient aucune authentification.</p>
<p>L'un d'eux, qui servait à enregistrer les requêtes de recherche des utilisateurs, concaténait les noms de champs JSON directement dans les requêtes SQL sans aucun filtrage. Une injection SQL classique, la faille la plus documentée du web depuis vingt ans.</p>
<p>Les scanners de sécurité classiques comme OWASP ZAP étaient passés à côté, parce que les valeurs des paramètres, elles, étaient bien protégées. Mais pas les noms de champs.</p>
<h2 id="465-millions-de-messages-et-des-prompts-modifiables">46,5 millions de messages et des prompts modifiables</h2>
<p>Il a fallu seulement une quinzaine d'itérations à l'aveugle sur les messages d'erreur de la base, pour cartographier toute sa structure interne. Résultat : 46,5 millions de conversations en clair couvrant la stratégie, les fusions-acquisitions et les engagements clients de McKinsey, mais aussi 728 000 fichiers (192 000 PDF, 93 000 tableurs, 93 000 présentations), 57 000 comptes utilisateurs, 384 000 assistants IA et 3,68 millions de fragments de documents RAG avec les chemins de stockage S3.</p>
<p>Le pire, c'est que les 95 prompts système qui contrôlent le comportement de Lilli étaient accessibles en écriture. Une simple requête SQL UPDATE suffisait pour empoisonner les réponses du chatbot à l'ensemble des 40 000 consultants qui l'utilisent, sans laisser de trace.</p>
<h2 id="mckinsey-a-corrigé-en-un-jour">McKinsey a corrigé en un jour</h2>
<p>CodeWall a divulgué la faille le 1er mars, et McKinsey a réagi vite : tous les points d'accès non authentifiés ont été fermés, l'environnement de développement mis hors ligne et la documentation API retirée, le tout en une journée.</p>
<p>Histoire de rassurer tout le monde, le célèbre cabinet de conseil promet qu'aucune donnée client n'a été consultée par des personnes non autorisées. Sauf que l'adoption de Lilli dans l'entreprise est massive, puisque plus de 70% des employés de McKinsey l'utilisent au quotidien, avec quand même plus de 500 000 requêtes par mois, et une faille en place depuis... 2023 !</p>
<p>Quoi qu'il en soit, une injection SQL sur une plateforme qui tourne depuis deux ans et demi chez un cabinet qui vend du conseil en transformation numérique à, à peu près, la Terre entière, c'est quand même plus que cocasse.</p>
<p>Source :
<a href="https://www.theregister.com/2026/03/09/mckinsey_ai_chatbot_hacked/">The Register</a>
</p>