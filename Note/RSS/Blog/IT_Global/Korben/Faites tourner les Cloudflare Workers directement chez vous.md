---
title: "Faites tourner les Cloudflare Workers directement chez vous"
author: "Korben"
date: 2026-03-18T16:17:40.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement"
  - "self-hosting"
  - "Cloudflare"
  - "runtime"
  - "self-hosting"
  - "workerd"
rss_source: Blog
url: https://korben.info/workerd-cloudflare-runtime-javascript.html
note: 0
seen: false
---

<p>Pour faire tourner du JavaScript côté serveur, y'a pas que Node.js dans la vie. Y'a maintenant
<a href="https://github.com/cloudflare/workerd">workerd</a>
(prononcez &quot;worker-dee&quot;), qui est le runtime open source de Cloudflare, celui-là même qui fait tourner les Workers en prod (le service tourne depuis 2017, le runtime est open source depuis 2022), et que vous pouvez l'installer sur votre Debian, votre Mac ou même votre PC Windows avec un simple <code>npx</code>.</p>
<p>Mais alors pourquoi s'embêter avec un énième runtime JS ?</p>
<p>Hé bien parce que celui-ci n'est pas un runtime généraliste. C'est un vrai serveur HTTP pur et dur, basé sur le moteur V8 de Chrome, conçu pour recevoir des requêtes et y répondre. Pas de filesystem, pas d'accès disque sauvage... ici, votre code vit dans un isolate V8, bien cloisonné, et communique avec l'extérieur uniquement via des bindings explicites qu'on appelle des &quot;capabilities&quot;. En gros, votre Worker ne peut accéder qu'aux ressources qu'on lui a branchées dans son fichier de config
<a href="https://capnproto.org/">Cap'n Proto</a>
.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/workerd-cloudflare-runtime-javascript/workerd-cloudflare-runtime-javascript-2.png" alt="" loading="lazy" decoding="async">
<p>Et cela a plein d'avantages ! Par exemple, les attaques SSRF classiques c'est mort ! Et n'oubliez pas que c'est du JavaScript pur, donc y'a pas d'affreux <code>require('fs')</code> ni de <code>child_process</code> qui traîne.</p>
<p>Et le concept qui tue, ce sont les nanoservices. En fait, faut imaginer des microservices, mais qui tournent tous dans le même processus Linux, sur le même thread. Comme ça quand un nanoservice en appelle un autre, y'a zéro latence TCP, c'est un juste appel de fonction local !</p>
<p>Et vous pouvez en faire tourner des centaines sur un seul serveur parce que les API sont implémentées en C++ natif et tous les isolates V8 partagent le même code compilé en mémoire. C'est carrément pas intuitif, mais visiblement, ça tient la route.</p>
<p>Côté rétrocompatibilité, c'est cool puisque chaque Worker déclare une &quot;date de compatibilité&quot; dans son fichier <code>.capnp</code>. Comme ça, vous fixez <code>compatibilityDate = &quot;2024-06-15&quot;</code> et le runtime vous garantit que les API <code>fetch()</code> et <code>WebCrypto</code> se comporteront toujours comme à cette date-là, même si le binaire a été recompilé 200 fois depuis. Des releases sortant tous les jours, cette garantie n'est pas anecdotique !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/workerd-cloudflare-runtime-javascript/workerd-cloudflare-runtime-javascript-3.png" alt="" loading="lazy" decoding="async">
<p>Cap'n Proto, un format de sérialisation binaire créé par Kenton Varda, le même gars qui est derrière Protocol Buffers chez Google (excusez du peu). C'est un poil déroutant au début si vous êtes habitués au YAML ou au JSON, mais c'est très efficace et hyper rapide. Et pour ceux qui bossent déjà avec
<a href="https://korben.info/cloudflare-calls-plateforme-webrtc-serverless-apps-temps-reel.html">l'écosystème Cloudflare</a>
parce que vous avez l'Amérique qui coule dans les veines, sachez le runtime s'intègre nickel avec l'outil CLI Wrangler pour le dev local.</p>
<p>Par contre, attention, ce n'est PAS un sandbox sécurisé. Cloudflare le dit cash : si vous faites tourner du code potentiellement malveillant, faudra l'isoler dans une VM KVM ou un conteneur Docker. Hé oui les amis, en prod chez Cloudflare, y'a des couches de sécurité supplémentaires (isolation kernel Linux, patching V8 en urgence, segmentation par profil de risque) que le runtime seul ne fournit pas.</p>
<p>Le problème, c'est surtout Spectre et les bugs du moteur V8... car ça reste du code C++ compilé avec clang derrière. Après, pour du self-hosting de vos propres Workers sur votre VPS Ubuntu, c'est largement suffisant.</p>
<p>Maintenant pour tester concrétement c'est mui rapido.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npx workerd serve config.capnp
</span></span></code></pre><p>Vous écrivez un petit <code>hello.js</code> avec un <code>addEventListener(&quot;fetch&quot;)</code>, et hop, vous avez un serveur HTTP prêt à répondre sur le port 8080 de votre localhost. Et le truc sympa, c'est qu'on peut aussi l'utiliser comme proxy HTTP programmable !</p>
<p>Comme ça, au lieu de configurer des règles nginx ou Apache absconses, vous écrivez du JavaScript standard avec des <code>Request</code> et <code>Response</code> pour intercepter et router vos requêtes. Franchement, pour du reverse proxy avec de la logique métier, c'est quand même plus lisible que du <code>location ~ ^/api/(.*)$</code>. ^^</p>
<p>D'ailleurs, côté API, tout est basé sur les standards W3C : <code>fetch()</code>, <code>URL</code>, <code>WebCrypto</code>, <code>TextEncoder</code>, les classiques quoi. Donc si vous savez écrire du JS pour Firefox ou Chrome, vous savez écrire pour le moteur des Workers. Pas de modules propriétaires bizarres, contrairement à Node.js et tous ses packages <code>http</code>, <code>net</code>, <code>stream</code>...</p>
<p>Bref, c'est costaud, c'est gratuit, et ça tourne partout, avec un dossier <code>samples/</code> plein de configs prêtes à l'emploi.</p>
<p>Allez, je vous libère,
<a href="https://blog.cloudflare.com/workerd-open-source-workers-runtime/">vous pouvez foncer tester ça !!</a>
</p>