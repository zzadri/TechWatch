---
title: "Denuvo tombe en quelques heures grâce aux hyperviseurs"
author: "Korben"
date: 2026-03-31T10:01:14.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite"
  - "jeux-video/actualites-gaming"
  - "DRM"
  - "sécurité informatique"
rss_source: Blog
url: https://korben.info/denuvo-hyperviseur-bypass-pirates.html
note: 0
seen: false
---

<p><strong>Denuvo</strong>, la célèbre protection anti-piratage qui emmerde les joueurs PC depuis une décennie, traverse une sale période. Depuis début 2026, des pirates contournent la protection via des hyperviseurs, et les jeux protégés tombent désormais en quelques heures au lieu de plusieurs semaines : Resident Evil Requiem, Crimson Desert, Life is Strange: Reunion... tous craqués le jour de leur sortie ! Même Assassin's Creed Shadows, qui avait tenu 11 mois, a fini par tomber.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/denuvo-hyperviseur-bypass-pirates/denuvo-hyperviseur-bypass-pirates-1.jpg" alt="" loading="lazy" decoding="async">
<p>En fait, ces crackers ne s'embêtent plus à faire du reverse engineering sur les protections de Denuvo, ce qui leur prenait des mois. Ils ont monté un truc qui attaque sur 5 couches, du UEFI (Ring -2) jusqu'au processus du jeu (Ring 3). Un bootkit open source appelé EfiGuard désactive les protections au démarrage, puis un hyperviseur (SimpleSvm sur AMD, hyperkd sur Intel) prend le contrôle en Ring -1, sous le système d'exploitation. De là, il intercepte les CPUID, falsifie les structures mémoire Windows et triche sur les timings CPU pour que Denuvo croie que tout est normal. Un
<a href="https://github.com/RD945/hypervisor-crack-audit">audit de sécurité indépendant</a>
publié sur GitHub n'a certes trouvé aucun malware dans le package, mais prévient que le système est laissé sans protection le temps que l'hyperviseur tourne.</p>
<p>Pour que ça fonctionne, il faut bien sûr désactiver des protections Windows assez critiques comme le VBS (Virtualization-Based Security), le HVCI (Hypervisor-Enforced Code Integrity) et la vérification de signature des driver, ce qui ouvre un peu trop grand le système, qui pourrait alors se voir installer un rootkit ou autre malware...</p>
<p>Et côté matériel, c'est la loterie car ça tourne plutôt bien sur AMD, mais les processeurs Intel posent des soucis de stabilité qui nécessitent des bidouilles franchement dangereuses. FitGirl, la repackeuse la plus connue de la scène, avait même d'abord refusé de toucher à ces cracks en déclarant qu'&quot;<em>aucun jeu ne vaut les dommages potentiels irrécupérables qu'il peut causer à l'ordinateur</em>&quot;. Mais depuis, elle a changé d'avis après les améliorations apportées par KiriGiri et l'équipe MKDEV, et publie maintenant des repacks avec un tag &quot;HYPERVISOR&quot; bien visible. M'enfin bon, elle reste quand même prudente.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/denuvo-hyperviseur-bypass-pirates/denuvo-hyperviseur-bypass-pirates-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Irdeto, la boîte qui possède Denuvo, promet bien sûr une contre-mesure qui ne devrait pas ralentir les jeux. Les options sur la table sont : détecter la présence d'hyperviseurs tiers via les CPUID ou la latence CPU, ou imposer des vérifications de licence quotidiennes (ce qui emmerderait aussi les joueurs légitimes).</p>
<p>Et le pire dans tout ça, c'est que Denuvo a un impact mesurable sur les performances des jeux légitimes. Le blogueur Nathan Baggs et le développeur @valigo ont montré que la protection embarque une machine virtuelle qui compresse le code du jeu, bousille le cache processeur, perturbe le prédicteur de branchement et rajoute des instructions parasites. Cela veut dire concrètement que Ghostwire Tokyo mettait 200 secondes à démarrer avec Denuvo contre 54 sans, et Mass Effect Andromeda a gagné 12% de FPS quand la protection a été retirée.</p>
<p>Bref, c'est l'éternel jeu du chat et de la souris et Denuvo sait très qu'ils ne peuvent pas vaincre le piratage. Par contre, ils pouvaient jusqu'à présent maintenir une fenêtre de protection suffisante pour que les éditeurs récupèrent leur investissement sur les premières semaines de vente.</p>
<p>Mais avec ces bypasses hyperviseur, cette fenêtre vient de tomber à zéro. Gloups... Donc la vraie question maintenant, elle est surtout pour les joueurs légitimes : <em>Est-ce que la prochaine &quot;mise à jour de sécurité&quot; de Denuvo va encore bouffer des performances sur leur machine pendant que les pirates jouent sans protection, sans ralentissement, et sans payer ?</em></p>
<p>On verra bien mais pour l'instant, la tendance des
<a href="https://korben.info/heureusement-tous-les-editeurs-de-jeux-video-ne-sont-pas-pro-drm.html">éditeurs c'est plutôt de lâcher les DRM</a>
car ils ont compris un truc que Denuvo refuse d'admettre : <strong>Avec ces conneries de DRM, ce sont toujours les clients honnêtes qui trinquent !</strong></p>
<p>
<a href="https://torrentfreak.com/game-pirates-beat-denuvo-with-hypervisor-bypasses-irdeto-promises-countermeasure/">Source</a>
</p>
<p></p>