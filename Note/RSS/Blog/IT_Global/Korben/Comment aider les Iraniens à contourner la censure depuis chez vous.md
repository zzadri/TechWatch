---
title: "Comment aider les Iraniens à contourner la censure depuis chez vous"
author: "Korben"
date: 2026-01-24T23:32:40.000Z
type: site
subject:
category: IT Global
tags:
  - "tutoriels-guides/tutoriels-avances"
  - "vie-privee-anonymat/censure-liberte"
  - "anti-censure"
  - "censure"
  - "Iran"
  - "Psiphon"
rss_source: Blog
url: https://korben.info/psiphon-conduit-aider-iraniens-censure.html
note: 0
seen: false
---

<p>Si vous suivez un peu l'actu, vous savez que
<a href="https://korben.info/iran-la-chasse-aux-sorcieres-version-starlink-sintensifie.html">la censure en Iran</a>
, c'est pas une blague... Quand le gouvernement décide de couper internet durant les manifs, y'a des millions de personnes qui se retrouvent dans le noir.</p>
<p>Et là, y'a un truc que vous pouvez faire depuis chez vous pour aider.</p>
<p>
<a href="https://conduit.psiphon.ca/">Psiphon Conduit</a>
, c'est un outil qui permet de partager un bout de votre bande passante avec des gens qui en ont vraiment besoin. En gros, votre PC devient un nœud du réseau Psiphon, et des Iraniens (ou d'autres personnes censurées) peuvent passer par votre connexion pour accéder à internet librement.</p>
<p>Et voilà comment vous venez de devenir un petit maillon de la résistance numérique !</p>
<p>Le truc cool, c'est que Conduit tourne en arrière-plan sans rien vous demander, chiffre toutes les connexions, et ne collecte aucune donnée perso. Ça bouffe pas de ressources, et vous pouvez configurer la quantité de bande passante que vous voulez partager.</p>
<h2 id="ce-quil-vous-faut">Ce qu'il vous faut</h2>
<ul>
<li>Windows 10 ou 11 (il existe aussi une version Mac)</li>
<li>Python 3.6 ou plus (pour le firewall Iran-only)</li>
<li>Temps estimé : 5 minutes</li>
</ul>
<h2 id="installer-psiphon-conduit">Installer Psiphon Conduit</h2>
<p>Rendez-vous sur
<a href="https://conduit.psiphon.ca/en/download_conduit">la page de téléchargement officielle</a>
et récupérez la version Windows. C'est un exe classique, vous double-cliquez et c'est parti. L'application se loge dans la barre système et commence à partager automatiquement.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/psiphon-conduit-aider-iraniens-censure/psiphon-conduit-aider-iraniens-censure-2.png" alt="" loading="lazy" decoding="async">
<h2 id="réserver-votre-bande-passante-aux-iraniens">Réserver votre bande passante aux Iraniens</h2>
<p>Par défaut, quand vous faites tourner Conduit, des gens de n'importe quel pays peuvent utiliser votre connexion. Si vous voulez maximiser l'impact pour l'Iran spécifiquement, y'a un script Python qui fait exactement ça.</p>
<p>Téléchargez le projet
<a href="https://github.com/SamNet-dev/iran-conduit-firewall">iran-conduit-firewall</a>
sur GitHub. Extrayez le ZIP, puis lancez <code>RUN_AS_ADMIN.bat</code> en mode administrateur. Le script va alors créer des règles de firewall Windows qui bloquent toutes les connexions... sauf celles venant d'Iran. Plus de 2000 plages d'IP iraniennes sont whitelistées. Si vous êtes sous mac ou Linux, faudra lancer directement <em>iran_firewall.py</em> avec python.</p>
<p>L'interface vous propose 4 options :</p>
<ol>
<li>Activer le mode Iran-only (bloquer les autres pays)</li>
<li>Désactiver le mode Iran-only (tout le monde peut se connecter)</li>
<li>Vérifier le statut actuel</li>
<li>Utilitaires de gestion Conduit</li>
</ol>
<p>Et là, c'est tout ! Vos règles firewall restent actives même après fermeture du script, jusqu'à ce que vous les désactiviez explicitement.</p>
<h2 id="dépannage">Dépannage</h2>
<p>Si le script ne détecte pas Conduit, vérifiez qu'il est bien installé via le Microsoft Store ou en version standalone. Si vous avez des soucis avec les règles firewall, relancez le script en administrateur et choisissez l'option 2 pour tout réinitialiser.</p>
<p>Si vous avez une connexion correcte et envie de faire un geste concret pour la liberté d'accéder à internet, c'est le moment les copains !! Comme je vous avais déjà parlé de
<a href="https://korben.info/psiphon-un-outil-pour-contourner-la-censure.html">Psiphon</a>
ou
<a href="https://korben.info/lantern-un-clone-de-tor-sans-anonymat.html">Lantern</a>
, je pense que vous connaissiez déjà ces outils de contournement de la censure. Mais là, ils ont besoin de relais, et ce relais, ça peut être vous !</p>
<p>Merci pour eux !</p>