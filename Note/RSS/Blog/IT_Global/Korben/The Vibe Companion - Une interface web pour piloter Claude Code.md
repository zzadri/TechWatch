---
title: "The Vibe Companion - Une interface web pour piloter Claude Code"
author: "Korben"
date: 2026-02-10T16:03:37.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/logiciels-libres"
  - "Bun.sh"
  - "Claude"
  - "Claude AI"
  - "Claude Code"
  - "Companion"
  - "Web UI"
rss_source: Blog
url: https://korben.info/the-vibe-companion-web-ui-claude-code.html
note: 0
seen: false
---

<p>Claude Code, c'est super puissant... mais faut avouer que dans un terminal, quand l'IA commence à enchaîner les appels d'outils dans tous les sens, on se retrouve vite à lire de la Matrice sans les lunettes de Neo. Surtout si vous tentez le coup depuis un iPad ou un mobile, ça pique.</p>
<p>Mais c'était sans compter sur
<a href="https://github.com/The-Vibe-Company/companion">Companion</a>
, un projet open source qui vous colle une interface web par-dessus Claude Code. En gros, au lieu de scroller frénétiquement dans votre terminal comme un hamster sous caféine, vous avez une vraie UI avec des blocs rétractables, de la coloration syntaxique et une vue claire de ce que l'agent fabrique. Ça tourne sur desktop, mobile, tablette... bref, partout où y'a un navigateur. D'ailleurs, si vous préférez une
<a href="https://korben.info/opcode-gui-claude-code-asterisk.html">app desktop native</a>
, y'a aussi Opcode qui fait le taf.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/the-vibe-companion-web-ui-claude-code/the-vibe-companion-web-ui-claude-code-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le truc trop cool c'est que ça peut gérer plusieurs sessions en parallèle. Vous pouvez donc jongler entre différentes instances de Claude Code, chacune avec ses propres permissions. D'ailleurs, y'a 4 modes de permission : du &quot;je valide tout à la main&quot; au &quot;YOLO bypass all&quot; pour ceux qui aiment vivre dangereusement... et qui n'ont pas installé de
<a href="https://korben.info/claude-code-safety-net-plugin-securite-agent-ia.html">plugin de sécurité</a>
(on vous aura prévenus).</p>
<p>Chaque appel d'outil (Bash, Read, Write, WebSearch...) est affiché et vous pouvez approuver, refuser ou même éditer les commandes avant exécution. Si vous utilisez des sub-agents, Companion affiche les tâches imbriquées sous le parent. C'est propre.</p>
<p>Et puis y'a ce petit détail qui fait plaisir à savoir une barre de progression colorée qui montre l'occupation de votre fenêtre de contexte avec une estimation du coût en temps réel. Parce que bon, savoir que votre session de debug à 3h du mat' vient de vous coûter l'équivalent d'un kebab, c'est quand même pratique. Mais est ce que ça vous coûte vraiment de l'argent ??? Hé bien le projet utilise le flag un peu caché <code>--sdk-url</code> de Claude Code pour communiquer via WebSocket sur le port 3456.</p>
<p>Et au cas où vous vous demanderiez, pas besoin de clé API supplémentaire puisque ça se branche directement sur votre abo Claude Pro ou Team (même si Anthropic vient d'
<a href="https://korben.info/claude-plan-gratuit-outils-pro.html">ouvrir pas mal d'outils aux gratuits</a>
).</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/the-vibe-companion-web-ui-claude-code/the-vibe-companion-web-ui-claude-code-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pour l'installer, c'est pas la mer à boire. Faut juste avoir Bun sur votre bécane, et ensuite :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">bunx the-vibe-companion
</span></span></code></pre><p>Ensuite vous ouvrez <code>http://localhost:3456</code> et c'est parti. Pour les bidouilleurs, tout le code est sur GitHub, un <code>bun install</code> dans le dossier <code>companion/web</code> et vous avez votre instance de dev. Après y'a plus qu'à installer
<a href="https://korben.info/tailscale-reseau-prive-virtuel.html">Tailscale</a>
(ou votre propre VPN local) et vous avez accès à votre Claude Code depuis n'importe où.</p>
<p>Attention quand même, le protocole WebSocket est reverse-engineeré, donc si Anthropic change un truc demain... bon, vous voyez le délire, ça peut casser. Et si vous voulez en savoir plus sur les coulisses du
<a href="https://korben.info/claude-anthropic-protocole-mcp-connexion-donnees.html">protocole MCP</a>
d'Anthropic, j'en avais parlé il y a quelque temps. Mais en attendant, ça marche nickel et ça rend Claude Code nettement plus digeste qu'un terminal brut.</p>
<p>Allez jeter un œil !</p>