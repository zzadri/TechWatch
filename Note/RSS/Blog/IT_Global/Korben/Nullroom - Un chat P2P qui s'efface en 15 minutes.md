---
title: "Nullroom - Un chat P2P qui s'efface en 15 minutes"
author: "Korben ✨"
date: 2026-04-23T08:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "vie-privee-anonymat/chiffrement"
  - "vie-privee-anonymat/messageries-securisees"
  - "discussion chiffrée"
  - "nullroom"
  - "P2P"
  - "WebRTC"
rss_source: Blog
url: https://korben.info/nullroom-un-chat-p2p-qui-sefface-en-15-minutes.html
note: 0
seen: false
---

<p>Utiliser une conversation WhatsApp pour partager un mot de passe à un pote, c'est un peu comme écrire son code de carte bleue au marker dans des chiottes publics. Sauf que les messages, eux, restent des années dans l'historique car y'a personne qui viendra nettoyer ça. Heureusement,
<a href="https://www.nullroom.io/">Nullroom</a>
vient régler ce genre de bricole en mode radical, avec un chat P2P chiffré qui s'autodétruit au bout d'un quart d'heure, sans avoir à vous créer de compte et sans laisser de trace côté serveur.</p>
<p>Alors comment ça fonctionne ? Hé bien vous cliquez sur &quot;CREATE SECURE ROOM&quot;, un lien apparaît, vous le balancez à votre correspondant par le canal de votre choix (Signal, SMS, pigeon voyageur...etc), et hop, une session chiffrée s'ouvre entre vos deux navigateurs. Vous pouvez alors discuter, échanger éventuellement des fichier (jusqu'à 16 Mo max en beta), et après 15 minutes, la room s'évaporera. Purement et simplement et aucun serveur n'aura vu passer vos échanges (mis à par quelques bouts de métadonnées pour établir la connexion).</p>
<p>Sous le capot, y'a un truc crypto assez chouette qui est une clé de chiffrement AES-GCM 256 bits, générée côté client via l'API Web Crypto du navigateur, qui vit dans le fragment de l'URL (c'est la partie qui vient après le #). Et comme les navigateurs n'envoient JAMAIS ce fragment au serveur, vu que c'est un standard HTTP, vous êtes tranquille.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/nullroom-un-chat-p2p-qui-sefface-en-15-minutes/nullroom-un-chat-p2p-qui-sefface-en-15-minutes-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et voilà comment votre clé de session n'existe que chez vous et chez votre correspondant. Le serveur de Nullroom ne la voit pas, même pas une microseconde. C'est le même trick que celui qu'utilise
<a href="https://korben.info/privatebin-outil-ultime-partage-informations-securite.html">PrivateBin</a>
pour les snippets chiffrés, mais appliqué à du chat en direct.</p>
<p>Le flux de données, lui, passe en direct d'un navigateur à l'autre via WebRTC et le serveur ne sert comme je vous le disais plus haut, qu'à la poignée de main initiale.</p>
<p>Ensuite, les messages et les fichiers circulent en peer-to-peer, relayés via les serveurs TURN de Cloudflare quand votre NAT coince. Donc au pire, Cloudflare voit passer du trafic 100% chiffré, et pas le contenu en clair. Les logs serveur sont également désactivés sur les chemins des rooms, et les UUIDs de sessions vivent dans un Redis totalement volatile qui est nettoyé au bout de ces fameuses 15 minutes.</p>
<p>Niveau limites, une room c'est deux personnes max donc si vous cherchiez un remplaçant à Signal ou à Briar, ce n'est pas le bon outil. C'est juste une messagerie pour un échange ponctuel entre 2 personnes.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/nullroom-un-chat-p2p-qui-sefface-en-15-minutes/nullroom-un-chat-p2p-qui-sefface-en-15-minutes-3.png" alt="" loading="lazy" decoding="async">
<p>Et l'équipe ou l'entreprise derrière n'est pas affichée côté site (pas de mentions légales, pas de juridiction précisée), donc attention ! Ça reste du &quot;<em>faites-vous votre opinion</em>&quot; mais comme le code est open source (licence MIT) sur
<a href="https://github.com/nullroomio/nullroom.io">GitHub</a>
vous pouvez quand même l'analyser et monter votre propre infra Nullroom.</p>
<p>Pour le quotidien, c'est un service qui est bien foutu, que ce soit pour un mot de passe à filer à un collègue en télétravail, un lien temporaire à partager pendant une réu, une confidence à un pote qui n'a rien à faire dans les archives iMessage, ou encore un numéro de compte à transmettre vite fait avant que l'autre ne parte en vacances... Tous ces cas d'usage existent et la friction est quasi nulle donc c'est plutôt une bonne approche je trouve.</p>
<p>Voilà, si vous voulez tester le concept d'une conversation qui n'aura jamais eu lieu, filez sur nullroom.io.</p>