---
title: "Claude Code - Pilotez votre terminal depuis votre canapé"
author: "Korben"
date: 2026-02-26T11:46:37.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "tutoriels-guides/tutoriels-avances"
  - "Anthropic"
  - "Claude"
  - "Claude AI"
  - "Claude Code"
rss_source: Blog
url: https://korben.info/claude-code-remote-control.html
note: 0
seen: false
---

<p>Claude Code tourne en local et c'est son gros avantage car ça permet par exemple d'agir sur votre machine, de lancer des scripts...etc. Mais c'est aussi sa grosse limite car à cause de ça, vous êtes cloué devant votre terminal. J'étais en quête depuis un moment d'une solution et je vous avais déjà parlé de
<a href="https://korben.info/the-vibe-companion-web-ui-claude-code.html">Vibe Companion</a>
y'a pas longtemps mais tous ces outils vont disparaitre puisque Anthropic vient de sortir <strong>Remote Control</strong>, une feature qui transforme claude.ai ou l'app mobile en télécommande pour votre session locale. Comme ça, vos fichiers restent chez vous et seule l'interface voyage.</p>
<p>Votre ordi fait tourner Claude Code normalement, et vous, vous pouvez continuer à lui parler depuis votre iPhone, votre Android, votre iPad ou n'importe quel navigateur Chrome, Firefox, Safari... Pas de serveur exposé, pas de port ouvert, que du HTTPS sortant. C'est plutôt bien foutu vous allez voir !</p>
<h2 id="ce-quil-vous-faut">Ce qu'il vous faut</h2>
<p>Bon déjà, un abonnement Pro ou Max (pas le choix, les clés API ne marchent pas et les plans Team/Enterprise sont exclus pour le moment). Ensuite, vérifiez que Claude Code est installé et que vous êtes connecté via <code>/login</code>. Acceptez ensuite le &quot;workspace trust&quot; dans votre projet et hop, c'est tout côté prérequis.</p>
<h2 id="lancer-une-session">Lancer une session</h2>
<p>Deux options s'offrent à vous ensuite... Soit vous démarrez une nouvelle session dédiée :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">claude remote-control
</span></span></code></pre><p>Soit vous êtes déjà en train de bosser dans Claude Code et vous tapez <code>/rc</code> (alias de <code>/remote-control</code>). Avec <code>claude remote-control</code>, seule l'URL apparaît... donc appuyez sur espace pour afficher le joli QR code.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-remote-control/claude-code-remote-control-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>3 flags utiles (uniquement avec <code>claude remote-control</code>, pas <code>/rc</code>) : <code>--verbose</code> pour voir ce qui transite, <code>--sandbox</code> pour forcer le mode bac à sable (désactivé par défaut) et <code>--no-sandbox</code> pour le couper si vous l'avez activé dans votre config.</p>
<h2 id="se-connecter-depuis-un-autre-appareil">Se connecter depuis un autre appareil</h2>
<p>Ensuite, la méthode la plus rapide c'est de scanner le QR code avec votre téléphone. Sinon, copiez l'URL affichée et collez-la dans n'importe quel navigateur. Dernière option, allez sur
<a href="https://code.claude.com">claude.ai/code</a>
et votre session apparaît dans la liste (les sessions actives ont un petit point vert).</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-remote-control/claude-code-remote-control-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Une fois connecté, vous récupérez votre conversation en cours, vos fichiers, votre contexte... tout. Vous pouvez envoyer des messages, voir les résultats, approuver les modifications de fichiers. Bref, comme si vous étiez devant votre terminal, sauf que vous êtes dans votre canapé, votre lit ou en train de pousser le caddie chez Auchan !</p>
<h2 id="activer-par-défaut">Activer par défaut</h2>
<p>Maintenant, si vous voulez que CHAQUE session Claude Code soit automatiquement accessible à distance, tapez <code>/config</code> dans une session Claude Code, puis activez l'option &quot;<strong>Enable Remote Control for all sessions</strong>&quot;. Et voilà, plus besoin d'y réfléchir ! Chaque <code>claude</code> lancé dans un terminal sera pilotable depuis votre navigateur ou l'app mobile.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/claude-code-remote-control/claude-code-remote-control-4.png" alt="" loading="lazy" decoding="async">
</p>
<p>Vos sessions prennent le nom de votre dernier message (ou &quot;Remote Control session&quot; par défaut), donc utilisez <code>/rename mon-projet-cool</code> pour les retrouver facilement dans la liste sur claude.ai/code.</p>
<p>Sinon, dans Claude Code avec <code>/mobile</code> vous pouvez aussi afficher directement le QR code pour télécharger l'app Claude sur iOS ou Android.</p>
<h2 id="les-limites-à-connaître">Les limites à connaître</h2>
<p>Bon, après c'est pas non plus parfait car déjà, c'est cappé à UNE SEULE session à distance par instance de Claude Code (si vous en lancez une deuxième, la première se déconnecte). Par contre, plusieurs instances dans des terminaux différents peuvent chacune avoir leur session remote. Le terminal doit également rester ouvert (si vous le fermez, c'est fini). Mais bonne nouvelle quand même, si le laptop passe en veille ou que le réseau saute, ça se reconnectera tout seul au réveil. Le piège, c'est si la machine reste sans réseau plus de 10 minutes... là, la session expire et il faudra relancer <code>claude remote-control</code>.</p>
<p>Soyez rassurés quand même côté sécurité c'est propre (uniquement du HTTPS sortant sur le port 443, zéro port entrant et des identifiants éphémères), mais gardez en tête que
<a href="https://korben.info/quand-claude-code-pilote-votre-terminal.html">Claude Code a accès à votre terminal</a>
donc sauf si vous activez <code>--sandbox</code>, il peut de ce fait exécuter n'importe quelle commande... donc les mêmes précautions qu'en local s'appliquent !</p>
<p>Du coup si vous en avez marre de rester scotché devant votre terminal, maintenant vous savez quoi faire.</p>
<p>Merci à Lorenper !</p>