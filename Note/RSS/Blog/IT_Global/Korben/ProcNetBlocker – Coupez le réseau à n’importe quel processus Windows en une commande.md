---
title: "ProcNetBlocker – Coupez le réseau à n’importe quel processus Windows en une commande"
author: "Korben"
date: 2026-01-31T09:47:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "windows/astuces-windows"
  - "bloquer reseau"
  - "CLI Windows"
  - "firewall"
  - "pare-feu Windows"
  - "processus"
  - "ProcNetBlocker"
  - "telemetrie"
rss_source: Blog
url: https://korben.info/procnetblocker-bloquer-reseau-processus-windows-cl.html
note: 0
seen: false
---

<p>Vous avez un logiciel qui cause un peu trop avec Internet alors qu'il n'a rien à y faire ? Ou un petit utilitaire qui balance de la télémétrie dans votre dos sans vous demander votre avis ? Ou peut-être juste une application que vous voulez forcer en mode hors-ligne sans pour autant couper tout votre réseau ?</p>
<p>C'est LA situation classique où pour leur couper la chique, on finit par se battre avec les menus obscurs du pare-feu Windows. Sauf que maintenant, y'a un petit outil CLI qui fait exactement ça en une seconde : <strong>
<a href="https://autoclose.net/procnetblocker.html">ProcNetBlocker</a>
</strong>.</p>
<p>C'est un utilitaire Windows en ligne de commande qui permet de bloquer l'accès réseau de n'importe quel processus comme ça pas besoin de créer des règles à rallonge. Vous tapez une commande, et hop, le processus est instantanément coupé du monde extérieur. C'est idéal pour blinder sa
<a href="https://korben.info/windows-7-et-8-le-tracking-vous-concerne-aussi.html">vie privée face au tracking</a>
incessant de certains éditeurs.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/procnetblocker-bloquer-reseau-processus-windows-cl/procnetblocker-bloquer-reseau-processus-windows-cl-2.png" alt="" loading="lazy" decoding="async">
<p>L'outil est super flexible puisqu'il propose deux approches. La première, c'est de cibler un processus par son PID (l'identifiant de processus). C'est parfait pour agir dans l'urgence sur un truc qui tourne déjà. La seconde, c'est de bloquer par le chemin de l'exécutable. Là, c'est plus radical puisque l'outil crée une règle persistante qui s'appliquera à chaque fois que vous lancerez cette application précise.</p>
<p>Le truc est portable (un petit ZIP de 7,5 Mo), et faut juste avoir les droits administrateur (logique, puisqu'on touche au pare-feu) et s'assurer que le service du pare-feu Windows est bien en cours d'exécution. Si vous utilisez déjà des solutions comme
<a href="https://korben.info/securiser-windows-server-crowdsec.html">CrowdSec</a>
pour sécuriser vos serveurs, ProcNetBlocker sera un excellent complément pour vos postes de travail.</p>
<p>Une fois le ZIP récupéré sur le site d'AutoClose, voici les commandes magiques à connaître :</p>
<p><strong>1. Bloquer un processus par son PID</strong></p>
<p>Si vous connaissez l'ID du processus (via le gestionnaire des tâches ou un petit <code>tasklist</code>) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">procnetblocker.exe --block 1234
</span></span></code></pre><p><strong>2. Bloquer un exécutable de façon permanente</strong></p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">procnetblocker.exe --block &#34;C:\Chemin\Vers\MonApp.exe&#34; --exe
</span></span></code></pre><p><strong>3. Vérifier le statut d'un blocage</strong></p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">procnetblocker.exe --status &#34;C:\Chemin\Vers\MonApp.exe&#34; --exe
</span></span></code></pre><p><strong>4. Débloquer le réseau</strong></p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">procnetblocker.exe --unblock 1234
</span></span></code></pre><p>Le projet supporte Windows 7, 8, 10 et 11 (ainsi que les versions Server en 64 bits) et c'est un must-have pour ceux qui aiment garder le contrôle sur ce qui sort de leur ordi !</p>
<p>Merci à Woody pour le partage !</p>