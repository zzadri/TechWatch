---
title: "Microsoft débranche enfin MDT - Comment déployer Windows sans se ruiner (et sans le cloud) ?"
author: "Korben"
date: 2026-01-13T13:19:50.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "tutoriels-guides/tutoriels-avances"
  - "Ansible"
  - "Déploiement Windows"
  - "FOG Project"
  - "MDT"
  - "Microsoft"
  - "open source"
  - "sysadmin"
rss_source: Blog
url: https://korben.info/microsoft-fin-mdt-alternatives-deploiement-windows-guide.html
note: 0
seen: false
---

<p>Snif, snif sniiiif, c'est la fin d'une époque pour tous les admins système qui ont les mains dans le cambouis depuis plus de deux décennies.</p>
<p>Hé oui les amis, Microsoft vient de décider de <strong>débrancher la prise</strong> de son vénérable Microsoft Deployment Toolkit (MDT). Adios ce outil né en 2003 (sous le nom de BDD à l'époque) qui nous a sauvés la mise pendant plus de 20 ans pour installer des parcs entiers de bécanes sans y passer la nuit !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/microsoft-fin-mdt-alternatives-deploiement-windows-guide/microsoft-fin-mdt-alternatives-deploiement-windows-guide-2.png" alt="" loading="lazy" decoding="async">
<p>Alors pourquoi ce revirement ?</p>
<p>Bon, alors officiellement, c'est pour nous faire passer à des solutions &quot;modernes&quot; mais officieusement, beaucoup y voient une manœuvre pour nous pousser vers le passage à la caisse cloud avec <strong>Windows Autopilot</strong> et <strong>Intune</strong>. Forcément, un outil gratuit, local, qui ne remonte quasiment aucune télémétrie (contrairement aux usines à gaz actuelles) et qui permet de faire des masters aux petits oignons sans dépendre d'Azure, ça commençait à faire tache dans le catalogue de Redmond. (oooh yeah !)</p>
<p>Le problème, c'est que pour pas mal de boîtes, Autopilot nécessite des licences spécifiques (M365 Business Premium ou Intune Plan 1) et une connexion internet béton. Hé oui, tout le monde n'a pas envie de dépendre du cloud pour provisionner un poste.</p>
<p>Ça tombe bien, vous me connaissez, je ne vais pas vous laisser tomber. Alors si vous faites partie de ceux qui se retrouvent le cul entre deux chaises, sachez qu'il existe des alternatives sérieuses et surtout gratuites ou open source.</p>
<p>Pour l'imagerie pure et dure (le bare-metal), mon chouchou reste <strong>
<a href="https://github.com/FOGProject/fogproject">FOG Project</a>
</strong>. C'est une bête de course open source qui remplace avantageusement la partie imagerie de WDS. Ça gère le boot réseau (PXE), le multicast pour arroser des dizaines de PC d'un coup, et ça permet de capturer et déployer vos images Windows 10 ou 11. Et pour ceux qui veulent du plus classique,
<a href="https://korben.info/rescuezilla.html">Rescuezilla</a>
(le clone graphique de Clonezilla) fait aussi un boulot béton pour cloner des disques.</p>
<p>Mais là où ça devient vraiment chouette, c'est pour la configuration post-installation car plutôt que de s'enquiquiner avec des task sequences complexes, je vous conseille de regarder du côté d'<strong>Ansible</strong>. Oui, ça marche aussi pour Windows via WinRM (le mode standard) ou SSH ! Vous lancez un petit playbook YAML et hop, vos softs sont installés, vos paramètres de sécurité sont appliqués et votre machine est prête à l'emploi. C'est propre, reproductible et ça évite les erreurs humaines.</p>
<p>Pour ceux qui veulent bidouiller leur serveur de boot, n'oubliez pas non plus d'aller voir mon article sur
<a href="https://korben.info/netboot-serveur-pxe.html">Netboot.xyz</a>
qui est une mine d'or pour booter un grand nombre d'OS par le réseau.</p>
<p>Bref, même si Microsoft tente de nous enfermer dans sa cage dorée avec Autopilot, la communauté a déjà tout ce qu'il faut pour qu'on reste maîtres de notre infrastructure. Alors courage les admins !!! Une page se tourne mais les outils qui déchirent sont toujours là !</p>
<p>
<a href="https://www.theregister.com/2026/01/12/microsoft_deployment_platform/">Source</a>
</p>