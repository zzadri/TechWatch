---
title: "Social Analyzer - Scannez vos profils sociaux (OSINT)"
author: "Korben"
date: 2026-01-24T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "cybersecurite/outils-securite"
  - "investigation"
  - "open source"
  - "OSINT"
  - "Python"
  - "sécurité"
  - "social-media"
  - "tutoriel"
  - "vie privée"
rss_source: Blog
url: https://korben.info/social-analyzer-osint-tuto-1000-reseaux.html
note: 0
seen: false
---

<p>Qui n'a jamais eu envie de savoir si &quot;<em>KikouLolDu93</em>&quot; avait aussi un compte sur un site de rencontre ou un forum obscur de haxx0rs ? C'est humain, c'est de la curiosité... ou de l'OSINT (Open Source Intelligence) si vous voulez faire genre vous êtes un pro. Et pour ça, j'ai l'outil qu'il vous faut : <strong>
<a href="https://github.com/qeeqbox/social-analyzer">Social Analyzer</a>
</strong>.</p>
<p>Ce script est un détective privé numérique qui va frapper à la porte de plusieurs centaines de sites (Facebook, X (ex-Twitter), Instagram, Tinder, et des trucs bien plus niches) pour vérifier la présence d'un pseudo.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/social-analyzer-osint-tuto-1000-reseaux/social-analyzer-osint-tuto-1000-reseaux-2.png" alt="" loading="lazy" decoding="async">
<p>Développé par qeeqbox, Social Analyzer ne se contente pas de tester une URL. Il analyse les pages, vérifie les métadonnées, et vous sort un score de confiance de 0 à 100. Notez qu'un score de 100 n'est pas une preuve d'identité absolue (on n'est pas à la police scientifique), mais une forte probabilité basée sur les signaux trouvés. À l'inverse, un score de 0 peut signifier que c'est un homonyme, ou simplement que le site a bloqué la requête. Ça évite en tout cas de stalker la mauvaise personne trop vite.</p>
<p>L'outil est codé en JavaScript et Python, et vous pouvez l'utiliser en ligne de commande ou via une interface web plutôt propre si le terminal vous donne de l'urticaire.</p>
<h2 id="comment-on-installe-la-bestiole-">Comment on installe la bestiole ?</h2>
<p>Vous avez plusieurs options, mais la plus simple si vous avez Python 3 d'installé, c'est via pip (vérifiez bien que c'est le paquet officiel) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pip3 install social-analyzer
</span></span></code></pre><p>Et hop, c'est réglé. Ensuite pour lancer une recherche rapide, c'est aussi simple que :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">social-analyzer --username &#34;le_pseudo_a_chercher&#34;
</span></span></code></pre><p>Si vous êtes plus team NodeJS, vous pouvez aussi cloner le dépôt GitHub et lancer ça à la main :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/qeeqbox/social-analyzer.git
</span></span><span class="line"><span class="cl">cd social-analyzer
</span></span><span class="line"><span class="cl">npm install
</span></span><span class="line"><span class="cl">npm start
</span></span></code></pre><p>Ça lancera l'interface web sur votre machine (généralement sur le port 9005), et vous pourrez faire vos recherches tranquillement en cliquant sur des boutons.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/social-analyzer-osint-tuto-1000-reseaux/social-analyzer-osint-tuto-1000-reseaux-3.png" alt="" loading="lazy" decoding="async">
<h2 id="et-ça-marche-vraiment-">Et ça marche vraiment ?</h2>
<p>Franchement, oui. C'est même assez bluffant de voir tout ce qui ressort. Il peut même tenter d'extraire des infos supplémentaires comme la bio ou l'avatar si les sites ne sont pas trop protégés contre le scraping.</p>
<p>Par contre, petit disclaimer habituel : ce genre d'outil, c'est pour de l'investigation légitime. Genre vérifier vos propres traces numériques pour faire du nettoyage, ou pour des enquêtes de sécu. Ne commencez pas à l'utiliser pour harceler les gens, le web n'a pas besoin de ça.</p>
<p>D'ailleurs, si le sujet de l'OSINT vous branche, jetez un œil à mon article sur
<a href="https://korben.info/osint-pseudo-blackbird.html">Blackbird</a>
qui fait un boulot similaire, ou apprenez à
<a href="https://korben.info/osint-github.html">analyser un profil GitHub</a>
comme un chef.</p>
<p>Bref, Social Analyzer c'est puissant, c'est open source, et ça fait le café. À utiliser avec intelligence évidemment !</p>
<p>Merci à Lorenper !</p>