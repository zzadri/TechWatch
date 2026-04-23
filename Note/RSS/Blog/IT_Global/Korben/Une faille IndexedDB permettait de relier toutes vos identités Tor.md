---
title: "Une faille IndexedDB permettait de relier toutes vos identités Tor"
author: "Korben ✨"
date: 2026-04-23T06:12:23.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "vie-privee-anonymat/tor-darknet"
  - "cve"
  - "fingerprinting"
  - "Firefox"
  - "Mozilla"
  - "Tor"
  - "Tracking"
  - "vie privée"
  - "vulnérabilité"
rss_source: Blog
url: https://korben.info/firefox-tor-indexeddb-identifiant-stable.html
note: 0
seen: false
---

<p>Bon, les amis, si vous utilisez <strong>Tor Browser</strong> pour faire du sérieux, faut que vous sachiez un truc. Le bouton &quot;<strong>New Identity</strong>&quot;, censé vous donner une nouvelle identité vierge à chaque clic... bah il laissait filer, jusqu'à il y a peu de temps, <strong>un identifiant stable</strong> tant que Firefox tournait.</p>
<p>Deux chercheurs de
<a href="https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/">Fingerprint</a>
ont en effet trouvé comment une fonction toute bête du navigateur se transformait en empreinte unique de votre browser, partagée entre tous les sites que vous visitiez.</p>
<p>Il faut donc dès à présent faire la mise à jour vers Firefox 150 ou l'ESR 140.10.0 (la version long-terme utilisée par Tor Browser), ainsi que la dernière version de Tor Browser qui récupère le patch. Si vous voulez en savoir plus, la CVE c'est
<a href="https://www.mozilla.org/en-US/security/advisories/mfsa2026-30/">CVE-2026-6770</a>
, classé comme sévérité modérée par Mozilla.</p>
<p>Le truc marche en vase clos mais traverse les murs.</p>
<p>Mais avant, <strong>IndexedDB</strong> c'est quoi ?</p>
<p>En gros c'est une mini-base de données que les sites web peuvent créer dans votre navigateur, pour stocker des trucs en local (du cache, des données offline, l'état d'une app web). Chaque site peut y ranger plusieurs bases nommées, et une petite fonction JavaScript <code>indexedDB.databases()</code> permet au site de demander la liste de ses bases.</p>
<p>Rien de foufou sur le papier. Sauf que dans Firefox en navigation privée, le navigateur renomme en coulisse chaque base avec un identifiant aléatoire (UUID), et range tout ça dans une seule grosse table interne. Et le gros problème, c'est que cette table est partagée entre tous les sites ouverts, et pas cloisonnée site par site.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/firefox-tor-indexeddb-identifiant-stable/firefox-tor-indexeddb-identifiant-stable-2.png" alt="" loading="lazy" decoding="async">
<p>Et là, ça devient croustillant puisque quand un site redemande la liste de ses bases, Firefox la renvoie sans la trier, dans un ordre qui dépend de la structure interne de cette table partagée. Du coup, deux sites totalement différents qui créent chacun seize bases dans le même ordre récupèrent exactement la même suite en retour. Pas l'ordre de création donc mais une permutation bizarre, genre <code>g,c,p,a,l,f,n,d,j,b,o,h,e,m,i,k</code>.</p>
<p>Je vous passe les détails mais ça fait dans les 17 000 milliards de combinaisons possibles. Donc largement de quoi distinguer votre navigateur parmi des millions, comme une empreinte digitale qui colle au doigt !</p>
<p>Et ce qui pique vraiment c'est que cet identifiant survit à la fermeture de toutes vos fenêtres privées. Tant que le process Firefox tourne en arrière-plan, l'ID reste. Un site peut donc vous reconnaître après que vous ayez fermé vos onglets privés, rouvert une session pensée comme neuve, et revisité le site. Pour le user, c'est une session fraîche alors que pour le serveur c'est clairement le même navigateur qu'il y a dix minutes.</p>
<p>Côté Tor Browser c'est pire puisque le bouton &quot;New Identity&quot; a pour mission explicite de couper tout lien avec ce que vous faisiez avant. Il ferme les onglets, efface l'historique, vide les cookies, tire de nouveaux circuits Tor. La promesse officielle, c'est &quot;<em>empêcher votre activité future d'être liée à ce qui précède</em>&quot;.</p>
<p>Sauf que cette fameuse table interne, elle, ne bouge pas. Le New Identity reset donc tout sauf ce qu'il ignore. C'est comme changer de fringues dans le même ascenseur... en gardant le même parfum. Techniquement vous êtes différent, mais reconnaissable en deux secondes. Bref, c'est assez grave car un site capable d'exploiter la faille peut lier votre session avant-New-Identity à votre session après-New-Identity.</p>
<p>Tant qu'on n'a pas redémarré Firefox complètement, l'ID persiste.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/firefox-tor-indexeddb-identifiant-stable/firefox-tor-indexeddb-identifiant-stable-3.png" alt="" loading="lazy" decoding="async">
<p>Les chercheurs disent avoir fait une divulgation responsable, directement à Mozilla et au Tor Project avant publication donc c'est nickel, et les deux équipes ont poussé les patches avant de communiquer sur quoi que ce soit. Donc les utilisateurs à jour sont tout simplement protégés contre cette faille précise.</p>
<p>Après si vous êtes du genre parano, pensez à redémarrer complètement votre Tor Browser entre deux sessions vraiment sensibles. Ça coupe le process Firefox, ça vide cette fameuse table, et ça évite ce genre de surprise pour d'autres leaks similaires qu'on n'aurait pas encore trouvés.</p>
<p>A bon entendeur, salut !!</p>
<p>
<a href="https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/">Source</a>
</p>