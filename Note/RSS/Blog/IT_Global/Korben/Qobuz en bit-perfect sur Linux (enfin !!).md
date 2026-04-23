---
title: "Qobuz en bit-perfect sur Linux (enfin !!)"
author: "Korben"
date: 2026-03-31T09:24:07.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "multimedia-culture"
  - "open source"
  - "Qobuz"
rss_source: Blog
url: https://korben.info/qbz-qobuz-client-linux-bit-perfect.html
note: 0
seen: false
---

<p>Si vous êtes abonné <strong>Qobuz</strong> et que vous êtes sous Linux, vous connaissez cette douleur sourde qui vous coupe le souffle la nuit : <strong>IL N'Y A PAS DE CLIENT OFFICIEL</strong> ! Vous êtes donc condamné comme n'importe quel gueux à utiliser le lecteur web, qui est aussi &quot;audiophile-phile&quot; qu'un casque de chantier.</p>
<p>Mais heureusement,
<a href="https://github.com/vicrodh/qbz">QBZ</a>
vient régler ça, et vous allez voir, c'est du sérieux !</p>
<p>Il s'agit d'un client natif et open source (sous licence MIT) écrit en Rust avec Tauri 2.0 côté desktop et SvelteKit pour l'interface, ce qui fait que c'est léger, que ça démarre vite, et surtout ça gère le bit-perfect via 4 backends audio au choix : PipeWire, ALSA, ALSA Direct (accès exclusif au DAC) et PulseAudio.</p>
<img src="https://korben.info/qbz-qobuz-client-linux-bit-perfect/qbz-qobuz-client-linux-bit-perfect-1.avif" alt="" loading="lazy" decoding="async">
<p>Le switching de sample rate se fait alors à la volée, de 44.1 à 192 kHz, selon ce que votre DAC supporte. Pour les audiophiles... bah ça change tout par rapport au resampling sauvage du navigateur. Ouf, on est sauvé en fait ^^</p>
<p>Côté fonctionnalités, c'est clairement loin du petit projet bricolé un dimanche soir en vibe coding puisque ce lecteur décode nativement FLAC, MP3, AAC, ALAC, WavPack, Ogg Vorbis et Opus, le tout avec du gapless playback et de la normalisation de loudness EBU R128. Je comprends pas tout parce que je suis pas expert là dedans, mais si vous aimez la Hi-Fi, je sais que ça vous parle.</p>
<p>Y'a aussi une gestion de bibliothèque locale avec scan de dossiers et indexation SQLite, et même un import de playlists depuis Spotify, Apple Music, Tidal ou Deezer. Ainsi, si vous migrez vers Qobuz, ça vous fera gagner des heures plutôt que de tout vous retaper à créer à la main !</p>
<p>Niveau intégrations, c'est aussi super complet : scrobbling Last.fm et ListenBrainz, enrichissement MusicBrainz, pochettes via Discogs, contrôle MPRIS et touches média. Et le casting vers Chromecast, DLNA/UPnP et AirPlay est intégré. Le Chromecast directement depuis un client Linux sans bidouille, c'est pas courant, et ça fait plaizzz !</p>
<img src="https://korben.info/qbz-qobuz-client-linux-bit-perfect/qbz-qobuz-client-linux-bit-perfect-2.avif" alt="" loading="lazy" decoding="async">
<p>L'interface est également hyper soignée avec 26 thèmes au choix (Dark, OLED, Nord, Dracula, Tokyo Night...) et 17 panneaux de visualisation dont un spectre, un oscilloscope et un spectrogramme. Y'a même un mode immersif plein écran, le tout dispo en 5 langues dont le français.</p>
<p>Pour l'installation, c'est packagé proprement : Flatpak, AUR, Snap, AppImage, DEB, RPM et même un DMG pour macOS (Apple Silicon, expérimental) et si vous êtes sur Arch, un petit <code>yay -S qbz-bin</code> et c'est réglé.</p>
<p>Par contre, il y a quelques limites à connaître comme le seeking sur des pistes hi-res au-dessus de 96 kHz qui peut prendre 10 à 20 secondes. ALSA Direct bloque aussi les autres applis audio (logique, c'est l'accès exclusif). Et le bit-perfect via PipeWire est limité quand on lance le tout en sandbox Flatpak. En fait, le problème c'est que la sandbox bloque l'accès direct au matériel donc si vous voulez le max de qualité, optez pour le paquet natif.</p>
<p>Si
<a href="https://korben.info/comparatif-deezer-spotify-qobuz.html">Qobuz est votre service de streaming</a>
et que Linux est votre OS préféré d'amour, les alternatives payantes comme Audirvana ou Roon ne sont clairement pas données. C'est pour cela que je vous parle de <strong>
<a href="https://qbz.lol/">QBZ</a>
</strong> qui fait le boulot gratuitement comme un chef et dont le développeur (vicrodh) est super actif (il recherche des contributeurs si vous voulez l'aider).</p>
<p>Et un grand merci à Pierre pour le tuyau !</p>