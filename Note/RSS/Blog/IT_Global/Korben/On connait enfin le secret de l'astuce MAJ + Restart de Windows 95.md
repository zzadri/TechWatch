---
title: "On connait enfin le secret de l'astuce MAJ + Restart de Windows 95"
author: "Korben"
date: 2026-01-20T16:55:53.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/retrogaming-emulation"
  - "windows/astuces-windows"
rss_source: Blog
url: https://korben.info/windows-95-shift-restart-secret.html
note: 0
seen: false
---

<p>Le lancement de Windows 95, c'est un sacré souvenir pour moi... J'avais suivi ça de très près et j'en rêvait la nuit ^^. Puis cette musique &quot;Start Me Up&quot; des Rolling Stones, quel kiff ! C'était le futur, c'était fou fou ! Mais est-ce que vous vous souvenez de cette petite astuce de ninja qui permettait de redémarrer cet OS aussi vite qu'une baston dans un bar du 62 ???</p>
<p>J'suis sûr que non, mais moi je m'en souviens. En fait, il fallait maintenir la touche <strong>MAJ</strong> enfoncée en cliquant sur &quot;Redémarrer&quot;, et hop, au lieu de se taper tout le cirque du BIOS, Windows se relançait presque instantanément.</p>
<p>Et magie magie, le secret de cette sauce vient d'être raconté par l'inoxydable Raymond Chen, vétéran de chez Microsoft, et vous allez voir, c'est chouette !</p>
<p>En fait quand vous faisiez ce MAJ+Redémarrer, Windows envoyait un petit &quot;flag&quot; spécial baptisé <code>EW_RESTARTWINDOWS</code> au kernel 16 bits, comme ça au lieu de dire à la machine de faire un &quot;cold boot&quot; (un redémarrage à froid quoi..), le système fermait gentiment le kernel et le gestionnaire de mémoire virtuelle avant de faire redescendre le CPU en <strong>mode réel</strong>.</p>
<p>Et c'est là que le fameux <code>win.com</code> reprenait la main puisqu'en recevant ce signal, ça lui disait : &quot;<em>Hey gros, on ne s'arrête pas, on repart pour un tour !</em>&quot;.</p>
<p><code>win.com</code> essayait alors de remettre le système dans un état clean, comme s'il venait d'être lancé, sauf que pour relancer Windows en mode protégé, il fallait un gros bloc de mémoire contigu. Malheureusement, si vos logiciels avaient mis trop de bazar et fragmenté la RAM, l'astuce foirait et le PC finissait par faire un vrai reboot complet. Pas cool Raoul !</p>
<p>Par contre, si y'avait assez de mémoire contigu libre alors <code>win.com</code> relançait le VMM (Virtual Machine Manager) et l'interface graphique pouvait repartir sans repasser par la case départ. Un vrai exploit de champion quoi ! C'était pour l'époque une bidouille de génie car chaque seconde gagnée sur le chargement de l'OS était une grande victoire contre l'ennui !!</p>
<p>Chouette comme anecdote non ? Et si vous voulez
<a href="https://korben.info/testez-windows-95-dans-votre-navigateur-version-dosbox-compilee-en-javascript.html">croquer encore plus de madeleines</a>
et tester ça vous-même, y'a des outils comme
<a href="https://korben.info/emuos-hub-communautaire-vieux-softs.html">EmuOS</a>
qui simulent tout ça très bien. Et pour les puristes, vous monter un petit
<a href="https://korben.info/dosbian-dos-raspberry-pi.html">Dosbian sur Raspberry Pi</a>
reste la base pour bidouiller de vieux kernels.</p>
<p>Bref, même trente ans après, ces entrailles pourries de nos vieux OS recèlent encore de plein de petits secrets passionnants !</p>
<p>
<a href="https://devblogs.microsoft.com/oldnewthing/20260119-06/?p=111995">Source</a>
��</p>