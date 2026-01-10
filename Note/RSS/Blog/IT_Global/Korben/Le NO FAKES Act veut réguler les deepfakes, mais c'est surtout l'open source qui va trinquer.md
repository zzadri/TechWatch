---
title: "Le NO FAKES Act veut réguler les deepfakes, mais c'est surtout l'open source qui va trinquer"
author: "Korben"
date: 2026-01-09T14:36:38.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/legislation-juridique"
  - "intelligence-artificielle/ia-developpement"
  - "deepfake"
  - "états-unis"
  - "intelligence artificielle"
  - "législation"
  - "open source"
rss_source: Blog
url: https://korben.info/no-fakes-act-open-source-menace.html
note: 0
seen: false
---

<p>Après le DMCA, après
<a href="https://korben.info/non-au-projet-de-loi-dadvsi.html">la DADVSI</a>
, après SOPA, après PIPA, après EARN IT... voici le NO FAKES Act ! Bref, un nouveau <strong>projet de loi</strong> américain pondu par des gens qui visiblement n'ont jamais lancé un git clone de leur vie.</p>
<p>Le texte (
<a href="https://www.congress.gov/bill/119th-congress/senate-bill/1367">S.1367, 119e Congrès</a>
, introduit en avril 2025) part d'une intention louable qui est de protéger les gens contre les deepfakes non consentis. Vous savez, ces vidéos truquées où votre tête se retrouve sur un corps qui n'est pas le vôtre, de préférence à poil...</p>
<p>Mais comme toujours, l'enfer est pavé de bonnes intentions et la méthode choisie va potentiellement atomiser tout l'écosystème de l'IA open source.</p>
<p>En fait, une large partie des services qui hébergent du contenu généré par les utilisateurs devront mettre en place une logique de <em>notice-and-staydown</em> basée sur du &quot;<em>digital fingerprinting</em>&quot; afin de pouvoir retirer le contenu signalé et empêcher que les mêmes œuvres réapparaissent après notification. De quoi faire pleurer donc n'importe quel admin sys qui a déjà dû gérer un serveur de modération.</p>
<p>Et là où ça se corse c'est que contrairement au
<a href="https://korben.info/le-dmca-sassouplit-pour-le-plus-grand-bonheur-des-acheteurs.html">DMCA et ses exceptions</a>
, ce texte ne prévoit pas de véritable mécanisme de contre-notification façon DMCA. Quelqu'un signale votre contenu comme étant un deepfake ? Hop, c'est retiré. Vous pensez que c'est une erreur ? La seule voie prévue pour espérer une remise en ligne passe par une action en justice (sous 14 jours) contre l'expéditeur de la notification. Alors direction le tribunal fédéral, les amis...</p>
<p>Et les coûts de conformité estimés par la
<a href="https://ccianet.org/articles/the-real-costs-of-the-no-fakes-act/">CCIA</a>
donnent le vertige car en moyenne, ça devrait tourner à environ 1,64 million de dollars la première année pour une simple startup. Et je ne parle même pas des projets open source qui distribuent des modèles d'IA générative... Comment Stable Diffusion ou Whisper pourraient-ils implémenter du fingerprinting sur des modèles que n'importe qui peut télécharger et faire tourner localement ? Mystère et boule de gomme !</p>
<p>Le truc bien moche, c'est que le texte prévoit des dommages et intérêts pouvant grimper jusqu'à 750 000 dollars par œuvre pour les plateformes non conformes. Autrement dit, si une plateforme ne réagit pas correctement après notification, elle peut devenir bien plus exposée à ce que font ses utilisateurs avec des outils d'IA... Voilà donc de quoi sérieusement refroidir les ardeurs de quiconque voudrait partager un petit modèle open weights.</p>
<p>Dans un autre style, ça me rappelle
<a href="https://korben.info/youtube-dl-dans-la-sauce.html">l'affaire youtube-dl</a>
où le DMCA avait été utilisé pour faire retirer un outil open source de GitHub sauf que là, on passe à l'échelle supérieure.</p>
<p>Voilà donc encore un lance-flammes législatif imaginé pour tuer une mouche et malheureusement, l'open source risque d'être le dommage collatéral de ce texte mal calibré.</p>
<p>Voilà les amis... l'avenir de l'IA ouverte pourrait bien se jouer dans les mois qui viennent aux US, et ça, ça va faire mal.</p>
<p>
<a href="https://www.reddit.com/r/LocalLLaMA/comments/1i6t8ah/if_the_no_fakes_act_passes_it_will_destroy_open/">Source</a>
</p>