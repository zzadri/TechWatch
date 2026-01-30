---
title: "Plus de son sur Plex ? Pas de panique, voici le fix !"
author: "Korben"
date: 2026-01-16T05:22:19.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture/streaming-video"
  - "windows/astuces-windows"
  - "codec"
  - "Plex"
  - "Windows 11"
  - "Windows 11 24H2"
rss_source: Blog
url: https://korben.info/reparer-son-plex-windows-11-eac3.html
note: 0
seen: false
---

<p>Si vous avez récemment fait une mise à jour vers <strong>Windows 11 24H2</strong> et que vous êtes un utilisateur assidu de <strong>Plex</strong>, vous avez peut-être remarqué un truc étrange. L'image est nickel, tout se lance parfaitement, mais niveau son... c'est le silence radio absolu.</p>
<p>En particulier si vous tentez de lire des médias avec une piste audio <strong>EAC3 (Dolby Digital Plus)</strong> en 5.1. Vous avez beau monter le volume, vérifier vos câbles ou insulter votre carte son, rien n'y fait. Y'a que dalle...</p>
<p>Alors pas de panique les amis ! Ce n'est pas votre matériel qui est en cause, ni même Plex qui a décidé de bouder. C'est juste Microsoft qui, dans sa grande sagesse (et probablement pour des histoires de licences), a semble-t-il retiré ou cassé la gestion native du codec EAC3 dans cette version de Windows. Un grand classique qui me rappelle l'époque où
<a href="https://korben.info/windows-8-il-sera-impossible-de-lire-des-dvd-mouhahaha.html">Windows 8 avait viré la lecture DVD</a>
sans prévenir.</p>
<p>Heureusement, <strong>Andréa</strong>, un fidèle lecteur (merci à lui !), a creusé le sujet et nous partage la solution pour remettre tout ça d'équerre sans avoir besoin de formater ou de passer sous Linux (même si, entre nous, ce serait une excellente idée ^^).</p>
<h3 id="ce-quil-vous-faut">Ce qu'il vous faut</h3>
<ul>
<li>Un PC sous Windows 11 (version 24H2)</li>
<li>Le pack &quot;Dolby AC-3 / AC-4 Installer&quot; (voir plus bas)</li>
<li>5 minutes devant vous</li>
</ul>
<h3 id="la-solution-miracle">La solution miracle</h3>
<p>Pour corriger ce problème, il faut réinjecter les DLL manquantes dans le système. Et pour ça, un petit utilitaire bien pratique existe sur MajorGeeks.</p>
<ol>
<li>Allez récupérer le <strong>Dolby AC-3 / AC-4 Installer</strong>
<a href="https://www.majorgeeks.com/files/details/dolby_ac_3ac_4_installer.html">disponible ici sur MajorGeeks</a>
.</li>
<li>Lancez l'installation. Ça va remettre les fichiers nécessaires dans <code>System32</code> comme au bon vieux temps.</li>
<li><strong>Redémarrez votre PC</strong>. C'est Windows, ne posez pas de questions ;) .</li>
</ol>
<p>Une fois que la bête a redémarré, ouvrez votre client Plex.</p>
<p>Allez dans les paramètres Lecteur et assurez-vous d'être en &quot;Réglages de base&quot; (5.1 ou Stéréo) et surtout, <strong>désactivez le Passthrough</strong> si ce n'est pas indispensable pour votre ampli. Normalement, le son devrait revenir instantanément.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/reparer-son-plex-windows-11-eac3/reparer-son-plex-windows-11-eac3-2.png" alt="" loading="lazy" decoding="async">
<p>C'est quand même dingue qu'en 2026 on doive encore bidouiller des codecs à la main pour avoir du son, mais bon... Au moins, c'est réparable.</p>
<p>Voilà, si ça vous a sauvé la soirée film, n'hésitez pas à remercier Andréa qui a tout détaillé
<a href="https://plextuto.wixstudio.com/accueil/blog/r%C3%A9parer-le-son-%28eac3%29-sur-plex-pour-windows-11">sur son tuto complet ici</a>
.</p>
<p>Et pensez aussi à garder votre
<a href="https://korben.info/plex-media-server-mise-jour-securite-urgente.html">Plex Media Server à jour</a>
, c'est important pour la sécurité (même si ça ne règle pas les soucis de codecs Windows !).</p>