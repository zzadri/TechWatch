---
title: "Ils trouvent 100 failles dans le noyau Windows pour 600 dollars"
author: "Korben"
date: 2026-03-20T06:35:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "windows/securite-windows"
  - "Cybersécurité"
  - "IA"
  - "IA cybersécurité"
  - "reverse engineering"
  - "Zero Day"
rss_source: Blog
url: https://korben.info/agents-ia-100-bugs-kernel-windows.html
note: 0
seen: false
---

<p>2 chercheurs en sécurité, Yaron Dinkin et Eyal Kraft, viennent de publier les résultats d'une expérience qui devrait donner des sueurs froides à pas mal de monde... Ils ont découvert 521 vulnérabilités dans les pilotes du noyau Windows, dont une bonne centaine exploitables pour de l'escalade de privilèges. Et tout ça ne leur a coûté que 600 dollars !</p>
<p>Mais comment ont-ils fait ? Eh bien ils se sont construit un pipeline en 5 étapes. D'abord, il a fallu récupérer 1654 pilotes uniques depuis le catalogue Microsoft Update ainsi que depuis les sites des constructeurs.</p>
<p>Ensuite, ils ont lancé un prétraitement automatique pour classer les cibles par surface d'attaque. Pour faire simple, dans Windows, quand un logiciel veut causer à un pilote du noyau, il lui envoie des commandes appelées <strong>IOCTL</strong> (Input/Output Control)... c'est un peu la sonnette d'entrée entre le monde utilisateur et le monde noyau. Leur pipeline analysait donc la complexité des fonctions qui répondent à ces commandes (les &quot;handlers IOCTL&quot;). Plus un handler est complexe, plus il y a de chances qu'une erreur s'y planque.</p>
<p>Et ils cherchaient en priorité les pilotes qui utilisent un mode de transfert de données appelé <strong>METHOD_NEITHER</strong>, c'est-à-dire le mode &quot;démerde-toi&quot;. Car contrairement aux autres modes où Windows joue les intermédiaires et vérifie un minimum ce qui transite, ici le pilote reçoit directement les pointeurs bruts depuis l'espace utilisateur, sans aucun filet de sécurité du noyau. C'est ensuite au développeur du pilote de tout vérifier lui-même… et spoiler : beaucoup ne le font pas correctement ! Bref, c'est le genre de truc qui sent la vuln à plein nez.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/agents-ia-100-bugs-kernel-windows/agents-ia-100-bugs-kernel-windows-1.png" alt="" loading="lazy" decoding="async">
</p>
<p>Ensuite pour la recherche de vulnérabilité, c'est-à-dire vraiment le cœur de leur système, ils ont mis en place un conseil de 3 agents LLM avec chacun un rôle bien défini. Un agent décompile d'abord le binaire et renomme les fonctions, ensuite un autre identifie la surface d'attaque, et enfin le troisième audite chaque fonction pour trouver des corruptions mémoire. Le tout via
<a href="https://korben.info/openrouter-state-of-ai-100-trillions-tokens-2025.html">OpenRouter</a>
, en mixant les modèles pour optimiser le ratio vulnérabilités par token. Coût moyen par cible : 3 dollars.</p>
<p>Et les résultats obtenus sont assez crazy loco car sur 202 binaires analysés, ils ont trouvé 521 vulns au total dont 45% de bugs de lecture/écriture mémoire arbitraire. Et 70% de ces vulnérabilités sont classées High ou Critical.</p>
<p>Mais évidemment y'a du faux positif (environ 60%), donc ils ont dû faire une review manuelle de chacun de ces bugs. Mais même après le tri ça laisse plus de 100 bugs réellement exploitables pour de l'escalade de privilèges sur Windows 11 ! Et les vendeurs concernés, c'est pas des petits joueurs : AMD, Intel, NVIDIA, Dell, Lenovo, IBM, Fujitsu...</p>
<p>D'ailleurs, le cas du driver AMD Crash Defender (amdfendr.sys) est parlant. Le device est accessible en écriture par n'importe quel utilisateur, expose des IOCTLs sans validation de taille correcte et permet de la corruption heap. Avec un peu de pool grooming, on arrive donc à de l'exécution de code kernel. Et quand on sait que ce driver tourne sur les instances AWS EC2 Windows avec processeurs AMD, on comprend vite que la surface d'attaque s'étend largement jusqu'au cloud.</p>
<p>(En parlant de reverse engineering assisté par IA, perso en ce moment, je suis en train de faire joujou avec
<a href="https://korben.info/project-ire-agent-microsoft-detecte-malwares.html">Claude Code et Ghidra</a>
pour un projet dont je vous parlerai peut-être plus tard si j'y arrive, et franchement ça marche troooop bien c'est fou ! Les chercheurs de l'étude notent d'ailleurs qu'aujourd'hui, ils utiliseraient probablement &quot;<em>juste Claude Code avec des skills custom</em>&quot; plutôt que leur pipeline maison. C'est dire si l'outil d'Anthropic est fou !</p>
<p>Après le plus flippant dans cette histoire, comme d'habitude c'est pas les bugs. Non, ce sont les réactions des constructeurs car sur 15 vulnérabilités confirmées et rapportées à 8 vendeurs, toutes avec un score CVSS (gravité de la faille, sur 10) supérieur à 7, un seul a patché ! Il s'agit de Fujitsu, avec la
<a href="https://nvd.nist.gov/vuln/detail/CVE-2025-65001">CVE-2025-65001</a>
. Les autres ont rejeté les rapports ou baissé les priorités malgré des vidéos de proof-of-concept montrant par exemple un BSOD depuis un compte utilisateur standard !</p>
<p>Le problème c'est que certains de ces produits hardware sont en fin de vie. Donc y'a plus de support. Mais ils ne révoquent pas les certificats de signature du driver. Du coup, ces pilotes restent utilisables pour des attaques BYOVD (Bring Your Own Vulnerable Driver), où un attaquant chargerait volontairement un driver signé mais vérolé pour compromettre le noyau.</p>
<p>Si vous bossez en sécurité, les chercheurs ont publié
<a href="https://ydinkin.substack.com/p/100-kernel-bugs-in-30-days">une liste de 234 hashes</a>
en double-SHA256 pour vérifier si vos machines contiennent des drivers affectés. Pour checker vos drivers, c'est simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">sha256sum driver.sys | awk &#39;{print $1}&#39; | tr -d &#39;\n&#39; | sha256sum
</span></span></code></pre><p>...et vous comparez avec leur liste.</p>
<p>Ce qui est clair en tout cas, c'est que
<a href="https://korben.info/ia-microsoft-decouvre-20-failles-bootloaders-grub2.html">l'IA en cybersécurité</a>
n'est plus un concept de labo. Microsoft avait déjà son Security Copilot qui trouvait des failles dans GRUB2, et maintenant ces chercheurs indépendants qui scannent l'intégralité de l'écosystème drivers Windows pour le prix d'un Macbook Neo... La course entre attaquants et défenseurs vient clairement de changer de vitesse.</p>
<p>
<a href="https://ydinkin.substack.com/p/100-kernel-bugs-in-30-days">Source</a>
</p>