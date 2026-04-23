---
title: "Linux va abandonner le support du processeur Intel 486, sorti en 1989"
author: "Korben"
date: 2026-04-08T09:25:18.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "linux-open-source"
  - "Intel"
  - "Linux"
rss_source: Blog
url: https://korben.info/linux-va-abandonner-le-support-du-processeur-intel-486-sorti-en-1989.html
note: 0
seen: false
---

<p>Le noyau Linux 7.1 devrait supprimer la possibilité de compiler un noyau pour les processeurs Intel 486. C'est la première fois depuis 2012 qu'une architecture processeur est retirée du noyau, et le minimum requis passera du 486 au Pentium. L'Intel 486 a 37 ans.</p>
<h2 id="un-processeur-de-1989">Un processeur de 1989</h2>
<p>L'Intel 486 est sorti en 1989. C'est le processeur qui a fait passer les PC de la ligne de commande au monde graphique, et il a été vendu pendant une bonne partie des années 90.</p>
<p>Le 486SX, sa version sans coprocesseur mathématique, et l'AMD Elan, une variante embarquée, sont aussi concernés par cette suppression. Le patch a été proposé par Ingo Molnar, un des développeurs historiques du noyau Linux.</p>
<p>La dernière fois que Linux a retiré le support d'une architecture processeur, c'était en 2012, quand le 80386 avait été abandonné. Ca fait donc 14 ans que personne n'avait touché à ce genre de nettoyage.</p>
<h2 id="du-ménage-dans-le-code">Du ménage dans le code</h2>
<p>Le patch supprime trois options de configuration du noyau : M486, M486SX et MELAN. Sans ces options, il ne sera plus possible de compiler un noyau Linux spécifiquement pour un 486. Le processeur minimum deviendra le Pentium, qui supporte les instructions TSC et CMPXCHG8B, deux fonctions que le 486 ne gère pas.</p>
<p>Molnar explique que le code de compatibilité pour ces vieux processeurs pose régulièrement des problèmes et demande du temps de maintenance que les développeurs préfèrent consacrer à autre chose. Linus Torvalds avait d'ailleurs déclaré dès 2022 que les processeurs 486 n'étaient plus utilisés que comme pièces de musée.</p>
<h2 id="et-le-32-bits-alors-">Et le 32 bits, alors ?</h2>
<p>Le retrait du 486 ne veut pas dire que Linux abandonne le 32 bits. Le noyau continue de supporter les architectures 32 bits, et il y a encore suffisamment de processeurs Atom et de systèmes embarqués 32 bits en circulation pour que ça reste le cas un moment.</p>
<p>Mais la tendance est claire : l'avenir de Linux sur x86 est en 64 bits, et le code 32 bits finira par suivre le même chemin que le 486.</p>
<p>Aucune distribution Linux récente ne proposait de toute façon un noyau compilé pour 486. Les utilisateurs qui font tourner Linux sur ce type de matériel pourront continuer avec des noyaux plus anciens.</p>
<p>Ca concerne très peu de monde en pratique, mais c'est quand même un petit moment d'histoire informatique. Le 486 a été le premier vrai processeur grand public chez Intel, et le voir disparaître du noyau Linux après 37 ans de bons et loyaux services, ça fait quelque chose.</p>
<p>En tout cas les développeurs du noyau semblent soulagés de pouvoir enfin faire le ménage. Pour la petite histoire, mon premier PC était un 386 SX25, et je suis ensuite passé directement au Pentium 60 (celui qui avait le bug de la virgule flottante), je trouve ça dingue qu'avec tous les ordinateurs que j'ai eu chez moi, je n'ai jamais eu de 486 !</p>
<p>Source :
<a href="https://www.phoronix.com/news/Linux-7.1-Phasing-Out-i486">Phoronix</a>
</p>