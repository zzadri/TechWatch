---
title: "Z80 Sans, la police de caractères qui désassemble du code machine toute seule"
author: "Korben"
date: 2026-03-17T13:56:38.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "developpement/outils-developpement"
  - "code"
  - "font"
  - "opentype"
  - "police"
  - "z80sans"
rss_source: Blog
url: https://korben.info/z80-sans-la-police-de-caracteres-qui-desassemble-du-code-machine-toute-seule.html
note: 0
seen: false
---

<p>Un développeur a créé une police OpenType capable de convertir des opcodes hexadécimaux du processeur Z80 en instructions assembleur lisibles.</p>
<p>Il suffit de coller le code machine dans un traitement de texte, de changer la police, et les mnémoniques s'affichent en clair. Le projet, disponible sur GitHub, détourne les tables de substitution de glyphes de manière plutôt rigolote.</p>
<h2 id="une-police-pas-un-logiciel">Une police, pas un logiciel</h2>
<p>L'idée est en fait assez simple. Vous balancez une suite de caractères hexadécimaux dans LibreOffice Writer, puis vous sélectionnez cette police, Z80 Sans donc, et sous vos yeux ébahis, le texte se transforme en instructions assembleur.</p>
<p>Pas besoin d'installer un désassembleur, pas besoin de ligne de commande. La police fait tout le travail.</p>
<p>Derrière cette apparente simplicité, le développeur nevesnunes a exploité deux composants du standard OpenType que l'on retrouve habituellement dans des usages bien plus classiques : la table de substitution de glyphes (GSUB) et la table de positionnement (GPOS).</p>
<p>Ce sont les mêmes mécanismes qui permettent d'afficher correctement l'arabe ou de fusionner deux lettres en une ligature comme le &quot;æ&quot;. Ici, ils servent à reconnaître des séquences hexadécimales et à les remplacer par les mnémoniques Z80 correspondants.</p>
<h2 id="458-752-combinaisons-à-gérer">458 752 combinaisons à gérer</h2>
<p>Le Z80 est un processeur 8 bits qui accepte des adresses sur 16 bits et plusieurs registres comme opérandes. Résultat : une seule instruction peut donner jusqu'à 458 752 combinaisons possibles.</p>
<p>Et comme les octets hexadécimaux sont encodés dans un ordre différent de celui dans lequel ils doivent être affichés en assembleur, le problème se corse vite. Les adresses en little-endian et les offsets signés en complément à deux ajoutent encore une couche de difficulté.</p>
<p>Pour s'en sortir, nevesnunes a construit un parseur par descente récursive qui génère automatiquement toutes les règles de substitution nécessaires. Chaque quartet (0 à f) dispose de ses propres glyphes, soit 96 au total pour la partie numérique.</p>
<p>Le tout repose sur une édition directe des fichiers .ttx, la représentation XML des données de police, à partir de Noto Sans Mono et Droid Sans Mono.</p>
<h2 id="du-détournement-de-police-à-lart-de-la-bidouille">Du détournement de police à l'art de la bidouille</h2>
<p>Z80 Sans n'est pas le premier projet à détourner les capacités des polices OpenType. On a déjà vu Fontemon, un jeu vidéo complet caché dans une police, ou encore Addition Font, capable d'additionner deux nombres rien qu'avec le rendu typographique.</p>
<p>Il y a même eu Llama.ttf, qui embarquait un modèle d'IA directement dans un fichier de police. Mais un désassembleur complet pour un jeu d'instructions entier, c'est quand même autre chose en termes de complexité.</p>
<p>Visiblement, le projet comporte encore quelques petits bugs d'affichage sur certaines instructions complexes, et le code est qualifié par son propre auteur de &quot;qualité CTF&quot;, ce qui veut dire bidouille assumée.</p>
<p>Mais bon, on parle d'un type qui a réussi à faire rentrer un désassembleur Z80 dans une police de caractères. Les puristes de l'assembleur apprécieront le côté complètement absurde de la démarche, et les fans de rétro-informatique vont adorer.</p>
<p>Source :
<a href="https://lobste.rs/s/hbybe3/z80_sans_opentype_font_disassembles_z80">Lobste.rs</a>
</p>