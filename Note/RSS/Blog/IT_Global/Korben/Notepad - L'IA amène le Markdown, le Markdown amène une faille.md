---
title: "Notepad - L'IA amène le Markdown, le Markdown amène une faille"
author: "Korben"
date: 2026-02-11T19:45:11.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "IA"
  - "Microsoft"
  - "Notepad++"
  - "sécurité"
  - "Windows"
rss_source: Blog
url: https://korben.info/notepad-ia-faille-securite-windows.html
note: 0
seen: false
---

<p><strong>Notepad</strong>, c'est je crois LE truc le plus basique de Windows depuis 40 ans (avec winver.exe... lol). C'est un éditeur de texte tellement simple qu'il n'avait même pas de correcteur orthographique jusqu'en 2024. Sauf que Microsoft a décidé d'y coller de l'IA, et avec l'IA est arrivé le support du Markdown... et c'est ce parser Markdown tout neuf qui a ouvert une faille permettant d'exécuter du code à distance.</p>
<p>Mais lol.</p>
<p>Car oui mes amis, dans la foulée des fonctions IA (AI Rewrite, tout ça), le bloc-notes de Windows 11 sait maintenant interpréter le Markdown. Il gère désormais les fichiers .md, affiche les liens cliquables, le formatage...etc... et c'est là que ça coince !</p>
<p>En effet, la faille CVE-2026-20841 exploite une injection de commande via des liens malveillants dans un fichier Markdown. Vous ouvrez le fichier, vous cliquez sur le lien, et hop, exécution de code à distance sur votre bécane. Personne chez M$ n'avait pensé à filtrer les protocoles des URL. Résultat, un lien du type file:///C:/Windows/System32/cmd.exe ou ms-msdt:// s'exécute comme si de rien n'était.</p>
<p>C'est con, c'était si simple de limiter ça à http+s ... Bref, tout ça parce que maintenant ce machin a besoin d'aller sur Internet... Roooh</p>
<p>Cette faille fait partie du Patch Tuesday de février 2026, qui corrige au passage 58 vulnérabilités dont 6 zero-days déjà activement exploités. Microsoft classe celle de Notepad comme &quot;Important&quot; (pas &quot;Critical&quot;), parce qu'il faut quand même que vous cliquiez sur le lien piégé. Tu m'étonne John !</p>
<p>À noter que seul Windows 11 version 24H2 est concerné car sur Windows 10, le Notepad reste cette bonne vieille version offline qu'on connait sans Markdown ni IA... et du coup, pas de faille. Comme quoi, des fois être has been, ça a du bon ^^.</p>
<p>Rassurez-vous, ça n'empêchera pas Microsoft de continuer à injecter de l'IA dans TOUS ses outils Windows. Paint génère des images, Photos supprime les objets, l'Outil Capture retranscrit du texte... Bref, chaque app basique se transforme en usine à gaz connectée, avec la surface d'attaque qui va avec. (Je me demande quand la calculatrice aura besoin d'être connectée au net...)</p>
<p>Pour vous protéger, lancez donc Windows Update et installez le correctif de février. Si vous faites partie de ceux qui
<a href="https://korben.info/un-outil-pour-bloquer-les-mises-a-jour-forcees-de-windows-10.html">bloquent les mises à jour</a>
, c'est le moment de faire une exception et si vous êtes plutôt
<a href="https://korben.info/notepad-votre-editeur-de-texte-prefere-a-ete-pirate.html">team Notepad++</a>
... bah désolé pour vous aussi ^^.</p>
<p>
<a href="https://www.techspot.com/news/111287-unwanted-ai-upgrade-windows-notepad-created-serious-security.html">Source</a>
</p>