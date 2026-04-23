---
title: "Cloudflare /crawl - Aspirez un site entier en un seul appel API"
author: "Korben"
date: 2026-03-11T13:47:06.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/api-services"
  - "tutoriels-guides/tutoriels-avances"
  - "Cloudflare"
  - "crawler"
  - "web scraping"
rss_source: Blog
url: https://korben.info/cloudflare-browser-rendering-crawl-api.html
note: 0
seen: false
---

<p>Crawler un site entier, ça devrait pas être aussi compliqué. Et pourtant, entre les scripts maison qui cassent tous les 2 jours et les headless browsers qui bouffent de la RAM comme pas permis, c'est assez la galère ! Du coup, Cloudflare, dans sa grande bonté (lol) vient de sortir un endpoint <code>/crawl</code> (en open beta) dans la section Browser Rendering qui simplifie tout ça... vous balancez une URL dessus et hop, ça ASPIRE tout le site (oui oui).</p>
<p>En gros, vous envoyez une requête POST avec l'URL de départ, et le service se charge de découvrir les pages (via le sitemap, les liens internes, ou les deux), de les générer dans un navigateur headless, et de vous renvoyer le contenu en HTML, Markdown ou même en JSON structuré grâce à Workers AI. Le tout de manière asynchron ! Vous, vous récupérez juste un job ID et vous revenez plus tard chercher les résultats quand c'est prêt.</p>
<h2 id="créer-votre-token-api">Créer votre token API</h2>
<p>Avant toute chose, il vous faut un token API Cloudflare avec la permission &quot;Browser Rendering - Edit&quot;. Rendez-vous dans votre dashboard Cloudflare, section API Tokens, et créez-en un nouveau. Notez aussi votre Account ID (visible dans l'URL du dashboard ou dans la section Overview de n'importe quel domaine).</p>
<h2 id="lancer-un-crawl">Lancer un crawl</h2>
<p>Là, ensuite c'est hyper simple. Un seul appel curl suffit :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -X POST &#34;https://api.cloudflare.com/client/v4/accounts/VOTRE_ACCOUNT_ID/browser-rendering/crawl&#34; \
</span></span><span class="line"><span class="cl"> -H &#34;Authorization: Bearer VOTRE_TOKEN&#34; \
</span></span><span class="line"><span class="cl"> -H &#34;Content-Type: application/json&#34; \
</span></span><span class="line"><span class="cl"> -d &#39;{&#34;url&#34;: &#34;https://example.com&#34;}&#39;
</span></span></code></pre><p>Et là, vous récupérez un job ID en retour (genre <code>c7f8s2d9-a8e7-4b6e-...</code>). Par défaut, le crawler va explorer 10 pages max avec une profondeur quasi illimitée. Mais bon, 10 pages c'est vite limité, du coup vous pouvez ajuster tout ça comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -X POST &#34;https://api.cloudflare.com/client/v4/accounts/VOTRE_ACCOUNT_ID/browser-rendering/crawl&#34; \
</span></span><span class="line"><span class="cl"> -H &#34;Authorization: Bearer VOTRE_TOKEN&#34; \
</span></span><span class="line"><span class="cl"> -H &#34;Content-Type: application/json&#34; \
</span></span><span class="line"><span class="cl"> -d &#39;{
</span></span><span class="line"><span class="cl"> &#34;url&#34;: &#34;https://example.com/docs&#34;,
</span></span><span class="line"><span class="cl"> &#34;limit&#34;: 50,
</span></span><span class="line"><span class="cl"> &#34;depth&#34;: 3,
</span></span><span class="line"><span class="cl"> &#34;formats&#34;: [&#34;markdown&#34;],
</span></span><span class="line"><span class="cl"> &#34;render&#34;: false,
</span></span><span class="line"><span class="cl"> &#34;options&#34;: {
</span></span><span class="line"><span class="cl"> &#34;includePatterns&#34;: [&#34;https://example.com/docs/**&#34;],
</span></span><span class="line"><span class="cl"> &#34;excludePatterns&#34;: [&#34;**/changelog/**&#34;]
</span></span><span class="line"><span class="cl"> }
</span></span><span class="line"><span class="cl"> }&#39;
</span></span></code></pre><p>Le paramètre <code>render: false</code> permet de récupérer le HTML brut sans lancer de navigateur headless, c'est carrément plus rapide pour les sites statiques. Sachez quand même que pendant la beta, ce mode n'est pas facturé ! Youpi !</p>
<h2 id="récupérer-les-résultats">Récupérer les résultats</h2>
<p>Une fois le crawl lancé, vous interrogez le job avec un GET :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl &#34;https://api.cloudflare.com/client/v4/accounts/VOTRE_ACCOUNT_ID/browser-rendering/crawl/VOTRE_JOB_ID&#34; \
</span></span><span class="line"><span class="cl"> -H &#34;Authorization: Bearer VOTRE_TOKEN&#34;
</span></span></code></pre><p>Vous obtenez alors le statut (<code>running</code>, <code>completed</code>, <code>errored</code>...) et la liste des pages crawlées avec leur contenu dans le format demandé. Si le résultat dépasse 10 Mo, un curseur de pagination est inclus pour récupérer la suite.</p>
<h2 id="les-options-qui-tuent">Les options qui tuent</h2>
<p>Y'a quelques paramètres bien pensés pour les cas plus avancés :</p>
<ul>
<li><code>modifiedSince</code> et <code>maxAge</code> pour du crawling incrémental (ne re-crawler que les pages modifiées récemment)</li>
<li><code>source: &quot;sitemaps&quot;</code> pour ne suivre que le sitemap au lieu de parser tous les liens</li>
<li><code>jsonOptions</code> avec un prompt Workers AI pour extraire des données structurées automatiquement (genre récupérer le nom, le prix et le stock de 500 fiches produit d'un e-commerce en une seule passe)</li>
<li><code>rejectResourceTypes</code> pour bloquer images, fonts et CSS et accélérer le crawl</li>
<li><code>authenticate</code> pour les sites protégés par une auth HTTP basique</li>
</ul>
<p>Attention quand même, y'a quelques subtilités à savoir. Un job peut tourner 7 jours max et les résultats sont conservés 14 jours seulement, du coup pensez à les récupérer vite. Le crawler respecte le <code>robots.txt</code> (y compris le <code>crawl-delay</code>), et si un site vous bloque, les URLs apparaissent comme &quot;disallowed&quot; dans les résultats. Sauf que ça ne vous dit pas pourquoi, faudra aller checker le robots.txt vous-même.</p>
<p>Voilà, cette &quot;merveille&quot; pour les scrappeurs fous est dispo sur les plans Free et Paid de
<a href="https://developers.cloudflare.com/browser-rendering/rest-api/crawl-endpoint/">Workers</a>
, et si vous voulez aller plus loin, Cloudflare propose aussi des endpoints pour les
<a href="https://korben.info/cloudflare-bloque-ia-pay-per-crawl.html">screenshots, les PDF et le scraping ciblé</a>
.</p>
<p>Voilà, un petit crawler inclus dans le plan Free de Workers, qui respecte le robots.txt et qui sort du Markdown ou du JSON structuré... je vais surveiller ça de près !</p>