---
title: "Web-Check - Radiographiez n'importe quel site en un clic"
author: Korben
date: Tue, 06 Jan 2026 17:58:33 +0100
type: site
subject: 
category: IT
rss-source: Blog
url: https://korben.info/web-check-outil-osint-analyse-site-securite.html
seen: false
---


<p>Vous vous êtes déjà demandé ce que cache vraiment un site web ? Genre, au-delà de sa jolie façade ? Hé bien je vous présente
<a href="https://github.com/Lissy93/web-check">Web-Check</a>
, un scanner OSINT qui va déshabiller n'importe quel domaine pour vous montrer tout ce qui se passe sous le capot.</p>
<p>Je vous ai déjà parlé
<a href="https://korben.info/osint-rocks-outils-investigation-navigateur.html">d'OSINT.rocks</a>
qui centralise pas mal d'outils d'investigation. Et bien là, c'est un peu le même délire mais orienté analyse de sites web. Vous balancez une URL et hop, le projet vous ressort un rapport complet avec tout ce qu'il y a à savoir : certificat SSL, enregistrements DNS, en-têtes HTTP, géolocalisation du serveur, ports ouverts, stack technique utilisée... Bref, une vraie radio du site.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/web-check-outil-osint-analyse-site-securite/web-check-outil-osint-analyse-site-securite-2.png" alt="" loading="lazy" decoding="async">
<p>Ce qui est cool avec cette boîte à outils, c'est qu'elle ne se contente pas de gratter la surface puisque ça effectue plus de 30 types d'analyses différentes ! Vous voulez savoir si un site utilise un WAF (Web Application Firewall) ? Vérifier la configuration email (SPF, DKIM, DMARC) ? Voir l'historique du domaine via la Wayback Machine ? Tout est possible ! Et même les Core Web Vitals pour les obsédés de la performance !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/web-check-outil-osint-analyse-site-securite/web-check-outil-osint-analyse-site-securite-3.png" alt="" loading="lazy" decoding="async">
<p>Pour l'installer, c'est ultra simple. Si vous êtes team Docker (et vous devriez l'être), une seule commande suffit :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">docker run -p 3000:3000 lissy93/web-check
</span></span></code></pre><p>Et vous avez votre instance perso qui tourne sur localhost:3000. Pas besoin de galérer avec des dépendances ou de configurer quoi que ce soit. Du coup, vous pouvez scanner vos propres sites sans que vos requêtes passent par un service tiers.</p>
<p>Pratique pour les paranos de la vie privée !</p>
<p>Le projet tourne sous TypeScript avec Astro en front, et tout le code est disponible sur GitHub sous licence MIT. Ça veut dire que vous pouvez le modifier, l'héberger où vous voulez, et même contribuer si le coeur vous en dit.</p>
<p>La partie détection de stack technique me plait beaucoup. C'est un peu comme ce que fait
<a href="https://korben.info/ssh-audit-outil-indispensable-securiser-vos-serveurs.html">SSH-Audit pour les serveurs</a>
, sauf que l'outil identifie automatiquement les frameworks, CMS, bibliothèques JavaScript et autres composants utilisés par un site. Super utile donc pour les pentesters qui veulent mapper rapidement une cible, ou simplement pour les curieux qui se demandent &quot;tiens, c'est quoi cette techno qu'ils utilisent ?&quot;.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/web-check-outil-osint-analyse-site-securite/web-check-outil-osint-analyse-site-securite-4.png" alt="" loading="lazy" decoding="async">
<p>Vous avez aussi une démo en ligne sur
<a href="https://web-check.xyz/">web-check.xyz</a>
si vous voulez tester avant d'installer quoi que ce soit. Mais bon, pour une utilisation régulière, je vous conseille vraiment l'instance locale. C'est plus rapide et vous gardez le contrôle sur vos données.</p>
<p>Voilà, si vous bossez dans la sécu, si vous êtes journaliste d'investigation, ou si vous êtes juste curieux de savoir ce que racontent les sites que vous visitez, ce scanner OSINT devrait rejoindre votre boîte à outils.</p>
<p>Allez jeter un œil, et vous me remercierez je pense !</p>
