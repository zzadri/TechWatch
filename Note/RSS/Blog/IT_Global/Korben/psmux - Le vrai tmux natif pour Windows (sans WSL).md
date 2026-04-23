---
title: "psmux - Le vrai tmux natif pour Windows (sans WSL)"
author: "Korben"
date: 2026-03-16T08:08:03.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "windows/powershell-scripting"
  - "CLI"
  - "open source"
  - "PowerShell"
  - "Rust"
  - "terminal"
  - "tmux"
  - "Windows"
rss_source: Blog
url: https://korben.info/psmux-multiplexeur-terminal-windows-tmux-natif.html
note: 0
seen: false
---

<p>Splitter son terminal en plusieurs panneaux, gérer des sessions persistantes, le tout avec les mêmes raccourcis que tmux... mais sous un bon gros Windows des famille, nativement, en Rust et sans avoir besoin de se galérer avec WSL !</p>
<p>C'est exactement ce que fait
<a href="https://github.com/marlocarlo/psmux">psmux</a>
, un multiplexeur de terminal conçu pour PowerShell et cmd.exe qui utilise directement l'API ConPTY de Windows 10/11. Du coup, pas de couche d'émulation Unix, pas de Cygwin, pas de MSYS2... ça tourne direct sur votre bécane.</p>
<p>Pour ceux qui débarquent, un multiplexeur de terminal ça permet de découper votre console en plusieurs zones (des &quot;panes&quot; que j’appellerai &quot;panneau&quot; parce que merde c'est + français), de jongler entre plusieurs sessions, et surtout de retrouver votre boulot exactement là où vous l'avez laissé même après une déconnexion. Sous Linux, tout le monde utilise tmux pour ça mais sous Windows, jusqu'ici c'était soit WSL (installer tout un sous-système Linux juste pour splitter un terminal, c'est un peu overkill quand même !), soit des splits basiques via Windows Terminal qui ne gèraient ni les sessions persistantes ni le détachement. Snif...</p>
<img src="https://korben.info/psmux-multiplexeur-terminal-windows-tmux-natif/psmux-multiplexeur-terminal-windows-tmux-natif-1.gif" alt="" loading="lazy" decoding="async">
<p><em>psmux en action sous PowerShell</em></p>
<p>L'installation est rapide. Un petit <code>winget install psmux</code> et hop, c'est réglé. Ça passe aussi par Cargo, Scoop ou Chocolatey pour les puristes. Ensuite, vous tapez <code>psmux</code> dans PowerShell 7 et vous retrouvez vos marques : Ctrl+B pour le prefix, les mêmes commandes <code>split-window</code>, <code>new-session</code>, <code>attach</code>... L'outil implémente 76 commandes tmux avec plus de 126 variables de formatage. Et y'a même un mode copie Vim avec 53 raccourcis clavier.</p>
<p>Bref, si vous avez une mémoire musculaire ultra développée pour tmux, vous êtes chez vous !</p>
<p>Et le truc cool, c'est que psmux lit directement vos fichiers <code>.tmux.conf</code> existants. Du coup, vos raccourcis custom et pas mal de thèmes (Catppuccin, Dracula, Nord...) fonctionneront directement, même si les configs tmux les plus complexes avec des scripts bash ou TPM peuvent nécessiter des ajustements. Et y'a aussi
<a href="https://github.com/marlocarlo/Tmux-Plugin-Panel">Tmux Plugin Panel</a>
pour vous accompagner dans l'ajout de plugins et de thèmes.</p>
<p>Alors je vous connais les raloux sous OuinOuin, vous allez me dire &quot;<em>Windows Terminal fait déjà des splits avec Alt+Shift+D</em>&quot;... sauf que non, c'est pas pareil. Windows Terminal découpe votre fenêtre visuellement mais ne gère ni les sessions persistantes, ni le scripting, ni le détachement. Avec psmux, vous lancez une session le lundi, vous fermez votre terminal, vous revenez le mardi et tout est encore là : vos panneaux, vos processus, votre historique. C'est ça la vraie différence avec un simple split visuel.</p>
<p>D'ailleurs, si vous utilisez
<a href="https://korben.info/quand-claude-code-pilote-votre-terminal.html">Claude Code ou d'autres agents IA en ligne de commande</a>
, psmux intègre un support pour les agent teams qui permet à chaque agent de spawner dans son propre panneau automatiquement.</p>
<p>Côté support souris, c'est complet : clic pour sélectionner un panneau, drag pour redimensionner les bordures, molette pour remonter dans l'historique du buffer. Tout est activé par défaut, pas besoin de rajouter <code>set -g mouse on</code> comme sous tmux. L'outil tourne sous Windows 10 et 11, et le projet est sous licence MIT.</p>
<p>Après c'est encore jeune et y'a quelques galères connues notamment le support des caractères CJK et UTF-8 multi-octets qui peut se planter comme une merde sur des textes longs. Et <code>split-window -c</code> ne préserve pas toujours le répertoire courant (oubliez pas de vérifier votre <code>pwd</code> après un split). Par contre, le dev répond en quelques heures, et des PR externes sont mergées régulièrement... donc c'est bon signe !</p>
<p>Bref, c'est propre, c'est natif, et ça lit vos .tmux.conf ! Que demande le peuple barbus emprisonné sous Windows, finalement ? Hé bien pas grand chose de plus pour être heureux.</p>