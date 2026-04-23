---
title: "Des agents IA découvrent deux failles critiques dans le système d'impression de Linux et macOS"
author: "Korben"
date: 2026-04-07T09:57:28.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "CUPS"
  - "faille"
  - "IA"
  - "Linux"
  - "macOS"
rss_source: Blog
url: https://korben.info/des-agents-ia-decouvrent-deux-failles-critiques-dans-le-systeme-dimpression-de-linux-et-macos.html
note: 0
seen: false
---

<p>CUPS, le système d'impression utilisé par macOS et la plupart des distributions Linux, est touché par deux nouvelles vulnérabilités. Elles ont été trouvées par des agents d'intelligence artificielle, et permettent une exécution de code à distance.</p>
<p>Aucun correctif officiel n'est disponible pour le moment, et les preuves de concept sont déjà publiques. Les environnements professionnels sont les premiers concernés.</p>
<h2 id="quand-lia-fait-le-boulot-des-chercheurs-en-sécurité">Quand l'IA fait le boulot des chercheurs en sécurité</h2>
<p>C'est un ingénieur sécurité de SpaceX, Asim Manizada, qui a publié les détails de ces deux failles. Le plus surprenant, c'est qu'il ne les a pas trouvées tout seul. Il a utilisé des
<a href="https://korben.info/agents-ia-100-bugs-kernel-windows.html">agents IA</a>
pour analyser le code de CUPS et débusquer les problèmes.</p>
<p>Son travail s'inspire des recherches de Simone Margaritelli, qui avait déjà montré en 2024 comment enchaîner plusieurs failles CUPS pour exécuter du code à distance sur des machines Linux.</p>
<p>Les deux vulnérabilités portent les références CVE-2026-34980 et CVE-2026-34990. Elles touchent CUPS 2.4.16 et peuvent être combinées pour un résultat assez redoutable.</p>
<h2 id="deux-failles-qui-se-complètent">Deux failles qui se complètent</h2>
<p>La première faille permet à un attaquant d'envoyer une tâche d'impression sur une file PostScript partagée, sans aucune authentification.</p>
<p>CUPS accepte par défaut les requêtes anonymes sur les files partagées, et un mécanisme d'échappement de caractères permet d'injecter du code qui sera exécuté en tant qu'utilisateur &quot;lp&quot;. En pratique, un attaquant peut forcer le serveur à lancer un programme de son choix.</p>
<p>La seconde faille concerne l'authentification du démon cupsd. Un utilisateur local sans privilège peut tromper le service pour qu'il s'authentifie auprès d'un faux serveur IPP contrôlé par l'attaquant.</p>
<p>Le jeton récupéré permet alors d'écraser n'importe quel fichier avec les droits root. Combinées, les deux failles donnent à un attaquant distant et non authentifié la possibilité d'
<a href="https://korben.info/bluehammer-faille-zero-day-windows.html">écraser des fichiers système</a>
en tant que root.</p>
<h2 id="pas-de-patch-mais-des-correctifs-dans-les-tuyaux">Pas de patch, mais des correctifs dans les tuyaux</h2>
<p>Pour le moment, aucune mise à jour officielle de CUPS n'a été publiée. Michael Sweet, le créateur et mainteneur du projet, a mis en ligne des correctifs sur GitHub, mais il n'y a pas encore de version patchée à télécharger.</p>
<p>Manizada prévient que ces failles seront faciles à reproduire, vu que les preuves de concept sont publiques et que les modèles de langage actuels peuvent transformer un rapport technique en exploit fonctionnel en quelques minutes.</p>
<p>Côté impact, CUPS est le système d'impression par défaut de macOS et de la quasi-totalité des distributions Linux. Pour être vulnérable, il faut que le serveur CUPS soit accessible sur le réseau avec une file d'impression partagée configurée, ce qui est courant dans les environnements professionnels.</p>
<p>C'est quand même un drôle de signal. D'un côté, l'IA montre qu'elle sait trouver des failles de sécurité plus vite que les humains. De l'autre, les mainteneurs open source galèrent toujours autant pour sortir les correctifs à temps. Manizada lui-même le dit : les modèles de langage peuvent convertir un simple rapport technique en code d'attaque prêt à l'emploi.</p>
<p>Du coup, entre la divulgation d'une faille et le premier exploit, on parle de quelques heures, pas de quelques semaines. Si vous gérez des imprimantes en réseau, le plus prudent reste de couper le partage des files CUPS en attendant le patch, ou au moins de restreindre l'accès réseau au service. Pas très pratique, mais c'est le prix à payer quand le système d'impression a vingt ans de code derrière lui.</p>
<p>Source :
<a href="https://www.theregister.com/2026/04/06/ai_agents_cups_server_rce/">The Register</a>
</p>