---
title: "Fast SAM 3D Body - Quand l'IA scanne votre corps en 3D en 65ms"
author: "Korben"
date: 2026-03-17T13:33:27.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "robots-drones-vehicules/robots-robotique"
  - "motion capture"
  - "robot humanoïde"
rss_source: Blog
url: https://korben.info/fast-sam-3d-body-reconstruction-temps-reel-robots.html
note: 0
seen: false
---

<p>Vous prenez une photo de quelqu’un avec votre téléphone et magie magie, en une fraction de seconde, vous obtenez <strong>un modèle 3D complet de son corps</strong>. Ses bras, ses jambes, ses mains, ses pieds... tout y est, modélisé en 3D comme si vous aviez un vrai studio de motion capture à Hollywood.</p>
<p>Et ben c’est exactement ce que fait
<a href="https://github.com/facebookresearch/sam-3d-body">SAM 3D Body</a>
, un modèle d’IA développé par Meta.</p>
<p>En gros, vous lui filez une image de vous et l’IA reconstruit votre corps en volume, avec le squelette, les articulations et la surface de la peau. Jusqu’ici, ce genre de techno existait déjà mais c’était hyper lent, genre plusieurs secondes par image. Donc pas top si vous vouliez que ça suive, par exemple, vos mouvements en direct.</p>
<p>Et c’est là qu’une équipe de chercheurs incroyable (USC, NVIDIA et Meta Reality Labs) a eu la bonne idée d’optimiser tout ça. Leur version accélérée, baptisée
<a href="https://yangtiming.github.io/Fast-SAM-3D-Body-Page/">Fast SAM 3D Body</a>
, fait exactement le même boulot mais quasiment 11 fois plus vite. Du coup, il ne faut plus que 65 millisecondes pour reconstruire un corps entier en 3D sur une RTX 5090. C’est à peu près le temps d’un clic de souris ! Autrement dit, on peut ENFIN faire du vrai temps réel !</p>
<p>Au lieu de faire tourner un algorithme qui optimise la pose du corps de manière itérative (ce qui prend du temps), ils ont tout simplement remplacé tout ça par un réseau de neurones qui donne directement le résultat en 1 passe. Et cette astuce seule rend la conversion entre formats de modèle 3D plus de 10 000 fois plus rapide ! C'est ouf !</p>
<p>Mais alors concrètement, à quoi ça sert tout ça ?</p>
<p>Hé bien d'abord à la robotique si chère à mon cœur car imaginez un
<a href="https://korben.info/unitree-g1-robot-humanoide-polyvalent-accessible.html">robot humanoïde comme le chinois Unitree G1</a>
équipé d’une simple caméra. Vous faites un geste devant lui, et il le reproduit instantanément avec ses bras et ses jambes.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/fast-sam-3d-body-reconstruction-temps-reel-robots/fast-sam-3d-body-reconstruction-temps-reel-robots-1.jpg" alt="" loading="lazy" decoding="async">
<p><strong>Robot chinois en dépression à cause d'un dropshipping mal exécuté</strong></p>
<p>Dans la vidéo partagée par l'équipe, on voit que le robot manipule des objets et se déplace en copiant les mouvements d’un humain filmé par une caméra, sans aucun capteur sur le corps.</p>
<div class="video-container" id="video-container-fast-sam-3d-body-reconstruction-temps-reel-robots-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/fast-sam-3d-body-reconstruction-temps-reel-robots/fast-sam-3d-body-reconstruction-temps-reel-robots-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/fast-sam-3d-body-reconstruction-temps-reel-robots/fast-sam-3d-body-reconstruction-temps-reel-robots-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Mais au delà de la robotique, c’est aussi une petite révolution pour tous les créatifs et les bidouilleurs car aujourd’hui, faire de la motion capture, ça coûte une blinde en matériel (combinaison à marqueurs, caméras infrarouges, studio dédié...et j'en passe).</p>
<p>Alors que là, avec une webcam et un bon GPU, vous pouvoir facilement capter des mouvements 3D exploitables pour de l’animation, du jeu vidéo indie ou du prototypage. Par contre, attention, ça ne remplacera pas un vrai studio pro pour de la production ciné, faut pas trop rêver non plus. Enfin, pour le moment !</p>
<p>Le code est dispo sur
<a href="https://github.com/yangtiming/Fast-SAM-3D-Body">GitHub</a>
, le paper sur
<a href="https://arxiv.org/abs/2603.15603">arXiv</a>
, et les modèles pré-entraînés de SAM 3D Body sur
<a href="https://huggingface.co/facebook/sam-3d-body-dinov3">Hugging Face</a>
. D’ailleurs, si vous voulez voir ce que donnent les
<a href="https://korben.info/robot-humanoide-lessive-domestique-figure-02.html">robots qui font la lessive</a>
avec ce genre de techno, c’est par là.</p>
<p>Bref, y’a plus qu’à tester !</p>
<p>
<a href="https://yangtiming.github.io/Fast-SAM-3D-Body-Page/">Source</a>
</p>