---
title: "Linux sur Mac avec Fedora Asahi Remix 43 (mais pas tous les Mac)"
author: "Korben"
date: 2026-03-18T17:33:33.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "linux-open-source/distributions-linux"
  - "Apple Silicon"
  - "Asahi Linux"
  - "Linux sur Mac"
rss_source: Blog
url: https://korben.info/fedora-asahi-remix-43.html
note: 0
seen: false
---

<p>Linux sur un Mac Apple Silicon en 2026 serait-ce enfin une option viable ?</p>
<p>En effet, <strong>Fedora Asahi Remix 43</strong> vient de sortir et la réponse est... ça dépend de votre Mac. Si vous êtes sur M1 ou M2, ça commence à être sérieux. M3 ? Ça boote depuis janvier mais c'est pas encore utilisable au quotidien. M4, on en est loin. Et M5, ils ne connaissent pas encore...</p>
<p>Du coup, pour ceux qui se demandent quel Linux installer sur un Mac à base de puce Apple, c'est clairement
<a href="https://asahilinux.org/">le choix le plus abouti</a>
du moment. La grosse news de cette version, c'est l'arrivée du support Mac Pro (le gros desktop à plusieurs milliers d'euros, oui oui). Y'a aussi les micros qui fonctionnent enfin sur les MacBook Pro et Max en M2, et le 120Hz qui débarque sur les MacBook Pro 14 et 16 pouces. Côté bureau, c'est KDE Plasma 6.6 par défaut avec GNOME 49 en alternative, et sous le capot, RPM 6.0 et le backend DNF5 pour la gestion des paquets.</p>
<p>Pour l'installer, c'est toujours la même commande magique :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl https://fedora-asahi-remix.org/install | sh
</span></span></code></pre><p>Ça se lance directement depuis macOS, ça partitionne votre SSD et ça pose le tout en dual boot. Votre système Apple reste donc intact à côté, et si ça ne vous plaît pas, vous pouvez tout virer proprement. Et si vous êtes déjà sur une version précédente (41 ou 42), la mise à jour passe par DNF System Upgrade ou Plasma Discover. Par contre, oubliez GNOME Software pour les montées de version, ça marche pas encore !</p>
<p>Sauf que... y'a un gros &quot;MAIS&quot; !</p>
<p>En effet, tout ça ne fonctionne qu'avec les puces M1 et M2 donc si vous avez un Mac récent en M3, ça bootera oui, mais le GPU tournera en mode software (LLVMpipe), donc ce sera hyper lent. Et en M4... bah c'est carrément pas encore prêt.</p>
<p>Parce que oui, le reverse-engineering des GPU d'Apple, c'est un boulot de titan, car depuis le départ d'Asahi Lina qui bossait sur le premier driver DRM en Rust du noyau Linux, ça avance forcément moins vite côté graphique. D'ailleurs,
<a href="https://korben.info/asahi-le-linux-des-nouveaux-macs.html">quand je vous en avais parlé la première fois en 2022</a>
, le Bluetooth et Thunderbolt manquaient déjà à l'appel... et c'est toujours pas complètement réglé ! En février 2025, le fondateur du projet Hector Martin avait aussi jeté l'éponge, et
<a href="https://korben.info/asahi-linux-perd-developpeur-gpu-avenir-incertain.html">on se demandait si le truc allait survivre</a>
. Visiblement, l'équipe restante (dont Neal Gompa et Davide Cavalca) a décidé de pas lâcher l'affaire 💪.</p>
<p>Côté perf GPU, le driver open source Honeykrisp est désormais conforme Vulkan 1.3 et grâce à l'émulation x86 via FEX + DXVK, des jeux AAA comme <strong>Cyberpunk 2077</strong> ou <strong>The Witcher 3</strong> tournent sur M1/M2. C'est encore en alpha, faut pas s'attendre à du 60 fps et il faut 16 Go de RAM minimum, mais des jeux indés comme Hollow Knight tournent également déjà à pleine vitesse. Tout ça en reverse-engineering sans aucune doc constructeur... c'est quand même beau ! (Et pas merci Apple pour la transparence, hein...).</p>
<p>Y'a aussi une variante Fedora Server pour ceux qui voudraient transformer leur Mac en serveur headless, ce qui est une utilisation un peu dingue d'une machine à ce prix-là, mais bon, chacun son délire ! Et aussi une image minimale pour les bidouilleurs qui veulent tout construire à la main. Voilà.</p>
<p>Voili voilou, si vous avez un M1 ou M2 sous la main, c'est le moment de tester. Et pour le reste, encore un peu de patience.</p>
<p>
<a href="https://fedoramagazine.org/fedora-asahi-remix-43-is-now-available/">Source</a>
</p>