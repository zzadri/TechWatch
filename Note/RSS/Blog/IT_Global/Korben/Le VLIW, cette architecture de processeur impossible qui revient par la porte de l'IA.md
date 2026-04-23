---
title: "Le VLIW, cette architecture de processeur "impossible" qui revient par la porte de l'IA"
author: "Korben"
date: 2026-04-08T13:10:52.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "intelligence-artificielle/ia-developpement"
  - "IA"
  - "Intel"
  - "itanium"
  - "vliw"
rss_source: Blog
url: https://korben.info/le-vliw-cette-architecture-de-processeur-impossible-qui-revient-par-la-porte-de-lia.html
note: 0
seen: false
---

<p>La
<a href="https://www.youtube.com/@Asianometry">chaîne YouTube Asianometry</a>
vient de publier une vidéo qui retrace l'histoire du VLIW, une architecture de processeur née dans les années 80 et longtemps considérée comme un échec. Sauf que cette technologie, enterrée avec l'Itanium d'Intel, refait surface dans les puces dédiées à l'intelligence artificielle. Et elle est peut-être déjà dans votre smartphone.</p>
<h2 id="le-principe-et-cest-un-peu-technique">Le principe, et c'est un peu technique</h2>
<p>Si vous ne connaissez pas Asianometry, c'est une chaîne qui décortique l'histoire des semi-conducteurs avec un vrai talent de vulgarisation, et cette vidéo sur le VLIW (pour Very Long Instruction Word) ne fait pas exception.</p>
<p>L'idée est assez simple sur le papier. Un processeur classique exécute ses instructions une par une, ou les réordonne à la volée avec du matériel dédié (c'est ce que font les puces modernes avec l'exécution &quot;out-of-order&quot;).</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/J7157XB8rxc?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le VLIW fait l'inverse : c'est le compilateur, le logiciel qui transforme le code en instructions machine, qui regroupe à l'avance plusieurs opérations dans un seul &quot;mot&quot; très long. Du coup, le processeur n'a plus qu'à exécuter le paquet en une seule fois, sans se pose la moindre question. Le matos est de fait plus simple, moins gourmand en énergie, et plus rapide.</p>
<p>Le problème, c'est que tout repose sur le compilateur. S'il ne trouve pas assez d'opérations à paralléliser, le processeur tourne à vide. Et écrire un compilateur capable de faire ça correctement, c'est un casse-tête qui a occupé des chercheurs pendant des décennies.</p>
<h2 id="litanium-le-plus-gros-pari-raté-dintel">L'Itanium, le plus gros pari raté d'Intel</h2>
<p>Les premières tentatives commerciales datent des années 80 avec Multiflow et Cydrome, deux entreprises qui ont fait faillite. Intel a sorti le i860 en 1989, un processeur VLIW quasi impossible à programmer. Et puis il y a eu l'Itanium. Développé avec HP à partir de 1994 sous le nom IA-64, ce processeur devait remplacer le x86 et dominer les serveurs. Les analystes prédisaient la fin des architectures classiques.</p>
<p>Quand l'Itanium est sorti en 2001 après dix ans de développement, les performances étaient décevantes, la compatibilité avec les logiciels existants était catastrophique, et AMD avait entre-temps lancé le x86-64 qui faisait tout pareil en restant compatible avec l'ancien. L'Itanium est devenu un produit de niche avant de disparaître. La presse tech l'a rebaptisé &quot;Itanic&quot;, en référence au Titanic.</p>
<h2 id="le-retour-par-lintelligence-artificielle">Le retour par l'intelligence artificielle</h2>
<p>Le VLIW n'a jamais complètement disparu. Texas Instruments l'utilise dans ses processeurs de traitement du signal depuis 1997 avec la famille TMS320C6000. Le DSP Hexagon de Qualcomm, celui qui gère l'inférence IA dans les puces Snapdragon, est lui aussi basé sur du VLIW.</p>
<p>Et Groq, la startup qui fait beaucoup parler d'elle pour la vitesse de ses puces d'inférence, utilise une architecture VLIW où le matériel ne prend aucune décision à l'exécution.</p>
<p>L'inférence de réseaux de neurones, c'est justement le type de calcul idéal pour le VLIW : des opérations régulières, prévisibles, massivement parallèles.</p>
<p>Pas besoin de réordonnancer quoi que ce soit, le compilateur peut tout planifier en amont. Des chercheurs travaillent d'ailleurs sur des extensions RISC-V qui intègrent des principes VLIW pour combiner le meilleur des deux mondes.</p>
<p>C'est quand même amusant de voir une technologie enterrée il y a vingt ans revenir grâce à l'IA. Le VLIW a échoué dans les années 2000 parce que le code des logiciels classiques est trop imprévisible pour être optimisé par un compilateur.</p>
<p>Mais l'inférence IA, c'est l'exact opposé : tout est prévisible et régulier. Du coup, l'architecture qui devait remplacer le x86 se retrouve à alimenter les accélérateurs IA de votre Snapdragon. Comme quoi, en informatique, rien ne meurt vraiment.</p>
<p>Source :
<a href="https://hackaday.com/2026/04/07/a-history-on-the-impossible-vliw-computing/">Hackaday</a>
</p>