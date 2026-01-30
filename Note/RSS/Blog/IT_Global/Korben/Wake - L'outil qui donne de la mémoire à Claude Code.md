---
title: "Wake - L'outil qui donne de la mémoire à Claude Code"
author: "Korben"
date: 2026-01-24T08:11:28.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "Claude Code"
  - "mcp"
  - "terminal"
rss_source: Blog
url: https://korben.info/wake-terminal-recorder-claude-code.html
note: 0
seen: false
---

<p>Vous utilisez Claude Code et vous passez votre temps à copier-coller vos logs de terminal pour lui donner du contexte ? Du genre, vous lancez une commande, ça se plante comme une merde, et là faut expliquer à l'IA ce qui s'est passé en faisant des screenshots ou du copier-coller à la main.</p>
<p>C'est vite relou mais heureusement, c'est totalement le problème que résout
<a href="https://github.com/joemckenney/wake">Wake</a>
, un petit outil en Rust qui enregistre automatiquement tout ce qui se passe dans votre terminal et le donne en offrande sacrée à Claude Code via le protocole MCP. Du coup, plus besoin de jouer les secrétaires IA, puisque Claudo Code, euuh Claude Code peut interroger votre historique de commandes avec les sorties et le contexte git quand il en a besoin.</p>
<p>Au début, vous lancez <code>wake shell</code> et hop, vous êtes dans une session enregistrée. Ensuite toutes vos commandes, leurs sorties, et même les infos de votre repo git, tout est capturé et stocké localement dans une base SQLite bien planquée dans <code>~/.wake/</code>. Puis quand vous posez une question à Claude Code, il peut aller piocher dans cet historique pour comprendre ce que vous avez fait.</p>
<p>L'installation se fait en une seule ligne (allez lire le script comme d'hab, hein) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -sSf https://raw.githubusercontent.com/joemckenney/wake/main/install.sh | sh
</span></span></code></pre><p>Après faut ajouter l'init dans votre <code>.zshrc</code> ou <code>.bashrc</code> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">eval &#34;$(wake init zsh)&#34;
</span></span></code></pre><p>Et pour brancher ça sur Claude Code :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">claude mcp add --transport stdio --scope user wake-mcp -- wake-mcp
</span></span></code></pre><p>Côté commandes, y'a <code>wake log</code> pour voir l'historique récent, <code>wake search &quot;machin truc&quot;</code> pour fouiller dedans, <code>wake dump</code> pour exporter en markdown et <code>wake annotate &quot;note&quot;</code> si vous voulez ajouter des petites marqueurs pour vous y retrouver plus tard. Le stockage reste en local sur votre machine, et les sorties sont limitées à 1 Mo par commande pour éviter de saturer la base.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/wake-terminal-recorder-claude-code/wake-terminal-recorder-claude-code-2.png" alt="" loading="lazy" decoding="async">
<p>Donc si vous êtes le genre de gaillard.e sans peur à
<a href="https://korben.info/quand-claude-code-pilote-votre-terminal.html">laisser Claude piloter votre terminal</a>
ou à utiliser
<a href="https://korben.info/transformez-claude-en-une-armee-de-developpeurs-a-votre-service.html">plusieurs agents en parallèle</a>
, c'est le genre d'outil qui peut vraiment vous faire gagner du temps car là où avant fallait tout expliquer à l'IA, maintenant elle voit directement ce que vous avez fait et pourquoi ça a merdé.</p>
<p>Le projet vient de sortir en v0.1.0, donc c'est encore tout frais. Ça supporte zsh et bash pour le moment. Par contre, fish c'est pas encore au programme.</p>