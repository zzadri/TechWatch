---
title: "Dotenv Mask Editor - Fini les clés API à l'air libre"
author: "Korben"
date: 2026-03-10T09:35:57.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "vie-privee-anonymat"
  - ".env"
  - "extension vscode"
  - "VSCode"
rss_source: Blog
url: https://korben.info/dotenv-mask-editor.html
note: 0
seen: false
---

<p>Et si vos fichiers .env se transformaient en un joli tableau avec des astérisques partout afin d'assurer la confidentialité de vos clés API et autres crédentials ? Hé bien c'est exactement ce que propose
<a href="https://github.com/xinbenlv/dotenv-mask-editor">Dotenv Mask Editor</a>
, une extension VS Code qui remplace carrément l'éditeur texte par une grille.</p>
<p>Du coup, vos clés API, tokens AWS, mots de passe PostgreSQL et autres <code>STRIPE_SECRET_KEY</code> s'affichent sous forme de <code>******</code> et vous pouvez bosser dessus même si quelqu'un mate par-dessus votre épaule.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dotenv-mask-editor/dotenv-mask-editor-2.png" alt="" loading="lazy" decoding="async">
<p>En gros, dès que vous ouvrez un fichier .env (ou .env.local, .env.production... bref, tout ce qui matche le pattern), l'extension vous présente vos variables dans un tableau à deux colonnes. Les clés à gauche, les valeurs masquées à droite. Pour modifier une valeur, hop, vous cliquez dessus et elle se dévoile le temps de l'édition. Vous cliquez ailleurs, c'est re-masqué. Pas de sauvegarde manuelle à faire, ça se fait tout seul.</p>
<p>Le masquage se déclenche à partir de 6 caractères (en dessous, c'est probablement pas un secret... genre <code>PORT=3000</code> ou <code>DEBUG=true</code>, on s'en fiche). Et le truc cool, c'est que tout tourne en local sur votre machine.</p>
<img src="https://korben.info/dotenv-mask-editor/dotenv-mask-editor-1.gif" alt="" loading="lazy" decoding="async">
<p>Si vous vous dites &quot;mais attends, y'a pas déjà
<a href="https://korben.info/securisez-vos-demos-de-code-avec-camouflage-le-protecteur-de-secrets-pour-vs-code.html">Camouflage</a>
pour ça ?&quot;... oui et non. Camouflage masque vos secrets avec un overlay pendant les démos et le partage d'écran, mais vous continuez à éditer dans l'éditeur texte classique. Dotenv Mask Editor, lui, change complètement l'interface, c'est un éditeur de tableau dédié aux variables d'environnement. Deux approches différentes du coup, et rien ne vous empêche d'utiliser les deux.</p>
<p>L'extension est sous licence MIT, fonctionne sur toutes les plateformes (Windows, Linux, macOS, même VS Code Web) et vous pouvez ajouter des patterns de fichiers personnalisés dans vos settings.json.</p>
<p>D'ailleurs, si vous voulez l'installer, c'est du classique : Ctrl+Shift+X dans VS Code (Cmd+Shift+X sur Mac), vous tapez &quot;dotenv mask&quot; et voilà.</p>
<p>Avec ça, vos secrets restent secrets mais faut quand même pas oublier de mettre votre .env dans le .gitignore hein. ^^</p>