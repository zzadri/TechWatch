---
title: "SSH dans l'initramfs - Rebootez vos serveurs chiffrés sans stress"
author: "Korben"
date: 2026-03-06T09:08:05.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "tutoriels-guides/tutoriels-avances"
  - "vie-privee-anonymat/chiffrement"
  - "chiffrement"
  - "chiffrement LUKS"
  - "Tailscale"
rss_source: Blog
url: https://korben.info/deverrouillage-disque-chiffre-distance.html
note: 0
seen: false
---

<p>Le chiffrement complet du disque, tout le monde vous dit que c'est la base. LUKS sous Linux, BitLocker sous Windows, FileVault sous macOS... sauf que personne vous dit quoi faire quand votre serveur reboot à 3h du mat et qu'il attend sagement sa passphrase.</p>
<p>Là, vous êtes coincé !!!!</p>
<p>Parce que oui, le truc vicieux avec le chiffrement intégral, c'est qu'au démarrage, le système ne peut pas lire le disque tant que vous n'avez pas tapé le mot de passe. Du coup, si votre machine est dans un datacenter ou chez un hébergeur, ben... faut se déplacer physiquement. Et ça c'est bien relou !!!</p>
<p>La solution, c'est d'embarquer un serveur SSH directement dans l'
<a href="https://korben.info/faille-cryptsetup-permet-dobtenir-acces-root-certaines-machines-linux.html">initramfs</a>
(oui, le mini OS qui tourne AVANT votre vrai système, sur le port 22). En gros, votre machine boot, charge l'initramfs, lance un serveur SSH... et vous n'avez plus qu'à vous connecter à distance pour taper la passphrase. Comme ça le disque se déverrouille et le boot continue. Voilà quoi, c'est simple la vie quand on lit Korben.info !! loool</p>
<h2 id="linitramfs-cest-quoi-exactement-">L'initramfs, c'est quoi exactement ?</h2>
<p>Alors pour ceux qui débarquent, l'initramfs c'est une archive compressée dans <code>/boot/initramfs-linux.img</code> qui contient un système Linux minimal. Son boulot, c'est de préparer le terrain avant de passer la main au vrai OS, genre charger les modules noyau, détecter le matériel, monter les systèmes de fichiers... et dans notre cas, demander la passphrase LUKS. Genre un second OS, mais en version bonsaï !</p>
<h2 id="installer-dropbear-dans-linitramfs">Installer Dropbear dans l'initramfs</h2>
<p>
<a href="https://github.com/mkj/dropbear">Dropbear</a>
, c'est un serveur SSH ultra-léger (environ 110 Ko) parfait pour l'initramfs.
<a href="https://jyn.dev/remotely-unlocking-an-encrypted-hard-disk/">L'article de jyn qui m'a inspiré pour cet article</a>
, recommande Arch Linux avec mkinitcpio, mais sachez que sous Debian/Ubuntu le paquet <code>dropbear-initramfs</code> fait le même boulot avec <code>update-initramfs</code>.</p>
<p>Sur Arch, vous installez <code>mkinitcpio-systemd-extras</code> puis vous modifiez <code>/etc/mkinitcpio.conf</code> pour ajouter les hooks réseau et Dropbear :</p>
<p><code>HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt filesystems fsck systemd-network dropbear)</code></p>
<p>Attention, l'ordre des hooks compte. Le réseau doit être configuré AVANT Dropbear, sinon votre serveur SSH démarre sans interface réseau. Pas super utile donc !</p>
<h2 id="configurer-le-réseau-dans-linitramfs">Configurer le réseau dans l'initramfs</h2>
<p>Ensuite faut créer un fichier de config réseau dans <code>/etc/systemd/network-initramfs/</code>. En fait, c'est du systemd-networkd classique, donc si vous avez déjà configuré ça, c'est pareil. Un simple fichier <code>.network</code> avec DHCP fait le job en Ethernet (et pour un serveur, c'est clairement recommandé). Pour les plus paranos, une IP statique marche aussi, sauf que faudra pas oublier de la mettre à jour si vous changez de réseau.</p>
<h2 id="la-touche-tailscale">La touche Tailscale</h2>
<p>Après si votre serveur est derrière un NAT ou un firewall, bah... le SSH classique ne passe pas. Du coup, jyn a eu la bonne l'idée d'embarquer
<a href="https://korben.info/tailscale-reseau-prive-virtuel.html">Tailscale</a>
dans l'initramfs aussi. Comme ça, la machine rejoint votre réseau privé Tailscale dès le boot, même avant le déchiffrement du disque.</p>
<p>Vous lancez <code>setup-initcpio-tailscale</code>, ça vous donne un lien d'authentification sur <code>login.tailscale.com</code> et c'est réglé. Après faut penser à configurer les ACL Tailscale pour que SEULE votre machine d'admin puisse se connecter à l'initramfs car OUI ON NE LAISSE PAS UN PUTAIN DE SSH ouvert sur un système pré-boot sans protection, HEIN ?? HEIN ?? Donc faites ça !!</p>
<h2 id="les-précautions-de-sécurité">Les précautions de sécurité</h2>
<p>Vous vous en doutez, y'a quand même quelques pièges à éviter. D'abord, les clés SSH de Dropbear dans l'initramfs (stockées dans <code>/etc/dropbear/</code>) doivent être DIFFÉRENTES de celles d'OpenSSH dans <code>/etc/ssh/</code>. Parce que l'initramfs n'est pas chiffré (bah oui, il doit tourner avant le déchiffrement), donc ces clés sont techniquement accessibles à quelqu'un qui a un accès physique au disque.</p>
<p>Ensuite, attention, limitez ce que Dropbear peut faire. Pas de shell complet, juste la commande <code>systemd-tty-ask-password-agent</code> qui sert uniquement à taper la passphrase. Comme ça, même si quelqu'un arrive à se connecter, il ne peut rien faire d'autre.</p>
<p>Et désactivez aussi l'expiration des clés Tailscale pour la machine initramfs via <code>--auth-key</code> avec un token non-éphémère, sinon votre serveur va se retrouver éjecté du réseau au pire moment.</p>
<h2 id="reconstruire-et-tester">Reconstruire et tester</h2>
<p>Une fois tout configuré, un petit <code>mkinitcpio -P</code> pour reconstruire l'initramfs et c'est bon. Si ça ne marche pas du premier coup, vérifiez les logs avec <code>journalctl -b</code>. Mais attention, testez ça sur une VM ou une machine avec accès console (IPMI, iDRAC, KVM-over-IP) d'abord, parce que si le réseau de l'initramfs ne monte pas, votre serveur devient une brique inaccessible... et là, c'est le vrai drame de votre vie qui commence (et la découverte de France Travail) !</p>
<p>Au prochain reboot, votre serveur va donc démarrer, charger l'initramfs, se connecter à Tailscale, lancer Dropbear... et attendre patiemment que vous tapiez la passphrase depuis votre canapé.</p>
<p>Si vous gérez des serveurs chiffrés à distance, c'est le genre de setup un peu touchy à la base mais qui change la vie. Comme ça, plus besoin de supplier / soudoyer / menacer (chacun sa technique) le technicien du datacenter d'astreinte de brancher un clavier ^^.</p>
<p>
<a href="https://jyn.dev/remotely-unlocking-an-encrypted-hard-disk/">Découvrir le tuto complet de Jyn ici !</a>
</p>