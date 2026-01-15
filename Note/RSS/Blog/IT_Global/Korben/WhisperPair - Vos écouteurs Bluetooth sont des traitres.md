---
title: "WhisperPair - Vos écouteurs Bluetooth sont des traitres"
author: "Korben"
date: 2026-01-15T16:00:25.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "vie-privee-anonymat/surveillance-tracking"
  - "Bluetooth"
  - "vulnérabilité"
  - "WhisperPair"
rss_source: Blog
url: https://korben.info/whisperpair-vos-ecouteurs-bluetooth-sont-des-traitres.html
note: 0
seen: false
---

<p>Si vous pensiez que vos écouteurs sans fil étaient capables de garder vos secrets, j'ai une mauvaise nouvelle pour vous !</p>
<p>Des chercheurs du groupe COSIC de la KU Leuven (les mêmes génies qui avaient déjà
<a href="https://korback.info/comment-voler-tesla-model-x.html">hacké des Tesla</a>
il y a quelques années) viennent de dévoiler <strong>WhisperPair</strong>. C'est le petit nom d'une série de vulnérabilités qui touchent le protocole <strong>Google Fast Pair</strong>, et vous allez voir, ça craint.</p>
<p>Le protocole Fast Pair, censé nous faciliter la vie en appairant nos gadgets en un clic, oublie en fait de vérifier si l'appareil est réellement en mode appairage. Du coup, n'importe quel petit malin situé à portée de Bluetooth (environ 15 mètres dans les tests) peut se connecter silencieusement à votre casque ou vos enceintes, même si vous êtes déjà en train d'écouter votre podcast préféré. Pas besoin de bouton, pas besoin de confirmation, rien. C'est un peu le retour de la faille
<a href="https://korback.info/vos-casques-bluetooth-peuvent-vous-espionner.html">BlueSpy dont je vous parlais l'année dernière</a>
, mais en mode industriel.</p>
<p>Et quand je dis industriel, je n'exagère pas car les chercheurs ont testé 25 modèles différents et 17 d'entre eux sont tombés comme des mouches. Des marques comme Sony, Jabra, JBL, Marshall, Xiaomi, OnePlus, Logitech et même les Pixel Buds de Google sont touchées. Et une fois connecté, le pirate peut faire pas mal de trucs sympas (ou pas) comme injecter son propre audio à fond dans vos oreilles, perturber vos appels, ou pire, activer le micro pour écouter ce qui se passe autour de vous.</p>
<p>Mais attendez ça va encore plus loin car pour certains modèles Sony et Google, un attaquant peut carrément enregistrer votre casque sur son propre compte Google. Et là, c'est le combo gagnant pour le stalker puisqu'il peut vous suivre à la trace via le réseau <strong>Find Hub</strong> (le &quot;Localiser&quot; de Google). Le plus dingue, c'est que ça fonctionne même si vous utilisez un iPhone et que vous n'avez jamais touché à un produit Android de votre vie.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/whisperpair-vos-ecouteurs-bluetooth-sont-des-traitres/whisperpair-vos-ecouteurs-bluetooth-sont-des-traitres-2.png" alt="" loading="lazy" decoding="async">
<p>Si vous recevez une alerte de tracking sur votre smartphone, vous penserez probablement à un bug de votre propre appareil alors que c'est un espion qui regarde vos déplacements en temps réel... C'est moche.</p>
<p>Bref, Google a bien essayé de patcher le truc, notamment pour Find Hub, mais les chercheurs ont déjà trouvé un moyen de contourner le correctif en quelques heures. C'est la course à l'échalote habituelle et le vrai souci, c'est que pour corriger ça proprement, il faut une mise à jour du firmware de chaque accessoire par son constructeur. Et on sait tous comment ça se passe... à moins d'avoir l'application dédiée de la marque (que personne n'installe jamais) et de penser à vérifier les updates, vos écouteurs resteront vulnérables pendant des années.</p>
<p>Du coup, que faire ?</p>
<p>Hé bien déjà, si vous bossez sur des trucs ultra-sensibles, méfiez-vous du Bluetooth dans les lieux publics. C'est moche à dire en 2026, mais la sécurité des objets connectés reste encore trop souvent le parent pauvre de l'ergonomie.</p>
<p>Et si vous voulez creuser les détails techniques, les chercheurs ont tout mis sur
<a href="https://whisperpair.eu/">leur site dédié</a>
.</p>
<p>
<a href="https://www.wired.com/story/google-fast-pair-bluetooth-audio-accessories-vulnerability-patches/">Source</a>
</p>