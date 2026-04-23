---
title: "GeForce Now Linux - NVIDIA lâche enfin son client natif pour les gamers manchots"
author: "Korben"
date: 2026-02-01T07:36:00.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/pc-gaming"
  - "linux-open-source"
  - "tutoriels-guides"
  - "Nvidia"
rss_source: Blog
url: https://korben.info/geforce-now-linux-nvidia-cloud-gaming.html
note: 0
seen: false
---

<p>Ça y est les amis, NVIDIA a enfin lâché <strong>son client
<a href="https://www.nvidia.com/en-us/geforce-now/download/">GeForce Now</a>
natif pour Linux</strong> ! Après des années à bidouiller avec des solutions non officielles ou à passer par le navigateur (beurk ^^), on a ENFIN droit à une vraie app qui tourne en natif.</p>
<p>Pour ceux qui débarquent, GeForce Now c'est donc le service de cloud gaming de NVIDIA. En gros, vous jouez à vos jeux sur des serveurs surpuissants équipés de RTX 5080, et le flux vidéo est streamé sur votre machine. Du coup, même si votre PC date de Mathusalem, vous pouvez faire tourner Cyberpunk 2077 en Ultra comme si de rien n'était.</p>
<p>Après y'a quand même un truc important à piger c'est que vos jeux, faut les acheter à côté. GeForce Now ne vend rien, il se connecte à vos bibliothèques Steam, Epic Games Store, Ubisoft Connect et compagnie. Ainsi, si vous possédez déjà des jeux sur ces plateformes, vous les retrouvez directement dans l'interface. Par contre, tous les jeux ne sont pas compatibles, mais il y a un catalogue d'environ 2000 titres supportés.</p>
<h2 id="ce-quil-vous-faut">Ce qu'il vous faut</h2>
<p>Côté config, c'est pas trop exigeant vu que c'est votre connexion internet qui fait le gros du boulot :</p>
<ul>
<li>Ubuntu 24.04 LTS (officiellement supporté, mais ça tourne aussi sur d'autres distros via Flatpak)</li>
<li>Un GPU compatible Vulkan Video pour le décodage H.264/H.265 (GeForce série 10 minimum, ou Intel/AMD récent)</li>
<li>Une connexion internet correcte : 15 Mbps pour du 720p, 25 Mbps pour du 1080p, et 65 Mbps si vous voulez taper dans le 5K à 120 fps</li>
<li>Latence réseau inférieure à 80ms (privilégiez l'Ethernet ou le WiFi 5 GHz)</li>
</ul>
<h2 id="comment-installer-le-bazar">Comment installer le bazar</h2>
<p>L'installation est carrément simple puisque NVIDIA distribue l'app via <strong>Flatpak</strong>, donc c'est universel. La première méthode qui est à mon sens la plus rapide c'est que vous téléchargiez le fichier .bin depuis le
<a href="https://www.nvidia.com/en-us/geforce-now/download/">site officiel</a>
. Ensuite vous le rendez exécutable et vous le lancez :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">chmod +x GeForceNOWSetup.bin
</span></span><span class="line"><span class="cl">./GeForceNOWSetup.bin
</span></span></code></pre><p>Deuxième méthode, si vous préférez tout faire en ligne de commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">flatpak</span> <span class="n">remote</span><span class="o">-</span><span class="n">add</span> <span class="o">--</span><span class="n">user</span> <span class="o">--</span><span class="k">if</span><span class="o">-</span><span class="ow">not</span><span class="o">-</span><span class="n">exists</span> <span class="n">GeForceNOW</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">international</span><span class="o">.</span><span class="n">download</span><span class="o">.</span><span class="n">nvidia</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">GFNLinux</span><span class="o">/</span><span class="n">flatpak</span><span class="o">/</span><span class="n">geforcenow</span><span class="o">.</span><span class="n">flatpakrepo</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="n">flatpak</span> <span class="n">install</span> <span class="n">flathub</span> <span class="n">org</span><span class="o">.</span><span class="n">freedesktop</span><span class="o">.</span><span class="n">Platform</span><span class="o">//</span><span class="mf">24.08</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="n">flatpak</span> <span class="n">install</span> <span class="o">-</span><span class="n">y</span> <span class="o">--</span><span class="n">user</span> <span class="n">GeForceNOW</span> <span class="n">com</span><span class="o">.</span><span class="n">nvidia</span><span class="o">.</span><span class="n">geforcenow</span>
</span></span></code></pre><p>Attention, petit piège : si vous êtes sous Wayland et que la fenêtre refuse de s'ouvrir, y'a un fix :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">flatpak override --user --nosocket=wayland com.nvidia.geforcenow
</span></span></code></pre><h2 id="les-abonnements-parce-que-faut-bien-payer">Les abonnements... parce que faut bien payer</h2>
<p>NVIDIA propose trois formules :</p>
<ul>
<li><strong>Gratuit</strong> : sessions d'une heure max, qualité standard 1080p/60fps, et vous aurez des pubs. C'est suffisant pour tester le service.</li>
<li><strong>Performance à 10,99€/mois</strong> : là ça devient intéressant. Sessions de 6 heures, qualité jusqu'à 1440p/60fps avec le ray tracing activé, et plus de pubs. C'est le sweet spot pour la plupart des joueurs.</li>
<li><strong>Ultimate à 21,99€/mois</strong> : le Graal. Vous jouez sur des serveurs équipés de RTX 5080, avec du DLSS 4, jusqu'à 5K à 120 fps ou 1080p à 360 fps si vous avez un écran gaming qui suit. Sessions de 8 heures.</li>
</ul>
<p>Petit détail qui peut piquer, depuis janvier 2026, y'a un cap de 100 heures de jeu par mois sur les abos payants. Si vous dépassez, c'est 2,99€ (Performance) ou 5,99€ (Ultimate) par tranche de 15 heures supplémentaires. Bon, 100 heures par mois ça fait quand même 3h20 par jour... sauf si vous faites des sessions marathon le week-end, ça devrait aller.</p>
<p>En tout cas, avoir le DLSS 4 et le ray tracing natifs sur Linux via le cloud, c'est quand même un sacré pas en avant. D'ailleurs, ça tombe bien au moment où
<a href="https://korben.info/linux-gaming-90-pourcent-jeux-windows-compatibles.html">90% des jeux Windows tournent maintenant sur Linux</a>
grâce à Proton... Entre le cloud gaming et la compatibilité native, y'a jamais eu de meilleur moment dans l'histoire de l'Humanité pour lâcher Windows si vous êtes un gamer ^^.</p>
<h2 id="dépannage-rapide">Dépannage rapide</h2>
<p>Si l'installation plante avec « Flatpak not found », installez d'abord Flatpak via votre gestionnaire de paquets (<code>sudo apt install flatpak</code> sur Ubuntu).</p>
<p>Si vous avez des saccades, vérifiez que votre GPU supporte bien Vulkan Video. Sur les cartes NVIDIA, passez sur une session X11 plutôt que Wayland... sauf si vous avez une RTX série 30 ou plus récente, là ça devrait passer.</p>
<p>Pour les problèmes de latence, branchez-vous en Ethernet si possible. Le WiFi 5 GHz ça passe, mais attention au 2.4 GHz qui ajoute un sacré jitter.</p>
<p>Bref, si vous voulez jouer à des jeux AAA sur Linux sans vous prendre la tête avec Wine ou Proton,
<a href="https://blogs.nvidia.com/blog/geforce-now-thursday-linux/">GeForce Now</a>
est maintenant une option carrément viable.</p>
<p>Amusez-vous bien !</p>