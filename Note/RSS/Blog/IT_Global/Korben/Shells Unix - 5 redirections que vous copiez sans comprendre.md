---
title: "Shells Unix - 5 redirections que vous copiez sans comprendre"
author: "Korben"
date: 2026-02-27T08:53:32.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "tutoriels-guides/tutoriels-avances"
  - "Bash commandes"
  - "terminal"
  - "Terminal Linux"
rss_source: Blog
url: https://korben.info/redirections-bash-qui-sauvent-ta-vie.html
note: 0
seen: false
---

<p><code>2&gt;&amp;1</code>, <code>&gt;</code>, <code>&gt;&gt;</code>, <code>2&gt;/dev/null</code>... Si ces symboles dans votre terminal Linux ou macOS vous font autant flipper qu'un regex, respirez un grand coup ! Quand vous aurez lu cet article, vous verrez qu'en fait c'est super simple à comprendre, et en 5 minutes vous saurez enfin ce que vous copiez-collez depuis des années depuis StackOverflow.</p>
<p>En fait, dans les shells Unix (bash, zsh, etc.), y'a 3 canaux de base : <strong>stdin</strong> (entrée, numéro 0), <strong>stdout</strong> (sortie normale, numéro 1) et <strong>stderr</strong> (les erreurs, numéro 2). Tout le reste, de <code>&gt;</code> à <code>2&gt;/dev/null</code>, découle de ces 3 numéros.</p>
<h2 id="---écrire-dans-un-fichier-et-tout-écraser"><code>&gt;</code> - Écrire dans un fichier (et tout écraser)</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">echo &#34;Salut&#34; &gt; fichier.txt
</span></span></code></pre><p>Ça redirige stdout vers <code>fichier.txt</code>. Si le fichier existe déjà... c'est mort, il est écrasé sans sommation. Du coup, faites gaffe avec vos logs, une commande mal placée et ce sont des heures de données qui disparaissent.</p>
<p>D'ailleurs, si vous êtes du genre parano (et oui, vous avez raison !), <code>set -o noclobber</code> dans votre <code>.bashrc</code> empêchera <code>&gt;</code> d'écraser un fichier existant lors d'une commande tapée à la main. Pour y arriver, il faudra utiliser <code>&gt;|</code> pour forcer.</p>
<h2 id="---ajouter-à-la-suite"><code>&gt;&gt;</code> - Ajouter à la suite</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">echo &#34;Ligne 2&#34; &gt;&gt; fichier.txt
</span></span></code></pre><p>Même principe que <code>&gt;</code>, sauf que ça ajoute à la fin au lieu d'écraser. C'est ce que vous voulez 99% du temps pour des logs (sauf si vous voulez repartir de zéro, là <code>&gt;</code> fait le job). Une lettre de différence entre &quot;<em>tout va bien</em>&quot; et &quot;<em>où sont passés mes logs, boudiouuu ???</em>&quot;.</p>
<h2 id="2---rediriger-les-erreurs"><code>2&gt;</code> - Rediriger les erreurs</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">commande_foireuse 2&gt; erreurs.log
</span></span></code></pre><p>Le <code>2</code> c'est stderr, en gros (y'a pas d'espace entre le 2 et le <code>&gt;</code>, sinon bash croit que 2 est un argument). Tout ce qui sort en erreur finit dans <code>erreurs.log</code> au lieu de polluer votre terminal. Perso, je trouve ça super pratique pour garder une trace propre quand vous lancez des scripts via <code>crontab -e</code>.</p>
<p>Et <code>2&gt;&gt;</code> existe aussi, pour cumuler les erreurs au fil du temps au lieu d'écraser le fichier à chaque exécution.</p>
<h2 id="21---fusionner-erreurs-et-sortie-normale"><code>2&gt;&amp;1</code> - Fusionner erreurs et sortie normale</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">commande &gt; output.log 2&gt;&amp;1
</span></span></code></pre><p>Le fameux ! Le <code>&amp;1</code> dit à bash &quot;<em>le 1 c'est un file descriptor, pas un fichier qui s'appelle littéralement 1</em>&quot;. Du coup stderr (2) est redirigé vers le même endroit que stdout (1), ou plutôt vers là où stdout pointe au moment où bash évalue la ligne. Ça va, vous suivez toujours ? ^^</p>
<p>Attention, l'ordre compte ! Bash lit les redirections de gauche à droite. <code>&gt; output.log 2&gt;&amp;1</code>, stdout pointe vers le fichier, puis stderr suit... tout va dans le fichier. <code>2&gt;&amp;1 &gt; output.log</code>, stderr copie stdout qui pointe ENCORE vers le terminal, puis stdout est redirigé vers le fichier. Résultat, les erreurs restent dans votre terminal. Le piège classique.</p>
<p>Et <code>&amp;&gt;</code> fait la même chose en plus court :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">commande &amp;&gt; output.log
</span></span></code></pre><p><code>&amp;&gt;</code> est super pratique, mais spécifique à bash / zsh donc pour la portabilité, préférez quand même <code>&gt; fichier 2&gt;&amp;1</code>.</p>
<h2 id="2devnull---le-trou-noir"><code>2&gt;/dev/null</code> - Le trou noir</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">find / -name &#34;*.conf&#34; 2&gt;/dev/null
</span></span></code></pre><p><code>/dev/null</code>, c'est le trou noir d'Unix. Tout ce que vous envoyez là-dedans disparaît. Super pratique avec <code>find</code> qui vous crache 200 &quot;Permission denied&quot; pour un seul résultat utile.</p>
<p>Et si vous voulez TOUT faire disparaître (stdout + stderr) ? Un petit <code>&amp;&gt;/dev/null</code> et c'est réglé. Pratique dans vos scripts <code>/etc/cron.d/</code> quand vous voulez zéro bruit (bon, j'exagère un chouïa, je sais...).</p>
<p>Si vous aimez les
<a href="https://korben.info/les-raccourcis-clavier-pour-bash-terminal-linux-et-macos.html">raccourcis bash</a>
, j'ai aussi ce qu'il faut.</p>
<p>Bref, voilà ce sont juste 5 opérateurs à retenir, et avec ça vous couvrez à peu près tout. Donc la prochaine fois que vous copierez un <code>2&gt;&amp;1</code>, au moins vous saurez pourquoi.</p>
<p>
<a href="https://stackoverflow.com/questions/818255/what-does-21-mean">Source d'inspiration</a>
</p>