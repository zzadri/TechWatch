---
title: "Cloudflare vs Italie - Le bras de fer sur le Piracy Shield ne fait que commencer"
author: "Korben"
date: 2026-01-12T12:28:23.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/legislation-juridique"
  - "vie-privee-anonymat/censure-liberte"
  - "vie-privee-anonymat/hadopi-telechargement"
  - "blocage DNS"
  - "censure"
  - "Cloudflare"
  - "Italie"
  - "Matthew Prince"
  - "Piracy Shield"
rss_source: Blog
url: https://korben.info/cloudflare-italie-blocage-piratage-quitter-pays.html
note: 0
seen: false
---

<p>Alors que l'Italie pensait avoir trouvé l'arme ultime contre le piratage avec son fameux &quot;<strong>Piracy Shield</strong>&quot;, voici que voilà que Cloudflare vient de leur renvoyer une gifle mémorable. C'était prévisible et j'ai envie de dire tant mieux car je pense que la neutralité du net mérite mieux et je ne suis pas fan de l'idée de transformer des hébergeurs et autres prestataires techniques en garant de la moral a.k.a. en censeurs automatisés.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cloudflare-italie-blocage-piratage-quitter-pays/cloudflare-italie-blocage-piratage-quitter-pays-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>Matthew Prince, le patron de Cloudflare, n'a pas l'intention de se laisser faire (
<a href="https://arstechnica.com/tech-policy/2026/01/cloudflare-may-pull-servers-out-of-italy-over-order-that-it-block-pirate-sites/">Source</a>
)</em></p>
<p>Si vous vous demandez de quoi je parle, je vous propose de reprendre tout ça depuis le début. En effet, l'autorité italienne de régulation des communications (AGCOM) vient de coller une amende de <strong>14,2 millions d'euros à Cloudflare</strong>. Pourquoi ? Hé bien tout simplement parce que l'entreprise refuse de se plier à un ordre de blocage DNS datant de février 2025 sur son service <strong>1.1.1.1</strong> pour filtrer les sites de streaming illégaux de la Serie A (Si vous ne connaissez pas la Serie A, c'est un championnat de foot à la con). Cette prune est quand même égale à 1% de son chiffre d'affaires annuel, bref Cloudflare est carrément dans la sauce.</p>
<p>Toujours pour ceux qui débarquent, le Piracy Shield est un système censé permettre aux ayants droit de soumettre des adresses IP et des noms de domaine à bloquer dans un délai de 30 minutes après notification. Sauf que dans la vraie vie, ça ne marche pas tout à fait comme ça. Matthew Prince, le patron de Cloudflare, n'a d'ailleurs pas mâché ses mots en affirmant que l'Italie tente d'imposer une véritable &quot;censure globale&quot; sans surveillance judiciaire ni transparence. Pour lui, c'est comme essayer d'arrêter l'eau avec une passoire tout en inondant les voisins.</p>
<p>Techniquement, Cloudflare explique qu'obliger d'opérer un blocage DNS/IP sur ses 200 milliards de requêtes quotidiennes, cela augmenterait significativement la latence pour les utilisateurs de ses résolveurs. Et surtout, le risque de surblocage est gigantesque. Rappelez-vous, en octobre 2024, ce magnifique système avait réussi l'exploit
<a href="https://www.01net.com/actualites/bouclier-contre-piratage-italien-bloque-acces-google-drive.html">de bloquer Google Drive</a>
pour toute l'Italie pendant trois heures (et certains blocages partiels ont même persisté bien après). Gloups ! C'est ce genre de dérives qui inquiète, surtout quand on sait que le système a déjà fait désactiver plus de 65 000 domaines en deux ans, selon l'AGCOM.</p>
<p>Et je vous parle pas de coût humains et techniques que ça engendre pour les opérateurs comme Cloudflare.</p>
<p>La réponse de Matthew Prince est d'ailleurs assez radicale puisque Cloudflare envisage carrément de retirer tous ses serveurs des villes italiennes, de couper ses services de cybersécurité gratuits pour les utilisateurs locaux et même d'annuler son soutien pro bono pour les prochains Jeux olympiques de Milan-Cortina. Bye Bye l'investissement, basta la collaboration !</p>
<p>On se retrouve donc dans une situation où Cloudflare se voit contraint de choisir entre ses principes et le marché italien. Si vous suivez un peu l'actu, vous savez que
<a href="https://korben.info/blocage-dns-fai-francais-streaming-illegal.html">les services DNS sont de plus en plus ciblés</a>
par des obligations de blocage, mais l'Italie semble vouloir aller plus loin que les autres.</p>
<p>Si la France a déjà ordonné à cinq gros fournisseurs de VPN de bloquer certains sites de streaming sportif, l'offensive italienne contre les infrastructures de base du web est un cran au-dessus. Heureusement, il existe encore des résistances techniques et
<a href="https://korben.info/ces-protocoles-ennemis-de-la-censure-des-fai.html">ces protocoles ennemis de la censure</a>
comme le DoH ou l'ECH (Encrypted Client Hello) rendent la tâche plus complexe pour les autorités, même si cela n'empêchera jamais un blocage pur et dur par IP.</p>
<p>Bref, reste à savoir maintenant comment ceci sera réellement appliqué dans les mois qui viennent... En attendant, si vous utilisez Cloudflare en Italie (ou ailleurs), surveillez de près les évolutions de votre service car le bras de fer ne fait que commencer.</p>
<p>
<a href="https://arstechnica.com/tech-policy/2026/01/cloudflare-may-pull-servers-out-of-italy-over-order-that-it-block-pirate-sites/">Source</a>
</p>