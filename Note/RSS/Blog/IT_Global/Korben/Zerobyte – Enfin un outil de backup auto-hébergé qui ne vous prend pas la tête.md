---
title: "Zerobyte – Enfin un outil de backup auto-hébergé qui ne vous prend pas la tête"
author: "Korben"
date: 2026-02-05T09:58:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/self-hosting"
  - "backup"
  - "Docker"
  - "open source"
  - "Rclone"
  - "Restic"
  - "sauvegarde"
  - "self-hosted"
rss_source: Blog
url: https://korben.info/zerobyte-backup-automatise-restic-self-hosted.html
note: 0
seen: false
---

<p>Vous faites des sauvegardes régulières de vos données ? Non ?</p>
<p>Bon, je ne vais pas vous faire la morale, mais le jour où votre disque dur décidera de rendre l'âme ou que votre serveur VPS partira en fumée, vous allez vraiment regretter de ne pas avoir investi dix minutes dans un système de backup sérieux.</p>
<p>Alors, ouiiii, c'est vrai, on a souvent la flemme parce que c'est chiant à configurer. Entre les scripts bash qui plantent sans prévenir et les crontabs illisibles, y’a de quoi s'arracher les cheveux. C'est là qu'intervient <strong>
<a href="https://github.com/nicotsx/zerobyte">Zerobyte</a>
</strong>, un projet open source qui veut réconcilier les allergiques du terminal avec la sécurité de leurs données.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/zerobyte-backup-automatise-restic-self-hosted/zerobyte-backup-automatise-restic-self-hosted-1.jpg" alt="" loading="lazy" decoding="async">
</p>
<p>Zerobyte est donc une plateforme d'automatisation de sauvegarde auto-hébergée qui vient poser une interface web moderne et ultra propre par-dessus le moteur <strong>Restic</strong>. Si vous avez déjà lu mon guide sur les
<a href="https://korben.info/comment-sauvegardez-vos-fichiers-avec-restic.html">backups avec Restic</a>
, vous savez que c'est du solide. Ça fait du chiffrement côté client, de la déduplication et de la compression. En gros, vos données sont blindées avant même de quitter votre machine et seules les modifs sont envoyées, ce qui est parfait pour ne pas exploser son forfait data ou son stockage cloud.</p>
<p>L'interface web permet surtout de tout piloter sans jamais toucher à une ligne de commande. Vous définissez vos &quot;volumes&quot; (ce qu'il faut sauver), vos &quot;repositories&quot; (où stocker tout ça) et vos &quot;jobs&quot; (quand lancer les opérations).</p>
<p>Pour les sources, l'outil est hyper flexible puisqu'il supporte aussi bien les dossiers locaux que les partages réseau via <strong>NFS, SMB, WebDAV ou SFTP</strong> et côté destination, c'est carrément Byzance puisque vous pouvez envoyer vos snapshots vers du S3 (AWS, MinIO, Wasabi), du Google Cloud, de l'Azure ou utiliser l'intégration <strong>rclone</strong> qui ouvre la porte à plus de 70 fournisseurs différents. C’est l’outil idéal pour mettre en place une véritable
<a href="https://korben.info/backupviz-visualisation-sauvegarde-3-2-1.html">stratégie 3-2-1</a>
sans se prendre la tête.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/zerobyte-backup-automatise-restic-self-hosted/zerobyte-backup-automatise-restic-self-hosted-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pour l'installation, pas de surprise, ça se passe via <strong>Docker Compose</strong>. C'est léger, ça s'isole bien et ça tourne en deux minutes. Un petit bémol quand même le projet est encore jeune donc ça peut encore bouger pas mal au niveau de l'architecture. Mais pour du monitoring et de la gestion simplifiée de snapshots Restic, c'est déjà redoutable. Vous pouvez explorer vos sauvegardes directement depuis le dashboard et restaurer un fichier précis en trois clics.</p>
<p>Et pour ne rien gâcher, le projet est sous licence libre, ce qui colle parfaitement à l'esprit qu'on aime ici !</p>
<p>Bref, si vous cherchez une solution pour centraliser la gestion de vos sauvegardes sans finir en PLS devant un terminal,
<a href="https://github.com/nicotsx/zerobyte">Zerobyte</a>
mérite clairement que vous y jetiez un œil.</p>