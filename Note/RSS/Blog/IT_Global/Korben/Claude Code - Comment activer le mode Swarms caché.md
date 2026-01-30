---
title: "Claude Code - Comment activer le mode Swarms caché"
author: "Korben"
date: 2026-01-26T10:49:49.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/chatbots-llm"
  - "tutoriels-guides/tutoriels-avances"
  - "agent IA"
  - "Anthropic"
  - "Auto Claude"
  - "Claude Code"
  - "IA multi-agents"
rss_source: Blog
url: https://korben.info/claude-code-activer-mode-swarms-cache.html
note: 0
seen: false
---

<p>Vous utilisez Claude Code, le CLI d'Anthropic ? Hé bien figurez-vous qu'il y a des fonctionnalités cachées dedans, et pas des moindres ! Un dev nommé Mike Kelly a fouillé dans le JavaScript minifié du CLI et il a découvert un truc dingue : un mode &quot;<strong>Swarms</strong>&quot; qui transforme votre assistant <strong>en véritable chef d'équipe capable de déléguer le travail à plusieurs agents en parallèle</strong>.</p>
<p>En gros, au lieu de parler à une seule IA qui code, vous parlez à un team lead. Et ce team lead, lui, il ne code pas... il planifie, découpe les tâches et les dispatche à une équipe de spécialistes qui bossent en même temps. Du coup quand vous validez un plan, il spawn plusieurs agents workers qui partagent un tableau de tâches, communiquent entre eux via une sorte de boîte aux lettres interne, et reviennent vous faire leur rapport une fois le boulot terminé.</p>
<p>Le truc c'est que cette fonctionnalité existe DÉJÀ dans le code de l'outil CLI, mais elle est verrouillée derrière un feature flag côté serveur (un truc qui s'appelle <code>tengu_brass_pebble</code> pour les curieux). Mike a donc créé
<a href="https://github.com/mikekelly/claude-sneakpeek">claude-sneakpeek</a>
, un outil qui patche le CLI pour forcer ce flag à <code>true</code>. Hop, les fonctionnalités cachées deviennent accessibles. Si vous avez déjà lu
<a href="https://korben.info/transformez-claude-en-une-armee-de-developpeurs-a-votre-service.html">mon article sur Auto-Claude</a>
, vous voyez le genre... Ce sont des agents en parallèle qui bossent pendant que vous faites autre chose, genre lire mes articles pour entrapercevoir le futur ^^.</p>
<h2 id="ce-qui-se-débloque">Ce qui se débloque</h2>
<p>Une fois le patch appliqué, vous avez accès à :</p>
<ul>
<li><strong>TeammateTool</strong> : pour spawner des équipes d'agents</li>
<li><strong>Delegate mode</strong> : le Task tool peut lancer des agents en arrière-plan</li>
<li><strong>Teammate mailbox</strong> : les agents peuvent s'envoyer des messages entre eux</li>
<li><strong>Swarm spawning</strong> : orchestration native multi-agents</li>
</ul>
<p>Concrètement, quand vous demandez une tâche complexe, l'IA peut maintenant découper le travail, créer des sous-tâches avec dépendances, et lancer plusieurs workers qui vont bosser en parallèle sur leurs morceaux respectifs. Et ça consomme moins de tokens que de tout faire séquentiellement, contrairement à ce qu'on pourrait croire.</p>
<h2 id="comment-linstaller">Comment l'installer</h2>
<p>L'installation est hyper simple. Vous lancez :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npx @realmikekelly/claude-sneakpeek quick --name claudesp
</span></span></code></pre><p>Ensuite, ajoutez le dossier bin à votre PATH si c'est pas déjà fait :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">echo</span> <span class="s1">&#39;export PATH=&#34;$HOME/.local/bin:$PATH&#34;&#39;</span> <span class="o">&gt;&gt;</span> <span class="o">~/.</span><span class="n">zshrc</span> <span class="o">&amp;&amp;</span> <span class="n">source</span> <span class="o">~/.</span><span class="n">zshrc</span>
</span></span></code></pre><p>Et voilà, vous pouvez lancer <code>claudesp</code> au lieu de <code>claude</code> pour avoir la version avec les features débloquées !</p>
<p>Le truc bien pensé, c'est que ça installe une instance COMPLÈTEMENT isolée. Votre installation normale de l'outil CLI reste intacte, avec sa propre config, ses sessions et ses serveurs MCP. Zéro interférence.</p>
<h2 id="comment-ça-marche-sous-le-capot">Comment ça marche sous le capot</h2>
<p>Pour les curieux qui veulent comprendre le hack, c'est assez chouette. En fait, le CLI est du JavaScript minifié, et il contient une fonction qui ressemble à ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">function i8(){if(Yz(process.env.CLAUDE_CODE_AGENT_SWARMS))return!1;return xK(&#34;tengu_brass_pebble&#34;,!1)}
</span></span></code></pre><p>Cette fonction vérifie le feature flag côté serveur. Le patch la remplace simplement par :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">function i8(){return!0}
</span></span></code></pre><p>Bref, au lieu de checker le flag, ça retourne toujours <code>true</code>. Simple mais efficace.</p>
<h2 id="pour-mettre-à-jour-ou-désinstaller">Pour mettre à jour ou désinstaller</h2>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npx @realmikekelly/claude-sneakpeek update claudesp
</span></span><span class="line"><span class="cl"># Mise à jour
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">npx @realmikekelly/claude-sneakpeek remove claudesp
</span></span><span class="line"><span class="cl"># Désinstallation
</span></span></code></pre><p>Voilà, si vous êtes fan d'automatisation et que vous voulez pousser le CLI dans ses retranchements, c'est clairement un truc à tester ! Le mode Swarms change la donne pour les projets complexes où paralléliser les tâches fait gagner un temps fou.</p>
<p>
<a href="https://github.com/mikekelly/claude-sneakpeek">Source</a>
</p>