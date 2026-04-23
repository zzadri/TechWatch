---
title: "MultiDrive - Du clonage de disque gratuit par les pros du forensic"
author: "Korben"
date: 2026-02-25T08:21:13.000Z
type: site
subject:
category: IT Global
tags:
  - "tutoriels-guides"
  - "windows/logiciels-windows"
  - "backup"
  - "clonage de disque"
  - "clonage disque dur"
rss_source: Blog
url: https://korben.info/multidrive-clonage-disque-gratuit.html
note: 0
seen: false
---

<p><strong>MultiDrive</strong>, c'est un outil Windows gratuit pour cloner, sauvegarder et effacer vos disques. Jusque-là, rien de foufou... sauf que derrière, y'a Atola Technology. Et dans le monde du forensic numérique, Atola c'est pas n'importe qui (labos d'investigation, forces de l'ordre, 20 ans de métier, basés au Canada avec une équipe en Ukraine)... bref, ce sont des gens qui connaissent les disques durs sur le bout des doigts.</p>
<p>Du coup, quand ils sortent un outil gratuit pour le grand public, je tends forcement l'oreille.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/multidrive-clonage-disque-gratuit/multidrive-clonage-disque-gratuit-2.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>Côté fonctionnalités, vous avez donc le
<a href="https://korben.info/diskcopy-cloner-disque-dur.html">clonage disque-à-disque</a>
(HDD vers SSD, tout ça), y compris le disque boot (pratique pour migrer votre Windows vers un SSD), la sauvegarde complète en ZIP ou RAW, et l'effacement sécurisé avec patterns HEX ainsi que de la vérification d'intégrité en MD5, SHA256, SHA512... bref, y'a ce qu'il faut. Mais le gros plus pour les admins, c'est le mode CLI via <code>mdcli</code>. Comme ça, hop, vous scriptez vos backups et ça tourne tout seul !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/multidrive-clonage-disque-gratuit/multidrive-clonage-disque-gratuit-3.jpeg" alt="" loading="lazy" decoding="async">
</p>
<p>En gros, ça donne ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl"># Lister les disques connectés
</span></span><span class="line"><span class="cl">mdcli list
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Sauvegarder un disque boot en ZIP compressé
</span></span><span class="line"><span class="cl">mdcli backup d1 E:\myfolder\backup.zip
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Cloner un disque vers un autre avec checksum SHA1
</span></span><span class="line"><span class="cl">mdcli clone d3 d4 -q SHA1
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Effacer un disque avec un pattern HEX perso
</span></span><span class="line"><span class="cl">mdcli erase d2 -p BADA
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"># Restaurer un disque depuis un backup ZIP
</span></span><span class="line"><span class="cl">mdcli restore E:\folder\backup.zip d3
</span></span></code></pre><p>Et les tâches peuvent tourner en parallèle comme ça, vous lancez PLUSIEURS clonages en même temps, chacun avec son propre bouton pause/reprise. Et si votre vieux disque a des secteurs morts, MultiDrive s'en fiche puisqu'il gère les erreurs de lecture et continue sans broncher. Pour ceux qui connaissent
<a href="https://korben.info/rescuezilla.html">Rescuezilla</a>
, c'est un peu la même philosophie mais natif Windows, SANS clé USB bootable.</p>
<div class="video-container" id="video-container-multidrive-clonage-disque-gratuit-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/multidrive-clonage-disque-gratuit/multidrive-clonage-disque-gratuit-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/multidrive-clonage-disque-gratuit/multidrive-clonage-disque-gratuit-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Après, c'est closed-source mais c'est 100% gratuit (même en usage pro), et Atola s'engage à garder ça gratos. On verra s'ils respectent leur parole... quoiqu'il en soit, la
<a href="https://multidrive.io/terms">licence est consultable</a>
sur leur site si vous voulez creuser avant d'aller plus loin.</p>
<p>Et côté doc, ils ont des tutos pour à peu près tout : backup sur disque externe, migration de Windows vers un autre disque, clonage SSD vers SSD, wipe de clé USB... chaque opération est détaillée étape par étape, c'est bien ficlé.</p>
<p>À
<a href="https://multidrive.io/download">télécharger ici</a>
ou via <code>winget install multidrive</code>.</p>