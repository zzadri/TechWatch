---
title: "CompHost - Compostez vos vieux Android en serveurs"
author: "Korben"
date: 2026-03-16T05:34:25.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "self-hosting"
  - "tutoriels-guides/tutoriels-avances"
  - "Android"
  - "recyclage"
  - "self-hosting"
  - "serveur"
  - "termux"
rss_source: Blog
url: https://korben.info/comphost-club-serveur-telephone.html
note: 0
seen: false
---

<p>Un vieux smartphone Android, c'est quoi en fait ? Un bon petit quad-core, 1 ou 2 Go de RAM, et du WiFi. Soit de quoi largement servir des pages web finalement... Hé bien
<a href="https://wiki.comphost.club/">CompHost</a>
vous montre comment en faire un serveur en quelques commandes, sans rooter quoi que ce soi. Vous faut juste Termux et basta !</p>
<p>En gros, vous installez
<a href="https://f-droid.org/">Termux depuis F-Droid</a>
sur n'importe quel Android 7+ (pour Android 5-6, y'a également une version spéciale dispo sur GitHub), vous tapez <code>pkg update &amp;&amp; pkg upgrade -y</code> puis <code>termux-setup-storage -y</code>, et hop, vous avez un environnement Linux sur votre téléphone.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/comphost-club-serveur-telephone/comphost-club-serveur-telephone-1.jpeg" alt="" loading="lazy" decoding="async">
<p><em>Un vieux téléphone qui sert des pages web, la classe quand même</em></p>
<p>De là, un <code>pkg install python</code> suivi d'un <code>python -m http.server 8080</code> et votre serveur web tourne ! Pensez surtout à lancer <code>termux-wake-lock</code> pour éviter qu'Android tue le processus en arrière-plan, sinon votre super site web ne sera pas accessible longtemps.</p>
<p>Le wiki fournit aussi des fiches PDF, une cheatsheet Termux et des présentations annotées pour ceux qui voudraient par exemple animer un atelier. Bref, j'ai trouvé ça plutôt bien ficelé !</p>
<p>D'ailleurs, j'sais pas si vous vous souvenais, mais
<a href="https://korben.info/far-computer-vieux-telephone-serveur-web-postmarketos.html">je vous avais déjà parlé de Far Computer</a>
qui héberge un site sur un Fairphone 2 avec PostmarketOS, sauf que CompHost a une approche un peu différente. En fait y'a pas besoin de flasher l'OS ni besoin d'avoir un PC Linux sous la main et encore moins un bootloader à déverrouiller. Vous installez une app, vous ouvrez un terminal, c'est parti. Du coup c'est bien plus accessible, même si faut quand même être prêt à taper quelques commandes.</p>
<p>Le truc sympa avec Termux, c'est que ça tourne dans une sandbox Android classique, donc sans root et le gestionnaire de paquets <code>pkg</code> donne accès à tout ce qu'il faut pour héberger ce que vous voulez comme Python, Node.js, nginx...</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/comphost-club-serveur-telephone/comphost-club-serveur-telephone-1.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et aussi bizarre que ça puisse paraitre, votre vieux Samsung de 2018 a largement les specs pour servir un site statique, une petite API ou même un wiki perso. Et vu que ces machins consomment que dalle en électricité (2-3 watts à otut casser), c'est carrément viable comme micro-serveur permanent branché dans un coin (surveillez quand même l'état de la batterie, les vieilles cellules Li-ion n'aiment pas forcement rester en charge 24/7).</p>
<p>Après côté limites, attention, c'est pas pour iPhone et pour les Android vraiment antiques (genre Android 4 et moins), le wiki renvoie vers PostmarketOS qui flashe une vraie distrib Linux sur le mobile... là c'est plus technique, par contre.</p>
<p>Ce projet CompHost est dispo sur
<a href="https://gitlab.com/mar_ver/wiki.comphost.club/">GitLab</a>
et comme ça, au moins, plutôt que de jeter vos appareils, vous leur filez une utilité concrète. Puis ça permet de piger ce qu'est vraiment un serveur web... Et quand je vois que
<a href="https://korben.info/smartphones-cluster-kubernetes-postmarketos.html">certains montent même des clusters Kubernetes avec des vieux smartphones</a>
, je me dit que y'a vraiment un filon à creuser côté recyclage / compostage de vieux matos.</p>
<p>Et qui sait, peut-être qu'un jour, Korben.info tournera sur l'un de ces trucs ?</p>