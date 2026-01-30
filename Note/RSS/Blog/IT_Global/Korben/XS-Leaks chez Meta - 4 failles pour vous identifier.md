---
title: "XS-Leaks chez Meta - 4 failles pour vous identifier"
author: "Korben"
date: 2026-01-16T11:42:09.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/gafam-tech"
  - "cybersecurite/failles-vulnerabilites"
  - "Bug Bounty"
  - "Facebook"
  - "meta"
  - "sécurité"
  - "vie privée"
  - "vulnérabilité"
  - "XS-Leaks"
rss_source: Blog
url: https://korben.info/cross-site-leaks-facebook-meta-xs-leaks-failles.html
note: 0
seen: false
---

<p>Youssef Sammouda, un chercheur en sécurité connu sous le pseudo sam0, vient de publier
<a href="https://ysamm.com/uncategorized/2026/01/16/cross-site-leaks.html">un article détaillant pas moins de 4 vulnérabilités de type XS-Leaks</a>
qu'il a découvertes chez Meta. Pour vous la faire courte, ce genre de faille permet à un site malveillant de déduire des informations sur vous sans même avoir besoin de pirater quoi que ce soit. Heureusement, tout a été patché depuis !</p>
<p>La première faille concernait <strong>Workplace</strong> (la version entreprise de Facebook) et son intégration avec Zoom. En gros, un attaquant pouvait créer une page web qui chargeait le callback Zoom de Workplace dans une iframe, et selon que l'utilisateur était connecté ou non à Meta Work, la redirection se comportait différemment. Et là, pouf, l'attaquant savait si vous étiez un utilisateur Meta Work. Pas besoin d'accéder à vos données, juste de mesurer combien de temps met une redirection. Vicieux, non ? Meta a casqué 2 400 dollars pour cette trouvaille.</p>
<p>La deuxième faille, c'était le bon vieux bouton Like de Facebook. Vous savez, ce petit widget qu'on trouve sur des millions de sites web ? Eh bien si vous étiez connecté à Facebook, le plugin pouvait révéler si vous aviez liké une page spécifique ou pas. Un attaquant n'avait qu'à mesurer le nombre de frames dans l'iframe pour le savoir. Encore 2 400 dollars dans la poche de notre chercheur.</p>
<p>La troisième était plus technique et bien trouvée. Le fichier signals/iwl.js de Facebook utilise Object.prototype pour ses opérations. En manipulant ce prototype depuis la page parente, un attaquant pouvait provoquer des erreurs différentes selon l'état de connexion de l'utilisateur, et même récupérer son ID Facebook. Ça, ça valait 3 600 dollars.</p>
<p>Et voilà, la quatrième concernait l'identification des employés Meta eux-mêmes via les domaines internes. Celle-là n'a pas rapporté de bounty (juste un &quot;informative&quot;), mais elle montre bien l'étendue du problème.</p>
<p>Au total, Youssef a empoché 8 400 dollars entre décembre 2024 et mai 2025, le temps que Meta corrige tout ça. Alors oui, c'est cool que ces failles soient maintenant corrigées mais ça fait quand même réfléchir sur la quantité de données qui peuvent fuiter sans même qu'on s'en rende compte.</p>
<p>Pour ceux qui veulent creuser le fonctionnement des
<a href="https://korben.info/programme-bug-bounty.html">programmes de bug bounty</a>
, c'est vraiment un système génial et hyper vertueux où tout le monde est gagnant. Les chercheurs sont payés pour trouver des failles, les entreprises patchent avant que les méchants n'exploitent. Y'a vraiment de quoi faire dans ce domaine.</p>
<p>Bref, bien joué Youssef Sammouda, grâce à lui quelques failles de moins chez Meta, et ça c'est cool !</p>
<p>
<a href="https://ysamm.com/uncategorized/2026/01/16/cross-site-leaks.html">Source</a>
</p>