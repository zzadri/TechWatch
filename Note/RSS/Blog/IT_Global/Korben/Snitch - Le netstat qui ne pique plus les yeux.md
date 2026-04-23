---
title: "Snitch - Le netstat qui ne pique plus les yeux"
author: "Korben"
date: 2026-02-27T07:56:14.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "administration réseau"
  - "alternative open source"
  - "monitoring"
rss_source: Blog
url: https://korben.info/snitch-netstat-ss-alternative-tui.html
note: 0
seen: false
---

<p>Si vous avez déjà tapé <code>[ss -tulnp](https://www.it-connect.fr/lister-les-ports-en-ecoute-sous-linux-avec-lsof-netstat-et-ss/)</code> dans un terminal, vous savez que c'est moche. Genre, VRAIMENT moche. Les colonnes qui se chevauchent, les adresses tronquées, bref c'est un festival du bordel. Mais c'était sans compter sur ce dev qui a pondu
<a href="https://github.com/karol-broda/snitch">Snitch</a>
, un outil en Go sous licence MIT qui vient concurrencer ss et netstat... sauf que pour une fois, c'est lisible, regardez :</p>
<img src="https://korben.info/snitch-netstat-ss-alternative-tui/snitch-netstat-ss-alternative-tui-1.gif" alt="" loading="lazy" decoding="async">
<p><em>L'interface de Snitch en action, sobre et lisible</em></p>
<p>En gros, c'est un ss moderne avec une interface TUI interactive. Vous lancez la commande dans votre terminal et tadaaa, vous avez un tableau propre avec toutes vos connexions réseau, les processus associés, les ports, les protocoles... le tout avec des couleurs et une navigation au clavier. Rien à voir donc avec le pavé monochrome habituel !</p>
<p>Le truc cool aussi ce sont les filtres. Vous pouvez taper <code>snitch ls proto=tcp state=listen</code> pour ne voir que les sockets TCP en écoute, ou <code>snitch ls proc=nginx</code> pour traquer votre serveur web. Y'a même un filtre <code>contains=</code> pour chercher dans les adresses... genre <code>contains=google</code> pour voir tout ce qui cause avec Mountain View.</p>
<p>D'ailleurs, côté commandes c'est en fait bien fichu. <code>snitch ls</code> pour un tableau statique, <code>snitch json</code> pour du JSON brut si vous voulez scripter, et <code>snitch watch -i 1s</code> pour streamer les connexions en temps réel. Du coup ça s'intègre nickel dans vos pipelines.</p>
<p>La TUI elle-même vaut le détour. Vous naviguez avec j/k (comme dans Vim, forcément), vous basculez TCP/UDP avec t/u, et le plus jouissif... vous pouvez killer un processus directement avec la touche K. Plus besoin de noter le PID et d'ouvrir un autre terminal ! Sauf que attention, sur Linux faut quand même lancer en root pour avoir les infos complètes sur les processus, parce que l'outil va lire dans <code>/proc/net/*</code>. Ça ne marche pas non plus sur Windows, c'est Linux et macOS uniquement.</p>
<p>Pour ceux qui aiment personnaliser leur terminal (oui, je vous connaîs...), y'a une quinzaine de thèmes, Catppuccin, Dracula, Nord, Tokyo Night, Gruvbox... la config se fait dans <code>~/.config/snitch/snitch.toml</code> et l'outil peut aussi conserver vos préférences de filtres entre les sessions (faut activer <code>remember_state</code> dans la config).</p>
<p>Côté installation, c'est pas la mer à boire. <code>brew install snitch</code> sur macOS, <code>go install github.com/karol-broda/snitch@latest</code> si vous avez Go, <code>yay -S snitch-bin</code> sur Arch, et y'a même des images Docker pour les plus prudents !</p>
<p>Donc si vous êtes du genre à
<a href="https://korben.info/sniffnet-surveiller-trafic-reseau.html">surveiller votre trafic réseau</a>
ou à garder un oeil sur vos
<a href="https://korben.info/outils-crise-linux-indispensables-pros-it.html">outils de diagnostic Linux</a>
, c'est clairement à tester.</p>
<p>Perso, pour du debug réseau rapide, je trouve que c'est carrément plus agréable que de se taper un <code>ss -tulnp</code>.</p>