---
title: "Peon Ping - Donnez de la voix à vos agents IA"
author: "Korben"
date: 2026-03-19T14:12:39.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "intelligence-artificielle/chatbots-llm"
  - "Claude Code"
  - "open source"
rss_source: Blog
url: https://korben.info/peon-ping-notifications-warcraft-agents-ia.html
note: 0
seen: false
---

<p>&quot;<em><strong>Something need doing ?</strong></em>&quot; Si cette réplique vous file un frisson nostalgique, alors vous allez adorer
<a href="https://github.com/PeonPing/peon-ping">Peon Ping</a>
!!</p>
<p>Il s'agit d'un outil CLI open source qui joue des voix de personnages de jeux vidéo quand vos agents IA ont besoin de votre attention. Vous lancez Claude Code, vous passez sur autre chose, et le moment venu, un peon de Warcraft III vous gueule &quot;<em><strong>Work complete!</strong></em>&quot; quand c'est terminé.</p>
<p>Concrètement, ce truc s'intercale via des hooks entre vous et votre IDE, comme ça, chaque événement (démarrage de session, fin de tâche, erreur, demande de permission) déclenche une réplique différente. Du coup le peon dit &quot;<em>Something need doing?</em>&quot; quand l'agent attend un input, et &quot;<em>I can't do that!</em>&quot; quand y'a une erreur.</p>
<div class="video-container" id="video-container-peon-ping-notifications-warcraft-agents-ia-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Ça marche avec Claude Code, Cursor, Codex, et une dizaine d'autres outils (Kiro, Windsurf, Copilot, Gemini CLI, OpenCode, Antigravity, Rovo Dev CLI...), tout ça livré avec plus de 160 packs sonores dans 14 langues, de GLaDOS à
<a href="https://korben.info/starcraft-pc-game-pass-terrans-zergs-protoss.html">StarCraft</a>
en passant par Zelda, Red Alert 2 ou Team Fortress 2.</p>
<h2 id="installation">Installation</h2>
<p>Deux options principales. La plus propre, via Homebrew :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install PeonPing/tap/peon-ping
</span></span></code></pre><p>Sinon, le bon vieux curl :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -fsSL https://raw.githubusercontent.com/PeonPing/peon-ping/main/install.sh | bash
</span></span></code></pre><p>Et pour Windows, y'a un script PowerShell :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">Invoke-WebRequest -Uri &#34;https://raw.githubusercontent.com/PeonPing/peon-ping/main/install.ps1&#34; -UseBasicParsing | Invoke-Expression
</span></span></code></pre><p>Par défaut, l'installeur télécharge 5 packs (Warcraft, StarCraft, Portal). Si vous voulez tout d'un coup :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -fsSL https://raw.githubusercontent.com/PeonPing/peon-ping/main/install.sh | bash -s -- --all
</span></span></code></pre><p>Attention par contre, sous WSL2, il faudra installer ffmpeg au préalable pour lire les formats audio autres que WAV.</p>
<h2 id="configuration">Configuration</h2>
<p>Une fois installé, lancez le setup :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">peon-ping-setup
</span></span></code></pre><p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Ça détectera votre environnement, configurera les hooks et téléchargera les packs sonores en local. Ensuite, dès votre prochaine session Claude Code, vous entendrez un joli &quot;Ready to work?&quot; au démarrage.</p>
<p>Maintenant, si Warcraft c'est pas votre truc et que vous voulez changer de voix, genre passer à GLaDOS (une IA qui vous insulte pendant que vous codez avec une IA... ahahah), ça se fait en une commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">peon packs use glados
</span></span></code></pre><p>Vous pouvez binder un pack à un dossier spécifique avec <code>peon packs bind glados</code>, comme ça, chaque projet a sa propre ambiance sonore, et si vous êtes du genre à aimer les trucs en français, il y a aussi des packs dans la langue du roi Arthur.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-3.png" alt="" loading="lazy" decoding="async">
<p>Moi j'en ai rien à foutre, j'installe les packs Age of Empires + Red Alert ou rien !!</p>
<h2 id="les-commandes-utiles">Les commandes utiles</h2>
<p>Tout passe par la commande <code>peon</code> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">peon status # Vérifier si c&#39;est actif
</span></span><span class="line"><span class="cl">peon volume 0.7 # Régler le volume
</span></span><span class="line"><span class="cl">peon pause # Couper le son (réunion...)
</span></span><span class="line"><span class="cl">peon resume # Remettre le son
</span></span><span class="line"><span class="cl">peon packs list # Voir les packs installés
</span></span><span class="line"><span class="cl">peon packs next # Passer au pack suivant
</span></span><span class="line"><span class="cl">peon preview # Écouter un aperçu
</span></span></code></pre><p>Petit détail bien pensé, le système de &quot;no repeats&quot; fait qu'il ne jouera jamais le même son deux fois de suite dans la même catégorie. Et vous pouvez activer/désactiver chaque catégorie individuellement (greeting, acknowledge, complete, error, annoyed) si y'a des sons qui vous cassent les pieds.</p>
<p>En bonus, le terminal affiche le nom du projet et son statut dans le titre de l'onglet, avec un petit point indicateur quand c'est terminé. De grosses bannières desktop s'afficheront aussi quand un événement se produit, même si vous êtes sur une autre app.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-4.png" alt="" loading="lazy" decoding="async">
<p>Et si vous bossez en SSH ou dans un devcontainer, y'a un mode relay qui renvoie l'audio sur votre machine locale via <code>peon relay --daemon</code>. Pas mal du tout, hein ?</p>
<h2 id="le-mode-peon-trainer">Le mode Peon Trainer</h2>
<p>Maintenant, c'est là que ça part complètement en cacahuète car Peon Ping intègre un mode fitness qui vous rappelle de faire des pompes et des squats pendant que vous codez. L'objectif : 300 reps par jour, rien que ça !!</p>
<p>Dès que vous ouvrez une session, le Peon vous accueille avec un &quot;<em>Pushups first, code second! Zug zug!</em>&quot;. Ensuite, toutes les 20 minutes environ, il vous relance. Et si vous ignorez, ça escalade jusqu'à &quot;<em>You sit too long! Peon say do pushups NOW!</em>&quot;.</p>
<p>Pour logger vos reps en pleine session de code, pas besoin de quitter le terminal :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">peon trainer on # Activer le mode trainer
</span></span><span class="line"><span class="cl">/peon-ping-log 25 pushups # Logger 25 pompes
</span></span><span class="line"><span class="cl">/peon-ping-log 30 squats # Logger 30 squats
</span></span></code></pre><p>Quand vous atteignez les 300, le Peon célèbre avec un &quot;THREE HUNDRED! Human strong like orc now!&quot; et vous laisse tranquille pour le reste de la journée. Pas mal comme incentive pour bouger un peu entre deux refactorisations, non ?</p>
<p>Pour ceux qui utilisent
<a href="https://korben.info/claude-code-safety-net-plugin-securite-agent-ia.html">Claude Code au quotidien</a>
, y'a aussi un serveur MCP intégré qui permet à l'agent de choisir lui-même quel son jouer. L'agent qui communique en répliques de Warcraft... on vit une époque formidable !</p>
<p>D'ailleurs, les plus motivés peuvent carrément créer leurs propres packs via
<a href="https://openpeon.com/create">openpeon.com</a>
. Le format suit la spec ouverte CESP (Coding Event Sound Pack), comme ça n'importe quel IDE peut l'adopter.</p>
<h2 id="le-peon-pet">Le Peon Pet</h2>
<p>Et le truc le plus mignon du projet c'est ce petit orc animé qui squatte un coin de votre écran. Ce Peon Pet réagit en temps réel aux événements de Claude Code. Il dort quand rien ne se passe, se réveille au démarrage d'une session, tape frénétiquement du clavier quand l'agent bosse, et fait sa danse de la victoire quand la tâche est terminée. C'est du Electron + Three.js, le tout en open source bien sûr.</p>
<div class="video-container" id="video-container-peon-ping-notifications-warcraft-agents-ia-2.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-2.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/peon-ping-notifications-warcraft-agents-ia/peon-ping-notifications-warcraft-agents-ia-2.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>En résumé, c'est votre Tamagotchi de développeur, sauf qu'au lieu de le nourrir, c'est lui qui vous engueule pour bosser.</p>
<p>Voilà, si checker votre terminal toutes les 30 secondes pour voir si Claude Code a avancé dans sa life, ça vous saoule, c'est le genre de petit outil con mais génial qui change la vie.</p>
<p>Zug zug !</p>