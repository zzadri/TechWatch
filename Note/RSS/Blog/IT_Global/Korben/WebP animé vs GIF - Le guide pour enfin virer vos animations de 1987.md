---
title: "WebP animé vs GIF - Le guide pour enfin virer vos animations de 1987"
author: "Korben"
date: 2026-03-06T08:55:04.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/web-developpement"
  - "tutoriels-guides/astuces-productivite"
  - "animation"
  - "CSS"
  - "ffmpeg"
  - "formats image"
  - "GIF"
  - "HTML"
  - "ImageMagick"
  - "transparence"
  - "web performance"
  - "WebP"
rss_source: Blog
url: https://korben.info/webp-anime-vs-gif-transparence-couleurs.html
note: 0
seen: false
---

<p>Le GIF, c'est un format que j'adore mais qui date de 1987. Ouais c'est super vieux quoi (désolé les gens qui sont né cette année là ou avant...On est ensemble...loool). C'est l'époque où Rick Astley cartonnait et où Internet n'existait même pas encore pour le grand public. Et pourtant, y'a encore plein de gens qui s'en servent pour leurs animations avec notamment de la transparence. Alors c'est cool mais aujourd'hui, je vous propose qu'on règle ça une bonne fois pour toute.</p>
<p>Le problème du GIF en fait c'est assez technique puisque ça se compose de <strong>8 bits de couleur</strong> (256 couleurs max) et surtout d'un <strong>alpha 1 bit</strong>. Chaque pixel est donc soit totalement opaque, soit totalement transparent, y'a pas d'entre-deux. Du coup quand vous avez une animation avec des bords arrondis ou des ombres portées, vous vous retrouvez avec des bords tout crénelés et moches. Ça donne un effet &quot;<em>découpage aux ciseaux de maternelle</em>&quot; qu'on aime bien parce que ça fait très rétro mais bon, on peut faire mieux aujourd'hui.</p>
<img src="https://korben.info/webp-anime-vs-gif-transparence-couleurs/webp-anime-vs-gif-transparence-couleurs-1.gif" alt="" loading="lazy" decoding="async">
<p>Car avec le WebP animé, c'est une autre histoire. Là on passe à <strong>24 bits de couleur</strong> (plus de 16 millions de couleurs) et un <strong>alpha 8 bits</strong>, c'est-à-dire 256 niveaux de transparence au lieu de juste oui/non. Les dégradés, les ombres, les bords anti-aliasés... tout ça passe nickel et vos animations ont enfin l'air pro au lieu de sortir d'un site GeoCities.</p>
<p>Et niveau poids, y'a pas photo. Google annonce ~64% de réduction en lossy par rapport au GIF même si en pratique, comptez entre 50 et 70% de gain selon la complexité de l'animation. Cela veut dire que sur une page web avec plusieurs animations, ça fait une SACRÉE différence niveau temps de chargement.</p>
<p>Et côté compatibilité, en 2026 la question ne se pose plus puisque Chrome, Firefox, Safari (depuis iOS 14 en 2020), Edge... bref tout le monde supporte le WebP animé. Donc ces conneries de compatibilité, c'est plus une excuse !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/webp-anime-vs-gif-transparence-couleurs/webp-anime-vs-gif-transparence-couleurs-2.png" alt="" loading="lazy" decoding="async">
<h3 id="convertir-avec-gif2webp-la-méthode-recommandée">Convertir avec gif2webp (la méthode recommandée)</h3>
<p>L'outil officiel de Google s'appelle <code>gif2webp</code> (il est inclus dans
<a href="https://korben.info/minipic-compressez-images-clic-sans-perte-qualite.html">libwebp</a>
) et c'est ce qu'il y a actuellement de plus fiable pour ce job.</p>
<p>Installez-le d'abord comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># macOS
</span></span><span class="line"><span class="cl">brew install webp
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Ubuntu/Debian
</span></span><span class="line"><span class="cl">sudo apt install webp
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Windows (via chocolatey)
</span></span><span class="line"><span class="cl">choco install webp
</span></span></code></pre><p>Ensuite, la conversion de base est plutôt simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Lossy, qualité 70, boucle infinie
</span></span><span class="line"><span class="cl">gif2webp -lossy -q 70 -loop 0 -m 4 input.gif -o output.webp
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Mode mixed (le meilleur ratio en général)
</span></span><span class="line"><span class="cl"># Choisit automatiquement lossless ou lossy frame par frame
</span></span><span class="line"><span class="cl">gif2webp -mixed -q 70 -loop 0 -m 4 input.gif -o output.webp
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Compression max (plus lent, fichier plus petit)
</span></span><span class="line"><span class="cl">gif2webp -lossy -q 70 -loop 0 -m 6 input.gif -o output.webp
</span></span></code></pre><p>Le paramètre <code>-m</code> c'est la méthode de compression, de 0 (rapide) à 6 (lent mais meilleur ratio). Perso, <code>-m 4</code> je trouve que c'est le sweet spot comme on dit. Et le mode <code>-mixed</code> est intéressant aussi parce qu'il analyse chaque frame et décide tout seul si c'est mieux en lossy ou lossless.</p>
<h3 id="avec-ffmpeg">Avec ffmpeg</h3>
<p>Après si vous avez déjà
<a href="https://korben.info/ffmpeg-pour-les-nuls.html">ffmpeg</a>
installé (et si vous êtes sur ce blog, y'a de bonnes chances), ça marche aussi :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Conversion basique GIF vers WebP animé
</span></span><span class="line"><span class="cl">ffmpeg -i input.gif -c:v libwebp_anim -loop 0 -lossless 0 -q:v 70 output.webp
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Qualité max (lossless)
</span></span><span class="line"><span class="cl">ffmpeg -i input.gif -c:v libwebp_anim -loop 0 -lossless 1 output.webp
</span></span></code></pre><p>Le <code>-c:v libwebp_anim</code> force l'encodeur WebP animé (sans ça, ffmpeg choisit parfois le mauvais codec et vous obtenez un WebP statique avec juste la première frame... pas génial). Le <code>-q:v</code> va de 0 à 100, et je pense que 70 c'est un bon compromis.</p>
<h3 id="avec-imagemagick">Avec ImageMagick</h3>
<p>Avec celui là c'est comme ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">magick input.gif -coalesce -quality 80 -loop 0 output.webp
</span></span></code></pre><p>Le <code>-coalesce</code> est important car les GIF optimisés stockent souvent juste les différences entre frames pour gagner de la place. Cette option reconstruit chaque frame en entier avant la conversion, sinon vous risquez des artefacts visuels bien moches.</p>
<h3 id="conversion-en-masse">Conversion en masse</h3>
<p>Après convertir UN fichier c'est bien, mais si vous avez 200 GIFs à migrer, faut automatiser :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Convertir tous les GIFs d&#39;un dossier
</span></span><span class="line"><span class="cl">for f in *.gif; do
</span></span><span class="line"><span class="cl"> gif2webp -mixed -q 70 -m 4 &#34;$f&#34; -o &#34;${f%.gif}.webp&#34;
</span></span><span class="line"><span class="cl"> echo &#34;$f converti&#34;
</span></span><span class="line"><span class="cl">done
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Avec un rapport de taille avant/après
</span></span><span class="line"><span class="cl">for f in *.gif; do
</span></span><span class="line"><span class="cl"> gif2webp -mixed -q 70 -m 4 &#34;$f&#34; -o &#34;${f%.gif}.webp&#34;
</span></span><span class="line"><span class="cl"> size_gif=$(stat -f%z &#34;$f&#34; 2&gt;/dev/null || stat -c%s &#34;$f&#34;)
</span></span><span class="line"><span class="cl"> size_webp=$(stat -f%z &#34;${f%.gif}.webp&#34; 2&gt;/dev/null || stat -c%s &#34;${f%.gif}.webp&#34;)
</span></span><span class="line"><span class="cl"> ratio=$((100 - size_webp * 100 / size_gif))
</span></span><span class="line"><span class="cl"> echo &#34;$f: -${ratio}%&#34;
</span></span><span class="line"><span class="cl">done
</span></span></code></pre><h3 id="intégrer-sur-un-site-web">Intégrer sur un site web</h3>
<p>Ensuite pour mettre vos images animées sur votre site web, la méthode propre, c'est l'élément <code>&lt;picture&gt;</code> qui permet de proposer un fallback GIF pour les (rares) navigateurs récalcitrants :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">&lt;picture&gt;
</span></span><span class="line"><span class="cl"> &lt;source srcset=&#34;animation.webp&#34; type=&#34;image/webp&#34; /&gt;
</span></span><span class="line"><span class="cl"> ![](animation.gif)
</span></span><span class="line"><span class="cl">&lt;/picture&gt;
</span></span></code></pre><p>Après je pense que le fallback GIF n'est vraiment plus indispensable pour le web classique mais par contre si vous envoyez des animations par email comme un le bon boomer que vous êtes, gardez le GIF en fallback parce que les clients mail, c'est un autre monde.</p>
<p>Ah et attention, j'ai lu certains articles qui suggèrent d'utiliser <code>@supports</code> en CSS pour détecter le WebP. Genre <code>@supports (background: url(truc.webp))</code>. Sauf que ça ne marche PAS. La règle <code>@supports</code> teste si une déclaration CSS est syntaxiquement valide, pas si le navigateur sait décoder le format d'image. Donc elle passera toujours, même sans support WebP. Donc si vous avez besoin d'une détection côté CSS, utilisez plutôt <code>image-set()</code> avec <code>type()</code>, mais franchement le <code>&lt;picture&gt;</code> fera le job.</p>
<h3 id="et-lavif-animé-dans-tout-ça-">Et l'AVIF animé dans tout ça ?</h3>
<p>Alors vous avez peut-être entendu parler de l'
<a href="https://korben.info/jxl-avif-nouveaux-formats-image-efficients.html">AVIF</a>
, le format qui fait encore mieux que le WebP en compression. Pour les images statiques, c'est vrai, l'AVIF déchire (support Chrome, Firefox, Safari).</p>
<p>Mais pour les animations ? Bah c'est pas encore ça. Chrome n'affiche que la première frame, Safari ne le supporte pas du tout, et Firefox le cache derrière un flag (<code>image.avif.sequence.enabled</code>).</p>
<p>Bref, on en reparlera dans 2-3 ans.</p>
<h3 id="quel-format-pour-quel-usage-">Quel format pour quel usage ?</h3>
<p>Hé oui, y'a un choix à faire parce que le WebP animé n'est pas non plus LA solution à tout. Voici ce que je vous propose en fonction de ce que vous voulez proposer comme animation :</p>
<ul>
<li><strong>WebP animé</strong> : stickers, emojis, petites animations en boucle avec transparence. Le meilleur ratio poids/qualité pour ce cas.</li>
<li><strong>Vidéo MP4/WebM</strong> : si votre animation dépasse 5 secondes ou n'a pas besoin de transparence, une vidéo sera TOUJOURS plus légère. Un MP4 pèse ~50% de moins qu'un WebP animé pour le même contenu. Utilisez ``.</li>
<li><strong>
<a href="https://fr.wikipedia.org/wiki/Lottie_%28animation%29">Lottie</a>
</strong> : pour les animations vectorielles (icônes, UI), c'est imbattable en poids (quelques Ko) et c'est scalable. Faut juste le player JS (~60 Ko mis en cache). J'suis sûr que vous ne connaissiez pas !!</li>
<li><strong>APNG</strong> : si vous avez besoin de lossless absolu (logos, texte animé), c'est supporté partout mais c'est lourdingue.</li>
</ul>
<p>Voilà, si vous avez encore des GIFs animés avec transparence qui traînent sur votre site, vous savez maintenant ce qu'il vous reste à faire.</p>
<p>Amusez-vous bien !</p>