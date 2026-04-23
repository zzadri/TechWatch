---
title: "sandbox-exec - L'outil de sandboxing caché de votre Mac"
author: "Korben"
date: 2026-04-16T07:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "tutoriels-guides/tutoriels-avances"
  - "isolation sandbox"
  - "Sandbox"
  - "sécurité macOS"
rss_source: Blog
url: https://korben.info/sandbox-exec-sandboxing-macos.html
note: 0
seen: false
---

<p>Sandbox-exec, c'est un utilitaire en ligne de commande dont pas grand monde ne parle mais qui est intégré à macOS et qui permet de lancer n'importe quel programme dans un bac à sable sécurisé, avec des restrictions sur mesure. Apple l'a déprécié, mais ça marche toujours... et c'est franchement pratique.</p>
<p>Avec ce truc, il suffit de créer un petit fichier de profil (extension .sb) et vous lancez votre commande avec <code>sandbox-exec -f profil.sb votre_commande</code>. En faisant ça, le programme de votre choix tournera dans un environnement verrouillé où il ne pourra accéder qu'à ce que vous autorisez explicitement.</p>
<p>Ensuite, vous avez deux philosophies. Soit vous bloquez tout par défaut et vous n'autorisez que le strict nécessaire, c'est-à-dire l'approche parano parfaite pour tester du code louche. Soit vous autorisez tout et vous ne bloquez que ce qui craint. La première est plus sûre, la seconde plus rapide à mettre en place.</p>
<p>Voici un exemple concret pour avoir un terminal coupé du réseau. Suffit de 3 lignes de profil (c'est du LISP) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">(version 1)
</span></span><span class="line"><span class="cl">(allow default)
</span></span><span class="line"><span class="cl">(deny network*)
</span></span></code></pre><p>Et là, <code>sandbox-exec -f no-network.sb zsh</code> vous donnera un shell qui peut tout faire sauf se connecter à Internet. Sympa donc pour lancer un script dont vous n'êtes pas sûr à 100% ! Par contre, pour les apps GUI c'est plus capricieux... en testant la même chose avec Firefox, le navigateur arrive quand même à se connecter (il passe probablement par un autre mécanisme réseau). Du coup, pour les applications graphiques, faudra tester au cas par cas.</p>
<p>D'ailleurs, macOS embarque déjà plein de profils dans <code>/System/Library/Sandbox/Profiles/</code>. Ce sont ceux qu'Apple utilise pour ses propres services et certains sont bien commentés, ce qui en fait une super base pour créer les vôtres (Votre IA personnelle en sera ravie ^^).</p>
<p>Côté debug, si un programme plante dans le bac à sable sans explication, la commande <code>log stream --predicate 'sender==&quot;Sandbox&quot;'</code> affichera en temps réel toutes les opérations bloquées. Comme ça, vous voyez exactement ce qui coince et vous ajustez votre profil en conséquence.</p>
<p>Après comme je vous le disais en intro, Apple a officiellement déprécié sandbox-exec car elle préfère pousser son App Sandbox via Xcode, pensé pour les apps du Mac App Store. Mais bon pour isoler rapidement un script en ligne de commande, l'App Sandbox ne sert à rien. Du coup, cet utilitaire CLI reste le seul moyen natif de faire du sandboxing à la volée sur Mac.</p>
<p>Et avec les agents IA qui exécutent du code YOLO partout sur nos machines, avoir un outil comme celui-ci pour isoler un process sans rien installer, c'est plutôt cool je pense ! Si vous utilisez déjà
<a href="https://korben.info/opcode-gui-claude-code-asterisk.html">des outils comme Opcode</a>
(une GUI pour Claude Code) qui intègrent déjà du sandboxing, c'est exactement cette couche en dessous. Il s'agit de Seatbelt, le framework de sandboxing kernel de macOS, qui fait tout le boulot au niveau OS.</p>
<p>Bref, si la sécurité de votre Mac vous préoccupe, allez gratouiller un peu ça. Tous les profils sont déjà sur votre machine, y'a plus qu'à jouer avec !</p>
<p>
<a href="https://igorstechnoclub.com/sandbox-exec/">Source</a>
</p>