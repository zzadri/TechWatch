---
title: "PineTS - Vos scripts TradingView enfin libérés !"
author: "Korben"
date: 2026-02-02T10:59:02.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "Pine Script"
  - "pineTS"
  - "tradingview"
rss_source: Blog
url: https://korben.info/pinets-pine-script-nodejs.html
note: 0
seen: false
---

<p>Vous connaissez sûrement <strong>TradingView</strong> pour suivre les cours de la bourse / crypto, et son fameux langage <strong>Pine Script</strong>. C'est top pour bidouiller des indicateurs techniques sans se prendre la tête, mais dès qu'on veut sortir du bac à sable pour intégrer ça dans un bot perso ou un backend, ça se corse sévère. Alors moi je fais pas tout ça, ni trading, ni dev autour du trading, mais je sais qu'on peut se retrouver souvent bloqué par les limites de la plateforme.</p>
<p>Hé bien bonne nouvelle pour tous les traders en culottes courtes qui n'ont pas encore compris que le DCA c'est + efficace que le day-trading, Alaa-eddine (un lecteur fidèle, coucou !) a bossé sur un projet qui va vous plaire : <strong>
<a href="https://quantforgeorg.github.io/PineTS/">PineTS</a>
</strong>.</p>
<p>PineTS ce n'est pas encore l'un de ses parseurs bancal mais un vrai transpiler ET un runtime complet qui permet d'exécuter du code Pine Script directement dans un environnement Javascript ou TypeScript. Il vous faudra évidemment Node.js et votre bon vieux navigateur pour que ça fonctionne.?</p>
<p>Vous prenez votre script <code>ta.rsi(close, 14)</code>, vous lancez un <code>npm install pinets</code> et hop, ça tourne sur votre serveur. PineTS gère la &quot;transpilation&quot; (non, c'est pas quand on a chaud sous les bras ^^) à la volée et fournit une implémentation des fonctions standard de Pine Script (v5 et v6). Il supporte déjà plus de 60 indicateurs techniques (SMA, EMA, MACD, Bollinger...), le multi-timeframe et même le streaming de données temps réel.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pinets-pine-script-nodejs/pinets-pine-script-nodejs-2.png" alt="" loading="lazy" decoding="async">
<p>Du coup, ça ouvre des portes assez dingues ! Et si vous vous demandez si <strong>Pine Script est similaire à JavaScript</strong>, la réponse est &quot;pas tout à fait&quot;, mais PineTS fait le pont entre les deux mondes. Vous pouvez grâce à ça récupérer des données de marché via n'importe quelle API (CCXT, Binance...), les passer à la moulinette PineTS, et utiliser le résultat pour trigger des ordres ou nourrir une IA.</p>
<p>Attention par contre, tout n'est pas encore supporté à 100%. Sauf si vous restez sur du standard, là c'est royal... Mais si vous utilisez des fonctions graphiques très exotiques, faudra vérifier tout pour ne pas finir sur la paille. Le seul truc qui manque peut-être, c'est une compatibilité totale avec les scripts v4, mais bon, on est en v6 maintenant et pour la logique de trading pure, c'est propre.</p>
<p>D'ailleurs, pour ceux qui utilisent <strong>ChatGPT pour écrire du Pine Script</strong>, sachez que vous pouvez maintenant intégrer ces snippets générés par l'IA directement dans vos propres applis Node.js. C'est quand même plus flexible que de copier-coller ça dans TradingView à chaque fois.</p>
<p>Et ce n'est pas tout (hé oui ^^) car pour la partie visuelle, il a aussi sorti également <strong>
<a href="https://github.com/QuantForgeOrg/QFChart">QFChart</a>
</strong>, une bibliothèque dédiée pour afficher le tout avec de jolis graphiques financiers. C'est le combo gagnant pour se faire un dashboard de trading sur mesure sans dépendre de l'infra de TradingView.</p>
<p>
<img src="https://korben.info/pinets-pine-script-nodejs/pinets-pine-script-nodejs-1.gif" alt="" loading="lazy" decoding="async">
</p>
<p>Perso, je trouve ça génial pour ceux qui veulent garder la main sur leur exécution ou faire du backtesting sérieux avec leurs propres données. En fait, c'est exactement ce qu'il manquait aux traders-developpeurs pour coder leur propre logique de A à Z. Le projet est open source et dispo sur GitHub et y'a même un
<a href="https://quantforge.org/playground/">playground</a>
pour tester vos scripts en live et voir la transpilation en temps réel.</p>
<p>Si vous faites du trading algo, ça vaut clairement le coup d'œil.</p>
<p>
<a href="https://github.com/QuantForgeOrg/PineTS">PineTS</a>
est à découvrir ici ! Et un grand merci à Alaa-eddine pour le partage !</p>