---
title: "OneDrive ou pourquoi tout le monde déteste le cloud de Microsoft ?"
author: "Korben"
date: 2026-01-08T08:40:17.000Z
type: site
subject:
category: IT Global
tags:
  - "vie-privee-anonymat"
  - "windows/astuces-windows"
rss_source: Blog
url: https://korben.info/onedrive-microsoft-dark-pattern-alternatives.html
note: 0
seen: false
---

<h2 id="is_partnership-false">� vous les aviez laissées&quot;]
is_partnership: false</h2>
<p>Besoin de vous faire une petite frayeur ? Oui, je sais y'a déjà Poutine, Trump, Macron et compagnie et on n'a vraiment pas besoin de se faire baliser plus... mais quand même, j'ai ce qu'il vous faut... Pour tester votre niveau de résilience et de résistance au stress, essayez donc un peu de <strong>désactiver la sauvegarde OneDrive sur votre PC Windows</strong>.</p>
<p>Parce que si vous avez installé Windows 10 ou 11 récemment, vous avez sûrement remarqué cette petite icône de nuage toute moche qui squatte votre barre des tâches. C'est ✨ <strong>OneDrive</strong> ✨, le service de stockage de Microsoft. Et le moins qu'on puisse dire, c'est qu'il est encore plus pot de colle que vous avec votre collègue Samantha.</p>
<p>Hé oui, comme le raconte
<a href="https://www.tiktok.com/@jasonkpargin/video/7591592052954025246">Jason Pargin</a>
, Microsoft a mis en place ce qu'on appelle un joli &quot;<strong>dark pattern</strong>&quot;. Vous savez, ces interfaces conçues pour vous piéger ou vous forcer la main.</p>
<p>L'arnaque est simple... Lors de la configuration ou après une mise à jour, Windows peut vous proposer avec beaucoup d'insistance d'activer la ✨<strong>Sauvegarde OneDrive</strong>✨. Ça sonne bien, non ?</p>
<p>Sauf que ce que ça fait réellement, c'est <strong>déplacer</strong> vos fichiers (Documents, Images, Bureau) vers le dossier OneDrive local pour les synchroniser. Cela veut dire qu'ils ne sont plus &quot;chez vous&quot; à l'emplacement habituel, mais qu'ils sont dans le dossier OneDrive (et donc sur les serveurs de Microsoft).</p>
<p>Du coup, c'est rapidement le drame quand vous décidez que non, finalement, vous ne voulez pas que vos photos de vacances soient sur les serveurs de Redmond, et que vous désactivez la sauvegarde... <strong>POUF PIF PAF POUF !</strong> A ce moment là, vos fichiers ne sont plus visibles à leur emplacement d'origine. Ils restent certes dans le dossier OneDrive quelque part dans le cloud, mais le dossier d'origine, lui, est vide.</p>
<p>Ce genre de comportement peut faire penser à un ransomware pour un néophyte, sauf que c'est une vraie &quot;fonctionnalité&quot; officielle. Vos fichiers sont toujours dans le dossier OneDrive, mais ils ont été dégagé de vos dossiers locaux standards. Et si vous essayez de supprimer les fichiers du cloud pour faire le ménage, c'est encore pire car la synchro bidirectionnelle risque de les effacer aussi de votre disque dur si vous ne faites pas gaffe (pensez à vérifier la corbeille OneDrive si ça vous arrive). Bref, c'est infernal et même si je n'utilise pas OneDrive, dites vous que j'ai déjà eu le même genre de déconvenues avec iCloud... Donc bon, c'est pas quelque chose non plus réservée uniquement à Microsoft.</p>
<h2 id="alors-comment-reprendre-le-contrôle-sans-tout-casser-">Alors comment reprendre le contrôle sans tout casser ?</h2>
<p>Si vous voulez vous débarrasser de cette sangsue sans perdre vos données, il ne faut pas y aller à la hache.</p>
<ol>
<li>Ouvrez les <strong>Paramètres</strong> de OneDrive (clic droit sur le nuage).</li>
<li>Allez dans l'onglet <strong>Sauvegarde</strong> (ou &quot;Sync and backup&quot;).</li>
<li>Cliquez sur <strong>Gérer la sauvegarde</strong>.</li>
<li>Désactivez les dossiers (Documents, Images, Bureau).</li>
<li><strong>Important</strong> : Vos fichiers ne reviendront pas tout seuls à leur place. Vous devrez aller les chercher manuellement dans votre dossier OneDrive local (généralement <code>C:\Users\VotreNom\OneDrive</code>) et les remettre dans vos dossiers locaux.</li>
</ol>
<p>Si ça vous emmerde vraiment (et je vous comprends), j'avais déjà expliqué en détail
<a href="https://korben.info/windows-10-comment-desactiver-onedrive.html">comment désactiver totalement OneDrive sous Windows 10</a>
. La méthode reste globalement la même pour Windows 11.</p>
<h2 id="les-vraies-alternatives-existent-">Les vraies alternatives existent !</h2>
<p>Maintenant que vous avez repris la main, par quoi on remplace ça ? Parce que la synchro, c'est quand même pratique.</p>
<p>Alors si vous cherchez une alternative respectueuse de votre vie privée, oubliez Google Drive et compagnie mais regardez plutôt du côté de
<a href="https://nextcloud.com/fr/">Nextcloud</a>
. C'est LA référence open source que vous pouvez
<a href="https://korben.info/nextcloud-raspberry.html">héberger vous-même sur un petit serveur (ou un NAS ou un Raspberry Pi)</a>
ou passer par un hébergeur éthique. Y'a même des
<a href="https://www.hanssonit.se/nextcloud-vm/">VM de Nextcloud ici</a>
ou une
<a href="https://github.com/nextcloud/all-in-one">version Docker ici</a>
... Merci à Mr Magpie et Bami !</p>
<p>Et d'ailleurs, pour ceux qui veulent du clé en main français, jetez un œil à
<a href="https://korben.info/sync-in-alternative-francaise-nextcloud-dechire.html">Sync-in, une excellente alternative basée sur Nextcloud</a>
dont je vous ai déjà parlé.</p>
<p>Pour ceux qui veulent juste de la synchro entre machines sans stocker ça sur un serveur tiers (&quot;<em>le cloud, c'est l'ordinateur de quelqu'un d'autre</em>&quot;, rappelez-vous),
<a href="https://syncthing.net">Syncthing</a>
est une merveille. C'est du pair-à-pair avec connexions chiffrées (TLS), rapide, et ça marche du feu de dieu.</p>
<p>Enfin, si vous voulez du stockage cloud chiffré de bout en bout sans vous prendre la tête avec l'hébergement,
<a href="https://proton.me/drive">Proton Drive</a>
(par les créateurs de ProtonMail) est une solution solide, même si l'offre gratuite est un peu limitée en espace.</p>
<p>Bref, ne laissez pas Microsoft décider où doivent vivre vos fichiers. C'est votre machine, ce sont vos données.</p>
<p>Allez, enjoy (et faites des backups, des vrais) !</p>
<p>[Source](
<a href="https://it.slashdot.org/story/26/01/07/152242/everyone-hates-onedrive-micros">https://it.slashdot.org/story/26/01/07/152242/everyone-hates-onedrive-micros</a>
</p>