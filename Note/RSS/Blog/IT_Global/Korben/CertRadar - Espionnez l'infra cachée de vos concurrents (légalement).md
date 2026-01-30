---
title: "CertRadar - Espionnez l'infra cachée de vos concurrents (légalement)"
author: "Korben"
date: 2026-01-26T11:07:55.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hacking-pentest"
  - "cybersecurite/outils-securite"
  - "certificat SSL"
  - "OSINT"
  - "pentest"
  - "reconnaissance de domaine"
rss_source: Blog
url: https://korben.info/certradar-espionnage-certificats-ssl.html
note: 0
seen: false
---

<p>Vos concurrents vous cachent des choses. Enfin, j'crois ^^</p>
<p>Leur infrastructure secrète, leurs projets en cours, leurs lancements prévus... Et pourtant, une bonne partie de tout ça est en fait visible si on sait où regarder...</p>
<p>Comment ? Grâce aux logs <strong>Certificate Transparency</strong>, c'est-à-dire les registres publics où les autorités de certification reconnues par les navigateurs enregistrent les certificats SSL qu'elles émettent.</p>
<p>Du coup, quand une boîte prépare un nouveau service sur staging.secret-project.example.com, hop, le certificat SSL est enregistré dans les logs CT et devient visible pour qui sait chercher. Et c'est exactement à ça que sert
<a href="https://certradar.net/">CertRadar</a>
, un outil gratuit qui va fouiller ces logs pour vous.</p>
<p>Perso j'adore ce genre d'outil pour le pentest et la veille concurrentielle. Vous tapez un domaine et bam, vous récupérez une bonne partie des sous-domaines qui ont eu un certificat SSL. Y'a de quoi faire pleurer un admin sys qui pensait que son serveur de dev était bien planqué !</p>
<p>CertRadar propose plusieurs modules. Le <strong>Cert Log Search</strong> qui est le coeur du truc, fouille les logs CT pour trouver les certificats émis pour un domaine. Le <strong>TLS Scanner</strong> analyse la config TLS de n'importe quel serveur (versions supportées, ciphers, tout ça). Le <strong>Header Search</strong> inspecte les en-têtes HTTP. Y'a aussi un <strong>RDAP Lookup</strong> pour les infos whois, un <strong>Domain Health</strong> pour vérifier la santé globale d'un domaine, et même un <strong>Multi-Domain Report</strong> pour analyser plusieurs domaines d'un coup.</p>
<p>Maintenant, mettons que vous voulez cartographier l'infrastructure de votre concurrent. Vous entrez leur domaine principal dans le Cert Log Search, et vous récupérez une liste de leurs sous-domaines visibles dans les logs CT : api.example.com, staging.example.com, admin-panel.example.com, dev-v2.example.com... Certains noms sont parfois très parlants sur les projets en cours !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/certradar-espionnage-certificats-ssl/certradar-espionnage-certificats-ssl-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>D'ailleurs, si vous cherchez d'autres méthodes pour
<a href="https://korben.info/comment-trouver-les-sous-domaines-de-nimporte-quel-site.html">trouver les sous-domaines d'un site</a>
, j'avais déjà parlé de SubFinder qui fait ça en ligne de commande.</p>
<p>La différence avec CertRadar c'est que tout se passe dans le navigateur, pas besoin d'installer quoi que ce soit. Vous allez sur le site, vous tapez votre requête, et vous avez vos résultats. Hyper fastoche.</p>
<p>Pour ceux qui font de la sécu, c'est clairement un outil qui a sa place dans votre arsenal. La partie Cert Log Search et RDAP c'est de la reconnaissance passive pure, vous ne touchez pas aux serveurs cibles. Par contre le TLS Scanner et le Header Search vont activement interroger les serveurs, donc à utiliser uniquement sur des domaines où vous avez l'autorisation. Vous pouvez découvrir des endpoints oubliés, des serveurs de staging exposés, des APIs non documentées... Bref, tout ce que les équipes IT auraient préféré garder discret.</p>
<p>Et comme les logs Certificate Transparency sont publics par design (c'est fait pour améliorer la transparence et détecter les certificats frauduleux), consulter ces données est parfaitement légal. James Bond peut aller se rhabiller, la vraie surveillance se fait en open source maintenant !</p>
<p>Si vous voulez jouer les espions légaux, c'est cadeau les copains. Comme d'hab que du bon ici ^^</p>