---
title: "Visualisez le tracking web en temps réel avec CookieViz de la CNIL"
author: "Korben"
date: 2026-01-20T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "vie-privee-anonymat/surveillance-tracking"
  - "CNIL"
  - "cookies"
  - "extension"
  - "Firefox"
  - "open source"
  - "Tracking"
  - "vie privée"
rss_source: Blog
url: https://korben.info/cookieviz-cnil-tracking-visualisation-dataviz.html
note: 0
seen: false
---

<p>Aujourd'hui, on va parler d'un truc qui gratte un peu : <strong>le tracking web</strong>.</p>
<p>Vous savez, cette sensation d'être suivi par une armée de régies publicitaires dès qu'on clique sur un article de presse ou qu'on cherche une nouvelle paire de pompes. Bah la CNIL, via son laboratoire d innovation (le LINC), développe depuis 2013 un outil qui permet de mettre des images sur ce sentiment de persécution numérique : <strong>
<a href="https://github.com/LINCnil/CookieViz">CookieViz</a>
</strong>.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cookieviz-cnil-tracking-visualisation-dataviz/cookieviz-cnil-tracking-visualisation-dataviz-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'outil de dataviz du LINC (
<a href="https://linc.cnil.fr/cookieviz-une-dataviz-en-temps-reel-du-tracking-de-votre-navigation">Source</a>
)</em></p>
<p>CookieViz, c'est un logiciel de dataviz en temps réel qui analyse les interactions entre un navigateur et les serveurs distants. Vous naviguez via l'outil (qui embarque son propre navigateur pour la version desktop) et celui-ci débusque les cookies et les requêtes observables envoyées vers des domaines tiers.</p>
<p>Et souvent, le résultat ressemble à un gros plat de cyber spaghettis où chaque fil mène à un tracker différent.</p>
<p>La version 2.3, publiée en juin 2022 (ça date un peu, c'est vrai) reste la référence stable du projet. Le système d'analyse a été revu pour être plus stable et le navigateur intégré est plus sécurisé et la visualisation met en avant le rôle central des places de marché publicitaires dans les mécanismes d'enchères en temps réel (RTB). Vous verrez ainsi comment un seul clic peut déclencher une cascade de connexions vers des acteurs dont vous n'avez jamais entendu parler.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cookieviz-cnil-tracking-visualisation-dataviz/cookieviz-cnil-tracking-visualisation-dataviz-3.png" alt="" loading="lazy" decoding="async">
<p><em>Le projet est open source et disponible sur GitHub (
<a href="https://github.com/LINCnil/CookieViz">Source</a>
)</em></p>
<p>Alors oui, pour ceux qui se demandent comment voir les cookies de suivi sans installer un logiciel complet, les navigateurs comme Chrome ou Firefox proposent des outils rudimentaires dans leurs menus de réglages. Mais franchement, à côté de CookieViz, c'est un peu comme essayer de comprendre le trafic routier en regardant par le trou d'une serrure.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cookieviz-cnil-tracking-visualisation-dataviz/cookieviz-cnil-tracking-visualisation-dataviz-4.png" alt="" loading="lazy" decoding="async">
<p>Pour les amateurs de bidouille, sachez aussi que c'est du logiciel libre sous licence GPLv3 donc vous pouvez donc aller gratter le code, l'améliorer ou simplement vérifier que la CNIL ne vous espionne pas en douce (ahaha, je plaisante hein...^^).</p>
<p>L'outil est dispo en version desktop pour Windows, Linux et macOS et il existe aussi une extension officiellement publiée pour
<a href="https://github.com/LINCnil/cookieviz-extension">Firefox</a>
, tandis que les utilisateurs de Chrome ou Opera devront passer par une installation manuelle du code depuis la branche Chromium du projet.</p>
<p>Moi j'ai préféré l'installé à la main comme ceci en clonant le projet :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/LINCnil/CookieViz
</span></span><span class="line"><span class="cl">cd CookieViz
</span></span></code></pre><p>Puis modifiez le <strong>package.json</strong> pour utiliser une version moderne de NW.js<br>
(la version 0.64.1 originale n'est plus disponible). Dans devDependencies, remplacez :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">&#34;nwjs-builder-phoenix&#34;: &#34;^1.15.0&#34;
</span></span></code></pre><p>par :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">&#34;nw&#34;: &#34;0.92.0-sdk&#34;
</span></span></code></pre><p>Et dans scripts, remplacez :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">&#34;start&#34;: &#34;run --x64 --mirror https://dl.nwjs.io/ .&#34;
</span></span></code></pre><p>par :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">&#34;start&#34;: &#34;nw .&#34;
</span></span></code></pre>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cookieviz-cnil-tracking-visualisation-dataviz/cookieviz-cnil-tracking-visualisation-dataviz-5.png" alt="" loading="lazy" decoding="async">
<p>Puis installez et lancez :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npm install
</span></span><span class="line"><span class="cl">npm run start
</span></span></code></pre><p>Ensuite, vous voilà paré pour l'audit !</p>
<p>Et si vous voulez vraiment reprendre le contrôle, n'oubliez pas qu'il existe d'autres solutions complémentaires. Vous pouvez par exemple essayer d'
<a href="https://korben.info/user-agent-switcher-extension-firefox-proteger-vie-privee-bloquer-tracking.html">embrouiller les sites avec User-Agent Switcher</a>
(même si c'est loin d'être une protection ultime face au fingerprinting moderne) ou carément
<a href="https://korben.info/cookie-autodelete-pour-mieux-controler-vos-cookies.html">automatiser le nettoyage avec Cookie AutoDelete</a>
. Mais perso, je trouve que pour l'aspect pédagogique et &quot;prise de conscience&quot;, CookieViz reste un outil de premier plan.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cookieviz-cnil-tracking-visualisation-dataviz/cookieviz-cnil-tracking-visualisation-dataviz-6.png" alt="" loading="lazy" decoding="async">
</p>
<p>Voilà, si vous voulez voir la gueule de votre tracking en direct et réaliser que la vie privée sur le web moderne ça n'existe pas (sauf ici), allez donc faire un tour sur le site du
<a href="https://linc.cnil.fr/">LINC</a>
.</p>
<p>De quoi verser une petite larme sur le web d'antan...</p>
<p>
<a href="https://linc.cnil.fr/cookieviz-une-dataviz-en-temps-reel-du-tracking-de-votre-navigation">Source</a>
</p>