---
title: "Mistikee - Le gestionnaire de mots de passe à déni plausible"
author: "Korben"
date: 2026-02-07T06:48:34.000Z
type: site
subject:
category: IT Global
tags:
  - "vie-privee-anonymat/gestionnaires-mots-de-passe"
  - "brute force"
  - "chiffrement"
  - "déni plausible"
  - "gestionnaire de mots de passe"
rss_source: Blog
url: https://korben.info/mistikee-gestionnaire-mots-de-passe-deni-plausible.html
note: 0
seen: false
---

<p>Vous connaissez le concept de déni plausible appliqué aux mots de passe ? L'idée c'est que si quelqu'un chope votre coffre-fort de passwords et tente de le cracker en brute force, il va obtenir des résultats... mais jamais savoir si ce sont les bons. Niark niark !</p>
<p>Hé bien c'est exactement le principe de
<a href="https://mistikee.app/">Mistikee</a>
, un gestionnaire de mots de passe développé par un dev indé français. Le truc qui le différencie de tout ce qu'on connait (Bitwarden,
<a href="https://korben.info/keepass-logiciel-gestion-mots-passe.html">KeePass</a>
et compagnie), c'est que le mot de passe maitre n'est JAMAIS stocké. Du coup, peu importe ce que vous tapez comme mot de passe maitre, Mistikee va toujours vous donner une réponse. Sauf que seul le bon mot de passe maitre donnera la bonne réponse... les autres donneront des résultats tout aussi crédibles mais complètement faux.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mistikee-gestionnaire-mots-de-passe-deni-plausible/mistikee-gestionnaire-mots-de-passe-deni-plausible-2.png" alt="" loading="lazy" decoding="async">
<p><em>Mistikee, le gestionnaire de mots de passe à déni plausible</em></p>
<p>En gros, un attaquant qui tente un brute force va se retrouver avec des milliers de réponses plausibles et aucun moyen de savoir laquelle est la bonne. Bon courage ! Comme si chaque clé ouvrait la serrure, mais donnait accès à une pièce différente (et y'a qu'une seule vraie pièce). Oui, comme dans Peacemaker ^^.</p>
<p>Côté technique, l'app régénère vos mots de passe à la volée à partir du mot de passe maitre via une dérivation cryptographique. Pas de base de données déchiffrable, pas de fichier .kdbx qu'on peut attaquer avec hashcat ou john.</p>
<p>Attention quand même : Faut choisir un mot de passe maitre SOLIDE, hein... parce que si vous mettez &quot;1234&quot;, le déni plausible ne va pas faire de miracles. Et si vous oubliez votre vrai mot de passe maitre ? Terminé. Aucune récupération possible (c'est le revers de la médaille, forcément).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mistikee-gestionnaire-mots-de-passe-deni-plausible/mistikee-gestionnaire-mots-de-passe-deni-plausible-3.png" alt="" loading="lazy" decoding="async">
<p><em>Les écrans de Mistikee sur mobile</em></p>
<p>L'outil est dispo sur Android, iOS, macOS et Windows et tout est stocké en local sur votre appareil avec une synchro chiffrée de bout en bout via le cloud si vous voulez utiliser plusieurs appareils. Par contre, pas d'extension navigateur pour le moment, faudra copier-coller à la main... c'est pas le plus pratique si vous avez 50 comptes sur lesquels vous connecter dans la journée. Et le modèle économique est honnête, c'est gratuit avec une option premium en paiement unique à 4,99 euros (pas d'abonnement, ça nous change des Dashlane et compagnie qui vous ponctionnent +40 balles par an).</p>
<p>Voilà j'ai fait le tour... Alors ça ne remplacera pas forcément votre
<a href="https://korben.info/localpass-gestionnaire-mots-de-passe-offline.html">gestionnaire habituel</a>
pour le quotidien, surtout si vous avez 200+ entrées avec des TOTP et tout le bazar. Mais faut voir ça plutôt un coffre-fort complémentaire pour vos secrets les plus sensibles, ceux où vous voulez vraiment cette couche de protection supplémentaire contre le brute force. Par exemple pour un journaliste ou un activiste qui traverse une frontière avec son laptop c'est pas rien.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/HaJ1TfmeTUo?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Bref, allez jeter un oeil !</p>
<p>Et merci à Matthieu pour la découverte.</p>