---
title: "ClamUI - Enfin un antivirus graphique sous Linux"
author: "Korben"
date: 2026-03-18T15:47:30.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "linux-open-source/logiciels-libres"
  - "antivirus"
rss_source: Blog
url: https://korben.info/clamui-antivirus-linux-gui.html
note: 0
seen: false
---

<p><strong>ClamAV</strong>, tout le monde connaît. C'est le moteur antivirus open source qui tourne sur à peu près tous les serveurs mail de la planète. Sauf que côté bureau Linux, à part ClamTk qui commence à dater, les options pour le piloter avec une interface graphique sont plutôt limitées.</p>
<p>Heureusement,
<a href="https://github.com/linx-systems/clamui">ClamUI</a>
vient corriger le tir avec une vraie application desktop qui se présente comme une interface GNOME native bien léchée pour scanner vos fichiers, gérer la quarantaine et garder un oeil sur la sécurité de votre bécane. Un petit</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">flatpak install flathub io.github.linx_systems.ClamUI
</span></span></code></pre><p>...et c'est réglé !</p>
<p>Bon, vous allez me dire &quot;<em>Un antivirus sous Linux, pour quoi faire ? Moi j'ai une vraie barbe, je bois de la chouffe cul-sec et suffit de pas installer n'importe quoi, c'est tout !!! Linux ça se mérite les moldus !</em>&quot; tout en embrassant vos biceps ramollis ^^.</p>
<p>Mais vous oubliez que si vous partagez des fichiers avec des machines Windows, si vous gérez un serveur de mails ou un NAS familial, scanner ce qui transite c'est pas du luxe. Et ClamUI rend la chose carrément accessible, là où avant fallait jongler avec des outils en ligne de commande comme ceux qu'on trouve dans les
<a href="https://korben.info/analyse-de-malwares.html">distributions d'analyse de malwares</a>
.</p>
<p>Côté fonctionnalités, c'est d'ailleurs plutôt complet ! L'appli détecte automatiquement les clés USB et disques externes quand vous les branchez, et peut les scanner direct sans que vous leviez le petit doigt (un peu comme
<a href="https://korben.info/nettoyeur-cle-usb.html">CIRCLean sur Raspberry Pi</a>
, mais sans le matériel dédié). Y'a aussi l'intégration VirusTotal pour les fichiers véritablement louches, du coup vous pouvez croiser les résultats avec une soixantaine de moteurs de détection en un clic.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/clamui-antivirus-linux-gui/clamui-antivirus-linux-gui-2.png" alt="" loading="lazy" decoding="async">
<p>Une chose bien pensée aussi, c'est l'intégration dans les gestionnaires de fichiers comme Nautilus, Dolphin, Nemo... un clic droit sur n'importe quel répertoire et vous lancez un scan. Ça s'installe également dans le system tray avec des notifications en temps réel, genre &quot;scan terminé, zéro menace détectée&quot; ou &quot;attention, fichier suspect déplacé en quarantaine&quot;.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/clamui-antivirus-linux-gui/clamui-antivirus-linux-gui-3.png" alt="" loading="lazy" decoding="async">
<p>Pour les bidouilleurs, ClamUI propose deux backends au choix, c'est à dire soit le daemon clamd, plutôt que clamscan en direct, parce que clamd garde les signatures en mémoire et scanne beaucoup plus vite. Mais si vous voulez pas d'un service qui tourne en permanence, clamscan fait le job. Vous pouvez aussi programmer des scans automatiques via systemd ou cron, donc même un vieux serveur Debian peut tourner en pilote automatique.</p>
<p>Y'a aussi une CLI complète derrière l'interface graphique, idéale pour l'intégrer à vos scripts. <code>clamui scan</code>, <code>clamui quarantine</code>, <code>clamui profile</code>, <code>clamui status</code>... tout sort en JSON si vous voulez scripter le truc. Les codes retour sont d'ailleurs très propres : 0 si c'est clean, 1 si y'a des menaces, 2 si erreur. &quot;Èzé&quot; comme dirait Booba ! De quoi intégrer ça dans un pipeline de vérification maison sans se prendre la tête !</p>
<p>Le projet est sous licence MIT, tourne avec Python 3.11+ et les sources sont
<a href="https://github.com/linx-systems/clamui">sur GitHub</a>
.</p>
<p>Merci à Lorenper pour la découverte !</p>