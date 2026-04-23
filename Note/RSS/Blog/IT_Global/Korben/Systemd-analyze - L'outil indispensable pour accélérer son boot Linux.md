---
title: "Systemd-analyze - L'outil indispensable pour accélérer son boot Linux"
author: "Korben"
date: 2026-02-16T09:46:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "boot"
  - "diagnostic"
  - "Linux"
  - "optimisation"
  - "systemd"
  - "terminal"
rss_source: Blog
url: https://korben.info/systemd-analyze-accelerer-boot-linux.html
note: 0
seen: false
---

<p>Vous trouvez que votre Linux met 3 plombes à démarrer et vous regardez l'écran de boot défiler en vous demandant ce qui peut bien prendre autant de temps ?</p>
<p>Hé bien bonne nouvelle los amigos del manchos, si vous utilisez une distribution basée sur <strong>systemd</strong> (comme Debian, Ubuntu, Fedora, Arch, et compagnie), il existe un outil natif déjà installé qui permet de diagnostiquer tout ça :
<a href="https://man.archlinux.org/man/systemd-analyze.1.en">systemd-analyze</a>
</p>
<p>Ce truc c'est un peu le médecin légiste de votre démarrage système. Il dissèque chaque étape, identifie les unités qui traînent la patte, et vous permet de comprendre où part votre précieux temps. Pour ceux qui débarquent, systemd est le système d'initialisation adopté par la plupart des distributions modernes, et il permet justement de lancer plein de trucs en parallèle pour gagner du temps.</p>
<p>Pour commencer, la commande de base c'est tout simplement :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemd-analyze time
</span></span></code></pre><p>Elle vous sort un récapitulatif du temps passé dans chaque phase, généralement le kernel, l'initrd (le RAM disk initial), et l'espace utilisateur. Selon votre configuration, vous pourriez aussi voir passer le firmware ou le bootloader. Ça donne un truc du genre &quot;<em>Startup finished in 2.5s (kernel) + 19s (initrd) + 47s (userspace)</em>&quot;. Déjà là, vous savez si le problème vient de votre noyau ou de vos services.</p>
<p>Mais le truc vraiment cool pour fouiller un peu plus dans le détail, c'est :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemd-analyze blame
</span></span></code></pre><p>Cette commande vous balance la liste des unités systemd, triées par le temps qu'elles ont mis à s'initialiser. C'est un peu comme un classement des cancres de la Ve République. Vous voyez direct qui sont les boulets qui ralentissent tout le monde. Genre ce service réseau qui attend 20 secondes une connexion qui n'arrivera jamais, ou ce truc de logs qui prend son temps pour se réveiller.</p>
<p>Attention quand même, y'a un petit piège car un service qui met 10 secondes à démarrer ne signifie pas forcément que votre boot est rallongé de 10 secondes. Pourquoi me diriez-vous ? Hé bien parce que systemd lance plein de trucs en parallèle. Un service peut donc prendre son temps tranquille pendant que d'autres bossent en même temps sans bloquer personne.</p>
<p>Pour vraiment piger ce qui coince sur le chemin critique, lancez plutôt :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemd-analyze critical-chain
</span></span></code></pre><p>Ça, c'est le top car ça vous montre la chaîne critique, c'est-à-dire la séquence exacte d'événements qui détermine vraiment votre temps de démarrage final. Vous voyez exactement quelles unités sont sur le chemin et lesquelles attendent les autres. Le temps après le &quot;@&quot; indique quand l'unité est devenue active, et le temps après le &quot;+&quot; montre combien de temps elle a pris pour démarrer. C'est bien plus fiable que <em>blame</em> pour identifier les vrais goulots d'étranglement.</p>
<p>Et si vous êtes du genre visuel, y'a même :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemd-analyze plot &gt; boot.svg
</span></span></code></pre><p>Et avec ça, hop, ça génèrera un magnifique graphique SVG qui représentera la chronologie de votre séquence de boot. Vous pourrez ensuite l'ouvrir dans votre navigateur et voir en un coup d'oeil ce qui démarre quand et combien de temps ça dure. C'est super pratique pour épater la galerie ou juste visualiser l'ordre de lancement.</p>
<p>Maintenant, une fois que vous avez identifié les coupables, comment on fait pour accélérer tout ça ?</p>
<p>Déjà, vous pouvez désactiver les services dont vous n'avez pas besoin avec :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">sudo systemctl disable nom-du-service
</span></span></code></pre><p>Gardez en tête que <em>disable</em> supprime seulement le lancement automatique au boot, mais n'empêche pas une activation indirecte via une dépendance ou un socket. Si vous voulez vraiment qu'un service ne démarre plus jamais, utilisez <em><strong>mask</strong></em>. Et surtout, ne désactivez pas n'importe quoi comme un bourrin, hein ! Je vous connais ! Non, non, avant de toucher à un service, vérifiez d'abord ce qui en dépend :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemctl list-dependencies nom-du-service
</span></span></code></pre><p>Car si vous cassez un truc important, votre système risque de ne plus démarrer correctement. Donc si vous n'êtes pas sûr, gardez vos mimines dans vos poches. D'ailleurs, si vous bidouillez vos fichiers d'unité (comme pour
<a href="https://korben.info/shiori-gestionnaire-marque-pages-simple-efficace.html">automatiser Shiori</a>
par exemple), sachez que vous pouvez aussi les vérifier pour débusquer les erreurs avec :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">systemd-analyze verify /chemin/vers/unite.service
</span></span></code></pre><p>C'est super pratique pour éviter les mauvaises surprises au prochain redémarrage. Voilà et si vous cherchez d'autres astuces pour
<a href="https://korben.info/comment-augmenter-lautonomie-de-votre-pc-portable-linux-en-moins-de-10-minutes.html">optimiser votre machine Linux</a>
, n'hésitez pas à jeter un oeil <strong>à mon article sur TLP</strong>.</p>
<p>Ah j'oubliais, y'a aussi la commande <em>systemd-analyze security</em> qui permet d'analyser le niveau d'exposition sécurité de vos services. Elle attribue un score heuristique d'exposition basé sur les options de durcissement (hardening) actives. Plus le score est bas, mieux le service est protégé contre d'éventuelles failles. C'est donc un excellent point de départ pour identifier les services qui mériteraient un peu plus de love côté isolation.</p>
<p>Bref, cet analyseur de démarrage c'est vraiment l'outil indispensable pour qui veut comprendre et optimiser son boot Linux. C'est natif, c'est puissant, et ça vous évite de passer des heures à chercher pourquoi votre machine met autant de temps que vous à se réveiller le matin ^^.</p>