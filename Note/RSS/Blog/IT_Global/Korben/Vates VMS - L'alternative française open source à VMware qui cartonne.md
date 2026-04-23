---
title: "Vates VMS - L'alternative française open source à VMware qui cartonne"
author: "Korben"
date: 2026-02-23T09:41:51.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source"
  - "linux-open-source/administration-serveur"
  - "alternative open source"
  - "migration vmware"
  - "virtualisation"
  - "VMWare"
rss_source: Blog
url: https://korben.info/vates-alternative-vmware-open-source.html
note: 0
seen: false
---


-- Article en partenariat avec <strong>VATES</strong> --
<p>Vous avez vu le bazar chez VMware depuis que Broadcom a racheté la boîte ? Les prix qui flambent, les licences qui changent tous les quatre matins, les clients historiques qui reçoivent des factures multipliées par je sais pas combien... C'est la panique générale dans les DSI !</p>
<p>Et pendant ce temps-là, y'a une boîte française basée à Grenoble qui se frotte les mains. Pas par
<a href="https://fr.wikipedia.org/wiki/Schadenfreude">schadenfreude</a>
hein, mais parce qu'ils bossent depuis 2012 sur <strong>une alternative open source</strong> à VMware. Vous l'aurez compris, je parle de
<a href="https://vates.tech">Vates</a>
et de leur stack complète baptisée <strong>Vates VMS</strong>.</p>
<p>J'ai donc eu l'occasion de mettre les mains dans le cambouis avec leur lab de test la semaine dernière. Ils m'ont prêté 3 serveurs HPE Moonshot rien que pour moi, avec accès VPN, et carte blanche pour faire mumuse. J'avoue, au début je pensais galérer avec la config réseau... Eh bah non. J'installe XCP-ng en une dizaine de minutes, je configure le VLAN qui va bien, et c'est parti.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vates-alternative-vmware-open-source/vates-alternative-vmware-open-source-2.png" alt="" loading="lazy" decoding="async">
<p>Mais avant, je vous propose de poser un peu les bases pour ceux qui débarquent. Vates VMS, c'est une suite complète qui comprend XCP-ng (l'hyperviseur bare-metal de Type 1, basé sur Xen... oui oui, le même Xen qui fait tourner AWS depuis des lustres) et Xen Orchestra (l'interface web pour tout gérer). Le tout en 100% open source, hébergé par la Linux Foundation.</p>
<p>Et là vous allez me dire &quot;<em>ouais mais open source, c'est souvent la version bridée avec les vraies features payantes</em>&quot;. Eh bien non, chez Vates c'est différent ! En fait, tout est dispo gratos sur GitHub. Leur modèle économique repose sur le support et l'accompagnement, et pas sur des licences à la c*n facturées au core ou au socket. Un prix fixe par serveur physique, point barre. Comme ça y'a pas de surprise sur la facture, ni de calculette à sortir quand vous ajoutez de la RAM.</p>
<p>D'ailleurs, ils viennent de sortir Xen Orchestra 6, entièrement réécrit en Vue.js. Et pour l'avoir testé, je peux vous dire que l'interface est vraiment fluide, moderne, et surtout pensée pour qu'on s'y retrouve sans avoir besoin d'un doctorat en VMwarologie. Vous gérez vos VMs, vos backups, vos migrations, votre monitoring... tout ça depuis un navigateur sur n'importe quel OS.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vates-alternative-vmware-open-source/vates-alternative-vmware-open-source-3.png" alt="" loading="lazy" decoding="async">
<p>Et y'a même XO Lite, une version ultra-légère embarquée directement dans XCP-ng pour les opérations de base. Bon, faut pas s'attendre à tout gérer avec ça car c'est vraiment pour le dépannage quand vous n'avez pas accès au serveur principal. Mais c'est pratique quand vous êtes en déplacement et qu'il faut redémarrer une VM en urgence.</p>
<p>Pour les boîtes qui veulent se barrer de VMware, ils ont également développé des outils de migration V2V. Ça fonctionne pour 90% des usages VMware existants (attention quand même aux configs exotiques avec du vSAN ou des plugins proprio, là faut prévoir un peu plus de boulot). Et l'architecture est suffisamment proche de VMware pour que la transition se fasse sans tout réinstaller from scratch.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vates-alternative-vmware-open-source/vates-alternative-vmware-open-source-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Côté fonctionnalités avancées, y'a également XOSTOR pour ceux qui veulent faire de l'hyperconvergence. C'est leur SAN virtuel basé sur DRBD qui transforme vos disques locaux en stockage partagé avec réplication et haute disponibilité. Comme ça, plus besoin de SAN externe hors de prix, puisque vos serveurs XCP-ng deviennent un cluster de stockage distribué.</p>
<p>Pour les DevOps, c'est aussi la fête ! Terraform, Pulumi, Ansible, API REST, CLI... tout y est. J'ai pas eu le temps de tester Terraform en profondeur, mais le provider XO existe bien sur le registry HashiCorp. Ils ont même un projet Pyrgos pour déployer Kubernetes directement depuis Xen Orchestra. Bref, c'est cloud-native ready.</p>
<p>Perso, ce qui m'a vraiment convaincu durant mes tests, c'est qu'on n'a pas 15 outils différents avec lesquels jongler. J'ai bien sûr testé la création de VM, les snapshots, les backups incrémentaux... tout passe par la même interface. Un seul éditeur qui maîtrise toute la stack, de l'hyperviseur jusqu'aux sauvegardes, c'est quand même le kiff. Sans oublier la doc qui est claire comme de l'eau de roche et le support répond vraiment (enfin pour ceux qui prennent un contrat, sinon y'a la communauté qui est plutôt active sur le forum).</p>
<p>Côté références, ils ont plus d'un millier de clients dans le monde entier. Même la NASA utilise les outils de Vates (hé ouais quand même, c'est la classe !), sans oublier des universités, des hôpitaux, l'ANSSI... C'est du sérieux !</p>
<p>Et pour les administrations françaises qui doivent passer par les marchés publics, Vates est référencé chez CAIH, CANUT et UGAP. Du coup pas besoin de monter un appel d'offres complexe, vous pouvez commander directement via les catalogues. Et si vous vous demandez comment ça se compare à
<a href="https://korben.info/vmware-esxi-est-a-nouveau-gratuit.html">ESXi</a>
ou à
<a href="https://korben.info/des-scripts-tout-faits-pour-votre-proxmox.html">Proxmox</a>
, sachez que l'architecture est vraiment proche de VMware (donc migration facilitée), mais avec la philosophie open source en plus.</p>
<p>Alors oui, c'est un article sponsorisé, mais sincèrement si vous êtes sur VMware et que vous regardez vos factures arriver avec des sueurs froides depuis le rachat par Broadcom, ça vaut vraiment le coup de jeter un œil. C'est français, c'est open source, c'est maintenu par une équipe d'une centaine de personnes et ça fait très bien le taf.</p>
<p>Y'a même un essai d'un mois pour tester avant de se décider, histoire de ne pas acheter
<a href="https://fr.wiktionary.org/wiki/acheter_chat_en_poche">chat en poche</a>
(oui c'est une vraie expression du XVe siècle que je viens de découvrir alors je vous la transmets, faites en bon usage).</p>
<p>Bref, si la souveraineté numérique et l'indépendance technologique c'est votre truc (ou si vous en avez juste marre de vous faire racketter),
<a href="https://vates.tech">allez voir ce qu'ils proposent</a>
, c'est top !</p>