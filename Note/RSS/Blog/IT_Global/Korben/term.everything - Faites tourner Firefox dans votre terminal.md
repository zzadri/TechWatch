---
title: "term.everything - Faites tourner Firefox dans votre terminal"
author: "Korben"
date: 2026-04-01T08:14:20.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "Linux"
  - "open source"
  - "SSH"
  - "wayland"
rss_source: Blog
url: https://korben.info/term-everything-gui-terminal-linux.html
note: 0
seen: false
---

<p>Et si je vous disais qu'on pouvait faire tourner Firefox dans un terminal ? Et pas un navigateur en mode texte, hein. Non, le véritable Firefox, avec ses onglets, les images, la totale... Hé oui c'est possible et que ça fonctionne via SSH, donc depuis un serveur distant. Bienvenue dans le futur (ou le passé, j'sais plus trop) !</p>
<p>
<a href="https://github.com/mmulet/term.everything">Term.everything</a>
c'est un compositeur Wayland construit from scratch en Go qui, au lieu de balancer l'image sur votre écran, la convertit en caractères ANSI et l'affiche dans le terminal. Du coup, n'importe quelle app GUI Linux peut tourner là-dedans. Firefox, un gestionnaire de fichiers, un lecteur vidéo... et même Doom (parce que si ça peut pas faire tourner Doom, ça compte pas). Le binaire fait une poignée de Mo, c'est sous licence AGPL-3.0, et y'a zéro dépendance externe.</p>
<p>
<img src="https://korben.info/term-everything-gui-terminal-linux/term-everything-gui-terminal-linux-1.gif" alt="" loading="lazy" decoding="async">
</p>
<p>L'outil propose 2 modes d'affichage. Le mode basique qui convertit les pixels en blocs Unicode, et dont la qualité dépend du nombre de lignes et colonnes de votre terminal. Plus vous zoomez out (Ctrl+- sur Alacritty), plus c'est net... mais plus ça rame. Donc si votre terminal supporte le protocole image, genre Kitty ou iTerm2, l'autre mode, c'est du rendu pleine résolution et là non seulement c'est pas dégeu mais en plus ça marche bien !</p>
<p>Le truc vraiment dingue, c'est surtout le SSH parce que si vous avez un serveur Linux distant, vous vous connectez dessus en SSH, vous lancez <code>term-everything firefox</code> et hop, Firefox s'affiche dans votre terminal local. Pas de X11 forwarding relou à mettre en place ni de VNC / RDP zarbi.</p>
<p>
<img src="https://korben.info/term-everything-gui-terminal-linux/term-everything-gui-terminal-linux-2.gif" alt="" loading="lazy" decoding="async">
</p>
<p>Pour les admins sys qui gèrent des serveurs headless, c'est quand même sympa ! D'ailleurs si vous aimez
<a href="https://korben.info/sshx-terminal-collaboratif-securise-web.html">les outils SSH bien pensés</a>
, celui-ci aussi va vous plaire.</p>
<p>Par contre, on est encore en bêta et certaines apps vont planter ou refuser de se lancer. C'est normal, c'est un compositeur Wayland complet écrit par un seul gars (chapeau l'artiste !). Ce n'est donc pas le genre de truc qu'on met en prod, mais pour du dépannage sur un serveur Debian distant ou juste pour la beauté du geste, ça envoie du pâté.</p>
<p>Le créateur de term.everything est d'ailleurs le même qui avait codé
<a href="https://github.com/mmulet/font-game-engine">Fontemon</a>
, un jeu vidéo caché dans une police de caractères. On est donc clairement dans la catégorie &quot;parce qu'on peut le faire et que c'est marrant&quot;.</p>
<p>
<img src="https://korben.info/term-everything-gui-terminal-linux/term-everything-gui-terminal-linux-3.gif" alt="" loading="lazy" decoding="async">
</p>
<p>Bref, si vous voulez épater vos collègues en lançant KDE dans un terminal par-dessus SSH, ou juste jouer à Doom dans tmux,
<a href="https://github.com/mmulet/term.everything">c'est par là que ça se passe.</a>
</p>
<p>Amusez-vous bien et merci à Lorenper pour l'info !</p>