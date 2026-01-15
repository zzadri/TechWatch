---
title: "Glide - Le fork Firefox entièrement hackable pour les fans de Vim"
author: "Korben"
date: 2026-01-15T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "Firefox"
  - "Linux"
  - "macOS"
  - "navigateur"
  - "open source"
  - "TypeScript"
  - "Vim"
rss_source: Blog
url: https://korben.info/glide-browser-firefox-fork-typescript-vim.html
note: 0
seen: false
---

<p>Coucou les petits amis, ça roule ? Aujourd'hui on va parler d'un truc qui va plaire aux barbus, aux fans de raccourcis qui font mal aux doigts et à tous ceux qui considèrent que la souris est une invention du démon.</p>
<p>Ça s'appelle <strong>
<a href="https://glide-browser.app/">Glide</a>
</strong> et l'idée c'est de proposer un fork de Firefox entièrement hackable via du TypeScript et pas juste une extension qui se fait brider par le modèle de sécurité de Mozilla. C'est donc un vrai navigateur où vous avez la main sur tout ce qui touche au logiciel.</p>
<div class="video-container" id="video-container-glide-browser-firefox-fork-typescript-vim-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/glide-browser-firefox-fork-typescript-vim/glide-browser-firefox-fork-typescript-vim-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/glide-browser-firefox-fork-typescript-vim/glide-browser-firefox-fork-typescript-vim-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Le développeur, Robert Craigie, en avait marre de voir ses raccourcis Vim sauter sur certains domaines protégés. Du coup, il a pris les sources de Firefox et il a injecté une couche de personnalisation totale. On peut définir ses propres modes (Normal, Insert, Hint, Ignore), créer des macros qui exécutent des processus externes, ou même configurer un raccourci pour cloner un dépôt GitHub et l'ouvrir direct dans Neovim.</p>
<p>Franchement, le truc est hyper fluide. Le mode &quot;Hint&quot; (touche f) permet de cliquer sur la plupart des liens sans jamais lâcher le clavier, et le raccourci <code>gI</code> cible automatiquement le plus gros champ de texte de la page. C'est magique, on gagne un temps de dingue.</p>
<p>Pour ceux qui se demandent la différence avec
<a href="https://korben.info/tridactyl-firefox-raccourcis-vim.html">Tridactyl</a>
, c'est simple : ici, il n'y a plus de bac à sable pour la configuration. On est chez soi, avec un accès direct aux APIs du navigateur et la possibilité de piloter des scripts système sans se prendre la tête. Attention toutefois, Glide est encore en version alpha (basé sur Firefox 144.0b8), ce qui signifie que le fork a un peu de retard sur les derniers patchs de sécurité de Mozilla. À utiliser en connaissance de cause, donc.</p>
<p>Pour l'instant, c'est dispo uniquement pour macOS et Linux. Mais si vous kiffez le minimalisme et que vous voulez un navigateur qui ne vous traite pas comme un simple utilisateur à qui on cache les réglages, Glide mérite clairement le coup d'œil.</p>
<p>Ça redonne un peu de fun à la navigation web, loin des usines à gaz bourrées d'IA qui essaient de deviner ce que vous voulez faire !</p>
<p>Merci à Lorenper !</p>
<p>
<a href="https://blog.craigie.dev/introducing-glide/">Source</a>
</p>