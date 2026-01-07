---
title: "Dembrandt - Aspirez le design system de n'importe quel site en une commande"
author: Korben
date: Tue, 06 Jan 2026 09:30:00 +0100
type: site
subject: 
category: IT
rss-source: Blog
url: https://korben.info/dembrandt-extraction-design-system-cli.html
seen: false
---


<p>Vous bossez sur un projet et vous vous dites &quot;Tiens, le site de [insérez ici une grosse boîte] a un design plutôt bien foutu, j'aimerais bien voir comment ils ont structuré leurs css&quot;.</p>
<p>Hé bien y'a un outil pour ça, et il s'appelle <strong>
<a href="https://www.dembrandt.com/">Dembrandt</a>
</strong>.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dembrandt-extraction-design-system-cli/dembrandt-extraction-design-system-cli-2.png" alt="" loading="lazy" decoding="async">
<p><em>Dembrandt en action</em></p>
<p>En gros, c'est un petit outil en ligne de commande qui va analyser n'importe quelle URL et en extraire tout le design system : les couleurs (primaires, secondaires, variables CSS), la typographie (familles, tailles, graisses), les espacements, les bordures, les ombres et même les patterns de composants UI.</p>
<p>Le truc s'installe en une ligne avec npm (<code>npm install -g dembrandt</code>) et après vous avez juste à taper <code>dembrandt stripe.com</code> par exemple. En moins d'une seconde, l'outil va alors faire un rendu de la page avec Playwright, analyser le DOM, détecter les styles et vous ressort tout ça bien structuré avec des scores de confiance pour chaque couleur.</p>
<p>Ce que j'aime bien, c'est que ça exporte directement en JSON ou au format W3C Design Tokens si vous voulez l'utiliser avec Style Dictionary. Pratique pour alimenter votre propre design system ou pour documenter celui d'un client qui n'a jamais pris le temps de le faire... (il en faut)</p>
<p>Y'a aussi quelques options sympas comme <code>--dark-mode</code> pour extraire la palette sombre, <code>--mobile</code> pour simuler un viewport iPhone, ou <code>--browser=firefox</code> si le site que vous voulez analyser a des protections Cloudflare qui bloquent Chromium.</p>
<p>Bon, ça marche pas sur les sites qui utilisent Canvas ou WebGL pour le rendu, et faut pas s'attendre à des miracles
<a href="https://neodelta.eu/glossaire/spa">sur les SPA</a>
qui chargent tout en async. Mais pour la majorité des sites, c'est vraiment efficace.</p>
<p>Le projet est open source sous licence MIT, donc vous pouvez l'auditer, le forker, le modifier comme bon vous semble. Et niveau légalité, analyser du HTML/CSS public pour de la veille concurrentielle ou de la documentation, c'est considéré comme du fair use dans la plupart des juridictions, donc vous êtes good !</p>
<p>Bref, si vous faites du design system, de l'audit UX ou juste de la veille sur ce que font les autres, c'est un outil à garder sous le coude.</p>
<p>Merci à Lorenper pour le partage !</p>
