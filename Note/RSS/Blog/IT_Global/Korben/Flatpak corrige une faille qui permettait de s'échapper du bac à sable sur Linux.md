---
title: "Flatpak corrige une faille qui permettait de s'échapper du bac à sable sur Linux"
author: "Korben"
date: 2026-04-08T07:43:48.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "linux-open-source"
  - "Flatpak"
  - "fuite"
  - "Linux"
rss_source: Blog
url: https://korben.info/flatpak-corrige-une-faille-qui-permettait-de-sechapper-du-bac-a-sable-sur-linux.html
note: 0
seen: false
---

<p>Le système de distribution d'applications Linux vient de publier la version 1.16.4, qui corrige quatre failles de sécurité découvertes dans son mécanisme de bac à sable.</p>
<p>La plus critique permettait à une app de sortir de son environnement isolé pour accéder à tous les fichiers de la machine et y exécuter du code. Le Steam Deck et la plupart des grandes distributions sont concernés.</p>
<h2 id="quatre-failles-dont-une-critique">Quatre failles, dont une critique</h2>
<p>Flatpak, c'est le format de distribution d'applications qui s'est imposé sur Linux ces dernières années. Son principe : chaque application tourne dans un bac à sable isolé du reste du système, un peu comme sur iOS. C'est aussi le format utilisé par le Steam Deck de Valve pour installer des applications en mode bureau.</p>
<p>La version 1.16.4, publiée le 7 avril, corrige quatre failles de sécurité. La plus grave, référencée CVE-2026-34078, est une vraie mauvaise surprise : une application pouvait exploiter des liens symboliques dans les options d'exposition du portail Flatpak pour accéder à l'intégralité des fichiers de la machine hôte, et même y exécuter du code.</p>
<h2 id="des-fichiers-supprimés-et-des-téléchargements-détournés">Des fichiers supprimés et des téléchargements détournés</h2>
<p>La deuxième faille (CVE-2026-34079) permettait de supprimer des fichiers sur la machine hôte en passant par un bug dans le cache du chargeur dynamique <a target="_blank" rel="noreferrer noopener" href="http://ld.so/">ld.so</a>. Flatpak supprimait les fichiers de cache obsolètes sans vérifier que le chemin fourni par l'application pointait bien vers le bon répertoire.</p>
<p>Deux autres problèmes ont aussi été corrigés : l'un permettait de lire des fichiers via le service système de Flatpak, l'autre de perturber le téléchargement d'une application lancé par un autre utilisateur, sans possibilité de l'arrêter proprement.</p>
<h2 id="qui-doit-mettre-à-jour">Qui doit mettre à jour</h2>
<p>Toutes les distributions Linux qui utilisent Flatpak sont concernées, et c'est un paquet de monde : Fedora, Ubuntu, Linux Mint, SteamOS sur le Steam Deck, et bien d'autres.</p>
<p>La mise à jour vers la version 1.16.4 est disponible, ou le sera très vite, via les canaux habituels de chaque distribution. Si vous utilisez un Steam Deck en mode bureau avec des apps Flatpak installées via Discover, la mise à jour devrait arriver automatiquement.</p>
<p>C'est quand même un comble : un système conçu pour isoler les applications qui laisse une porte grande ouverte vers tout le système. Que Flatpak se fasse prendre en défaut sur son coeur de métier, ça fait un peu désordre.</p>
<p>Bon par contre, la réactivité a été bonne : la faille a été identifiée et corrigée, et les détails n'ont été publiés qu'avec le correctif disponible. C'est la base, mais au moins c'est fait.</p>
<p>Source :
<a href="https://www.phoronix.com/news/Flatpak-1.16.4-Released">Phoronix</a>
</p>