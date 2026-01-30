---
title: "Un générateur de mots de passe qui utilise des regex"
author: "Korben"
date: 2026-01-28T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "developpement/outils-developpement"
  - "expressions régulières"
  - "generateur"
  - "mot de passe"
  - "open source"
  - "regex"
  - "sécurité"
  - "TypeScript"
rss_source: Blog
url: https://korben.info/generateur-mot-de-passe-regex-contraintes.html
note: 0
seen: false
---

<p>Vous avez déjà galéré à créer un mot de passe qui respecte les 42 règles imposées par un site un peu trop zélé ? Genre au moins 16 caractères, une majuscule, une minuscule, un chiffre, un caractère spécial, et surtout pas le prénom de votre chat ni votre date de naissance ?</p>
<p>C’est le genre de micro-agression qui peut flinguer une matinée ^^.</p>
<p>Heureusement, y’a un dev qui a eu une idée de génie en <strong>inversat complètement le problème grâce à la puissance brute des expressions régulières.</strong></p>
<p>Son outil s'appelle <strong>
<a href="https://gruhn.github.io/regex-utils/password-generator.html">RegExp Password Generator</a>
</strong> et comme son nom l'indique, c'est un générateur de mots de passe qui fonctionne avec des regex. Au lieu de cocher des cases un peu nazes dans une interface classique, vous définissez vos contraintes ligne par ligne sous forme d'expressions régulières.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/generateur-mot-de-passe-regex-contraintes/generateur-mot-de-passe-regex-contraintes-1.png" alt="" loading="lazy" decoding="async">
<p>Par exemple, vous balancez <code>^.{16,32}$</code> pour imposer une longueur entre 16 et 32 caractères, <code>[0-9]</code> pour exiger au moins un chiffre, and <code>[A-Z]</code> pour une majuscule. L’outil va alors calculer l’intersection de tous vos patterns pour vous sortir 5 mots de passe aléatoires qui matchent absolument toutes vos règles simultanément.</p>
<p>L'outil repose heureusement sur la bibliothèque TypeScript <strong>@gruhn/regex-utils</strong>. Pour ceux qui font du code, vous savez que manipuler des regex pour faire des intersections ou des compléments, c'est normalement une purge monumentale que la plupart des langages de programmation ne gèrent pas nativement.</p>
<p>C'est pourquoi ici, la lib fait tout le sale boulot de calcul d'ensemble pour s'assurer que vos contraintes ne sont pas contradictoires. Si vous demandez un truc impossible (genre un mot de passe qui doit être composé uniquement de chiffres ET uniquement de lettres), l’outil vous le dit direct au lieu de mouliner dans le vide.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/generateur-mot-de-passe-regex-contraintes/generateur-mot-de-passe-regex-contraintes-2.png" alt="" loading="lazy" decoding="async">
<p>Et tout tourne en local dans votre navigateur donc c'est cool pour la vie privée, par contre, gardez en tête que la lib supporte un sous-ensemble bien précis de la syntaxe RegExp de JavaScript. Inutile donc tenter des trucs ultra exotiques comme les <em>
<a href="https://fr.javascript.info/regexp-lookahead-lookbehind">lookbehinds</a>
</em> complexes, l'outil risque de vous renvoyer une erreur.</p>
<p>Le côté pratique, c'est que vos contraintes sont directement encodées dans l'URL. Du coup, vous pouvez bookmarker une config précise pour un site spécifique ou la partager avec vos collègues sans avoir à tout retaper à chaque fois. Un petit compteur affiche même le nombre total de combinaisons possibles avec vos règles, histoire de vérifier que vous n'avez pas créé un mot de passe trop prévisible (ou au contraire, un truc tellement restrictif qu'il n'existe qu'une seule possibilité).</p>
<p>Bref, j'ai trouvé ça original !</p>