---
title: "YOR - Le robot open source à 10 000 dollars à monter soi-même"
author: "Korben"
date: 2026-04-05T05:28:52.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "robots-drones-vehicules/robots-robotique"
  - "Bras robotique"
  - "Raspberry Pi 5"
  - "robot DIY"
  - "robot open source"
rss_source: Blog
url: https://korben.info/yourownrobot-ai.html
note: 0
seen: false
---

<p>Quand je vois tout le taf que j'ai à la maison, je vous avoue que je rêve d'un robot qui vide le lave-vaisselle, arrose les plantes et ramasse le linge pendant que moi je glandouille sur le canapé (ou que je bosse parce que je glandouille jamais en fait...Argh...). Hé bien bonne nouvelle, une équipe de chercheurs de NYU vient de publier les plans complets pour en construire un et tout ça en open source pour environ 9 200 dollars !</p>
<p>YOR, pour &quot;<strong>
<a href="https://yourownrobot.ai/">Your Own Robot</a>
</strong>&quot;, c'est un robot mobile avec deux bras articulés, une base sur roues qui se déplace dans tous les sens, et un lift télescopique qui est tout simplement... un vérin de bureau debout. Du coup le robot peut descendre à 60 cm du sol pour ramasser vos chaussettes et monter à 1,24 m pour atteindre un placard en hauteur. Et le vérin se verrouille tout seul en cas de coupure de courant (comme ça, pas de bras qui s'écrasent au sol...).</p>
<div class="video-container" id="video-container-yourownrobot-ai-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/yourownrobot-ai/yourownrobot-ai-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/yourownrobot-ai/yourownrobot-ai-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Le coût total des composants revient comme je vous le disais à environ 9 200 dollars. Les deux bras représentent à eux seuls plus de la moitié du budget (5 000 dollars), la base roulante un bon quart (2 700 dollars). Le reste, c'est de l'électronique grand public et des profilés alu et le cerveau, c'est un Raspberry Pi 5 avec 16 Go de RAM. Quand on sait qu'un Mobile ALOHA (le robot de Stanford) revient à environ 32 000 dollars et que les plateformes commerciales dépassent les 100 000... y'a pas photo !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/yourownrobot-ai/yourownrobot-ai-1.png" alt="" loading="lazy" decoding="async">
<p><em>YOR et ses deux bras articulés sur base omnidirectionnelle</em></p>
<p>Un truc original dans ce robot, ce sont les pinces. L'équipe a d'ailleurs conçu des grippers custom capables de manipuler des objets délicats ou de serrer fort ce qui est bien utile et y'a aussi une caméra stéréo sur la tête pour que le robot cartographie son environnement et se repère tout seul dans une pièce.</p>
<p>Pour le piloter, pas besoin de matériel exotique puisque des manettes Meta Quest 3 suffisent. Vous restez debout derrière le robot et vous contrôlez tout, les bras, la base, la hauteur. Et le truc cool, c'est que quand vous déplacez la base, les pinces restent stables sur l'objet qu'elles tiennent. Cela lui permet par exemple d'attraper une assiette et de se déplacer vers le
<a href="https://korben.info/helix-02-robot-vide-lave-vaisselle.html">lave-vaisselle</a>
sans tout faire valdinguer.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/yourownrobot-ai/yourownrobot-ai-2.png" alt="" loading="lazy" decoding="async">
<p><em>YOR en action : lave-vaisselle, arrosage et ramassage</em></p>
<p>Côté recherche, l'équipe est même allée encore plus loin. En pilotant le robot à la main une centaine de fois (avec des iPhones fixés sur les pinces comme caméras supplémentaires), ils ont entraîné une IA capable de reproduire les gestes toute seule. Résultat, 9 réussites sur 10 dans un test de tri des déchets en autonomie (la poubelle JAUNE !!!!), du genre donc attraper un carton avec les deux bras, le soulever, contourner un obstacle, le déposer dans la poubelle de tri... et tout ça sans intervention humaine. Et bien sûr, si vous voulez tester vos propres algos avant de risquer du vrai matos, y'a un simulateur pour ça.</p>
<p>L'empreinte au sol de cette bestiole fait 43 × 34,5 cm. En gros, la taille d'un carton à pizza. Le projet est porté par une équipe de NYU et UC Berkeley et parmi les auteurs, on retrouve Soumith Chintala (NYU), le co-créateur de PyTorch. Toute la doc de construction est dispo sur
<a href="https://build.yourownrobot.ai/">build.yourownrobot.ai</a>
, avec la liste complète des composants en Google Sheets, les modèles CAD et le code Python sous licence MIT sur
<a href="https://github.com/YOR-robot/YOR">GitHub</a>
.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/yourownrobot-ai/yourownrobot-ai-3.png" alt="" loading="lazy" decoding="async">
<p><em>YOR face à la concurrence : petit, pas cher, open source</em></p>
<p>J'ai rarement vu un projet aussi bien documenté pour ce niveau de complexité mais attention quand même, ça reste un projet de recherche, et pas un kit Lego. Faut savoir souder, câbler des batteries, et être à l'aise avec Python et Git. C'est donc un sacré projet de plusieurs week-ends (comptez plutôt des mois si vous débutez). Mais c'est aussi ça qui est cool, puisque vous construisez VOTRE robot, et pas celui d'un constructeur chinois que vous avez payé une couille en dropshipping.</p>
<p>Si les
<a href="https://korben.info/toddlerbot-robot-humanoide-250-ridiculise-geants.html">robots open source</a>
vous branchent, le ToddlerBot à 4 300 dollars propose également une approche bipède imprimable en 3D, et si vous voulez voir ce que la coordination bimanuelle donne
<a href="https://korben.info/korben-aura-robot-humanoide.html">à l'échelle industrielle</a>
... y'a du choix.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/yourownrobot-ai/yourownrobot-ai-4.png" alt="" loading="lazy" decoding="async">
<p>Bref, 9 200 dollars, licence MIT, la liste complète des composants, ça fait grave envie !! En tout cas, c'est le genre de projet à suivre de prêt...</p>
<p>
<a href="https://arxiv.org/abs/2602.11150">Source</a>
</p>