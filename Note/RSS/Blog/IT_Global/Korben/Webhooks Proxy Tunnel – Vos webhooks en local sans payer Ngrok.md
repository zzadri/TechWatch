---
title: "Webhooks Proxy Tunnel – Vos webhooks en local sans payer Ngrok"
author: "Korben"
date: 2026-01-29T09:28:53.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "tutoriels-guides/tutoriels-avances"
  - "Cloudflare"
  - "Cloudflare Workers"
  - "Ngrok"
  - "Node.js"
rss_source: Blog
url: https://korben.info/webhooks-proxy-tunnel-local-ngrok.html
note: 0
seen: false
---

<p>Ce matin, je cherchais un moyen simple de tester des webhooks en local sans passer par
<a href="https://korben.info/ngrok-creer-un-tunnel-pour-vos-applications-locale.html">ce bon vieux Ngrok</a>
qui est devenu un peu relou avec ses limites en version gratuite. J'ai d'abord pensé à monter mon propre serveur VPN (coucou Tailscale), mais franchement flemme.</p>
<p>Et puis tout à fait par hasard (aaah les joies de la sérendipité) je suis tombé sur cet outil qui devrait vous plaire, surtout si vous développez des applis qui doivent recevoir des notifications HTTP (GitHub, Stripe, Slack...). Ben oui vous connaissez la galère... votre serveur de dev est sur &quot;localhost&quot;, donc inaccessible depuis l'extérieur, du coup, impossible de recevoir ces fameux webhooks sans ouvrir votre routeur ou utiliser un tunnel.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/webhooks-proxy-tunnel-local-ngrok/webhooks-proxy-tunnel-local-ngrok-1.jpeg" alt="" loading="lazy" decoding="async">
<p>C'est là qu'intervient
<a href="https://github.com/peter-leonov/webhooks-proxy-tunnel">Webhooks Proxy Tunnel</a>
!</p>
<p>Grâce à cet outil, au lieu de multiplier les intermédiaires, vous déployez votre propre tunnel... directement sur l'infrastructure de Cloudflare. Et le meilleur c'est que ça tourne généralement très bien sur leur offre gratuite (dans la limite des quotas Workers évidemment, donc attention si vous bourrinez comme un fifou).</p>
<p>L'outil utilise un Cloudflare Worker couplé à un Durable Object (une sorte de mini-serveur d'état). Le Worker reçoit alors les requêtes publiques sur une URL en HTTPS (genre &quot;truc.workers.dev&quot;) et les transmet via une WebSocket à un petit client Node.js qui tourne sur votre machine. Et hop, le trafic arrive sur votre port local.</p>
<p>Perso, je trouve ça brillant car même si le trafic passe techniquement par Cloudflare (puisque c'est leur infra), vous gardez la main sur le code qui s'exécute et vous évitez d'envoyer vos données à un service tiers supplémentaire dont vous ignorez tout.</p>
<p>Pour l'installer, ne plus c'est hyper fastoche. Il vous faut juste un compte Cloudflare et Node.js. J'ai testé l'install en moins de 5 minutes, vous clonez le dépôt, vous installez les dépendances et vous lancez le déploiement (qui vous demandera de vous authentifier) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/peter-leonov/webhooks-proxy-tunnel.git
</span></span><span class="line"><span class="cl">cd webhooks-proxy-tunnel/worker
</span></span><span class="line"><span class="cl">npm install
</span></span><span class="line"><span class="cl">npm run deploy
</span></span></code></pre><p>Une fois déployé, le script vous donne une URL et il ne vous reste plus alors qu'à lancer le client local en lui disant où taper (par exemple votre port 3000) et le tour est joué !! Vous pouvez même gérer plusieurs tunnels en parallèle si vous bossez sur plusieurs projets, chaque tunnel ayant son ID unique.</p>
<p>Attention quand même, c'est conçu pour du développement hein, pas pour streamer de la 4K. Les requêtes doivent tenir en mémoire (limite de 100 Mo environ) donc sauf si vous transférez des fichiers énormes via vos webhooks, ça passera crème pour du JSON ou des petits payloads binaires.</p>
<p>Voilà, si vous cherchiez une alternative self-hosted et gratuite pour vos tests, c'est clairement un outil à garder sous le coude. Et si vous avez besoin de trucs plus costauds pour du réseau d'entreprise, jetez un œil à
<a href="https://korben.info/tailscale-reseau-prive-virtuel.html">Tailscale</a>
ou
<a href="https://korben.info/octelium-zero-trust-open-source-vpn-alternative.html">Octelium</a>
.</p>
<p>
<a href="https://github.com/peter-leonov/webhooks-proxy-tunnel">Source</a>
</p>