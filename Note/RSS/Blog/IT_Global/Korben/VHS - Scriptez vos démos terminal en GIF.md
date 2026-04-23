---
title: "VHS - Scriptez vos démos terminal en GIF"
author: "Korben"
date: 2026-02-01T08:36:27.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
rss_source: Blog
url: https://korben.info/vhs-creer-gif-terminal.html
note: 0
seen: false
---

<p>Vous vous souvenez des cassettes VHS ?</p>
<p>Bon, là rien à voir avec le magnétoscope de mémé qui clignote à 12:00 mais je suis quand même content de vous présenter
<a href="https://github.com/charmbracelet/vhs">VHS</a>
, un petit outil open source concocté par la team Charm dont je vous ai déjà parlé.</p>
<p>Y'a pas longtemps, je cherchais un moyen propre de faire une petit démo d'un projet perso et je ne sais pas si vous connaissez
<a href="https://korben.info/terminalizer-enregistrez-partagez-sessions-terminal-gif.html">Terminalizer</a>
(j'en avais déjà parlé), mais là pour le coup, j'ai préféré l'approche de VHS parce qu'au lieu d'enregistrer votre terminal en &quot;live&quot; comme Terminalizer et de me faire stresser à chaque faute de frappe, ça me permet de scripter entièrement en amont ma démo.</p>
<p>En fait vous écrivez un fichier &quot;.tape&quot; avec vos instructions, et l'outil génère un rendu (GIF, MP4, WebM) nickel chrome. C'est donc le rêve de tous les perfectionnistes comme moi qui recommencent 15 fois la même capture parce qu'ils ont oublié un <em>sudo</em> ou qu'ils ont bafouillé sur le clavier.</p>
<img src="https://korben.info/vhs-creer-gif-terminal/vhs-creer-gif-terminal-1.gif" alt="" loading="lazy" decoding="async">
<p>Pour l'installer, comme d'hab :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install vhs
</span></span></code></pre><p>Après si vous passez par Docker, c'est possible aussi mais il vous faudra impérativement ttyd et ffmpeg installés sur votre machine pour que ça tourne.</p>
<p>Ensuite, voici à quoi ressemble un scénario en .tape :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">Output demo.gif
</span></span><span class="line"><span class="cl">Set FontSize 20
</span></span><span class="line"><span class="cl">Set Width 1200
</span></span><span class="line"><span class="cl">Type &#34;echo &#39;Salut les amis !&#39;&#34;
</span></span><span class="line"><span class="cl">Sleep 500ms
</span></span><span class="line"><span class="cl">Enter
</span></span><span class="line"><span class="cl">Sleep 2s
</span></span></code></pre><p>Et là, c'est magique, vous lancez la commande et c'est parti :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">vhs demo.tape
</span></span></code></pre><p>Il lance alors un terminal invisible, tape les commandes pour vous, et enregistre le rendu. Hop, c'est dans la boîte mes petits Spielberg !</p>
<p>Mais ça ne s'arrête pas là puisqu’on peut aussi contrôler la vitesse de frappe pour donner un effet plus naturel, ou utiliser la commande &quot;Wait&quot; pour mettre le script en pause jusqu'à ce qu'une certaine chaîne de caractères apparaisse à l'écran. Genre pour ne pas couper la vidéo pendant un &quot;npm install&quot; qui dure trois plombes.</p>
<p>Et ce qui est top moumoute avec
<a href="https://github.com/charmbracelet/vhs">VHS</a>
, c'est que comme c'est du code, vous pouvez versionner vos démos sur Git. Mieux encore, vous pouvez les intégrer dans votre CI/CD avec GitHub Actions. Du coup, si votre CLI change, votre GIF de documentation se régénère automatiquement (à condition de configurer le commit du résultat, bien sûr). C'est ti pas beau ça ?</p>
<p>Comme ça s'en est fini des GIFs flous ou des screencasts qui pèsent une tonne. Avec VHS c'est propre, c'est net, et c'est maintenable !</p>