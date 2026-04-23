---
title: "Un chercheur construit le premier processeur ternaire fonctionnel depuis 60 ans"
author: "Korben"
date: 2026-03-18T15:26:05.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/science-recherche"
  - "hardware-diy"
  - "5500fp"
  - "processeur"
  - "ternaire"
rss_source: Blog
url: https://korben.info/un-chercheur-construit-le-premier-processeur-ternaire-fonctionnel-depuis-60-ans.html
note: 0
seen: false
---

<p>Un chercheur indépendant vient de présenter le 5500FP, un processeur qui ne fonctionne pas en binaire mais en ternaire. Là où nos puces actuelles raisonnent en 0 et 1, celui-ci ajoute un troisième état : le -1. Le tout tourne sur un FPGA classique, et c'est le premier matériel ternaire généraliste depuis les années 1960.</p>
<h2 id="trois-états-au-lieu-de-deux">Trois états au lieu de deux</h2>
<p>Nos processeurs fonctionnent tous en binaire : chaque bit vaut 0 ou 1. Le système ternaire, lui, remplace le bit par un trit, qui peut valoir -1, 0 ou +1. Sur le papier, un trit stocke environ 1,58 fois plus de données qu'un bit. L'idée n'est pas nouvelle : le célèbre informaticien Donald Knuth a décrit le système ternaire comme le plus élégant des systèmes numériques.</p>
<p>Dans les années 1950, une équipe de l'Université de Moscou avait construit le Setun, le premier ordinateur ternaire. Mais la technologie binaire a pris le dessus, et depuis les années 1960, plus personne n'avait fabriqué de matériel ternaire fonctionnel.</p>
<h2 id="le-5500fp-un-processeur-risc-à-24-trits">Le 5500FP, un processeur RISC à 24 trits</h2>
<p>Claudio Lorenzo La Rosa, chercheur indépendant, a conçu le 5500FP : un processeur RISC de 24 trits qui fonctionne à 20 MHz sur un FPGA classique. Il dispose de 120 instructions et gère la synchronisation atomique en natif. La carte de développement est en open hardware.</p>
<p>Comme le Setun avant lui, le 5500FP simule la logique ternaire à partir de composants binaires : chaque trit est représenté par deux portes logiques. Ce n'est donc pas aussi efficace qu'un vrai circuit ternaire, mais ça a un avantage de taille : on peut le construire avec des composants disponibles dans le commerce, et il communique sans problème avec le reste du monde informatique, qui reste 100% binaire.</p>
<h2 id="pourquoi-cest-intéressant-">Pourquoi c'est intéressant ?</h2>
<p>Le ternaire équilibré simplifie certaines opérations que le binaire gère mal. Les nombres négatifs, par exemple, se manipulent sans bit de signe dédié : il suffit d'inverser tous les trits. La représentation des chiffres est aussi plus compacte.</p>
<p>Mais bon, le 5500FP reste un prototype de recherche à 20 MHz, on est très loin d'un concurrent pour les puces que l'on trouve dans nos Mac ou nos iPhone. L'objectif de La Rosa est de passer à terme du FPGA au silicium, ce qui permettrait d'atteindre des fréquences bien plus élevées.</p>
<p>C'est le genre de projet qui rappelle que l'informatique aurait pu prendre un chemin totalement différent. Le binaire s'est imposé dans les années 1960 pour des raisons industrielles plus que scientifiques, et depuis, personne n'a vraiment remis en question ce choix.</p>
<p>Source :
<a href="https://zenodo.org/records/18881738">Zenodo</a>
</p>