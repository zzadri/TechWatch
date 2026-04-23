---
title: "Helix 02 - Le robot qui vide votre lave-vaisselle pour de vrai"
author: "Korben"
date: 2026-01-30T08:06:54.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "robots-drones-vehicules/robots-robotique"
  - "Boston Dynamics"
  - "domotique"
  - "Figure AI"
  - "Helix 02"
  - "intelligence artificielle"
  - "robot humanoïde"
  - "robot Optimus"
rss_source: Blog
url: https://korben.info/helix-02-robot-vide-lave-vaisselle.html
note: 0
seen: false
---

<p>Vous vous souvenez peut-être de <strong>Figure 01</strong> qui nous avait tous bluffés l'année dernière en se faisant couler un petit café (qui a dit &quot;dans sa couche ??) ?</p>
<p>Hé bien, la startup Figure AI ne chôme pas (contrairement à nous le vendredi matin) puisqu'elle vient de dévoiler son <strong>Helix 02</strong>, la nouvelle version de son cerveau numérique.</p>
<p>Et là, accrochez-vous bien parce qu'on passe un cap ! En effet, ce robot est désormais capable de <strong>vider un lave-vaisselle</strong> de manière totalement autonome.</p>
<div class="video-container" id="video-container-helix-02-robot-vide-lave-vaisselle-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Alors je sais ce que vous vous dites : &quot;<em>Super, un truc à 150 000 balles pour faire ce que mon ado refuse de faire gratuitement</em>&quot;. Sauf que la prouesse technique derrière est assez dingue. Jusqu'à présent, les robots humanoïdes, notamment ceux de <strong>Boston Dynamics</strong> (le fameux Atlas), fonctionnaient beaucoup sur de la &quot;théorie du contrôle&quot;. En gros, des maths complexes pour garder l'équilibre, et du code impératif pour dire &quot;lève le bras de 30 degrés&quot;. C'est hyper précis, mais c'est lourd à coder et ça manque de souplesse.</p>
<p>Là, Figure a tout misé sur une approche <strong>pixels-to-action</strong> de type &quot;End-to-End&quot;. C'est ce qu'ils appellent le <strong>System 0</strong>.</p>
<div class="video-container" id="video-container-helix-02-robot-vide-lave-vaisselle-2.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-2.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-2.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>En gros, ils ont viré un peu moins de <strong>110 000 lignes de code C++</strong> (le langage bien verbeux qu'on adore détester) pour les remplacer par un modèle d'IA unifié. Le robot &quot;regarde&quot; avec ses caméras et le réseau de neurones décide directement des mouvements. Et c'est comme ça que d'un coup, le robot gère tout : l'équilibre, la manipulation des objets glissants, et même la correction de ses propres erreurs en temps réel.</p>
<p>C'est un peu comme si votre Roomba avait soudainement appris à faire du parkour tout en tenant un plateau de verres en cristal.</p>
<p>Bon, vous vous en doutez, le marketing ne nous dévoile pas tout car il y a un petit piège derrière cette innovation. En fait cette approche &quot;tout IA&quot; a aussi des limites car si le modèle hallucine un mouvement, le robot peut très bien décider de lancer votre assiette en porcelaine de Limoges à travers la pièce. C'est donc pour ça qu'ils gardent quand même des garde-fous (System 1 et System 2) pour la planification à long terme. Mais c'est pas encore demain que je laisserai ce machin seul avec mon chat, sauf si je veux le transformer en frisbee ^^.</p>
<p>D'ailleurs, si vous suivez un peu l'actu des
<a href="https://korben.info/korben-aura-robot-humanoide.html">robots humanoïdes</a>
, vous savez que la concurrence est rude notamment avec l'
<a href="https://korben.info/robot-optimus-tesla-autonome-domestique.html">Optimus de Tesla</a>
. Mais perso, je trouve que Figure a carrément une longueur d'avance sur la fluidité &quot;humaine&quot;, là où Optimus fait encore un peu &quot;mec bourré qui essaie de marcher droit&quot;. J'adorerai avoir un kit de dev pour jouer avec ce truc, mais vu le prix, je vais plutôt me rabattre sur Raspberry Pi... on fait avec ce qu'on a !</p>
<div class="video-container" id="video-container-helix-02-robot-vide-lave-vaisselle-3.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-3.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/helix-02-robot-vide-lave-vaisselle/helix-02-robot-vide-lave-vaisselle-3.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Et pour nous les bidouilleurs dans tout ça ?</p>
<p>Hé bien si vous n'avez pas 150 000 $ sous le matelas, sachez qu'il existe des projets open-source comme le <strong>
<a href="https://korben.info/toddlerbot-robot-humanoide-250-ridiculise-geants.html">ToddlerBot</a>
</strong> (un petit robot à environ 250$ imprimable en 3D) qui permettent de s'initier à la robotique bipède sans vendre un rein. C'est moins classe que Helix, mais au moins, si ça tombe, ça casse juste du PLA. Un coup de colle et c'est reparti !</p>
<p>Bref, on n'est pas encore au stade où il viendra vous border le soir, mais pour ce qui est des corvées ménagères, ça sent bon la fin de l'esclavage humain (pour le remplacer par celui des machines, mais chut, faut pas leur dire).</p>
<p>Amusez-vous bien !</p>
<p>
<a href="https://www.figure.ai/news/helix-02">Source</a>
</p>