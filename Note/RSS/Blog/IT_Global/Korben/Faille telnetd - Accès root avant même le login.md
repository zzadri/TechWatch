---
title: "Faille telnetd - Accès root avant même le login"
author: "Korben"
date: 2026-03-18T14:08:40.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "linux-open-source/administration-serveur"
  - "cve"
  - "faille RCE"
  - "sécurité informatique"
  - "telnet"
  - "vulnérabilité critique"
rss_source: Blog
url: https://korben.info/faille-telnetd-cve-2026-32746-rce-root.html
note: 0
seen: false
---

<p>Telnet en big 2026... bah oui ça existe encore les amis ! Et surtout c’est toujours aussi troué ! J'en veux pour preuve le daemon telnetd de GNU InetUtils qui vient de se prendre une 2ème faille critique en l’espace de deux mois, et celle-là, elle pique de fou !</p>
<p>Il s'agit de la
<a href="https://nvd.nist.gov/vuln/detail/CVE-2026-32746">CVE-2026-32746</a>
, elle permet d’obtenir un shell root sur n’importe quel serveur Linux ou BSD exposant le port 23, et l’attaque se fait avant même que le prompt de login n’apparaisse. Pas besoin de mot de passe, pas besoin de compte. Juste une bonne vieille connexion TCP et un paquet SLC malformé et c'est parti mon kiki !</p>
<p>En fait, le bug se planque dans le handler SLC (Set Local Characters) du code source C de telnetd. Ainsi, quand un client ouvre une socket TCP sur le port 23, y’a une phase de négociation d’options avant l’authentification. L’attaquant envoie alors un paquet SLC contenant un nombre anormal d'octets, et ça déclenche un buffer overflow de type out-of-bounds write dans la mémoire du processus. Et boom, exécution de code arbitraire avec les privilèges root ! Et ça, ça donne un score CVSS de 9.8 sur 10 soit quasi la note maximale !</p>
<p>Toutes les versions de GNU InetUtils telnetd jusqu’à la 2.7 sont touchées. Toutes vulnérables, et pour le moment, aucun patch n’est disponible à ce jour. C’est la boîte de cybersécurité israélienne Dream, via son chercheur Adiel Sol, qui a découvert le pot aux roses et publié l’advisory le 11 mars dernier. Le patch officiel du mainteneur GNU est attendu pour le 1er avril (et non, c’est pas un poisson).</p>
<p>Ça craint surtout qu'il y a à peine 2 mois, une autre faille critique dans le même daemon, la CVE-2026-24061 (aussi scorée 9.8), avait déjà été divulguée. Et celle-là, la CISA l’a depuis ajoutée à son catalogue de vulnérabilités activement exploitées dans la nature. Ça me rappelle carrément
<a href="https://korben.info/faille-rce-critique-linux-cauchemar-admins.html">la faille RCE dans cups-browsed</a>
l’an dernier... Ces vieux services réseau, c’est dingue comme ça revient régulièrement.</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/18rSQfBABeE?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Donc gaffe à vous parce que si vous avez du telnetd qui traîne quelque part (serveurs Debian, switchs Cisco, automates Siemens, imprimantes HP réseau...), faut agir vite.</p>
<p>Déjà, désactivez le service avec un</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemctl stop telnet.socket &amp;&amp; systemctl disable telnet.socket
</span></span></code></pre><p>ou éditez <code>/etc/xinetd.d/telnet</code> si vous êtes sur un vieux système.</p>
<p>Sinon, on bloque le port 23 avec un</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">iptables -A INPUT -p tcp --dport 23 -j DROP
</span></span></code></pre><p>... plutôt que de laisser ça ouvert aux quatre vents. Isolez aussi l’accès via un VLAN dédié aux seuls réseaux autorisés et faites tourner le daemon sans les privilèges root si votre config le permet. Et en couche supplémentaire, je vous recommande le
<a href="https://korben.info/outil-knockr-port-knocking-securise.html">port knocking</a>
qui permet de masquer vos ports aux scans automatiques (ça ne corrige pas la faille, mais ça réduit la surface d’exposition).</p>
<p>Par contre, le problème vous l'aurez compris, c’est que beaucoup de ces équipements ne supportent pas forcément SSH. Donc y’a encore des tonnes et des tonnes de switchs managés et d’automates industriels coincés sur telnet parce que le constructeur n’a jamais jugé bon de supporter autre chose.</p>
<p>Et dans ces cas-là, le seul vrai plan de secours finalement, c’est ce bon vieux firewall et un peu d’isolation réseau. C'est pas l'idéal, mais c’est toujours mieux que rien.</p>
<p>Bref, bloquez le port 23 et passez à SSH. C’est quand même pas compliqué, meuuuuh !!</p>
<p>
<a href="https://thehackernews.com/2026/03/critical-telnetd-flaw-cve-2026-32746.html">Source</a>
</p>