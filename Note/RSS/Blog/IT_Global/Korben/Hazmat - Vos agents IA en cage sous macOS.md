---
title: "Hazmat - Vos agents IA en cage sous macOS"
author: "Korben"
date: 2026-04-08T13:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "intelligence-artificielle"
  - "Claude Code"
  - "isolation sandbox"
  - "macOS"
  - "open source"
  - "Sandbox"
  - "sécurité"
rss_source: Blog
url: https://korben.info/hazmat-sandbox-macos-agents-ia.html
note: 0
seen: false
---

<p>J'sais pas si vous vous en rendez compte mais les agents IA qui codent sur votre machine ont accès à vos clés SSH, vos credentials AWS, votre Keychain et compagnie. Ils ont accès à TOUT ! C'est comme filer les clés de votre appart à un gars que vous avez croisé sur le parking de Leclerc y'a pas 5 min.</p>
<p>
<a href="https://github.com/dredozubov/hazmat">Hazmat</a>
prend le problème à l'envers : au lieu de demander poliment à l'agent de se tenir tranquille, il l'enferme dans un compte macOS séparé. Du coup, vos <code>~/.ssh</code>, <code>~/.aws</code>, votre Keychain deviennent structurellement inaccessibles. Pour en profiter, faut faire un</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install dredozubov/tap/hazmat
</span></span></code></pre><p>puis</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cd /tmp
</span></span></code></pre><div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">hazmat init --bootstrap-agent claude
</span></span></code></pre><p>Et hop, 10 minutes plus tard votre agent tourne dans sa cage. (le premier snapshot est ultra loooong mais après c'est de l'incrémental donc ça ira plus vite)</p>
<p>L'isolation repose sur 3 couches indépendantes, un peu comme les sas d'un sous-marin. Il y a d'abord un utilisateur <code>agent</code> dédié (vos fichiers perso deviennent alors hors de portée, point). Ensuite, une politique seatbelt générée dynamiquement à chaque session qui consiste à ce que le kernel de macOS vérifie chaque accès fichier et refuse tout ce qui n'est pas explicitement autorisé pour cette session précise.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hazmat-sandbox-macos-agents-ia/hazmat-sandbox-macos-agents-ia-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et par-dessus, des règles pf firewall qui empêchent l'agent d'envoyer du trafic SMTP, IRC, FTP, Tor ou VPN. Comme ça, un agent qui tentera d'exfiltrer vos données par mail se retrouvera bloqué net au niveau du noyau.</p>
<p>Côté supply chain, Hazmat force <code>npm ignore-scripts=true</code> par défaut. Comme ça, par exemple
<a href="https://korben.info/axios-lune-des-bibliotheques-les-plus-populaires-de-npm-piratee-pour-installer-un-cheval-de-troie.html">le fameux hack axios</a>
qui livrait un RAT via un hook <code>postinstall</code> en 2 secondes chrono n'est plus possible ici ! Y'a aussi une blocklist DNS qui redirige les services de tunnel connus (ngrok, pastebin, webhook.site) vers localhost. Contre un domaine perso fraîchement enregistré, ça passera mais les vecteurs d'exfiltration classiques, ça devrait résister.</p>
<p>Hazmat utilise TLA+, le même formalisme que les ingés d'Amazon utilisent pour vérifier les protocoles de DynamoDB. Genre, l'installation des règles sudoers AVANT le firewall (évidemment, ça crée une fenêtre de vulnérabilité), les restrictions qui bloquaient les lectures mais pas les écritures, ou encore une restauration cloud sans vérifier qu'un snapshot existait...etc, c'est le genre de truc qu'aucun test unitaire n'aurait chopé.</p>
<p>Ça supporte Claude Code (y compris le fameux <code>--dangerously-skip-permissions</code>), OpenCode et Codex. Attention par contre, si votre projet utilise Docker, y'a deux cas de figure : soit le daemon Docker est privé au projet et Hazmat le route automatiquement vers un mode Docker Sandbox, soit c'est un daemon partagé et là faudra passer <code>--docker=none</code> explicitement.</p>
<p>La commande <code>hazmat explain</code> montre aussi exactement ce que le sandbox autorise avant de lancer quoi que ce soit... et ça, c'est pas du luxe quand on sait pas trop ce qu'on va lâcher dans la nature. Le <code>hazmat diff</code> qui affiche les changements faits par l'agent depuis le dernier snapshot Kopia, c'est plutôt bien pensé. Et si l'agent casse un truc ? <code>hazmat restore</code> et c'est reparti, comme un Ctrl+Z géant pour tout votre projet.</p>
<p>Si vous avez déjà
<a href="https://korben.info/teabase-environnement-developpement-macos-securise.html">configuré votre Mac avec teaBASE</a>
pour sécuriser votre env de dev, c'est un complément logique.</p>
<p>Côté limites, faut être honnête, Seatbelt n'est pas documenté par Apple depuis macOS 10.5 et c'est du defense-in-depth, et pas une vraie frontière de VM. Quand à l'exfiltration HTTPS elle n'est pas bloquée car l'agent peut toujours <code>curl</code> n'importe quoi sur le port 443. C'est logique mais bon, c'est pas étanche à 100% quoi...</p>
<p>Et surtout c'est macOS only pour l'instant (le port Linux est en chantier), et bien sûr le <code>/tmp</code> partagé entre les comptes locaux reste un vecteur potentiel. J'aurais aimé aussi que le réseau soit coupé par défaut sauf whitelist, mais bon, faudra attendre. Après entre ça et laisser Claude Code en roue libre avec les pleins pouvoirs sur votre machine... y'a pas photo.</p>
<p>Bref, pour du vibe coding sur Mac, c'est le minimum vital.</p>