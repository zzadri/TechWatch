---
title: "Textarea - Un éditeur de texte qui vit sa meilleure vie dans son URL"
author: "Korben"
date: 2026-01-22T17:59:26.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/logiciels-libres"
  - "éditeur minimaliste"
rss_source: Blog
url: https://korben.info/textarea-github-minimalist-editeur.html
note: 0
seen: false
---

<p>Ah ils sont chaud bouillants les développeurs en ce moment ! Surtout quand je tombe sur une pépite comme <strong>
<a href="https://textarea.my/">textarea</a>
</strong>, je me dis que la recherche des choses simples façon Herta a encore de beaux jours devant elle.</p>
<p>J'sais pas si on peut le qualifier d'éditeur le plus minimaliste du monde mais c'est sûr qu'il n'y a pas de chichi ni de menus à rallonge dedans... Cet outil vit côté client dans votre navigateur et sa particularité c'est qu'il peut stocker ce que vous écrivez directement dans le &quot;hash&quot; (#) de l'URL. En gros, vous tapez votre prose, et hop, l'adresse dans votre barre de navigation s'allonge au fur et à mesure, contenant toutes vos données compressées.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">https://textarea.my/#U1YITswpLVHISS1WSMzNLOZyLM3KLy1KUc8ozdRRyM9TKEktLkkFkhUliUWpiQqpQKWJCmWZqQpAcYWk1JycVAVFRQA=
</span></span></code></pre><p>Vos notes resteront au chaud dans votre localStorage (soumis aux quotas habituels de votre navigateur) ainsi que dans cette fameuse URL que vous pouvez copier-coller pour partager votre texte. <strong>Textarea</strong> utilise l'algorithme <em>deflate</em> pour compresser vos données, ce qui lui permet de maximiser ce qu'on peut faire tenir dans une URL avant de venir heurter la limite de longueur du navigateur.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/textarea-github-minimalist-editeur/textarea-github-minimalist-editeur-1.webp" alt="" loading="lazy" decoding="async">
<p><em>L'interface de textarea.my - difficile de faire plus épuré (
<a href="https://textarea.my">Source</a>
)</em></p>
<p>Si vous avez déjà goûté à d'autres éditeurs &quot;Distraction-Free&quot;, vous savez à quel point c'est reposant pour l'esprit de ne pas avoir 50 boutons qui clignotent partout. Et comme ici, on est sur du pur Markdown, vous pouvez même bidouiller le style de votre document en modifiant l'élément `` via les DevTools. Et si vous maîtrisez la syntaxe, sachez que l'outil gère même quelques paramètres de style directement dans l'URL. C'est pas piqué des vers !</p>
<p>Le truc marrant dans cet éditeur c'est son <code>/qr</code> qui lorsque vous l'ajoutez à la fin de l'URL vous permet d'avoir un joli QR Code de votre note. Comme ça y'a plus qu'à le scanner et hop, vous avez le document. Pratique pour transférer une note sur votre mobile sans vous embêter avec un service de synchro quelconque.</p>
<p>Voilà, je vous laisse essayer ça, et vous m'en direz des nouvelles. C'est dispo en open source
<a href="https://github.com/antonmedv/textarea">sur GitHub en cliquant ici</a>
.</p>
<p>
<a href="https://textarea.my/">Écrivez bien !</a>
</p>