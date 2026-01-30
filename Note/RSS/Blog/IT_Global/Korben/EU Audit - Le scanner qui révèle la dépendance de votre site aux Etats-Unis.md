---
title: "EU Audit - Le scanner qui révèle la dépendance de votre site aux Etats-Unis"
author: "Korben"
date: 2026-01-27T16:22:58.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/legislation-juridique"
  - "developpement/outils-developpement"
  - "alternatives GAFAM"
  - "défense de la vie privée"
  - "GAFAM"
rss_source: Blog
url: https://korben.info/eu-audit-scanner-souverainete.html
note: 0
seen: false
---

<p>Vous savez combien de services américains vous utilisez sur votre site web utilise sans que vous ne le sachiez réellement ??? Aucun ? Bah et les Google Fonts pour la typo, Cloudflare pour le CDN, YouTube pour les vidéos embarquées, Google Analytics pour les stats et j'en passe des vertes et des pas mûres... ??? Faudrait pas les oublier !</p>
<p>Ainsi même si votre hébergement est chez O2Switch ou Scaleway en France, vos visiteurs peuvent envoyer des données aux USA sans que vous le réalisiez.</p>
<p>Et ça pose un vrai problème juridique car je sais pas si vous vous souvenez du Privacy Shield mais c'était ce fameux accord qui permettait de transférer légalement des données vers les États-Unis ? Hé bien il a été invalidé par la Cour de Justice européenne en 2020. Tout comme Safe Harbor avant lui en 2015 en fait. Et il y a maintenant le Data Privacy Framework, mais rien ne garantit qu'il tiendra plus longtemps que les précédents.</p>
<p>C'est là qu'intervient
<a href="https://lightwaves.io/en/eu-audit/">EU Audit</a>
, un scanner gratuit développé par un studio autrichien. Vous entrez l'URL de votre site et en quelques secondes, l'outil analyse vos principales dépendances : hébergement, polices, analytics, CDN, vidéos embarquées, widgets de chat, trackers sociaux et cartes. Chaque élément est vérifié pour déterminer s'il est hébergé dans l'UE ou pas et à la fin, vous obtenez <strong>un score de « souveraineté européenne »</strong> en pourcentage.</p>
<p>Perso, j'ai testé sur korben.info et je me suis pris une claque. Principalement à cause de Cloudflare et de mes embed de vidéos Youtube.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/eu-audit-scanner-souverainete/eu-audit-scanner-souverainete-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pourtant, j'ai plus rien sur mon site à part ça, et mon hébergeur c'est o2Switch et c'est bien en France. Il me parle de &quot;Social&quot; mais j'ai rien du tout, à part des liens vers mes réseaux sociaux... J'sais pas peut être que ça suffit. En fait, suffirait que je vire Cloudflare pour repasser un dans le vert déjà mais je n'ai pas connaissance d'une solution équivalente et pas trop cher (parce que je fais plus de trafic que j'ai de moyens pour le financer, sniiif) qui assure du CDN, de la sécurité, des workers...etc. Ça existe peut-être mais dans ce cas, envoyez moi un mail pour que j'aille voir ça. Après pour l'embed YouTube, pareil, je vois pas trop quoi faire vu que je relaie surtout des vidéos YouTube parce que la Terre entière met ses vidéos là bas...</p>
<p>Bien sûr, j'ai trouvé l'idée de ce scanner pas mal du tout. Ça permet de visualiser rapidement où sont les fuites de données potentielles... Je ne les utilise pas mais y'a Google Fonts par exemple. C'est un classique... Chaque visiteur fait une requête vers les serveurs de Google, qui récupère son IP au passage. Pareil pour les vidéos YouTube embarquées, les maps Google, ou le sempiternel vieux pixel Facebook que certains laissent encore traîner sans même s'en rendre compte. D'ailleurs si vous voulez
<a href="https://korben.info/personal-security-checklist-guide-securite-numerique-vie-privee-protection-donnees.html">auditer votre propre hygiène numérique</a>
, j'avais fait un guide complet sur le sujet.</p>
<p>Bon après, l'outil ne détecte pas tout (les scripts inline ou les appels API cachés dans votre code, par exemple). Et pour un blog perso sans données sensibles, c'est peut-être un peu overkill. Mais si vous gérez des sites pour des entreprises ou des clients sensibles (administrations, santé, éducation...), y'a de quoi réfléchir ! Surtout que le passage à des alternatives européennes n'est pas toujours aussi compliqué qu'on le croit.
<a href="https://korben.info/collecter-ethiquement-donnees.html">Matomo</a>
au lieu de Google Analytics, des polices auto-hébergées, OpenStreetMap au lieu de Google Maps...</p>
<p>Si vous voulez soutenir un web indépendant et que je puisse continuer à dénicher ce genre d'outils, ça se passe sur
<a href="https://patreon.com/korben">mon Patreon</a>
.</p>
<p>Bref, si vous voulez faire le point sur la dépendance de votre site aux GAFAM, c'est gratuit et ça prend 30 secondes.</p>