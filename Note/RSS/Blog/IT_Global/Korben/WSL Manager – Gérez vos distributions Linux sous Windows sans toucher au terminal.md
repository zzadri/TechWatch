---
title: "WSL Manager – Gérez vos distributions Linux sous Windows sans toucher au terminal"
author: "Korben"
date: 2026-02-02T09:14:00.000Z
type: site
subject:
category: IT Global
tags:
  - "tutoriels-guides/astuces-productivite"
  - "windows/logiciels-windows"
  - "Docker"
  - "Flutter"
  - "gestionnaire"
  - "GUI"
  - "Linux"
  - "Windows"
  - "WSL"
  - "WSL2"
rss_source: Blog
url: https://korben.info/wsl2-distro-manager-gui-windows-linux.html
note: 0
seen: false
---

<p>Vous utilisez WSL sous Windows mais vous en avez marre de devoir jongler avec les commandes PowerShell dès qu'il s'agit de gérer vos distributions ?</p>
<p>C'est vrai que taper du <code>wsl --import</code> ou du <code>wsl --unregister</code> à chaque fois qu'on veut tester une nouvelle instance, ça finit par être un peu lourd.</p>
<p>Heureusement, y’a un dev, Eric Trenkel (alias bostrot), qui a eu la bonne idée de sortir <strong>
<a href="https://github.com/bostrot/wsl2-distro-manager">WSL Manager</a>
</strong> (qu'on connaissait aussi sous le nom de WSL2 Distro Manager), une interface graphique complète pour piloter tout ça sans se faire mal au terminal.</p>
<p>Cette application, développée avec Flutter offre une vue d'ensemble sur toutes vos instances WSL installées. Ainsi, en un clic, vous pouvez les démarrer, les arrêter, les renommer ou même changer leur version.</p>
<p>Mais là où l'outil excelle, c'est dans sa capacité à importer de nouveaux environnements. Pour ceux qui se demandent comment ça se passe pour récupérer des distributions exotiques, sachez que WSL Manager permet de télécharger et d'utiliser n'importe quelle image <strong>Docker</strong> comme base pour une instance WSL, et ce, sans même avoir besoin d'installer Docker Desktop sur votre machine.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wsl2-distro-manager-gui-windows-linux/wsl2-distro-manager-gui-windows-linux-2.png" alt="" loading="lazy" decoding="async">
<p>Par exemple si vous voulez un Alpine minimaliste pour du test ou un Kali pour du pentest, vous l'importez direct depuis les registres Docker et hop, vous avez un nouveau système prêt à l'emploi.</p>
<p>C'est d'ailleurs un excellent complément à des outils comme
<a href="https://korben.info/dockstation-docker-developpeur.html">DockStation</a>
si vous voulez garder une approche visuelle de vos conteneurs, ou même
<a href="https://korben.info/winboat-windows-docker-linux.html">WinBoat</a>
pour faire tourner du Windows dans Docker. L'application propose aussi des &quot;Quick Actions&quot;, qui sont en gros des petits scripts prédéfinis que vous pouvez exécuter directement sur vos instances pour automatiser les tâches répétitives. Vous pouvez également lancer directement
<a href="https://korben.info/nouveau-terminal-windows-10.html">Windows Terminal</a>
ou VS Code dans la distribution de votre choix en un seul clic.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wsl2-distro-manager-gui-windows-linux/wsl2-distro-manager-gui-windows-linux-1.jpg" alt="" loading="lazy" decoding="async">
</p>
<p>Si ça vous branche, plusieurs options s'offrent à vous pour l'installer. Comme le projet est open source sous licence GPL-3.0, vous pouvez récupérer les exécutables gratuitement sur la page GitHub du projet.</p>
<p>
<a href="https://apps.microsoft.com/detail/9nws9k95nmjb?hl=en-gb&amp;gl=FR">Il existe aussi une version sur le Microsoft Store</a>
et notez aussi que bien que des paquets winget ou Chocolatey existent, ils sont souvent maintenus par la communauté et pas forcément à jour, donc privilégiez le téléchargement direct ou le Store pour être tranquille.</p>
<p>Voilà, si vous passez vos journées sous Linux tout en restant dans l'écosystème Microsoft, WSL Manager c'est le feu et ça permet de se concentrer sur son boulot plutôt que sur la syntaxe des commandes de gestion système.</p>
<p>Merci à Lorenper pour la découverte !</p>