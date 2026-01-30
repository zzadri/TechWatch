---
title: "Command & Conquer : Generals - Un ver attaque ce jeu mort depuis 12 ans"
author: "Korben"
date: 2026-01-28T18:16:18.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "jeux-video"
  - "Command &amp; Conquer"
  - "Exploitation de failles"
  - "faille"
  - "RCE"
  - "worm"
rss_source: Blog
url: https://korben.info/command-conquer-generals-faille-malware-ver.html
note: 0
seen: false
---

<p>C'est un délire ça ! Je crois que je viens de lire le truc le plus improbable de l'année. Sérieux, vous vous souvenez de <strong>Command &amp; Conquer : Generals</strong> ? Mais siiii, ce RTS de légende sorti en 2003 bien après C&amp;C et Red Alert !! Hé bien accrochez-vous, car même s'il est techniquement mort depuis la fermeture de GameSpy en 2014, il fait encore parler de lui.</p>
<p>Et pas pour de bonnes raisons. Argh !</p>
<p>Une équipe de chercheurs de chez Atredis Partners s'est penchée sur le code source du jeu, libéré par Electronic Arts début 2025. Au début, j'ai pensé qu'ils avaient juste trouver quelques bugs mineurs, mais en fait, ils ont découvert une série de failles de sécurité totalement dingues qui permettent à n'importe qui de prendre le contrôle de votre PC via le jeu. Carrément...</p>
<p>En réalité le jeu utilise une architecture P2P (peer to peer, qu'on devrait renommer pour l'occasion Pire Trop Pire ^^) qui fait que chaque joueur est connecté directement aux autres. Les chercheurs ont alors mis au point un &quot;ver&quot; baptisé <em>General Graboids</em> qui exploite ces failles pour se propager d'un joueur à l'autre. Concrètement, il utilise une vulnérabilité dans la fonction <code>NetPacket::readFileMessage</code> pour provoquer un bon vieux <em>stack overflow</em>.</p>
<p>Et bim bam boum, une fois en place, l'attaquant peut faire ce qu'il veut. Le ver droppe une DLL malicieuse (genre <code>dbghelp.dll</code>) directement dans le dossier du jeu et l'exécute. Vous êtes en pleine partie et hop, un script force votre base à tout vendre (&quot;Sell Everything&quot;). Puis c'est Game Over et après ça devient la fête du slip avec exécution de commandes système, installation de malwares...etc Y'a qu'à demander, tout est possible.</p>
<p>Ça fait flipper, non ?</p>
<div class="video-container" id="video-container-command-conquer-generals-faille-malware-ver-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/command-conquer-generals-faille-malware-ver/command-conquer-generals-faille-malware-ver-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/command-conquer-generals-faille-malware-ver/command-conquer-generals-faille-malware-ver-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Bon alors bien sûr
<a href="https://github.com/TheSuperHackers/GeneralsGameCode">la communauté a réagi</a>
super vite (contrairement à EA qui a juste répondu &quot;<em>c'est EOL, salut bisou</em>&quot;). Des correctifs non officiels existent déjà pour boucher ces trous béants mais bonne nouvelle quand même, ça ne concerne que le multijoueur. Si vous jouez en solo dans votre coin, vous ne risquez rien (sauf de perdre contre l'IA qui triche de fou...).</p>
<p>Alors bien sûr, moi aussi j'ai été surpris, mais pour ceux qui se demandent si <strong>on peut encore jouer à Command &amp; Conquer Generals</strong>, la réponse est oui, mais franchement, installez les patchs communautaires ou <strong>GenTool</strong> avant de vous lancer en multi sinon, vous risquez de finir avec un PC zombifié par ce jeu vieux de 20 ans.</p>
<p>Bref, si vous voulez voir les détails techniques
<a href="https://www.atredis.com/blog/2026/1/26/generals">tout est documenté ici</a>
. C'est quand même fou de voir à quel point le code de l'époque était une passoire.</p>
<p>Pour plus d'actu cybersécurité, vous pouvez aussi suivre
<a href="https://www.linkedin.com/company/korben-info/">Korben sur LinkedIn</a>
.</p>
<p>Et si vous cherchez d'autres histoires de vieux trucs qu'on démonte, jetez un œil à ce que j'écrivais sur
<a href="https://korben.info/splinter-cell-xbox-lin-format-reverse-engineering.html">le reverse engineering de Splinter Cell</a>
.</p>