---
title: "DoomBuds - DOOM tourne maintenant sur des écouteurs (oui vraiment)"
author: "Korben"
date: 2026-01-27T13:20:03.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "hardware-diy"
  - "Doom"
  - "retrogaming"
rss_source: Blog
url: https://korben.info/doombuds-doom-ecouteurs.html
note: 0
seen: false
---

<p>&quot;<strong>Est ce que ce truc peut faire tourner Doom ???</strong>&quot;</p>
<p>C'est LA question qui hante les développeurs depuis 1993 et à chaque fois qu'on pense avoir atteint le fond, quelqu'un creuse encore un peu. Arin Sarkisian, un développeur australien vient en effet de porter le FPS culte d'id Software sur... <strong>des écouteurs</strong>. Oui, des écouteurs !</p>
<p>J'ai d'abord cru à une connerie quand j'ai vu passer le projet sur GitHub mais non. Le délire est bien réel et plutôt technique puisqu'il a flashé ses
<a href="https://www.notebookcheck.biz/PineBuds-Pro-PINE64-lance-des-oreillettes-TWS-avec-un-meilleur-ANC-que-les-AirPods-Pro-de-Apple.672888.0.html">PineBuds Pro</a>
, des écouteurs sans fil qui acceptent un firmware open source (y'en a pas des masses sur le marché). Le CPU a été overclocké à 300 MHz au lieu des 100 MHz d'origine, le mode basse consommation a été désactivé, et hop, il s'est arrangé pour y faire tourner un port du shooter. Tout ça sur un appareil qui a quand même moins d'1 Mo de RAM, c'est fort je trouve ! Si ça ne vous impressionne pas, je vous rappelle quand même que le jeu original demandait 4 Mo minimum en 1993.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/doombuds-doom-ecouteurs/doombuds-doom-ecouteurs-2.png" alt="" loading="lazy" decoding="async">
<p>Alors après ces écouteurs n'ont pas d'écran, vous vous en doutez. C'est pourquoi le rendu se fait via streaming JPEG à 18 images par seconde vers un smartphone connecté. C'est pas du 144 Hz, clairement, mais ça tourne ! D'ailleurs, si vous avez la flemme d'installer tout ce bazar, le dev a mis en ligne
<a href="https://doombuds.com/">une version jouable directement depuis votre navigateur</a>
, sur SES propres écouteurs. Vous pouvez donc littéralement jouer à distance sur les PineBuds d'un mec à l'autre bout du monde. C'est complètement dingue !!</p>
<p>Edit : Oups, c'est cassé.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/doombuds-doom-ecouteurs/doombuds-doom-ecouteurs-3.png" alt="" loading="lazy" decoding="async">
<p>Côté installation, attention quand même car faut se retrousser un peu les manches. Déjà c'est Docker obligatoire, et si vous êtes sous Windows, WSL2 aussi. Y'a un firmware modifié à flasher, puis un package JavaScript standalone pour le streaming. Le projet utilise doomgeneric, un port pensé pour être facilement adaptable. Par contre, si vous avez des PineBuds avec un firmware récent, y'a apparemment quelques galères de compatibilité à prévoir... j'ai pas testé perso parce que j'ai pas ce genre d'écouteur, mais les issues GitHub sont remplies de gens qui galères ^^.</p>
<p>Donc si vous pensiez que faire jouer
<a href="https://korben.info/ces-rats-jouent-doom-casque-vr.html">des rats à DOOM avec un casque VR</a>
était déjà barré, bah là on a encore passé un cap. Bref, le meme &quot;<strong>Can it run Doom ?</strong>&quot; a encore de beaux jours devant lui.</p>
<p>Si ça vous a fait marrer, n'hésitez pas à partager. Vous pouvez me retrouver sur
<a href="https://www.facebook.com/ManuelDorne/">Korben sur Facebook</a>
pour plus de news insolites comme ça.</p>
<p>
<a href="https://github.com/arin-s/DOOMBuds">Source</a>
</p>