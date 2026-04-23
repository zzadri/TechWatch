---
title: "Basalt - Vos coffres Obsidian direct dans le terminal"
author: "Korben"
date: 2026-03-16T06:41:03.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "CLI"
  - "Markdown"
  - "Obsidian"
  - "prise de notes"
  - "Rust"
  - "TUI"
  - "Vim"
rss_source: Blog
url: https://korben.info/basalt-obsidian-terminal-tui.html
note: 0
seen: false
---

<p>Un TUI en Rust pour gérer vos coffres Obsidian sans quitter le terminal c'est ce que propose Basalt qui détecte automatiquement vos vaults, affiche le markdown avec un rendu visuel, et depuis la v0.12.3, y'a même un mode vim intégré. Le tout sans avoir besoin que la vraie app tourne en arrière-plan !</p>
<p>Et c'est là toute la différence avec
<a href="https://korben.info/obsidian-cli-piloter-notes-terminal.html">le CLI officiel d'Obsidian</a>
dont je vous parlais il y a quelques jours. Car le CLI a besoin de l'app qui tourne via un socket local. Basalt, lui, lit en fait vos fichiers .md directement sur le disque. Du coup, ça marche en SSH, sur un serveur headless, ou sur n'importe quelle machine où vous avez juste vos fichiers markdown. C'est carrément pratique !</p>
<p>L'installation se fait en une commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cargo install basalt-tui
</span></span></code></pre><p>Au premier lancement, l'outil va alors chercher automatiquement vos coffres en lisant le fichier de config (sous macOS c'est dans <code>~/Library/Application Support/obsidian/obsidian.json</code>). Comme ça, hop hop, vos vaults apparaissent, vous naviguez au clavier et vous passez d'un coffre à l'autre avec <code>Ctrl+G</code>. Vous pouvez aussi passer par
<a href="https://aquaproj.github.io/">aqua</a>
ou télécharger un binaire pré-compilé sur la page releases si vous préférez.</p>
<img src="https://korben.info/basalt-obsidian-terminal-tui/basalt-obsidian-terminal-tui-1.gif" alt="" loading="lazy" decoding="async">
<p><em>Basalt en action, navigation dans un vault Obsidian</em></p>
<p>Vous ouvrez alors une note et le markdown s'affiche avec un rendu visuel : les <code>#</code> disparaissent au profit d'indicateurs plus colorés, les blocs de code ont un fond distinct, les callouts <code>&gt; [!NOTE]</code> sont reconnus, et les wiki-links <code>[[Ma Note]]</code> sont également parsés. D'ailleurs, quand vous renommez une note avec <code>r</code>, tous les wiki-links qui pointent vers elle sont mis à jour automatiquement dans tout le vault. Pas de search-replace à la main, ça fait toujours du bien !</p>
<p>Après faut pas s'attendre à un clone complet non plus. Y'a pas de rendu pour le gras, l'italique ou les tableaux. Pas de recherche dans les notes. Pas de graph view. L'éditeur intégré est expérimental (pas d'undo, pas de copier-coller, pas de sélection). C'est assumé de ce que j'ai pu voir, car le projet se présente comme un compagnon minimaliste.</p>
<p>Et c'est justement pour ça que le mode vim est le bienvenu, à vrai dire. Vous pouvez activer ça dans votre config TOML comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">vim_mode = true
</span></span></code></pre>
<img src="https://korben.info/basalt-obsidian-terminal-tui/basalt-obsidian-terminal-tui-2.gif" alt="" loading="lazy" decoding="async">
<p><em>Le mode vim en action dans Basalt</em></p>
<p>Et là vous avez <code>hjkl</code> pour naviguer, <code>gg</code> / <code>G</code> pour sauter en haut et en bas, <code>w</code> / <code>b</code> pour les mots, <code>i</code> pour l'insertion. C'est pas forcément aussi complet qu'un vrai vim, mais franchement, pour parcourir vos notes c'est agréable.</p>
<p>Le vrai kiff, c'est la config TOML qui permet de lancer un éditeur externe sur la note en cours :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">[global]
</span></span><span class="line"><span class="cl">key_bindings = [
</span></span><span class="line"><span class="cl"> { key = &#34;ctrl+alt+e&#34;, command = &#34;exec:vi %note_path&#34; },
</span></span><span class="line"><span class="cl">]
</span></span></code></pre><p>Du coup, le workflow devient : Basalt pour naviguer et lire et un raccourci clavier pour ouvrir dans vim (ou n'importe quel éditeur) quand vous voulez éditer sérieusement. C'est le genre de combo qui fonctionne bien quand vous bossez en
<a href="https://korben.info/nb-editeur-notes-terminal.html">full terminal</a>
.</p>
<p>Le projet est sous licence MIT, écrit en Rust avec ratatui, et tourne sur Linux, macOS et Windows. Tiens, la v0.12.3 ajoute aussi la création de notes et dossiers directement depuis l'explorateur avec <code>n</code> et <code>N</code>... Ça avance plutôt vite comme projet !!</p>
<p>Voilà, si vos notes vivent dans des coffres et que le terminal c'est votre habitat naturel,
<a href="https://github.com/erikjuhani/basalt">Basalt</a>
fera bien le boulot.</p>