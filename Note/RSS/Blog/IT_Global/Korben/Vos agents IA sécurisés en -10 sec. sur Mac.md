---
title: "Vos agents IA sécurisés en -10 sec. sur Mac"
author: "Korben"
date: 2026-02-02T09:37:54.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "tutoriels-guides/tutoriels-avances"
  - "IA"
  - "Sandbox"
rss_source: Blog
url: https://korben.info/vibe-coding-terminal-llm.html
note: 0
seen: false
---

<p>Si vous faites du &quot;vibe coding&quot; avec Claude ou Codex, vous savez que laisser un agent IA faire sa life, c'est un peu risqué. Si celui-ci se met à exécuter des <code>rm -rf</code> sur votre ordi de boulot, vous êtes dans la merde !</p>
<p>Heureusement, Kevin Lynagh a sorti
<a href="https://github.com/lynaghk/vibe">Vibe</a>
et pour vous résumer le délire, c'est une VM Linux ultra-légère capable de sandboxer vos agents IA.</p>
<h2 id="ce-quil-vous-faut">Ce qu'il vous faut</h2>
<ul>
<li>Un Mac ARM (M1, M2, M3...)</li>
<li>macOS 13 Ventura minimum</li>
<li>Temps estimé : 5 minutes</li>
</ul>
<h2 id="installation">Installation</h2>
<p>Hop, on commence par installer Vibe. Plusieurs options s'offrent à vous :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">curl</span> <span class="o">-</span><span class="n">LO</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">lynaghk</span><span class="o">/</span><span class="n">vibe</span><span class="o">/</span><span class="n">releases</span><span class="o">/</span><span class="n">download</span><span class="o">/</span><span class="n">latest</span><span class="o">/</span><span class="n">vibe</span><span class="o">-</span><span class="n">macos</span><span class="o">-</span><span class="n">arm64</span><span class="o">.</span><span class="n">zip</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="n">unzip</span> <span class="n">vibe</span><span class="o">-</span><span class="n">macos</span><span class="o">-</span><span class="n">arm64</span><span class="o">.</span><span class="n">zip</span>
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl"><span class="n">sudo</span> <span class="n">mv</span> <span class="n">vibe</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">local</span><span class="o">/</span><span class="n">bin</span>
</span></span></code></pre>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vibe-coding-terminal-llm/vibe-coding-terminal-llm-2.png" alt="" loading="lazy" decoding="async">
<p>Et là, c'est prêt. C'est du Rust pur compilé avec le framework Virtualization.framework d'Apple, donc ça va viiiiite !</p>
<p>Et ce que vous pouvez voir au lancement de Vibe, c'est le mapping entre vos dossiers locaux liés à Claude, Codex et compagnie, et les dossiers qui sont dans la VM.</p>
<h2 id="premier-lancement">Premier lancement</h2>
<p>Pour démarrer une VM, c'est aussi simple que ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./vibe
</span></span></code></pre><p>Oui, c'est tout. 10 secondes plus tard, vous avez un shell Linux avec un accès réseau et un partage automatique de vos dossiers. Notez jute que la première fois il faut une connexion réseau pour télécharger l'image de base de Debian. Après, tout est en local.</p>
<p>Le truc cool, c'est que Vibe utilise un système copy-on-write où chaque VM part d'une image de base commune et seules les modifications sont stockées. Comme ça même si vous lancez 10 VMs, ça bouffe pas votre SSD.</p>
<p>Bon ok, j'en ai lancé que 2 en vrai mais l'idée est là ^^</p>
<h2 id="configurer-claude-ou-codex">Configurer Claude ou Codex</h2>
<p>Ensuite c'est simple, il suffit de lancer la commande Claude ou Codex directement dans le terminal que ça vous a créé, de les configurer comme si vous étiez sur votre ordinateur et puis c'est parti, vous pouvez les lancer avec le mode <code>--yolo</code> pour Codex ou avec <code>--allow-dangerously-skip-permissions</code> pour Claude.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/vibe-coding-terminal-llm/vibe-coding-terminal-llm-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Et c'est tout ! Si ça fait de la merde, ce sera dans la VM et vous ne risquerez rien ! Les fichiers sont bien sûr créés et dispo dans le répertoire dans lequel vous avez lancé vibe. Mais tout sera exécuté dans la VM donc y'a plus aucun risque.</p>
<p>Bref, si vous faites du vibe coding et que vous voulez pas finir avec un <code>sudo rm -rf /</code> généré par une IA un peu trop enthousiaste... bah voilà quoi. Le tout en moins de 1200 lignes de Rust, open source sous licence MIT.</p>
<p>Taaadaaaa !
<a href="https://github.com/lynaghk/vibe">À découvrir ici !</a>
</p>