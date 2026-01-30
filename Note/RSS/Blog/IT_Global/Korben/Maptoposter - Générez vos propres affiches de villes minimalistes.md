---
title: "Maptoposter - Générez vos propres affiches de villes minimalistes"
author: "Korben"
date: 2026-01-22T11:09:56.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "tutoriels-guides/astuces-productivite"
  - "carte"
  - "générateur posters"
  - "osm"
  - "poster"
rss_source: Blog
url: https://korben.info/maptoposter-generez-vos-propres-affiches-de-villes-minimalistes.html
note: 0
seen: false
---

<p>Si vous avez envie de refaire un peu votre déco chez vous, sans forcément raquer des fortunes chez des designers scandinaves en claquettes chaussettes, j'ai trouvé un petit soft qui va vous plaire. Ça s'appelle <strong>maptoposter</strong> et c'est un script Python qui permet de transformer la plupart des villes en une affiche minimaliste plutôt jolie</p>
<p>Vous lui donnez le nom d'une ville et son pays (c'est obligé pour pas que le script se perde), et il va piocher dans les données d'OpenStreetMap via la bibliothèque
<a href="https://wiki.openstreetmap.org/wiki/OSMnx">OSMnx</a>
pour vous dessiner un plan aux petits oignons au rendu propre généré par matplotlib avec des calques pour les routes, les parcs et l'eau. On est loin du screenshot Google Maps repassé au stylo Bic que certains vendent sur les marchés, ahaha.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/maptoposter-generez-vos-propres-affiches-de-villes-minimalistes/maptoposter-generez-vos-propres-affiches-de-villes-minimalistes-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et même sans les bâtiments qui ne sont pas inclus par défaut, je trouve que le rendu est vraiment très chouette... en tout cas suffisamment pour être encadré et exposé.</p>
<p>Et pas mal d'éléments sont également personnalisables, ce qui vous permettra de bricoler un truc propre avec les thèmes déjà inclus comme &quot;noir&quot; pour un look sombre ou &quot;sunset&quot; si vous êtes d'humeur nostalgique. Et si vous avez la flemme de choisir, vous pouvez même lui demander de générer la même ville avec tous les thèmes d'un coup.</p>
<p>Très pratique pour faire son choix avant de faire chauffer l'imprimante !</p>
<p>Maintenant pour ceux qui se demandent comment on installe ce bazar, c'est hyper fastoche. On récupère d'abord le dépôt, on installe les dépendances, et c'est parti :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/originalankur/maptoposter
</span></span><span class="line"><span class="cl">cd maptoposter
</span></span><span class="line"><span class="cl">pip install -r requirements.txt
</span></span></code></pre><p>Ensuite, pour sortir votre première affiche de Paris par exemple, c'est aussi simple que ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">python create_map_poster.py -c &#34;Clermont-Ferrand&#34; -C &#34;France&#34; -t noir -d 10000
</span></span></code></pre><p>Le paramètre <code>-d</code> définit le rayon en mètres autour du centre, donc vous pouvez vraiment zoomer sur votre quartier préféré ou prendre toute la métropole. D'ailleurs, ça me rappelle un peu
<a href="https://korben.info/creer-oeuvres-art-routes-ville-city-roads.html">City Roads</a>
dont je vous avais parlé il y a un bail, mais ici on a un peu plus de contrôle sur les thèmes JSON et les dégradés de couleurs.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/maptoposter-generez-vos-propres-affiches-de-villes-minimalistes/maptoposter-generez-vos-propres-affiches-de-villes-minimalistes-3.png" alt="" loading="lazy" decoding="async">
<p>On peut même ajouter des fondus dégradés sur les bords pour donner un petit côté artistique supplémentaire et tout ça sans passer par la case Photoshop. Je suis sûr aussi que le code peut être modifié pour traiter d'autres data que des cartes... En tout cas, si vous cherchez une idée cadeau originale ou si vous voulez juste donner un look original à votre bureau avec des posters de qualité, allez jeter un œil à ce projet.</p>
<p>Et n'oubliez pas de garder l'attribution OpenStreetMap si vous imprimez le résultat, c'est la moindre des choses !</p>
<p>
<a href="https://github.com/originalankur/maptoposter">C'est par ici que ça se passe</a>
!</p>
<p>Et merci à Lorenper !</p>