---
title: "Reinstall - Le script ultime pour réinstaller n'importe quel OS sur votre VPS (même Windows)"
author: "Korben"
date: 2026-02-06T09:22:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "tutoriels-guides/tutoriels-avances"
  - "Linux"
  - "réinstallation"
  - "script"
  - "serveur"
  - "sysadmin"
  - "VPS"
  - "Windows"
rss_source: Blog
url: https://korben.info/reinstall-script-vps-os-linux-windows.html
note: 0
seen: false
---

<p>Aujourd'hui, on va aller un peu plus loin que les simples bidouilles habituelles car je vais vous présenter <strong>
<a href="https://github.com/bin456789/reinstall">Reinstall</a>
</strong>, un outil qui va peut-être vous changer la vie si vous gérez des serveurs distants.</p>
<p>Vous connaissez la chanson... vous avez un VPS sous Debian et vous voulez passer sous Arch pour faire votre malin. Sauf que pour opérer ce changement, c'est la galère assurée !! Faut passer par l'interface web de l'hébergeur, booter sur une ISO via une console VNC qui rame sa maman, et prier pour que le réseau revienne après le reboot.</p>
<p>Eh bien ça c'est terminé grâce à ce script Reinstall. Vous lui balancez une commande, le script s'occupe de tout, et hop, votre serveur redémarre sur le nouvel OS de votre choix. Pas besoin d'accès IPMI, pas besoin de supplier le support technique, ça marche tout seul.</p>
<p>Et ça supporte pas mal d'OS... Côté Linux, y'a 19 distributions majeures : Alpine, Debian (de 9 à 13), Ubuntu (de 16.04 à 25.10), toute la famille Red Hat (AlmaLinux, Rocky, Oracle), Fedora, Arch, Gentoo, NixOS... Bref, y'a tout ce qu'il faut.</p>
<p>Et le truc qui va plaire à ceux qui font du cloud, c'est également le support de <strong>Windows</strong>. En effet, le script permet d'installer Windows Vista, 7, 8.1, 10, 11 et même Windows Server 2025.</p>
<p>Et rassurez-vous, il n'utilise pas des images bricolées par on ne sait qui, mais les ISO officielles de chez Microsoft. Lui se content d'injecter automatiquement les drivers VirtIO pour que ça tourne comme un charme sur n'importe quel cloud (AWS, GCP, Oracle Cloud...).</p>
<p>Aussi, le point le plus chiant quand on réinstalle un serveur distant, c'est la config réseau. Si on se loupe, on perd l'accès SSH et c'est fini. <strong>Reinstall</strong> gère ça intelligemment puisqu'il détecte votre IP (statique ou dynamique), gère l'IPv6, les passerelles exotiques et même les serveurs ARM.</p>
<h3 id="ce-quil-vous-faut-avant-de-tout-casser">Ce qu'il vous faut avant de tout casser</h3>
<ul>
<li><strong>RAM</strong> : 256 Mo pour Alpine/Debian, 1 Go pour Windows.</li>
<li><strong>Disque</strong> : 1 Go pour Linux, 25 Go minimum pour Windows.</li>
<li><strong>Accès</strong> : Un accès root/admin sur la machine actuelle.</li>
<li><strong>Temps estimé</strong> : Environ 5 à 15 minutes selon la vitesse de connexion de votre serveur.</li>
</ul>
<p>Un petit avertissement quand même... Ce script ne gère pas les conteneurs type OpenVZ ou LXC. Faut que ce soit une vraie VM (KVM, VMware, Hyper-V) ou un serveur bare-metal.</p>
<h3 id="le-tuto--le-tuto-">Le tuto ! Le tuto !</h3>
<p>C'est là que ça devient drôle. Pour installer un nouveau Linux (disons Debian 13) depuis votre système actuel, il suffit de faire un petit :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Télécharger le script
</span></span><span class="line"><span class="cl">curl -O https://raw.githubusercontent.com/bin456789/reinstall/main/reinstall.sh
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Lancer la réinstallation
</span></span><span class="line"><span class="cl">bash reinstall.sh debian 13 --password &#34;VotreMotDePasse&#34;
</span></span></code></pre><p>Si vous voulez tenter l'aventure Windows :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">bash reinstall.sh windows --image-name &#34;Windows 11 Enterprise LTSC 2024&#34; --lang fr-fr
</span></span></code></pre><p>Le script tourne même depuis Windows (via un <code>.bat</code>) si vous voulez faire l'inverse et repasser sous Linux.</p>
<p>Perso, je trouve ça quand même génial pour tester des trucs sans passer des plombes à configurer des ISO. Ça dépanne grave quand on veut repartir on une base saine en un clin d'œil. D'ailleurs, si vous avez besoin de sécuriser vos serveurs après l'install, j'avais parlé de
<a href="https://korben.info/fail2ban-interface-graphique.html">Fail2Ban</a>
il y a quelques temps, et c'est toujours une bonne idée. Et si vous avez peur de perdre vos données, jetez un œil à
<a href="https://korben.info/comment-sauvegardez-vos-fichiers-avec-restic.html">Restic</a>
pour vos backups.</p>
<p>Bref, si vous gérez des VPS et que vous en avez marre des consoles web préhistoriques, foncez tester ce truc (sur une machine de test d'abord, hein, venez pas pleurer après).</p>
<p>Bon, je vous laisse… Je vais aller me faire un petit café !</p>