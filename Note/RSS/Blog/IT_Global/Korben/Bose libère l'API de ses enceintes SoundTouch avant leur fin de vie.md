---
title: "Bose libère l'API de ses enceintes SoundTouch avant leur fin de vie"
author: "Korben"
date: 2026-01-08T12:58:41.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "hardware-diy/peripheriques"
  - "linux-open-source/self-hosting"
  - "API"
  - "bose"
  - "domotique"
  - "Home Assistant"
  - "open source"
rss_source: Blog
url: https://korben.info/bose-soundtouch-api-open-source-eol.html
note: 0
seen: false
---

<p>Si comme moi vous avez une enceinte <strong>Bose SoundTouch</strong> qui traîne chez vous, vous avez peut-être appris que la bestiole allait bientôt perdre son cerveau &quot;cloud&quot;. Bose a en effet annoncé la fin du support pour le 6 mai 2026, et de ce que j'ai compris, ça veut dire que votre enceinte va se transformer en brique connectée qui ne se connecte plus à grand chose.</p>
<p>Sauf que non !</p>
<p>Bose a fait un truc plutôt cool puisqu'ils ont publié
<a href="https://assets.bosecreative.com/m/496577402d128874/original/SoundTouch-Web-API.pdf">la documentation complète de l'API locale de leurs enceintes</a>
. Du coup, même quand les serveurs Bose fermeront boutique, vous pourrez continuer à bidouiller votre enceinte en local.</p>
<p>Perso, j'ai une petite SoundTouch 10 qui fait bien le boulot depuis des années, donc cette nouvelle me fait plutôt plaisir ! L'API tourne sur deux ports : le 8090 pour les commandes REST classiques (volume, presets, now_playing...) et le 8080 en WebSocket pour les notifications en temps réel. Le protocole s'appelle &quot;gabbo&quot;, et avec ça, y'a de quoi faire le ménage dans vos automatisations.</p>
<p>Un petit <code>curl http://votre-enceinte:8090/volume</code> et vous récupérez le niveau sonore. Un autre sur <code>/presets</code> et vous avez vos stations favorites. Et comme la découverte se fait en SSDP ou MDNS, ça s'intègrera nickel avec n'importe quel système domotique.</p>
<p>Et visiblement la communauté n'a pas attendu pour s'y mettre puisqu'il y a déjà
<a href="https://github.com/search?q=soundtouch&#43;bose&amp;type=repositories">plus d'une centaine de projets sur GitHub</a>
qui exploitent cette API. Le plus abouti c'est probablement <strong>
<a href="https://community.home-assistant.io/t/soundtouchplus-integration/633638">SoundTouchPlus</a>
</strong> pour Home Assistant, qui permet de contrôler toute la famille d'enceintes depuis votre dashboard.</p>
<p>Après ce qui va disparaître avec le cloud, c'est surtout les presets synchronisés et le streaming direct depuis l'app Bose. Mais le Bluetooth, l'AirPlay, Spotify Connect et le multiroom resteront fonctionnels et avec l'API locale, vous pouvez recréer vos presets en dur. Ouf !</p>
<p>C'est un peu le même délire que
<a href="https://korben.info/nolongerevil-thermostat-google-nest-bounty.html">ce qui s'est passé avec les thermostats Nest</a>
... quand le fabricant lâche l'affaire, c'est la communauté qui prend le relais sauf qu'ici, Bose joue le jeu en documentant proprement leur API avant de couper les serveurs. Et ça, c'est suffisamment rare pour être souligné !</p>
<p>Voilà... Si vous avez des SoundTouch, allez jeter un œil à l'API avant mai, histoire de préparer votre migration vers du 100% local.</p>
<p>
<a href="https://arstechnica.com/gadgets/2026/01/bose-open-sources-its-soundtouch-home-theater-smart-speakers-ahead-of-eol/">Source</a>
</p>