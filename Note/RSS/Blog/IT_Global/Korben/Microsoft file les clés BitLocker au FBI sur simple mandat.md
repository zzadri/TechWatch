---
title: "Microsoft file les clés BitLocker au FBI sur simple mandat"
author: "Korben"
date: 2026-01-24T00:03:10.000Z
type: site
subject:
category: IT Global
tags:
  - "vie-privee-anonymat/chiffrement"
  - "vie-privee-anonymat/surveillance-tracking"
  - "Bitlocker"
  - "chiffrement"
  - "FBI"
rss_source: Blog
url: https://korben.info/microsoft-bitlocker-fbi-cles.html
note: 0
seen: false
---

<p>Microsoft vient de confirmer qu'ils filent les clés de chiffrement BitLocker au FBI quand celui-ci débarque avec un mandat. Et même si on s'en doutait fooort, c'est
<a href="https://www.forbes.com/sites/thomasbrewster/2026/01/22/microsoft-gave-fbi-keys-to-unlock-bitlocker-encrypted-data/">la première fois</a>
qu'on a la preuve que ça arrive vraiment.</p>
<p>L'affaire s'est passée à Guam (une île américaine dans le Pacifique), où des agents fédéraux enquêtaient sur une histoire de fraude. Ils avaient besoin d'accéder aux ordis de suspects, sauf que les disques étaient chiffrés avec
<a href="https://korben.info/bitlocker-detourne-nouvelle-technique-mouvement-lateral.html">l'outil BitLocker</a>
, le chiffrement intégré à Windows. Du coup, ni une ni deux, le FBI a envoyé un mandat à Microsoft pour récupérer les clés de récupération stockées dans le cloud.</p>
<p>Et Microsoft a dit oui, bien sûr, voilà les clés, servez-vous, c'est cadeau !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/microsoft-bitlocker-fbi-cles/microsoft-bitlocker-fbi-cles-2.png" alt="" loading="lazy" decoding="async">
<p>Le truc, c'est que par défaut, quand vous activez BitLocker sur un PC avec un compte Microsoft, Windows envoie automatiquement une copie de votre clé de récupération sur les serveurs de Redmond. C'est présenté comme une fonctionnalité pratique, genre &quot;<em>au cas où vous oubliez votre mot de passe</em>&quot;. Sauf que du coup, Microsoft a accès à vos clés.</p>
<p>Et si Microsoft a accès, le gouvernement aussi.</p>
<p>Côté Apple, c'est une autre histoire. J'sais pas si vous vous souvenez de l'affaire de
<a href="https://korben.info/graykey-outil-deblocage-iphone-securite.html">San Bernardino</a>
en 2016 mais le FBI avait demandé à Apple de créer un firmware spécial pour désactiver les protections anti-bruteforce de l'iPhone d'un terroriste. Tim Cook avait dit non. Pas parce qu'Apple ne pouvait pas techniquement le faire, mais parce que créer cet outil aurait ouvert une brèche pour tout le monde.</p>
<p>Microsoft, eux, ont fait le choix inverse. Leur architecture
<a href="https://www.theregister.com/2026/01/23/surrender_as_a_service_microsoft/">permet explicitement</a>
de conserver une copie des clés côté serveur. Alors oui, c'est pratique si vous perdez votre mot de passe, mais c'est aussi une porte d'entrée pour quiconque a un mandat... ou autre chose.</p>
<p>Microsoft dit recevoir environ 20 requêtes par an pour des clés BitLocker, et qu'ils ne peuvent pas toujours y répondre, genre quand l'utilisateur n'a pas activé la sauvegarde cloud.</p>
<p>On s'en serait douté...</p>
<p>Bref, si vous utilisez BitLocker et que vous tenez vraiment à ce que vos données restent privées, désactivez la sauvegarde automatique de la clé sur le compte Microsoft.</p>
<p>Concrètement, pour cela vous avez deux options : <strong>utiliser un compte local</strong> au lieu d'un compte Microsoft (la clé ne sera jamais envoyée dans le cloud), ou si vous êtes sur Windows Pro/Enterprise, <strong>passer par les stratégies de groupe</strong> (<em>gpedit.msc → Configuration ordinateur → Modèles d'administration → Composants Windows → Chiffrement de lecteur BitLocker</em>) pour forcer la sauvegarde locale uniquement.</p>
<p>Autrement, vous pouvez aussi simplement sauvegarder votre clé sur une clé USB ou l'imprimer. C'est moins pratique, mais au moins elle reste chez vous.</p>
<p>
<a href="https://www.forbes.com/sites/thomasbrewster/2026/01/22/microsoft-gave-fbi-keys-to-unlock-bitlocker-encrypted-data/">Source</a>
</p>