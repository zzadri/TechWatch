---
title: "WinBoat - Une faille critique découverte dans l'outil de virtualisation"
author: "Korben"
date: 2026-01-16T05:38:55.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "linux-open-source"
  - "faille"
  - "faille critique"
rss_source: Blog
url: https://korben.info/winboat-guest-service-host-rce.html
note: 0
seen: false
---

<p>Si vous faites partie des curieux qui testent <strong>
<a href="https://korben.info/winboat-windows-apps-linux-docker.html">WinBoat</a>
</strong> (le projet open source de TibixDev pour lancer des applis Windows sous Linux via Docker), sachez qu'une vulnérabilité critique a été identifiée dans l'outil, et le scénario d'attaque est plutôt créatif.</p>
<p>Pour ceux qui ne connaissent pas, WinBoat est une appli Electron qui orchestre tout un petit monde (Docker / Podman, FreeRDP) pour rendre l'expérience Windows &quot;seamless&quot; sur votre bureau Linux. C'est ambitieux, c'est en beta, et forcément, il y a parfois des trous dans la raquette.</p>
<p>D'après le
<a href="https://hack.do/posts/winboat-guest-service-host-rce/">write-up technique publié sur hack.do</a>
, le problème venait de l'API locale exposée par WinBoat sur le port <code>7148</code>. Cette API HTTP n'était pas authentifiée, ce qui est souvent le début des ennuis.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/jwT2pQNbDpE?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le scénario décrit par le chercheur est le suivant : un attaquant héberge une page web malveillante et si vous visitez cette page avec votre navigateur (et sous réserve que les sécurités CORS/PNA ne bloquent pas la requête, ce qui dépend de votre config et du navigateur), elle peut envoyer des ordres à cette API locale <code>localhost:7148</code>.</p>
<p>L'API vulnérable (notamment le endpoint <code>/update</code>) permettrait alors de remplacer des composants internes du système invité. En gros, l'attaquant pourrait substituer le binaire <code>guest_server</code> légitime par une version malveillante.</p>
<p>Une fois que l'attaquant a compromis le conteneur Windows, il ne s'arrête pas là. Le chercheur explique que WinBoat permet au conteneur de communiquer des &quot;entrées d'application&quot; à l'hôte Linux. Si le conteneur compromis envoie un chemin forgé spécifiquement et que l'hôte tente de le lancer... c'est l'exécution de code arbitraire (RCE) sur votre machine Linux.</p>
<p>C'est un rappel assez violent que l'isolation, c'est compliqué à faire correctement, surtout quand on veut une intégration transparente entre deux systèmes.</p>
<p>La bonne nouvelle, c'est que le problème a été traité. La faille concernait les versions jusqu'à la <strong>v0.8.7</strong>. La version <strong>v0.9.0</strong> introduit une authentification obligatoire pour cette API locale, avec un mot de passe aléatoire généré au lancement, ce qui coupe l'herbe sous le pied de ce type d'attaque web.</p>
<p>Si vous utilisez WinBoat, la mise à jour est donc plus que recommandée et si le sujet de l'isolation vous intéresse, jetez un œil à mon tuto sur
<a href="https://korben.info/installer-wsl2-windows-linux.html">l'installation de WSL 2</a>
ou encore à cette
<a href="https://korben.info/faille-rce-critique-linux-cauchemar-admins.html">autre faille RCE critique</a>
qui a secoué le monde Linux récemment.</p>
<p>Bref, prudence avec les outils en beta qui exposent des ports locaux !</p>
<p>
<a href="https://hack.do/posts/winboat-guest-service-host-rce/">Source</a>
</p>