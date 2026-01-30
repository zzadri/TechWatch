---
title: "Telnetd - Une faille vieille de 11 ans offre un accès root"
author: "Korben"
date: 2026-01-26T15:05:35.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/failles-vulnerabilites"
  - "accès root"
  - "cve"
  - "faille critique"
  - "faille de sécurité"
  - "telnet"
  - "vulnérabilités Telnet"
rss_source: Blog
url: https://korben.info/telnetd-faille-root-exploit.html
note: 0
seen: false
---

<p>Telnet, ça vous dit quelque chose ?</p>
<p>C'est ce vieux protocole réseau non chiffré que nos arrières-arrières-arrières-grands-parents utilisaient pour se connecter à des serveurs distants. C'est un truc que vous pensiez peut-être enterré depuis belle lurette... Hé bien figurez-vous qu'<strong>une faille critique vieille de 11 ANS</strong> vient d'être découverte dans le serveur <strong>telnetd</strong> de <strong>GNU InetUtils</strong>. Et le pire c'est que des hackers l'exploitent déjà activement.</p>
<p>ARGH !</p>
<p>La vulnérabilité en question, baptisée
<a href="https://nvd.nist.gov/vuln/detail/CVE-2026-24061">CVE-2026-24061</a>
, permet de contourner complètement l'authentification et d'obtenir un accès root. Sans putain de mot de passe (!!!!).</p>
<p>Bon ok, faut quand même que le service telnetd soit actif et exposé, mais après c'est open bar les amis ! En gros, le serveur telnetd passe la variable d'environnement USER directement à la commande login sans la nettoyer. Du coup, un attaquant n'a qu'à définir <strong>USER sur <code>-f root</code></strong> et utiliser <code>**telnet -a**</code> pour se retrouver connecté en root.</p>
<p>C'est moche.</p>
<p>Concrètement, ça touche toutes les versions de GNU InetUtils de la 1.9.3 jusqu'à la 2.7. Ça touche donc des distributions Linux, de vieux routeurs, des capteurs industriels...etc. Après, les machines exposées sur Internet avec Telnet actif c'est quand même assez rare, donc faut pas non plus paniquer.</p>
<p>Cependant, les attaquants n'ont pas attendu. La société
<a href="https://www.labs.greynoise.io/grimoire/2026-01-22-f-around-and-find-out-18-hours-of-unsolicited-houseguests/">GreyNoise</a>
a documenté des exploitations actives entre le 21 et le 22 janvier, soit très rapidement après la divulgation du 20 janvier. Ils ont ainsi observé 18 adresses IP différentes lancer une soixantaine de sessions Telnet, avec 83% des tentatives ciblant directement le compte root. Du travail de pros.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/telnetd-faille-root-exploit/telnetd-faille-root-exploit-2.png" alt="" loading="lazy" decoding="async">
<p>Heureusement, <strong>un correctif existe</strong> \o/ : <strong>GNU InetUtils 2.8</strong> colmate la brèche mais combien de ces vieux équipements IoT ou industriels vont vraiment être mis à jour ? On connaît tous la chanson par cœur !</p>
<p>Mais bon, si vous avez des machines exposées avec telnetd actif, vous avez trois options : <strong>mettre à jour</strong> vers la version 2.8, <strong>désactiver</strong> complètement le service telnetd, ou <strong>bloquer</strong> le port TCP 23 au niveau du firewall. Perso, je vous conseille carrément de virer Telnet et de passer à SSH si c'est pas déjà fait. En 2026, y'a vraiment plus aucune excuse pour utiliser un protocole qui n'est pas chiffré.</p>
<p>Bref, encore une vieille faille qui traînait depuis 2015 et qui refait surface au pire moment.</p>
<p>Merci à
<a href="https://arfy.fr/dotclear/index.php?post/2026/01/26/howtogeek-Hackers-exploit-critical-telnetd-auth-bypass-flaw-to-get-root">Arfy</a>
pour l'info !</p>
<p>
<a href="https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-telnetd-auth-bypass-flaw-to-get-root/">Source</a>
</p>