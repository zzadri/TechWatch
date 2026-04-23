---
title: "Eonvelope - Vos emails méritent aussi un backup local"
author: "Korben"
date: 2026-03-16T09:26:12.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/sauvegarde-backup"
  - "self-hosting"
  - "archivage email"
  - "Docker"
  - "homelab"
  - "sauvegarde emails"
  - "self-hosted"
rss_source: Blog
url: https://korben.info/eonvelope-archivage-email-self-hosted.html
note: 0
seen: false
---

<p>On archive nos photos avec
<a href="https://korben.info/immich-solution-sauvegarde-auto-hebergee-photos-videos.html">Immich</a>
, nos documents avec
<a href="https://korben.info/readur-gestion-documentaire-ocr-rust-autoheberge.html">Readur</a>
, nos mots de passe avec
<a href="https://korben.info/bitwarden-gestionnaire-mots-passe-heberger-vous-meme.html">Vaultwarden</a>
... mais nos emails ? Ah bah non, ça on les laisse chez Google en croisant les doigts pour que tout se passe bien jusqu'à la fin de nos jours. C'est quand même un peu dinguo quand on y réfléchit sérieusement.</p>
<p>Et pourtant, y'a des années de conversations là-dedans ! Des factures en pièce jointe, des confirmations de commande, des échanges pro avec votre comptable, des mots de passe envoyés en clair (oui, hélas, ça arrive encore). Du coup, quand un hébergeur mail décide de changer ses conditions générales ou de fermer boutique, tout part à la poubelle si vous n'y faites pas attention.</p>
<p>
<a href="https://github.com/Dacid99/eonvelope">Eonvelope</a>
, c'est un outil open source en Python qui permet de sauvegarder automatiquement tout ça sur votre propre serveur et qui se lance avec un simple <code>docker compose up</code>.</p>
<p>Le truc, c'est que des outils comme
<a href="https://korben.info/sauvegarder-gmail-avec-gmvault.html">Gmvault</a>
font déjà le boulot via cron, mais uniquement pour Gmail et en ligne de commande alors qu'Eonvelope, lui, un peu à la manière de
<a href="https://korben.info/bichon-archiveur-emails-rust-recherche.html">Bichon</a>
, tourne en arrière-plan avec une interface web et archive en continu tous vos comptes. Franchement, c'est pas le même délire. Vous branchez vos comptes IMAP, POP3, Exchange, et même JMAP (le protocole poussé par Fastmail qui commence tout juste à se démocratiser), vous réglez la fréquence, et hop, vos mails atterrissent dans votre instance sans que vous ayez à y penser.</p>
<p>Attention par contre, c'est de l'archivage, pas un client mail... vous ne répondrez pas à vos mails depuis l'interface.</p>
<p>Côté installation, c'est du Docker avec seulement 2 conteneurs, le serveur web et la base de données. En fait, comptez 5 minutes chrono si vous avez déjà un serveur dédié ou un VPS, le fichier <code>docker-compose.yml</code> est fourni et les variables d'environnement sont bien documentées sur
<a href="https://eonvelope.readthedocs.io/">ReadTheDocs</a>
. Y'a même un mode basse consommation pour ceux qui font tourner ça sur un Raspberry Pi 4 avec 2 Go de RAM ou un petit Synology ! SSL et HTTPS sont inclus par défaut, et l'authentification multifacteur aussi.</p>
<p>Mais le vrai point fort, c'est les intégrations avec le reste de l'écosystème self-hosted. Concrètement, vous pouvez envoyer vos pièces jointes PDF vers Paperless-ngx pour l'OCR, les photos vers Immich, et exporter vos contacts vers votre carnet d'adresses Nextcloud. Y'a aussi un endpoint Prometheus pour brancher Grafana et suivre vos stats d'archivage. En gros, si vous avez déjà un homelab qui tourne, ça vient se brancher dessus comme une pièce de Lego.</p>
<p>L'interface web est en PWA (donc utilisable sur votre téléphone), avec un moteur de recherche, du filtrage par date et par expéditeur, des fils de conversation reconstitués et de l'import/export en EML et MBOX. Franchement, c'est propre. Y'a aussi une API REST pour ceux qui préfèrent scripter par-dessus plutôt que de passer par l'interface.</p>
<p>Le projet est sous licence AGPLv3 et son dev déclare l'utiliser lui-même au quotidien, ce qui est souvent bon signe. Notez que la
<a href="https://korben.info/sauvegarde-boite-email-gmail.html">migration depuis un backup existant</a>
n'est pas forcément fluide mais qui ne tente rien n'a rien !</p>
<p>Bref, ça comble un vrai manque dans la stack de nos machins auto-hébérgés mais je trouve que l'approche est clairement plus intégrée que ce qui existe (genre MailPiler ou un combo fetchmail+dovecot). À surveiller donc !</p>
<p>
<a href="https://noted.lol/eonvelope/">Source</a>
</p>