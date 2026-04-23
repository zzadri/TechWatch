---
title: "Faux entretiens d'embauche - Le piège qui vise les devs Next.js"
author: "Korben"
date: 2026-02-26T13:26:50.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/malwares-menaces"
  - "developpement"
  - "analyse de malware"
  - "NPM"
  - "phishing"
  - "supply chain attack"
rss_source: Blog
url: https://korben.info/fausses-interviews-malware-nextjs-devs.html
note: 0
seen: false
---

<p><strong>Des faux entretiens d'embauche avec des repos GitHub vérolés pour piéger les devs Next.js</strong>... on croit rêver et pourtant,
<a href="https://www.microsoft.com/en-us/security/blog/2026/02/24/c2-developer-targeting-campaign/">Microsoft vient de documenter cette campagne ciblée</a>
et vous allez voir, c'est violent.</p>
<p>En fait, un groupe de hackers se fait actuellement passer pour des recruteurs et contacte des développeurs JavaScript en leur proposant un entretien technique. Le deal c'est de cloner un repo GitHub pour un &quot;test de compétences&quot;... sauf que le repo en question est truffé de malware.</p>
<p>Microsoft a ainsi identifié plusieurs vecteurs d'infection planqués dans ces repos. Le premier, c'est via les fichiers de configuration VS Code, c'est à dire ceux dans le dossier <code>.vscode/</code>, qui peuvent exécuter du code dès que vous cliquez &quot;Trust&quot; à l'ouverture du projet (ce que la plupart des devs font sans réfléchir).</p>
<p>Le deuxième passe par un <code>npm run dev</code> piégé, la commande de dev classique qui lance le malware en même temps que le serveur (car oui, c'est aussi simple que ça...).</p>
<p>Et le troisième est encore plus sournois puisqu'il s'agit d'un module backend qui décode une URL depuis le fichier <code>.env</code>, exfiltre toutes les variables d'environnement (tokens cloud, clés API...), puis exécute du JavaScript reçu en retour. Sympaaaaaa....</p>
<p>Du coup, le malware est plutôt bien pensé. C'est un loader JavaScript qui se télécharge depuis l'infrastructure Vercel (comme ça, ça a l'air légitime), et qui s'exécute entièrement en mémoire, et spawne un processus Node.js séparé pour ne pas éveiller les soupçons. Une fois installé, il se connecte alors à un serveur C2 qui change d'identifiant régulièrement, histoire de compliquer la détection. Et là, ça se met à exfiltrer tout ce qui traîne... code source, secrets, credentials cloud... bref, tout ce qui a de la valeur.</p>
<p>Alors, comment on se protège de ce genre de menace quand on est un simple dev ? Hé bien déjà, vérifiez le profil du &quot;recruteur&quot;. Pas de site d'entreprise vérifiable, des messages génériques... c'est un joli red flag !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/fausses-interviews-malware-nextjs-devs/fausses-interviews-malware-nextjs-devs-2.png" alt="" loading="lazy" decoding="async">
<p>Ensuite, avant de lancer quoi que ce soit, lisez le <code>package.json</code> à la recherche de scripts suspects dans <code>preinstall</code>, <code>postinstall</code> ou <code>prepare</code>, inspectez le dossier <code>.vscode/</code> (surtout <code>tasks.json</code>), et faites un <code>npm install --ignore-scripts</code> pour bloquer l'exécution automatique des hooks. Lancez aussi un
<a href="https://korben.info/safe-npm-protection-supply-chain-attack-javascript.html">safe-npm</a>
et un <code>npm audit</code> une fois les dépendances installées. Et côté VS Code, désactivez l'exécution auto des tasks avec <code>&quot;task.allowAutomaticTasks&quot;: &quot;off&quot;</code> dans vos settings.</p>
<p>Ça me rappelle les campagnes type
<a href="https://korben.info/npm-shai-hulud-scanner-attaque-supply-chain.html">Shai-Hulud et les packages npm vérolés</a>
, mais avec un vecteur social bien plus élaboré. Le piège, c'est qu'on ne balance plus des packages malveillants dans le registry en espérant qu'un dev les installe par erreur... non, non, on cible directement les développeurs, un par un, en exploitant ce stress de la recherche d'emploi comme le ferait un conseiller France Travail quand vous arrivez en fin de droits chomdu...</p>
<p>Et si vous êtes en pleine recherche d'emploi, attention, ne lancez JAMAIS un projet d'un inconnu dans votre environnement principal. Utilisez une VM, un container Docker (<code>docker run --rm -it -v $(pwd):/app node:20 bash</code> et c'est réglé), ou au minimum un compte utilisateur séparé sans accès à vos tokens et clés SSH. On n'est jamais trop prudent !</p>
<p>Maintenant vous savez... si un recruteur vous envoie un repo GitHub sans profil LinkedIn ni site d'entreprise véritable et vérifiable... c'est que c'est pas un recruteur. Voilà voilà...</p>
<p>
<a href="https://www.theregister.com/2026/02/25/jobseeking_nextjs_devs_attack/">Source</a>
</p>