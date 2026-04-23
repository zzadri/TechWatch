---
title: "Windows 11 KB5074109 - La MAJ qui ruine vos sessions gaming Nvidia"
author: "Korben"
date: 2026-02-05T20:16:52.000Z
type: site
subject:
category: IT Global
tags:
  - "jeux-video/pc-gaming"
  - "windows/astuces-windows"
  - "bug"
  - "Nvidia"
  - "Windows Update"
rss_source: Blog
url: https://korben.info/windows-11-kb5074109-nvidia-framerate-gaming.html
note: 0
seen: false
---

<p>Si vous êtes gamer sous Windows 11 avec une carte <strong>Nvidia</strong>, lisez bien ce qui suit avant de cliquer sur &quot;<em>Mettre à jour</em>&quot;.</p>
<p>Parce que la mise à jour de janvier 2026 (KB5074109) est en train de foutre un bordel monstre sur les PC gaming équipés de GPU Nvidia. Chutes de framerate de 15 à 20 FPS, artefacts visuels qui apparaissent en plein milieu de vos parties, écrans noirs... bref, le package complet pour ruiner votre soirée gaming. Et apparemment, le problème est suffisamment répandu pour que Nvidia réagisse officiellement.</p>
<p>En effet, un représentant Nvidia a confirmé sur les forums GeForce que l'équipe était au courant. Sa recommandation est claire : <strong>Il faut désinstaller KB5074109 en attendant un correctif</strong>. Bon après, vous pourriez tenter de juste mettre à jour vos drivers Nvidia plutôt que de désinstaller le patch... sauf que non, j'ai regardé, ça change rien. Le problème vient bien du côté Windows, pas des drivers GPU.</p>
<p>Les symptômes sont variés et touchent autant les configs modestes que les gros setups. Des joueurs rapportent des rectangles de couleur qui apparaissent dans Forza Horizon 5, d'autres voient leur bureau se réinitialiser ou leur explorateur Windows planter en boucle. Du coup, même en dehors des jeux, c'est la fête. Pour info, le patch concerne Windows 11 en versions 25H2 et 24H2 (builds 26200.7623 et 26100.7623).</p>
<p>Pour désinstaller cette MAJ et retrouver vos performances, direction <em>Paramètres &gt; Windows Update &gt; Historique des mises à jour</em>. Tout en bas, vous avez &quot;<em>Désinstaller des mises à jour</em>&quot;. Cherchez KB5074109 dans la liste, cliquez sur <em>Désinstaller</em>, et redémarrez. Attention par contre, si vous avez Windows Update configuré en mode automatique (et c'est le cas par défaut hein...), pensez à mettre en pause les MAJ pendant 7 jours histoire que le patch se réinstalle pas dans votre dos. Après ça, vos FPS devraient revenir à la normale direct.</p>
<p>Microsoft a sorti un patch optionnel (KB5074105) qui corrige les écrans noirs dans certains cas. Sauf que pour les artefacts en jeu et les chutes de performances, ça ne fonctionne toujours pas. Et si vous avez activé
<a href="https://korben.info/gpu-scheduling-nvidia-amd.html">la planification GPU matérielle</a>
, essayez de la désactiver temporairement. C'est pas garanti, mais certains utilisateurs disent que ça réduit les artefacts... au prix d'un poil de latence en plus. À vous de voir si le compromis vaut le coup en attendant le vrai fix.</p>
<p>Et voilà comment en 2026, Microsoft continue de balancer des mises à jour de sécurité yolo qui font tout pêter ! On avait déjà eu
<a href="https://korben.info/nvidia-app-baisse-performances-jeux-solution.html">le coup de la NVIDIA App qui faisait chuter les perfs jusqu'à 15%</a>
y'a pas si longtemps, et maintenant c'est carrément Windows Update qui s'y met.</p>
<p>Bref, si vous êtes touché, désinstallez le patch pour profiter pleine balle de vos jeux en attendant que Microsoft et Nvidia règlent leurs affaires. Par contre si tout roule chez vous, gardez-le... c'est quand même un patch de sécuritén, hein ^^.</p>
<p>
<a href="https://www.tomshardware.com/software/windows/yet-another-windows-update-is-wreaking-havoc-on-gaming-rigs-worldwide-nvidia-recommends-uninstalling-windows-11-kb5074109-january-update-to-prevent-framerate-drops-and-artifacting">Source</a>
</p>