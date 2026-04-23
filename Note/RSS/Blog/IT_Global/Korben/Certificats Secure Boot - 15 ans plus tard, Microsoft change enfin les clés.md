---
title: "Certificats Secure Boot - 15 ans plus tard, Microsoft change enfin les clés"
author: "Korben"
date: 2026-02-11T09:12:42.000Z
type: site
subject:
category: IT Global
tags:
  - "windows/astuces-windows"
  - "windows/securite-windows"
  - "certificat"
  - "certificat racine"
  - "Secure Boot"
  - "Windows Update"
rss_source: Blog
url: https://korben.info/microsoft-secure-boot-certificats-2026.html
note: 0
seen: false
---

<p>Quinze ans que les mêmes certificats <strong>Secure Boot</strong> tournent sur tous les PC Windows de la planète. Et Microsoft n'en avait jamais changé les clés depuis 2011. Alors là on est donc sur un moment historique puisque c'est la première rotation de l'histoire. Autant dire que ça va piquer un peu pour ceux qui n'ont pas fait leurs mises à jour.</p>
<p>Ces certificats UEFI, ce sont eux qui vérifient que votre machine démarre bien avec un système d'exploitation légitime et pas un malware planqué dans le firmware.</p>
<p>Microsoft a donc
<a href="https://blogs.windows.com/windowsexperience/2026/02/10/refreshing-the-root-of-trust-industry-collaboration-on-secure-boot-certificate-updates/">commencé à déployer</a>
de nouveaux certificats via Windows Update, avec sa mise à jour KB5074109 de janvier. Si vous êtes sous Windows 11, normalement c'est transparent, ça va se faire tout seul en arrière-plan. Les constructeurs comme Dell, HP et Lenovo ont également bossé de leur côté pour mettre à jour le firmware de leurs machines.</p>
<p>Après le hic, c'est la deadline qui est pour fin juin 2026. C'est à cette date que les anciens certificats expirent. Et là, les machines qui n'auront pas reçu les nouveaux vont se retrouver dans ce que Microsoft appelle un &quot;<em>état de sécurité dégradé</em>&quot;. En gros, le démarrage sécurisé continuera de fonctionner, mais avec des clés périmées...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/microsoft-secure-boot-certificats-2026/microsoft-secure-boot-certificats-2026-2.png" alt="" loading="lazy" decoding="async">
<p>Pour ceux qui ont acheté un PC en 2024 ou après, pas de panique, les nouveaux certificats &quot;Windows UEFI CA 2023&quot; sont déjà intégrés dans le firmware. Mais si vous avez une machine plus ancienne, là faudra aller dans Paramètres &gt; Windows Update et vérifier manuellement que tout est bien passé.</p>
<p>Et pour
<a href="https://korben.info/bootkitty-premier-bootkit-linux-demasque-recherche.html">les amateurs de bootkits en tout genre</a>
, bonne nouvelle... la base de données DBX (celle qui blackliste les signatures compromises) est aussi mise à jour dans la foulée.</p>
<p>Mais attention, si vous êtes encore sous Windows 10, c'est là que ça se corse. En effet, Microsoft ne fournira les nouveaux certificats qu'aux utilisateurs qui ont souscrit le programme ESU (Extended Security Updates)... qui est payant. Du coup, tous les PC sous Windows 10 sans ESU vont rester avec les vieilles clés.</p>
<p>Je sens que vous êtes content ^^.</p>
<p>Pour vérifier votre situation, ouvrez donc PowerShell en admin et tapez <code>Confirm-SecureBootUEFI</code>. Si ça renvoie &quot;True&quot;, c'est bon. Si ça renvoie &quot;False&quot; ou que ça ne marche pas, c'est que votre BIOS n'a peut-être jamais activé le Secure Boot. Ensuite, vérifiez dans Windows Update que la KB5074109 est bien installée. Après sur du matériel d'entreprise, votre admin sys a probablement déjà géré le truc (enfin j'espère).</p>
<p>Si KB5074109 est bien passée vous pouvez dormir tranquille.</p>
<p>Enfin... jusqu'à la prochaine faille. Niark niark !</p>
<p>
<a href="https://blogs.windows.com/windowsexperience/2026/02/10/refreshing-the-root-of-trust-industry-collaboration-on-secure-boot-certificate-updates/">Source</a>
</p>