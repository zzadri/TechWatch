---
title: "Memos - Pour conserver votre inspiration et vos idées en lieu sûr"
author: "Korben"
date: 2026-02-05T06:41:24.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/self-hosting"
  - "logiciel libre"
  - "Memos"
  - "prise de notes auto-hébergée"
rss_source: Blog
url: https://korben.info/hub-notes-memos.html
note: 0
seen: false
---

<p>J'ai souvent des tas d'idées à la con, mais comme vous le savez, pris par le tourbillon de la vie, on ne pense pas forcément à les noter et encore moins à les exploiter plus tard.</p>
<p>Il y a plein d'outils pour prendre des notes comme le célèbre Notion ou tout simplement l'app Notes d'Apple ou ce genre de trucs. Mais si vous êtes amateur de logiciel libre et inquiet par votre vie privée, le mieux c'est encore d'auto-héberger un outil comme
<a href="https://usememos.com/">Memos</a>
.</p>
<p>Voici le tutoriel que j'ai réalisé pour les patréons :</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/mA7dGc-vUOQ?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Memos est un outil développé en Go + React.js, qui peut tourner dans un Docker et qui permet en quelques secondes de noter votre prochaine idée de startup ou l'idée repas que vous venez d'avoir pour ce soir. Au niveau de son fonctionnement, l'interface de Memos ressemble un peu à Twitter et permet comme ça de prendre des notes aussi longues que vous voulez en markdown et d'y joindre des fichiers, des tags...etc.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hub-notes-memos/hub-notes-memos-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Ici, pas de tracking ni de télémétrie louche selon les développeurs, le projet mise à fond sur la vie privée. Vous installez ça sur votre serveur, votre Raspberry Pi 4 ou 5, ou même un vieux PC qui traîne, et hop, vous avez votre propre carnet de bord numérique. Si vous configurez un petit reverse proxy (genre Nginx ou Caddy) ou un VPN, c'est accessible de partout.</p>
<p>Vous pouvez l'utiliser uniquement pour vous ou créer des comptes également pour vos collègues et amis et après il y a plus qu'à faire des recherches dans tout ça pour retrouver vos meilleurs punchlines ou idées à la con.</p>
<p>Perso, j'ai choisi Docker pour l'installation parce que c'est quand même plus simple à mettre à jour et ça évite de polluer le système avec 50 dépendances. J'ai d'ailleurs passé 5 minutes à chercher le port par défaut avant de réaliser que c'était le 5230, comme écrit en gros dans la doc... la honte ! Bon, attention quand même avec la persistance des données : n'oubliez pas de bien monter votre volume (le <code>-v</code> dans la commande), sinon au premier redémarrage du conteneur, pffff, plus de notes !</p>
<p>Pour l'installation sur Linux ou macOS, ça se règle en une seule commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">docker</span> <span class="n">run</span> <span class="o">-</span><span class="n">d</span> <span class="o">--</span><span class="n">name</span> <span class="n">memos</span> \
</span></span><span class="line"><span class="cl"> <span class="o">-</span><span class="n">p</span> <span class="mi">5230</span><span class="p">:</span><span class="mi">5230</span> \
</span></span><span class="line"><span class="cl"> <span class="o">-</span><span class="n">v</span> <span class="o">~/.</span><span class="n">memos</span><span class="o">/</span><span class="p">:</span><span class="o">/</span><span class="k">var</span><span class="o">/</span><span class="n">opt</span><span class="o">/</span><span class="n">memos</span> \
</span></span><span class="line"><span class="cl"> <span class="n">neosmemo</span><span class="o">/</span><span class="n">memos</span><span class="p">:</span><span class="n">stable</span>
</span></span></code></pre><p>Tout est stocké dans une base SQLite (ou MySQL/PostgreSQL si vous préférez), vous pouvez le passer en langue française, en thème sombre si vous avez mal à vos petits yeux, et il y a même des APIs REST et gRPC pour connecter Memos à vos propres outils. D'ailleurs, si vous avez déjà testé
<a href="https://korben.info/poznote-notes-self-hosted-docker-open-source.html">Poznote</a>
, vous allez retrouver cet esprit &quot;légèreté avant tout&quot;. Sauf que Memos pousse le bouchon un peu plus loin sur l'aspect communautaire.</p>
<p>Bref, c'est libre, c'est léger et ça fait le job sans chichis.</p>
<p>
<a href="https://usememos.com/">À découvrir ici !</a>
</p>
<p><em>Article publié initialement le 24 mai 2023 et mis à jour le 5 février 2026.</em></p>