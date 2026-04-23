---
title: "selfh.st - L'annuaire vivant du self-hosting"
author: "Korben"
date: 2026-04-17T07:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "self-hosting"
  - "homelab"
  - "self-hosted"
  - "self-hosting"
rss_source: Blog
url: https://korben.info/selfh-st-apps-annuaire-self-hosting.html
note: 0
seen: false
---

<p>Quand on fait du self-hosting, y'a toujours ce moment où on se dit &quot;<em>tiens, y'aurait pas un truc open source pour ça</em>&quot;. Tenez par exemple, là je suis en train de chercher un machin open source pour un mariage qui permet aux invités de balancer leurs photos sur un serveur en scannant un QR Code. Et donc je me retrouve à scroller awesome-selfhosted sur GitHub, qui est une liste fleuve de +1500 projets, en essayant de deviner lesquels sont encore vivants.</p>
<p>Et c'est exactement ce problème qu'a voulu résoudre Ethan Sholly en lançant
<a href="https://selfh.st/apps/">selfh.st/apps</a>
en 2024. En gros, c'est un annuaire d'applications auto-hébergées avec des vrais filtres, du tri, et surtout des indicateurs d'activité. Le mec est aussi derrière la newsletter Self-Host Weekly.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/selfh-st-apps-annuaire-self-hosting/selfh-st-apps-annuaire-self-hosting-1.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de selfh.st/apps, avec fiches, filtres et indicateurs d'activité</em></p>
<p>Comme ça, au lieu de vous taper une liste brute, vous avez des fiches pour chaque app avec le nombre d'étoiles GitHub, la licence, le langage, les tags, et surtout un code couleur sur la date de dernière activité. Vert si le projet a reçu un commit dans les 6 derniers mois, jaune entre 6 et 12 mois, rouge au-delà d'un an. Pratique pour éviter d'installer un truc que plus personne ne maintient, genre un serveur Plex alternatif mort depuis 2022 !</p>
<p>Et le tri par défaut, c'est pas juste les étoiles GitHub sinon les gros projets à 50 000 étoiles écraseraient tout. L'algo prend en compte l'âge du repo, la date du dernier commit, et même l'intérêt Google Trends pour les projets non-GitHub. Du coup un outil avec 200 stars mais hyper actif peut remonter devant un dinosaure à 30k stars qui dort depuis 18 mois. J'ai trouvé ça pas bête comme filtrage.</p>
<p>D'ailleurs, chaque projet a son propre flux RSS filtré qui ne remonte que les releases stables. Pas de bêtas, pas de RC... juste les versions prêtes pour la prod. Comme ça, vous branchez ça dans votre FreshRSS ou Miniflux et vous êtes au courant des mises à jour sans checker chaque repo GitHub à la main ! Par contre, si vous aimez vivre dangereusement sur les nightly, là faudra passer par les flux officiels GitHub.</p>
<p>Le site va également plus loin que la simple liste d'apps puisqu'il propose aussi une section &quot;companions&quot;, contenant des apps compagnons qui étendent d'autres logiciels auto-hébergés (genre les extensions navigateur pour Linkedin ou les clients tiers pour Immich...etc).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/selfh-st-apps-annuaire-self-hosting/selfh-st-apps-annuaire-self-hosting-3.png" alt="" loading="lazy" decoding="async">
<p><em>La collection d'icônes pour personnaliser votre Homarr ou Dashy</em></p>
<p>Et surtout, y'a
<a href="https://selfh.st/icons/">selfh.st/icons</a>
avec des milliers d'icônes de dashboard en SVG, PNG et WebP, toutes en 512x512 ratio 1:1, indispensable pour personnaliser votre page d'accueil sur Homarr ou Dashy !</p>
<p>Le catalogue d'apps est sous licence CC0-1.0 (domaine public) et mis à jour tous les matins à 5h du mat' heure de New York (les icônes, elles, sont en CC-BY-4.0, donc pensez à créditer si vous les réutilisez). En 2 minutes de fouille j'y ai trouvé trois projets que je connaissais pas. Et si vous voulez ajouter le vôtre, le repo est ouvert sur
<a href="https://github.com/selfhst">https://github.com/selfhst</a>
.</p>
<p>Et si vous connaissez un outil pour mon projet de QR Code d'upload de photo de mariage, n'hésitez pas à me contacter.</p>
<p>Voilà, pour ceux qui font de
<a href="https://korben.info/self-hosting-guide-auto-hebergement.html">l'auto-hébergement</a>
au quotidien, c'est clairement un bookmark à garder sous le coude. Que vous cherchiez une alternative à Notion, un dashboard pour votre homelab, ou juste un truc pour remplacer un service cloud qui vous gonfle, y'a de quoi fouiller ! Et si vous cherchez des pistes pour commencer,
<a href="https://korben.info/opencloud-alternative-nextcloud-go-auto-hebergement.html">OpenCloud</a>
ou
<a href="https://korben.info/pocket-id-auth-oidc-passkey.html">Pocket ID</a>
sont de bons points de départ.</p>
<p>Bref, une mine d'or pour les homelabbers.</p>
<p>Merci à Maxime pour le lien !</p>