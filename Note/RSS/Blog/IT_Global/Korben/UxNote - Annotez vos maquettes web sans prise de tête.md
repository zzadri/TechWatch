---
title: "UxNote - Annotez vos maquettes web sans prise de tête"
author: "Korben"
date: 2026-02-01T18:08:37.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "developpement/web-developpement"
  - "annotation web"
rss_source: Blog
url: https://korben.info/uxnote-annotation-page-web.html
note: 0
seen: false
---

<p>Il y a quelques jours, un lecteur (merci Benjamin !) m'a envoyé un outil qu'il a bricolé lui-même avec Codex d'OpenAI et ça touche une petite corde sensible chez moi, d'où le fait que je vous en parle.</p>
<p>C'est pas souvent que je bosse avec des clients sur autre chose que des articles mais il m'est arrivé par le passé qu'un client m'envoie ses retours par mail, avec des captures d'écran floues, des flèches rouges partout et des commentaires du genre &quot;<em>le truc là, à gauche, je sais pas trop ??</em>&quot;.</p>
<p>Alors de mon côté, j'ai testé pas mal de solutions pour évier ça mais j'ai rien trouvé de foufou... Figma par exemple c'est top pour les retours mais faut que le client crée un compte (et ça, c'est jamais gagné), Marker.io c'est bien fichu mais c'est payant. J'avais même essayé Loom à un moment, mais bon, leur demander d'enregistrer leur écran c'était trop compliqué.</p>
<p>Alors que UxNote, lui, règle exactement ce problème sans rien de tout ça !</p>
<p>En fait, ça permet d'intégrer une balise JavaScript dans votre page (juste avant le <code>&lt;/body&gt;</code>) et hop, une petite toolbar apparaît.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="o">&lt;</span><span class="n">script</span> <span class="n">src</span><span class="o">=</span><span class="s2">&#34;https://github.com/ninefortyonestudio/uxnote/releases/download/v1.0.0/uxnote.min-v1.0.0.js&#34;</span><span class="o">&gt;&lt;/</span><span class="n">script</span><span class="o">&gt;</span>
</span></span></code></pre><p>Votre client peut alors surligner du texte, épingler des éléments avec des badges numérotés, ajouter des commentaires... et surtout, exporter tout ça proprement en JSON ou l'envoyer direct par mail.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/uxnote-annotation-page-web/uxnote-annotation-page-web-2.png" alt="" loading="lazy" decoding="async">
<p>Comme ça, fini le chaos habituel des retours clients façon &quot;<em>j'ai annoté le PDF que j'ai imprimé puis scanné</em>&quot;. Là, les commentaires sont directement contextualisés sur la page, exactement là où ils doivent être. C'est vrai que des outils d'annotation web existent depuis des lustres, mais UxNote a choisi le stockage 100% local (via le localStorage) plutôt que de monter un backend avec des comptes utilisateurs. Et c'est ce qui fait toute la différence niveau simplicité, avec les autres outils.</p>
<p>Par contre attention, si votre client vide son cache navigateur, il perd ses annotations... Perso je vous recommande donc de faire l'export JSON dès que possible pour éviter les mauvaises surprises.</p>
<p>L'outil propose aussi un mode &quot;assombrissement&quot; qui met en évidence la zone annotée (pratique pour se concentrer), des couleurs personnalisables, et même la possibilité de bloquer certains éléments de l'annotation avec l'attribut <code>data-uxnote-ignore</code>. Ça fonctionne sur les environnements de staging, en local, et même sur les
<a href="https://developer.mozilla.org/fr/docs/Glossary/SPA">SPA</a>
... sauf si vous avez une CSP ultra stricte, auquel cas faudra autoriser le script et les styles inline dans votre config.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/uxnote-annotation-page-web/uxnote-annotation-page-web-3.png" alt="" loading="lazy" decoding="async">
<p>Bref, si vous bossez avec des clients qui ont du mal à exprimer leurs retours autrement qu'en pièces jointes de 15 Mo,
<a href="https://uxnote.ninefortyone.studio/">UxNote</a>
pourrait bien sauver les quelques cheveux qu'il vous reste. Et en plus c'est gratuit, open source et
<a href="https://github.com/ninefortyonestudio/uxnote">disponible sur GitHub</a>
.</p>
<p>Que demande le peuple ???</p>
<p>Merci Benjamin !</p>