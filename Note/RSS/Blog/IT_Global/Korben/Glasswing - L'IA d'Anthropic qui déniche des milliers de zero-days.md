---
title: "Glasswing - L'IA d'Anthropic qui déniche des milliers de zero-days"
author: "Korben"
date: 2026-04-08T04:53:07.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "IA cybersécurité"
  - "zero-day IA"
rss_source: Blog
url: https://korben.info/glasswing-anthropic-ia-cybersecurite-zero-day.html
note: 0
seen: false
---

<p>Anthropic vient de lâcher une bombe !</p>
<p>Le labo derrière Claude a dévoilé le
<a href="https://www.anthropic.com/glasswing">Projet Glasswing</a>
, une initiative de cybersécurité qui embarque un nouveau modèle, <strong>Claude Mythos</strong>, tellement efficace pour trouver des failles qu'ils ont décidé de ne pas le rendre public. En gros, l'IA est devenue meilleure que la plupart des humains pour dénicher des vulnérabilités zero-day... et ça va faire mal ^^.</p>
<p>Concrètement, Mythos a trouvé des milliers de zero-days dans tous les OS et navigateurs majeurs ces dernières semaines. Et pas des failles mineures, hein ! Une vulnérabilité dans OpenBSD qui traînait depuis 27 ans, un bug dans FFmpeg vieux de 16 ans qui avait survécu à 5 millions d'itérations de tests automatisés... et des exploits chaînés dans le noyau Linux (3, 4, parfois 5 vulnérabilités enchaînées de manière autonome) qui permettent une escalade de privilèges complète. Comme le dit un chercheur dans la
<a href="https://www.youtube.com/watch?v=INGOC6-LLv0">vidéo de présentation</a>
: &quot;<em>J'ai trouvé plus de bugs ces dernières semaines que pendant tout le reste de ma carrière combinée</em>&quot;.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/INGOC6-LLv0?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Et le truc qui tue, c'est que Mythos n'a pas été entraîné spécifiquement pour la cybersécurité. Il a juste été entraîné pour être bon en code... et par effet de bord, il est devenu redoutable en sécu. En fait, les benchmarks sont assez parlants. Sur CyberGym (reproduction de vulnérabilités), Mythos tape du 83% contre 67% pour Opus 4.6. Mais c'est sur l'exploitation de Firefox 147 (en collaboration avec Mozilla je tiens à le préciser), que le fossé est le plus flippant : 84% de taux de réussite en exploitation shell, contre 15% pour Opus 4.6 et 4% pour Sonnet.</p>
<p>
<a href="https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf">Lors de tests internes</a>
, une version précoce de Mythos enfermée dans un sandbox sécurisé a réussi à s'en échapper (on lui en avait donné l'instruction pour le test), a développé un exploit multi-étapes pour accéder à Internet, puis a envoyé un email au chercheur pour le prévenir de son évasion. Le chercheur l'a reçu lorsqu'il était en train de faire sa pause sandwich dans un parc ! Dans moins de 0,001% des cas, ces versions précoces ont même carrément tenté de dissimuler des actions interdites en modifiant l'historique git pour ne pas laisser de traces. Bon, Anthropic précise que ces comportements ont été corrigés dans la version finale parce que c'était clairement pas tolérable... mais quand même.</p>
<p>Ce qui est vraiment impressionnant, c'est cette coalition derrière Glasswind. Apple, Microsoft, Google, AWS, NVIDIA, CrowdStrike, Cisco, Palo Alto Networks, JPMorgan, Broadcom, la Linux Foundation... des partenaires qui d'habitude se tirent dans les pattes, réunis autour de la même table, plus 40 autres organisations.</p>
<p>Le problème c'est que Mythos ne sera pas accessible au public. Trop dangereux. Seuls les professionnels de la sécurité vérifiés y auront droit, via un &quot;Cyber Verification Program&quot; dédié. Je suis triste, j'aurais vraiment kiffé le tester...</p>
<p>Anthropic met 100 millions de dollars de crédits sur la table pour la recherche, plus 2,5 millions pour l'OpenSSF et 1,5 million pour la fondation Apache. Le programme &quot;Claude for Open Source&quot; donne un accès dédié aux mainteneurs de projets open source. C'est du bon gros marketing c'est sûr, mais quand on voit le nombre de mainteneurs open source qui bossent seuls le soir sans budget sécu... franchement, c'est pas de refus.</p>
<p>Du coup, on vient vraiment de passer à une autre échelle.</p>
<p>
<a href="https://korben.info/ia-o3-vulnerabilite-zero-day-linux-premiere.html">L'année dernière, o3 d'OpenAI avait trouvé UN zero-day Linux</a>
et c'était déjà une première mondiale. Là, Mythos en trouve des milliers et crée des preuves de concept d'exploitation quasiment toujours du premier coup. C'est chouette pour la sécurité mais cette capacité est clairement un couteau à double tranchant. Entre les mains d'un défenseur, c'est un bouclier mais entre les mains d'un attaquant... bon, on préfère pas y penser.</p>
<p>Anthropic s'engage à publier un rapport dans les 90 jours sur les vulnérabilités patchées et à terme, ils veulent créer un organisme indépendant, public-privé, pour coordonner tout ça. Comme l'a dit le CTO de CrowdStrike : &quot;<em>ce qui prenait des mois prend maintenant des minutes</em>&quot;.</p>
<p>Bref, Glasswing c'est le moment où l'IA en cybersécurité passe du labo au terrain, mais maintenant reste à voir si le bouclier sera déployé plus vite que l'épée.</p>