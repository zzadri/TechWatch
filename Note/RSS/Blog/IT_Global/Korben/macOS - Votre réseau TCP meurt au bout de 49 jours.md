---
title: "macOS - Votre réseau TCP meurt au bout de 49 jours"
author: "Korben"
date: 2026-04-07T11:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "cybersecurite/failles-vulnerabilites"
  - "bug macOS TCP"
  - "overflow 32 bits"
  - "XNU kernel"
rss_source: Blog
url: https://korben.info/macos-tcp-bombe-49-jours.html
note: 0
seen: false
---

<p>49 jours, les amis, c'est la durée de vie d'un Mac avant que son réseau TCP ne s'effondre dans un silence assourdissant. Il suffit d'un overflow d'entier 32 bits dans le kernel XNU, une horloge interne qui se bloque, et hop, plus moyen d'ouvrir la moindre connexion. Le ping marche toujours, parce qu'ICMP se fout du TCP, mais pour le reste... c'est reboot obligatoire ou rien.</p>
<p>Pour savoir combien de temps il vous reste, tapez <code>uptime</code> dans le Terminal. Si votre Mac sous macOS Sequoia, Sonoma ou même Ventura tourne depuis plus de 7 semaines sans redémarrage, c'est le moment d'y remédier car le bug touche toutes les versions.</p>
<p>C'est l'équipe de
<a href="https://photon.codes/blog/we-found-a-ticking-time-bomb-in-macos-tcp-networking">Photon</a>
qui a révélé le problème. Celui-ci est apparu sur une flotte de Macs dédiée à la télémétrie iMessage. Pile 49,7 jours après le dernier redémarrage, plusieurs machines ont lâché en même temps. Plus de nouvelles connexions réseau, mais le ping répondait toujours.</p>
<p>En fouillant le code du
<a href="https://korben.info/kext-macos-ios-vulnerable.html">noyau XNU d'Apple</a>
(qui est open source, faut le rappeler), ils sont tombé sur une variable <code>tcp_now</code>, qui est un compteur 32 bits qui s'incrémente chaque milliseconde. En gros, imaginez un compteur kilométrique qui arrivé au max (environ 4,3 milliards), repasse à zéro.</p>
<p>Sauf que le code contient un garde fou censé empêcher l'horloge de reculer du genre &quot;<em>si la nouvelle valeur est plus petite que l'ancienne, on ne met pas à jour</em>&quot;. Ça a l'air malin mais en fait, au moment du rebouclage, patatras : la nouvelle valeur (proche de zéro) est forcément plus petite que l'ancienne (proche du max), du coup le garde fou bloque tout et l'horloge TCP se fige.</p>
<p>Et ensuite, ça part en cascade. Les connexions fermées restent normalement en TIME_WAIT durant 30 secondes sur macOS, avant d'être nettoyées par <code>tcp_gc()</code> mais avec l'horloge gelée, ce nettoyage ne se fait plus. Un <code>netstat -an | grep TIME_WAIT</code> montre alors la catastrophe en temps réel avec des connexions mortes qui s'empilent, et finissent par bouffer les 16 384 ports éphémères (range 49152-65535 sur macOS) restant... Et au bout de quelques heures, plus rien ne passe !</p>
<p>Photon a laissé tourner deux machines après l'overflow pour voir. Neuf heures plus tard, l'une affichait 8 000 connexions zombies et un load average de 49. La machine ne faisait plus que scanner sa propre file d'attente de connexions mortes.</p>
<p>Si ça vous rappelle quelque chose, c'est normal car j'sais pas si vous vous souvenais mais Windows 95 plantait au bout du même délai pour la même raison (le fameux <code>GetTickCount()</code> en 32 bits). Le Boeing 787 avait également un souci similaire au bout de 51 jours sur ses switches réseau, sans oublier le bug de l'an 2038 sous Unix, qui est la version signée du même phénomène. 30 ans séparent certains de ces bugs qui pourtant appartiennent à la même catégorie !</p>
<p>Après flippez pas car des devs avec des Macs à plus de 600 jours d'uptime disent n'avoir jamais eu le souci. À vrai dire, le bug ne se déclencherait que si votre Mac n'a aucun trafic TCP pile au moment de l'overflow. Si votre machine cause au réseau en permanence (et c'est le cas de 99% des Macs), l'horloge passe le cap sans broncher.</p>
<p>Les machines les plus exposées sont en fait les serveurs CI/CD sous macOS, les
<a href="https://korben.info/apfel-ia-mac-apple-silicon.html">Mac mini</a>
en ferme de build Jenkins ou GitHub Actions, les Mac Pro dédiés au rendu 3D avec Blender ou Cinema 4D. Le MacBook qui passe en veille tous les soirs n'est pas vraiment concerné (le compteur <code>tcp_now</code> ne tourne pas pendant la veille, donc le délai de 49 jours ne concerne que le temps d'activité réel).</p>
<p>Maintenant pour vérifier votre compte à rebours personnel, ouvrez un Terminal et collez y ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">boot_sec=$(sysctl kern.boottime | grep -o &#39;sec = [0-9]*&#39; | head -1 | awk &#39;{print $3}&#39;)
</span></span><span class="line"><span class="cl">now_sec=$(date +%s)
</span></span><span class="line"><span class="cl">remain=$(( 4294967 - (now_sec - boot_sec) ))
</span></span><span class="line"><span class="cl">echo &#34;Temps restant avant overflow : $((remain/3600))h $((remain%3600/60))m&#34;
</span></span></code></pre><p>Apple n'a pour l'instant rien communiqué sur le sujet, ce qui n'est guère surprenant vu que
<a href="https://korben.info/faille-apple-puce-t2.html">c'est un peu leur spécialité</a>
quand une vulnérabilité est remontée. L'équipe de Photon dit travailler sur un moyen de contourner le problème qui éviterait de rebooter, mais en attendant, le seul fix c'est le redémarrage, qui remet le compteur à zéro... et relance le compte à rebours.</p>
<p>Bref, y'a rien à faire si ce n'est de vérifier votre uptime et faire éventuellement un petit reboot préventif. Tic tac, l'horloge tourne ^^.</p>
<p>
<a href="https://photon.codes/blog/we-found-a-ticking-time-bomb-in-macos-tcp-networking">Source</a>
</p>