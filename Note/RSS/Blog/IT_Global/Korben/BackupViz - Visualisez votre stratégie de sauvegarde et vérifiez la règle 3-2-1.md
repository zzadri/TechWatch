---
title: BackupViz - Visualisez votre stratégie de sauvegarde et vérifiez la règle 3-2-1
author: Korben
date: 2026-01-08T07:45:03.000Z
type: site
subject:
category: IT Global
tags:
  - developpement/devops-infrastructure
  - developpement/outils-developpement
  - backup
  - NAS
  - sauvegarde
  - sauvegarde 3-2-1-1-0
  - visualisation
  - webapp
rss-source: Blog
url: https://korben.info/backupviz-visualisation-sauvegarde-3-2-1.html
note: 5
seen: false
---

<p>Vous connaissez
<a href="https://korben.info/securisez-vos-donnees-avec-leviia-et-veeam-backup-3-2-1-1-0-accessible-efficace.html">la règle 3-2-1</a>
? Trois copies de vos données, sur deux supports différents, dont une hors site. C'est la base de toute stratégie de sauvegarde sérieuse. Sauf que dans la vraie vie, on a tous tendance à bidouiller notre infra au fil du temps, ajouter un disque par ci, un sync cloud par là... et au bout d'un moment, plus personne ne sait vraiment si on respecte encore cette fichue règle.</p>
<p>C'est exactement le problème que résout <strong>
<a href="https://www.backupviz.fr">BackupViz</a>
</strong>, une webapp française &quot;vibe-codée&quot; par Nicobroii, lecteur de korben.info. Avec cette app, vous dessinez votre infrastructure de sauvegarde de façon visuelle (NAS, serveurs, Proxmox, stockage cloud...) et l'outil analyse automatiquement si votre stratégie tient la route.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/backupviz-visualisation-sauvegarde-3-2-1/backupviz-visualisation-sauvegarde-3-2-1-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Concrètement, vous créez des éléments qui représentent vos machines et vos espaces de stockage, puis vous tracez des liens entre eux pour matérialiser les flux de synchronisation.
<a href="https://korben.info/quel-nas-synology-choisir.html">Synology</a>
Drive Sync vers un second NAS ? Hop, un trait. Cloud Sync vers du S3 ? Un autre trait. Sauvegarde manuelle mensuelle sur disque externe ? Encore un trait, mais en pointillés peut-être.</p>
<p>Et c'est là que ça devient vraiment cool puisque BackupViz ne se contente pas de faire joli. L'outil intègre une analyse automatique de la règle 3-2-1 et vous alerte si une de vos données n'a pas assez de copies, ou si tout est sur le même support, ou si vous n'avez rien en dehors de chez vous. Du coup, plus besoin de compter sur les doigts pour savoir si votre stratégie de redondance est béton.</p>
<p>Côté personnalisation, y'a de quoi faire. Vous pouvez customiser les couleurs des liens (pratique pour différencier les types de sync), ajouter des labels, jouer avec différents thèmes visuels (du mode sombre aux dégradés pastels), et même créer des attributs personnalisés pour noter l'IP d'une machine, une URL d'accès, voire un mot de passe si vous aimez vivre dangereusement.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/backupviz-visualisation-sauvegarde-3-2-1/backupviz-visualisation-sauvegarde-3-2-1-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>L'interface propose aussi une liste de tous vos éléments avec un moteur de recherche, ce qui devient vite indispensable quand votre infra commence à ressembler à un plat de spaghettis. Et pour ceux qui gèrent plusieurs contextes (perso/boulot), vous pouvez créer plusieurs projets et même les dupliquer. Notez que c'est gratuit jusqu'à 20 éléments ce qui est laaaaargment suffisamment pour la vie normale mais que si vous en voulez plus, faudra dépenser quelques euros (et c'est vraiment pas cher... 5 balles à vie ! WTF!?)</p>
<p>Bref, c'est le genre d'outil qu'on aurait aimé avoir depuis looooongtemps parce que faire des schémas de backup sur un bout de papier ou dans un fichier Draw.io, ça va 5 minutes.</p>
<p>Le projet est accessible gratuitement sur backupviz.fr et une démo vidéo de 1min30 est dispo sur YouTube pour voir la bestiole en action.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/m39uK54DDnE?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>