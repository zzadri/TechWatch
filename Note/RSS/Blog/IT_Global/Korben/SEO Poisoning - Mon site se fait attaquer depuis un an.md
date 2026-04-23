---
title: "SEO Poisoning - Mon site se fait attaquer depuis un an"
author: "Korben"
date: 2026-03-14T16:10:16.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "Google"
  - "OSINT"
  - "sécurité"
  - "SEO"
rss_source: Blog
url: https://korben.info/seo-poisoning-temoignage.html
note: 0
seen: false
---

<p>Le SEO poisoning, vous connaissez ?</p>
<p>C'est quand votre référencement se fait flinguer parce que votre site se retrouve associé à des sites de casino, de porno et de téléchargement illégal. Et devinez quoi... ça m'arrive depuis bientôt un an !</p>
<p>Tout a commencé l'année dernière quand un nom de domaine reprenant mon pseudo a été enregistré depuis la Chine. Un clone quasi parfait de korben.info, avec tout mon contenu aspiré, sauf que tous les liens avaient été remplacés par des redirections frauduleuses. Mon Patreon, mon Twitter, ma newsletter, mes liens Twitch... tout renvoyait vers des trackers douteux. En fait, ça a été fait via un service de clonage de sites à quelques yuans par mois (genre 50 yuans, soit 6 euros), capable d'aspirer l'intégralité des pages HTML, CSS, images et même l'ID Google Analytics. Sympa !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-2.png" alt="" loading="lazy" decoding="async">
<p><em>Hasard du scrapping, ils ont chopé ma version spéciale Pluribus que j'avais mise en ligne à l'époque.</em></p>
<p>Sur le coup, quand je m'en suis rendu compte, j'ai signalé le truc au registrar et j'ai attendu. Naïvement, je pensais que ça resterait un cas isolé. Par contre, attention... c'était juste l'apéro.</p>
<p>Car en décembre, ça s'est sérieusement accéléré. D'un coup, c'est pas un mais plusieurs réseaux distincts de sites qui se sont mis à publier du contenu m'associant à tout et n'importe quoi. Je vous parle de dizaines et de dizaines de sites, des .fr pour la plupart, montés de toute pièce avec du contenu bidon. Et là, bienvenue dans le monde merveilleux des PBN.</p>
<p>Un PBN, c'est un Private Blog Network. En gros, un ensemble de sites web qui ont l'air indépendants mais qui sont contrôlés par la même personne. À la base, ça sert à créer des backlinks pour faire monter un site dans les résultats de
<a href="https://korben.info/seo-ia-contenu-authentique-referencement-2025.html">référencement naturel</a>
. Ça peut être utilisé de manière plus ou moins légitime pour booster sa visibilité. Mais ça peut aussi servir à démolir celle des autres, en les noyant sous des liens toxiques, en les mélangeant avec des sites de casino en ligne, de contenus pour adultes ou de téléchargement illégal. Et c'est exactement ce qui arrive à mon site en ce moment.</p>
<p>Concrètement, dans mon cas, ça fonctionne de deux manières. La première, c'est du cloaking. Ces sites présentent à Googlebot du contenu qui reprend mes meta descriptions, mon nom, mon contenu... sauf que quand un vrai visiteur clique dessus depuis Google, il tombe sur une fausse page RedTube. Du porno, quoi. L'idée c'est que Google finisse par associer korben.info à du contenu pour adultes. La deuxième technique, c'est de noyer mon nom dans du contenu qui n'a rien à voir avec la tech. Des articles, des liens vers des casinos... Le but c'est que Google se dise &quot;<em>ah mais en fait korben.info c'est pas un média tech</em>&quot;, et que ma thématique soit complètement diluée dans les résultats de recherche.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Du coup, depuis 4 mois, mon quotidien c'est ça : contacter Google pour signaler les domaines frauduleux, écrire aux registrars pour faire fermer les noms de domaine, relancer les hébergeurs pour couper les serveurs. À vrai dire, entre les mails aux registrars, les formulaires abuse et les captures d'écran pour les dossiers, je passe 2-3 heures par jour là-dessus au lieu d'écrire des articles. J'ai même déposé des signalements auprès de la police. Première fois en 20 ans de blog que j'en arrive là !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-4.png" alt="" loading="lazy" decoding="async">
<p>Heureusement, à force de creuser, mes capacités en OSINT m'ont permis de cartographier tout le réseau : les connexions entre les sites, les gens qui se trouvent derrière... j'ai tout. Mais tant que les procédures sont en cours, je garde ça pour moi. Je ne peux pas vous mettre les captures d'écran les plus croustillantes de toute cette opération dont je suis la victime, j'en suis désolé...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-5.png" alt="" loading="lazy" decoding="async">
<p><strong>J'ai plus de place dans Maltego pour inscrire tout ce que j'ai trouvé.</strong></p>
<p>Et le problème, c'est que tous les jours, y'a des nouveaux qui apparaissent. Des .fr, des .site, des .website, des .online... Dans mon fichier disavow.txt sur la Search Console de Google, j'ai inscrit +93 domaines à rejeter.</p>
<p>Le disavow, pour ceux qui connaissent pas, c'est un fichier que vous soumettez à Google pour lui dire &quot;<em>ces liens qui pointent vers mon site, ignore-les, c'est pas moi</em>&quot;. Google dit que ses algorithmes détectent et ignorent déjà la plupart des liens toxiques automatiquement, mais le disavow reste une précaution supplémentaire. Sauf que quand vous voyez la liste s'allonger tous les jours, ça rassure pas des masses.</p>
<p>Vous le savez, le SEO c'est pas trop
<a href="https://korben.info/seo-en-direct-venez-me-voir-me-faire-demolir-par-des-experts-du-referencement.html">le domaine dans lequel je brille</a>
. Du coup, me retrouver sur mon ordi à éplucher des rapports WHOIS, des logs et des exports CSV de backlinks toxiques, c'est vraiment pas mon kiff. Et franchement, ça me fait flipper parce que mon site, c'est 20 ans de boulot et si demain il se fait blacklister ou noyer dans du contenu pourri, je perds une part de mon trafic... voire plus. Et comme Korben c'est littéralement ma vie, mon identité, c'est tout ce que j'ai.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-6.png" alt="" loading="lazy" decoding="async">
<p>Le truc dingue aussi, c'est que ces techniques datent du début des années 2010. C'est du old school mais bon, on s'y fait pas. J'ai l'impression de vider la mer avec une cuillère. Le problème c'est que ça ne s'arrête jamais. Vous en fermez 5, il en apparaît 10 !!!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/seo-poisoning-temoignage/seo-poisoning-temoignage-7.png" alt="" loading="lazy" decoding="async">
<p>Maintenant, si vous êtes dans le même cas, voici ce que vous pouvez faire. D'abord,
<a href="https://korben.info/80-bonnes-pratiques-seo.html">surveillez vos backlinks</a>
via la Search Console ou des outils comme Ahrefs.</p>
<p>Attention, ne regardez pas forcement que les nouveaux liens, vérifiez aussi les anciens qui auraient pu changer de destination. Si vous repérez des domaines louches qui pointent vers votre site, créez un fichier disavow.txt et soumettez-le à Google.</p>
<p>Ensuite, signalez les sites frauduleux aux registrars (les infos sont dans le WHOIS) et aux hébergeurs. Et si c'est grave, n'oubliez pas le signalement auprès de la police ou de la gendarmerie via cybermalvaillance. Ça crée une trace officielle, même si les suites judiciaires prennent du temps.</p>
<p>Bref, si parmi vous il y en a qui veulent me mettre un lien vers korben.info depuis leur site ou leur blog, reprendre un de , un mot sur les réseaux... ça m'aiderait. Chaque backlink sain aide à contrebalancer la merde ❤️.</p>
<p></p>