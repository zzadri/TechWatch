---
title: "Quand 2 frangins construisent une IA vidéo dans leur garage"
author: "Korben"
date: 2026-01-23T13:37:20.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/startups-business"
  - "intelligence-artificielle/generation-images"
rss_source: Blog
url: https://korben.info/quand-2-frangins-construisent-une-ia-video-dans-leur-garage.html
note: 0
seen: false
---

<p>Un modèle text-to-video open source, gratuit et capable de tourner ailleurs que sur un supercalculateur de la NASA ?</p>
<p>J'avoue, j'ai cru au fake en découvrant le truc, surtout quand on voit la puissance de feu qu'il faut chez OpenAI (Sora) ou Google (Veo) pour sortir le moindre clip de 3 secondes. Mais BON, parfois, il suffit de deux frères motivés pour bousculer un peu les géants de l'IA.</p>
<p>Et c'est 2 frères, ce sont Sahil et Manu Chopra, qui depuis l'automne 2022 bosse avec acharnement sur leur modèle de génération de vidéos baptisé <strong>
<a href="https://huggingface.co/collections/Linum-AI/linum-v2-2b-text-to-video">Linum</a>
</strong>.</p>
<p>Leur histoire est assez dingue et c'est pour ça que je vous la raconte aujourd'hui. En fait, au début, ils ont fait comme tout le monde. C'est à dire qu'ils ont essayé de bidouiller Stable Diffusion XL pour lui faire cracher de la vidéo. Ils ont fini par mettre au point une extension un peu &quot;hacky&quot; basé sur un modèle image, sauf que ça ne marchait pas très bien.</p>
<p>Enfin si, ça sortait des GIFs d'une seconde en 180p pour Discord mais pas vraiment de quoi faire trembler Hollywood et
<a href="https://korben.info/matthew-mcconaughey-trademark-ia-deepfake-analyse.html">Matthew McConaughey</a>
(lol). Le problème, c'est que les VAE (les encodeurs d'images) ne comprennent rien au temps qui passe, alors ils traitent chaque frame indépendamment et ça donne cet effet de scintillement insupportable qu'on retrouve dans pas mal de générateurs vidéo libre ou open source.</p>
<p>Du coup, ils ont pris une décision radicale. Tout foutre à la poubelle et repartir de zéro !</p>
<p>Ils ont donc passé deux longues années à batir <strong>Linum v2</strong> &quot;from scratch&quot;. Cela veut dire qu'il ont du trouver les données, entraîner des modèles de vision pour filtrer le dataset, mettre manuellement des légendes sur des milliers de vidéos, gérer les clusters de GPU... et j'en passe !</p>
<div class="video-container" id="video-container-quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/quand-2-frangins-construisent-une-ia-video-dans-leur-garage/quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/quand-2-frangins-construisent-une-ia-video-dans-leur-garage/quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Et à la clé de tout ce travail, ils ont fini par obtenir un modèle de <strong>2 milliards de paramètres</strong> (ce qui est minuscule pour de la vidéo, je tiens à le dire) capable de générer des clips de 2 à 5 secondes en 720p !</p>
<p>Et le plus beau c'est que c'est sous licence <strong>Apache 2.0</strong> donc en open source.</p>
<p>Pour réussir cette prouesse, ils n'ont pas eu d'autre choix que d'être malins.</p>
<p>Par exemple, ils ont choisi d'utiliser le VAE de Wan 2.1 (qui gère très bien la compression temporelle) pour ne pas réinventer la roue sur cette partie. Leur vision en fait, c'est de voir ces modèles comme des &quot;moteurs de rendu inversés&quot;. Au lieu de placer des polygones et des lumières comme dans Blender, vous décrivez la scène et le modèle fait le reste.</p>
<div class="video-container" id="video-container-quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mov">
<video controls preload="metadata" >
<source src="https://korben.info/quand-2-frangins-construisent-une-ia-video-dans-leur-garage/quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mov" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/quand-2-frangins-construisent-une-ia-video-dans-leur-garage/quand-2-frangins-construisent-une-ia-video-dans-leur-garage-1.mov&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Linum est un modèle encore jeune et la physique est parfois aux fraises puis ça manque de son mais pour une équipe de deux personnes face à des boîtes qui ont des milliards de budget, le résultat est plutôt pas mal. Faut saluer le taf !</p>
<p>Donc si vous avez une machine qui tient la route (ou un bon cloud) et quelques compétences techniques, sachez que les poids sont disponibles sur
<a href="https://huggingface.co/collections/Linum-AI/linum-v2-2b-text-to-video">Hugging Face si ça vous chauffe</a>
.</p>
<p>
<a href="https://www.linum.ai/field-notes/launch-linum-v2">Source</a>
</p>