---
title: "Comment votre imprimante vous espionne (et comment le vérifier)"
author: "Korben"
date: 2026-01-23T07:48:43.000Z
type: site
subject:
category: IT Global
tags:
  - "tutoriels-guides"
  - "vie-privee-anonymat/surveillance-tracking"
  - "défense de la vie privée"
  - "FBI"
  - "traçage des données"
rss_source: Blog
url: https://korben.info/comment-votre-imprimante-vous-espionne-et-comment-le-verifier.html
note: 0
seen: false
---

<p>Vous pensiez que votre imprimante de bureau était juste un objet d'un autre temps qui enchaine des bourrages papier toute la journée et vous réclame de l'encre hors de prix comme un enfant qui attend sa têtée ? Ben va falloir revoir vos priorités niveau paranoïa, parce que c'est bien plus que ça !</p>
<p>Une enquête du Washington Post vient en effet de révéler comment le FBI a identifié un de leurs lanceurs d'alerte grâce aux logs d'impression de son employeur. Aurelio Luis Perez-Lugones, spécialiste IT pour un sous-traitant du gouvernement américain, aurait fait <strong>des captures d'écran de documents classifiés</strong> dans un SCIF (ces salles ultra-sécurisées où même votre téléphone n'entre pas), puis les aurait collés dans Word avant de les imprimer.</p>
<p>Et comment ils l'ont su ?</p>
<p>Hé bien il semblerait que les logs d'impression de sa boîte aient joué un rôle clé dans l'enquête, en complément des caméras de vidéosurveillance, bien sûr.</p>
<p>Car oui, ces systèmes ne se contentent pas de noter &quot;<em>Jean-Michel a imprimé 47 pages le 15 janvier</em>&quot;. Non, ils peuvent stocker le contenu intégral des documents, les métadonnées, l'heure exacte, le poste de travail utilisé...etc. En gros, votre patron sait exactement ce que vous avez imprimé, et depuis combien de temps vous essayez de photocopier votre CV en douce.</p>
<p>Mais le plus flippant dans cette histoire, c'est que ça ne s'arrête pas aux logs réseau puisque même votre imprimante perso à la maison, elle-même, peut vous balancer, et cela depuis des décennies...</p>
<p>Vous avez déjà entendu parler des
<a href="https://korben.info/nouvelle-interview-dedward-snowden-nsa-surveillance.html">révélations d'Edward Snowden</a>
sur la surveillance de masse ? Ben là, c'est pareil, mais en version papier.</p>
<p>En effet, depuis les années 80, la plupart des imprimantes laser couleur intègrent un système de traçage appelé <strong>
<a href="https://fr.wikipedia.org/wiki/Code_d%27identification_de_machine">Machine Identification Code</a>
</strong> (MIC). Grâce à ce système, chaque page que vous imprimez contient une grille quasi-invisible de points jaunes d'environ 0,1 millimètre, espacés d'un millimètre. Ces points encodent le numéro de série de votre machine et la date/heure d'impression, ce qui fait que n'importe quel document imprimé peut être relié à une imprimante spécifique.</p>
<img src="https://korben.info/comment-votre-imprimante-vous-espionne-et-comment-le-verifier/comment-votre-imprimante-vous-espionne-et-comment-le-verifier-1.avif" alt="" loading="lazy" decoding="async">
<p><em>C'est discret, faut de bons yeux.</em></p>
<p>Le Chaos Computer Club et l'EFF
<a href="https://korben.info/comment-decoder-le-marqueur-cache-par-les-imprimantes-lasers.html">ont documenté ce système depuis des années</a>
et l'EFF maintient même une liste des fabricants qui utilisent ces mouchards (spoiler : la plupart des grandes marques y sont).</p>
<h2 id="comment-vérifier-si-votre-imprimante-vous-espionne">Comment vérifier si votre imprimante vous espionne</h2>
<p>Première étape : imprimez une page avec du contenu coloré sur fond blanc. Ensuite, examinez-la sous une lumière bleue ou un microscope et là vous verrez probablement une grille de points jaunes, à peine détectables à l'œil nu.</p>
<p>Pour les plus techniques d'entre vous, l'outil
<a href="https://github.com/dfd-tud/deda">DEDA</a>
(Dot Evidence Documentation and Analysis) développé par l'Université Technique de Dresde permet d'analyser et même d'anonymiser ces traces.</p>
<h2 id="comment-auditer-les-logs-dimpression-en-entreprise">Comment auditer les logs d'impression en entreprise</h2>
<p>Si vous êtes admin réseau ou simplement curieux de savoir ce que votre boîte enregistre, voici où chercher :</p>
<p><strong>Sur Windows Server</strong>, direction la console de gestion d'impression. Les logs sont généralement dans l'Observateur d'événements sous &quot;Applications et services&quot; &gt; &quot;Microsoft&quot; &gt; &quot;Windows&quot; &gt; &quot;PrintService&quot;. Activez les logs &quot;Operational&quot; si ce n'est pas déjà fait.</p>
<p><strong>Sur les imprimantes réseau</strong>, accédez à l'interface web d'administration (généralement l'IP de l'imprimante dans un navigateur). Cherchez une section &quot;Logs&quot;, &quot;Journal&quot; ou &quot;Historique des travaux&quot;. Certains modèles HP Enterprise ou Xerox stockent des semaines entières de données.</p>
<p><strong>Sur les serveurs d'impression centralisés</strong> type PaperCut ou Equitrac, c'est la fête car ces solutions peuvent stocker énormément de données, du nom d'utilisateur jusqu'au contenu OCR des documents scannés si des modules ou intégrations spécifiques ont été activés.</p>
<h2 id="comment-limiter-ces-traces">Comment limiter ces traces</h2>
<p>Pour les points jaunes, DEDA propose un mode d'anonymisation qui ajoute du bruit dans le pattern. C'est pas parfait, mais ça complique sérieusement le traçage !</p>
<p>Après pour les logs réseau, c'est plus compliqué... En entreprise, vous n'avez généralement pas le contrôle. Par contre, si c'est chez vous, désactivez simplement la journalisation dans les paramètres de votre imprimante et évitez les services cloud des fabricants.</p>
<p>Ah et une dernière chose : si vous imprimez des documents sensibles mes petits lanceurs d'alertes préférés, privilégiez <strong>une imprimante laser noir et blanc d'occasion payée en cash</strong>. Les modèles monochromes n'ont pas les fameux points jaunes, et une machine sans historique réseau, c'est une machine qui ne parle pas.</p>
<p>Encore une fois c'est difficile de lutter contre cette surveillance généralisée, mais au moins maintenant vous savez que votre imprimante n'est pas qu'un simple périphérique !</p>
<p>C'est potentiellement le meilleur indic de votre bureau !</p>
<p>
<a href="https://hardware.slashdot.org/story/26/01/21/2342252/fbis-washington-post-investigation-shows-how-your-printer-can-snitch-on-you">Source</a>
</p>