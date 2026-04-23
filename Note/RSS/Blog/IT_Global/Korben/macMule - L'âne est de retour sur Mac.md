---
title: "macMule - L'âne est de retour sur Mac"
author: "Korben"
date: 2026-04-08T09:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "vie-privee-anonymat/hadopi-telechargement"
  - "macOS"
  - "open source"
  - "Wine"
rss_source: Blog
url: https://korben.info/macmule-emule-macos-apple-silicon.html
note: 0
seen: false
---

<p>Vous vous souvenez d'eMule ? Le petit âne qui monopolisait votre connexion ADSL pendant 3 jours pour télécharger un fichier de 700 Mo... et les fameux &quot;Linux_ISO.avi&quot; qui n'étaient absolument pas des ISOs Linux ?</p>
<p>Eh bien le bougre est de retour sur macOS.
<a href="https://github.com/mderouet/macMule">macMule</a>
c'est eMule packagé en .app native, compatible Apple Silicon via Rosetta 2, zéro configuration. Vous glissez dans Applications, vous lancez, et hop ça se connecte tout seul aux serveurs ed2k et au réseau Kad. Hé oui, ça tourne encore en 2026.</p>
<p>Côté technique, l'app fait environ 1 Go parce qu'elle embarque Wine Crossover (la couche de compatibilité Windows par Gcenx). Le développeur Martin Derouet a pris le build Community x64 d'eMule par irwir, l'a wrappé dans un bundle .app self-contained, et comme ça, ça se lance comme n'importe quelle app Mac.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/macmule-emule-macos-apple-silicon/macmule-emule-macos-apple-silicon-2.png" alt="" loading="lazy" decoding="async">
<p>Y'a pas de dépendances externes à installer, et surtout pas de terminal à ouvrir. Les fichiers téléchargés atterrissent alors dans <code>~/Library/Application Support/macMule/drive_c/eMule/Incoming/</code>... c'est pas super intuitif comme chemin, mais au moins c'est rangé.</p>
<p>D'ailleurs, si vous avez suivi l'actualité de
<a href="https://korben.info/wine-10-0-linux-fait-tourner-apps-windows-arm.html">Wine 10.0 et le support ARM</a>
, vous savez que la couche de compatibilité Windows n'a jamais été aussi solide. macMule en profite directement. Et si vous voulez compiler votre propre build, le script est dispo : <code>./build.sh</code> pour la dernière version stable ou <code>./build.sh 0.70b</code> pour une version spécifique. Faut juste avoir Homebrew avec <code>wine-crossover</code> et Rosetta 2 installés.</p>
<p>J'ai été surpris que les réseaux ed2k et Kad soient encore debout. Mais c'est cool car ces réseaux hébergent des fichiers qu'on ne trouve nulle part ailleurs. Des archives oubliées, des vieux logiciels, des trucs que personne n'a jamais re-uploadé nulle part. C'est un peu le grenier d'Internet, poussiéreux mais plein de trésors pour qui sait chercher et plein de malwares aussi, alors gaffe à vous !</p>
<p>Attention quand même, ça reste un client P2P pour le réseau ed2k donc les précautions habituelles s'appliquent. Vérifiez ce que vous téléchargez, et n'oubliez pas que l'Arcom (ex-Hadopi) veille toujours au grain.</p>
<p>Bref, si vous avez la nostalgie du petit âne et que vous êtes sur Mac, c'est par là !</p>
<p>Merci à Martin pour la découverte !</p>