---
title: "ShareMyLogin - Partagez vos accès sans filer vos mots de passe"
author: "Korben"
date: 2026-01-29T14:48:14.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "vie-privee-anonymat/gestionnaires-mots-de-passe"
  - "ANSSI"
  - "mot de passe"
  - "open source"
  - "sécurité"
rss_source: Blog
url: https://korben.info/sharemylogin-partagez-vos-acces-sans-filer-vos-mots-de-passe.html
note: 0
seen: false
---

<p>Vous avez sûrement déjà eu ce moment de solitude où vous devez filer le mot de passe du WiFi, de Netflix ou d'un compte commun à un pote. Et là, comme un mec bourré qui recontacte son ex après une soirée déprimante, <strong>vous finissez par l'envoyer par SMS</strong> ou l'écrire sur un bout de papier qui finira à la poubelle.</p>
<p>C'est le genre de truc qui rend dingue niveau sécurité, mais bon, dans la vraie vie on le fait tous !</p>
<p>Au début, je cherchais donc juste un moyen simple de faire ça proprement, et je suis tombé sur <strong>ShareMyLogin</strong>. C'est un petit outil open source très bien pensé qui permet de partager des identifiants (ou n'importe quel secret) via un lien unique, en chiffrant tout directement dans votre navigateur (<strong>Chrome, Firefox, peu importe</strong>).</p>
<p>Le principe vous le connaissez, c'est du <strong>Zero Knowledge</strong>. Du coup, comme le chiffrement se fait localement avant l'envoi, le serveur ne reçoit techniquement que des données illisibles. C'est dans l'esprit de ce que proposent des services comme Bitwarden Send ou
<a href="https://korben.info/lockself-locktransfer-lockfiles-securite-fichiers-entreprise.html">LockTransfer pour les pros</a>
, mais ici sous forme d'un petit outil dédié et gratuit.</p>
<p>Côté technique, on retrouve donc bien de l'<strong>AES-256-GCM</strong> pour le chiffrement et du <strong>PBKDF2</strong> (avec 250 000 itérations) pour la dérivation de clé. Concrètement, vous tapez votre secret, l'outil génère un lien, et hop, vous filez ce lien à votre destinataire.</p>
<p>Ce qui est cool, c'est que le code est disponible sur
<a href="https://github.com/elandio-com/sharemylogin">GitHub</a>
. Je vous invite d'ailleurs à aller jeter un oeil à <code>encrypt.ts</code> et <code>decrypt.ts</code> qui montrent bien que la crypto est gérée côté client. Après, si vous utilisez la version hébergée, vous devrez faire confiance à l'administrateur pour qu'il ne modifie pas le code à la volée. Mais <strong>si vous hébergez votre propre instance</strong>, ce qui est franchement conseillé si vous êtes à cheval sur la sécu, c'est top !</p>
<p>Bien sûr pour le partage de mots de passe critiques au quotidien, je vous recommande d'utiliser les fonctions de partage de votre gestionnaire de mots de passe habituel. Mais pour un dépannage ponctuel, genre filer le code du digicode à un livreur ou un accès temporaire, ShareMyLogin fera très bien le job.</p>
<p>Le projet propose aussi une API si vous voulez intégrer ça dans vos propres moulinettes.</p>
<p>
<a href="https://sharemylogin.com/">Source</a>
</p>