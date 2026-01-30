---
title: "Pipenet – L'alternative moderne à localtunnel"
author: "Korben"
date: 2026-01-22T13:31:42.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "linux-open-source/logiciels-libres"
  - "alternative open source"
  - "mcp"
  - "open source"
rss_source: Blog
url: https://korben.info/pipenet-tunnel-localtunnel-alternative.html
note: 0
seen: false
---

<p>Si vous avez déjà galéré à rendre accessible votre serveur web local à des testeurs externes... Ne désespérez plus car aujourd'hui, je vais vous présenter <strong>
<a href="https://pipenet.dev/">Pipenet</a>
</strong>, un petit utilitaire qui va vous changer la vie !</p>
<p>On a tous connu ce moment où on veut montrer une démo à un client ou tester un webhook et en général c'est à ce moment là que le drame se produit ! Configuration de la box, pare-feu qui fait la tête, redirection de ports qui ne veut rien savoir... Grosso merdo c'est la fin de votre productivité pour la matinée !</p>
<p>Mais grâce à l'équipe de glama.ai qui a codé cette alternative au bon vieux localtunnel, vous allez pouvoir exposer vos services locaux sur Internet en un clin d'œil. Et ce qui est cool c'est que contrairement à d'autres solutions qui deviennent vite limitées ou payantes, Pipenet vous laisse un contrôle total ! C'est ça
<a href="https://github.com/punkpeye/pipenet">la pwouiiiissance du logiciel libre</a>
!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pipenet-tunnel-localtunnel-alternative/pipenet-tunnel-localtunnel-alternative-2.png" alt="" loading="lazy" decoding="async">
<p>Pour ceux qui se demandent ce qu'est exactement un tunnel TCP, c'est simplement un pont entre votre machine et le reste du monde !</p>
<p>Mais attention ! La sécurité (chiffrement et auth) dépend de la configuration ! Ça tombe bien puisque Pipenet supporte bien sûr le HTTPS et possède des options pour sécuriser votre propre serveur !</p>
<p>Il fait ça particulièrement bien en utilisant une architecture client et serveur. Vous pouvez donc utiliser leur serveur public par défaut (pipenet.dev) ou carrément héberger votre propre infrastructure de tunneling ! C’est top pour la confidentialité si vous pouvez l'auto-héberger !</p>
<p>Pour l'install, si vous avez Node.js, une simple commande suffit pour commencer à exposer votre port 3000 !</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npx pipenet client --port 3000
</span></span></code></pre><p>Et voilà, votre application devient alors accessible via <code>https://abc123.pipenet.dev</code>.</p>
<p>C'est aussi simple que ça ! Et si vous voulez un sous-domaine spécifique (parce que c'est plus classe), il suffit de leur demander (sous réserve de disponibilité évidemment) !</p>
<p>Mais là où Pipenet se démarque vraiment par rapport à la concurrence, c'est son approche pensée pour les environnements cloud ! Il supporte par exemple le multiplexage sur un seul port (via l'option <code>--tunnel-port</code>) ce qui est top pour les déploiements sur des plateformes comme Fly.io ou dans des conteneurs Docker où la gestion des ports peut vite devenir casse bonbon !</p>
<p>Vous pouvez même l'intégrer directement dans vos propres outils grâce à son API et c'est d'ailleurs ce qu'a fait glama.ai avec son outil <code>mcp-proxy</code> pour connecter des serveurs MCP locaux avec des clients IA distants ! Et si vous voulez savoir si Pipenet supporte le streaming ou les WebSockets... Hé bien la réponse est oui !</p>
<p>Ce petit pépère gère le trafic basé sur HTTP, y compris le
<a href="https://fr.wikipedia.org/wiki/Server-sent_events">SSE</a>
, donc pour tout ce qui est streaming et connexions full duplex WebSocket, c'est OK.</p>
<p>Pipenet est l'évolution moderne des outils comme
<a href="https://korben.info/rendre-visible-localhost-sur-le-net.html">Pagekite</a>
ou localtunnel et c'est un choix excellent pour la plupart des usages que je viens d'évoquer !</p>
<p>Amusez-vous bien !</p>
<p>
<a href="https://pipenet.dev/">Source</a>
</p>