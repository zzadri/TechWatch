---
title: "Smtp-Tunnel-Proxy - Déguisez votre trafic en simples emails"
author: "Korben"
date: 2026-02-01T11:36:29.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "vie-privee-anonymat/vpn-proxy"
rss_source: Blog
url: https://korben.info/smtp-tunnel-proxy.html
note: 0
seen: false
---

<p>Ce matin, en trainant sur GitHub (mon sport du dimanche, je sais c'est triste), je suis tombé sur un truc qui m'a intéressé et qui je pense vous sera utile (comme la plupart des trucs que je présente ici) surtout si vous êtes coincé derrière un pare-feu d'entreprise totalement paranoïaque. Ou encore si votre FAI s'amuse à brider certains protocoles. Ça peut arriver dans ces cas là, on se sent un peu comme un rat en cage, à chercher la moindre petite ouverture pour respirer un peu de notre liberté.</p>
<p>Cet outil, ça s'appelle <strong>Smtp-Tunnel-Proxy</strong> et le concept c'est de faire passer tout votre trafic pour de bêtes emails. Alors vous vous dites peut-être &quot;<em>Mouais, encore un tunnel qui va ramer comme pas possible</em>&quot;, mais en creusant un peu, vous allez voir, c'est pas con.</p>
<p>En fait ce que fait ce petit script Python (ou binaire Go) c'est qu'il enveloppe vos paquets TCP dans une connexion qui ressemble à s'y méprendre à du trafic SMTP chiffré. En gros, le truc simule un handshake avec un serveur mail (comme Postfix), lance le chiffrement TLS 1.2+, et hop, une fois le tunnel établi, il balance la purée en binaire sans que le DPI (Deep Packet Inspection) puisse y voir quelque chose. Comme ça le firewall n'y comprend plus rien, le petit chou ^^.</p>
<p>C'est un peu comme un
<a href="https://korben.info/configurer-un-tunnel-ssh-pour-telecharger-sur-bittorrent.html">tunnel SSH</a>
en fait mais déguisé en serveur mail, ce qui le rend beaucoup plus discret. Parce que là où un tunnel SSH peut être repéré par sa signature un peu trop évidente, une connexion SMTP chiffrée, c'est ce qu'il y a de plus banal sur le net. Du coup, ça passe crèèèème.</p>
<p>Niveau fonctionnalités, x011 (le dev) a fait les choses bien. Le truc est multi-utilisateurs avec des secrets partagés pour l'auth, supporte le multiplexing (plusieurs connexions dans un seul tunnel), et gère même une whitelist d'IP pour éviter que n'importe qui ne squatte votre tunnel. C'est propre quoi.</p>
<p>L'installation côté serveur est simplifiée grâce notamment à un script tout fait que vous pouvez lancer sur n'importe quel petit VPS. Un petit curl et c'est réglé :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -sSL https://raw.githubusercontent.com/x011/smtp-tunnel-proxy/main/install.sh | sudo bash
</span></span></code></pre><p>Et côté client, c'est encore plus simple car une fois votre utilisateur créé sur le serveur, vous récupérez un petit fichier zip contenant tout ce qu'il faut. Vous lancez le script <code>start.bat</code> ou <code>start.sh</code>, et boum, vous avez un proxy SOCKS5 local qui tourne sur <code>127.0.0.1:1080</code>.</p>
<p>Il ne vous reste alors plus qu'à configurer votre navigateur ou vos applications pour passer par ce proxy SOCKS, et vous voilà libre comme l'air.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/smtp-tunnel-proxy/smtp-tunnel-proxy-2.png" alt="" loading="lazy" decoding="async">
<p>C'est dingue ce qu'on peut faire avec un peu d'ingéniosité, non ?</p>
<p>Attention quand même, ça reste du tunnel, donc ne faites pas de bêtises avec... A moins que le DPI en face analyse l'entropie de manière ultra poussée (ce qui est rare car coûteux en ressources), ça devrait tenir, mais ne vous croyez pas invisible pour autant. Pour
<a href="https://korben.info/byebyedpi-vpn-imposture-censure-dpi.html">contourner de la censure</a>
ou accéder à vos services hébergés à la maison depuis un wifi public bridé, c'est donc l'outil parfait. Si les mails passent, tout passe !</p>
<p>Le code est dispo sur
<a href="https://github.com/x011/smtp-tunnel-proxy">GitHub</a>
pour ceux qui veulent. Perso je me garde ça sous le coude comme ça, ni vu ni connu j't'embouille sur ton wifi bridé nord coréen là ^^.</p>