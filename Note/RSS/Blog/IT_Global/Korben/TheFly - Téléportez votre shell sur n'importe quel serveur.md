---
title: "TheFly - Téléportez votre shell sur n'importe quel serveur"
author: "Korben"
date: 2026-02-25T08:59:14.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "linux-open-source/terminal-shell"
  - "dotfiles"
  - "open source"
  - "SSH"
  - "terminal"
rss_source: Blog
url: https://korben.info/thefly-shell-teleportation.html
note: 0
seen: false
---

<p>Si vous bossez sur des serveurs distants, vous connaissez cette douleur... D'un côté, vous avez votre terminal local aux petits oignons, vos alias, vos plugins... et hop, un petit <code>ssh root@serveur</code> et vous vous retrouvez avec un shell tout pourri, tout basique. Mais c'était sans compter sur Joknarf qui a pondu
<a href="https://github.com/joknarf/thefly">TheFly</a>
, un gestionnaire de plugins shell qui téléporte votre environnement via SSH ou sudo en un instant.</p>
<p>Le principe est pas bête du tout vous allez voir. En fait, vous installez vos plugins et dotfiles dans <code>~/.fly.d/</code> sur votre machine, et quand vous lancez <code>flyto user@serveur</code>, tout est empaqueté et envoyé dans <code>/tmp/.fly.$USER/</code> distant. Prompt perso, alias, fonctions... tout débarque avec vous, un peu comme un sac à dos pour votre shell.</p>
<img src="https://korben.info/thefly-shell-teleportation/thefly-shell-teleportation-1.gif" alt="" loading="lazy" decoding="async">
<p>Et le truc bien, c'est que ça ne modifie RIEN sur le serveur distant car tout vit dans <code>/tmp</code>, donc quand vous vous déconnectez... pouf, tout a disparu. Pas de fichier qui traîne, pas de <code>.bashrc</code> modifié donc c'est plutôt safe pour les environnements de prod où vous ne voulez pas laisser de traces.</p>
<p>Ça marche avec bash, zsh et même ksh (pour les nostalgiques). L'installation, c'est un curl en une ligne (à relire comme d'hab), ou alors brew, dnf, paquets .deb... y'a le choix. C'est du pur shell POSIX, donc y'a ZÉRO dépendance externe. Attention par contre, si votre <code>~/.fly.d/</code> dépasse 128 Ko, ça risque de ramer sur des connexions un peu lentes.</p>
<p>Ah et y'a aussi <code>flyas</code> pour faire pareil en sudo (attention, ça téléporte aussi vos plugins, donc vérifiez que ça colle avec votre politique de sécu), et <code>flysh</code> pour switcher de shell sans perdre vos réglages. Et puis <code>flypack</code> génère une archive auto-extractible pour avoir un script shell qui s'installe tout seul. Pas mal donc aussi pour partager votre config.</p>
<p>Côté plugins, c'est pas
<a href="https://korben.info/oh-my-zsh-framework-booster-shell-zsh.html">Oh My Zsh</a>
avec ses 350+ plugins, mais y'a l'essentiel. Un prompt custom (nerdp), un historique amélioré (redo), de la navigation de répertoires (seedee)... et shell-ng qui regroupe le tout d'un coup. Perso, c'est bien suffisant je trouve.</p>
<p>D'ailleurs si vous êtes du genre à
<a href="https://korben.info/decouvrez-gum-outil-ecrire-scripts-dotfiles.html">customiser votre shell</a>
au millimètre, TheFly s'intègrera bien dans votre workflow. En plus c'est sous licence, open source, et ça tourne sur Linux, macOS et même SunOS (bon ok, je sais, quasi personne utilise SunOS en 2026 mais bon...).</p>
<p>Voilà, comme ça si vous gérez une dizaine de serveurs au quotidien, ça vous fera gagner un paquet de temps !</p>
<p>Amusez-vous bien !</p>