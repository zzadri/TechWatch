---
title: "Bookokrat - Le lecteur EPUB pour les accros du terminal"
author: "Korben"
date: 2026-01-22T11:49:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "multimedia-culture/livres-ebooks"
  - "abonnement ebook"
  - "CLI"
  - "commande terminal"
  - "EPUB"
  - "Rust"
rss_source: Blog
url: https://korben.info/bookokrat-le-lecteur-epub-pour-les-accros-du-terminal.html
note: 0
seen: false
---

<p>Vous vous souvenez de l'époque où rien que de lire un texte sur un écran noir suffisait à notre bonheur ? C'était un temps où chaque pixel comptait et où la souris était encore en option... Alalala, hé bien, pour ceux qui ont gardé cette âme pure ou qui passent la plupart de leur temps dans un shell, je vous ai déniché <strong>
<a href="https://github.com/bugzmanov/bookokrat">Bookokrat</a>
</strong>, un lecteur EPUB conçu EXCLUSIVEMENT pour votre terminal.</p>
<p>Vous allez voir c'est super pour lire des livres pendant le boulot discretos ^^.</p>
<p>L'outil propose une interface en &quot;split-view&quot; avec les EPUB de votre répertoire courant à gauche et votre lecteur à droite. Et malgré le côté austère du terminal, Bookokrat ne fait pas de compromis puisqu'il gère comme un chef le MathML pour les formules mathématiques et affiche même les images !</p>
<img src="https://korben.info/bookokrat-le-lecteur-epub-pour-les-accros-du-terminal/bookokrat-le-lecteur-epub-pour-les-accros-du-terminal-1.gif" alt="" loading="lazy" decoding="async">
<p>Attention toutefois, le rendu dépendra de votre terminal. Par exemple sur Kitty, Ghostty ou iTerm2 c'est le top ! Mais sur Alacritty ce sera un peu moins bien, quand au Terminal.app de macOS qui ne supporte pas bien les protocoles graphiques, je vous laisse imaginer la lose.</p>
<p>Côté navigation, c'est du classique avec des raccourcis inspirés de Vim (hjkl pour les intimes ^^) afin de scroller, changer de chapitre ou chercher dans le texte. L'outil gère aussi les signets automatiques ce qui est pratique quand on n'a pas le temps de finir &quot;Guerre et Paix&quot; d'une traite et vous pouvez même ajouter des notes directement dans le texte pour ne rien oublier.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/bookokrat-le-lecteur-epub-pour-les-accros-du-terminal/bookokrat-le-lecteur-epub-pour-les-accros-du-terminal-1.png" alt="" loading="lazy" decoding="async">
<p>Y'a aussi un &quot;zen mode&quot; (Ctrl + z) pour ceux qui ont du mal à se concentrer, même si je trouve qu'il est un peu inutile, et comme c'est codé en Rust, c'est fluide de fou !</p>
<p>Maintenant, pour l'installer, c'est facile... Sous macOS, un coup de Brew :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install bookokrat
</span></span></code></pre><p>Sinon, via Cargo :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cargo install bookokrat
</span></span></code></pre><p>Voilà si vous cherchez un moyen propre de lire vos ebooks sans quitter votre shell, Bookokrat fera grave bien le taff. Puis je trouve que ça redonne un petit goût de
<a href="https://korben.info/microsoft-edit-retour-nostalgique-windows-11.html">nostalgie façon Edit</a>
à la lecture et c'est pas pour me déplaire.</p>