---
title: "Tunnelto - Exposez votre serveur local avec inspection du trafic"
author: "Korben"
date: 2026-02-23T09:25:00.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "developpement/outils-developpement"
  - "localhost"
  - "Ngrok"
  - "Rust"
  - "tunnel"
rss_source: Blog
url: https://korben.info/tunnelto-exposer-localhost-alternative-ngrok.html
note: 0
seen: false
---

<p>Si vous avez déjà eu besoin de montrer une app en dev à un client ou de tester un webhook Stripe sans vous farcir une config nginx, y'a de fortes chances que vous connaissiez
<a href="https://korben.info/ngrok-creer-un-tunnel-pour-vos-applications-locale.html">ngrok</a>
.</p>
<p>Hé bien
<a href="https://github.com/agrinman/tunnelto">Tunnelto</a>
fait sensiblement la même chose, mais en Rust et avec un truc en plus qui fait la différence : <strong>un dashboard d'introspection pour voir tout ce qui passe dans le tunnel.</strong></p>
<p>Du coup, vous lancez une commande, vous récupérez une URL publique genre <code>votresite.tunnelto.dev</code>, et hop, votre localhost devient accessible depuis n'importe où. Et surtout, vous pouvez inspecter toutes les requêtes HTTP qui transitent. Super utile quand vous débuguez une API ou que vous essayez de comprendre pourquoi ce foutu webhook ne se déclenche pas.</p>
<p>Pour l'installer, plusieurs options s'offrent à vous :</p>
<p><strong>Sur macOS via Homebrew</strong> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install agrinman/tap/tunnelto
</span></span></code></pre><p><strong>Via Cargo</strong> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cargo install tunnelto
</span></span></code></pre><p>Et pour exposer votre app qui tourne sur le port 8000 :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">tunnelto --port 8000
</span></span></code></pre><p>C'est tout ! Le service vous file une URL avec un sous-domaine aléatoire. Mais si vous voulez quelque chose de plus mémorable, vous pouvez demander un sous-domaine custom :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">tunnelto --port 8000 --subdomain monprojet
</span></span></code></pre><p>Et vous obtenez <code>monprojet.tunnelto.dev</code>. Pas mal pour une démo client, non ?</p>
<p>Bon, si vous avez suivi mes articles sur
<a href="https://korben.info/bore-tunnel-tcp-rapide-leger-ports-locaux.html">Bore</a>
ou
<a href="https://korben.info/tunnl-tunnel-ssh-localhost-internet-ngrok.html">Tunnl.gg</a>
, vous vous demandez peut-être la différence. Bore est ultra-minimaliste, Tunnl.gg ne nécessite même pas de client à installer... Tunnelto se situe entre les deux : plus complet que Bore avec son dashboard d'introspection, mais plus léger que ngrok avec son approche open source.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/tunnelto-exposer-localhost-alternative-ngrok/tunnelto-exposer-localhost-alternative-ngrok-2.png" alt="" loading="lazy" decoding="async">
<p>D'ailleurs, y'a un truc cool avec Tunnelto c'est que vous pouvez héberger votre propre serveur si vous ne voulez pas dépendre d'un service tiers. Pratique pour les entreprises qui veulent garder le contrôle sur leurs tunnels. Sous le capot, ça utilise également tokio pour l'async Rust, donc c'est rapide et ça consomme que dalle en ressources.</p>
<p>Bref, si ngrok vous paraît trop usine à gaz et que Bore manque de fonctionnalités pour vous, Tunnelto fera bien le taf surtout avec son module d'inspection du trafic HTTP, qui fait la diff quand on débugue des intégrations...</p>
<p>
<a href="https://github.com/agrinman/tunnelto">Source</a>
</p>