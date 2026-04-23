---
title: "VirtualBox - Oracle adopte enfin KVM sur Linux"
author: "Korben"
date: 2026-02-06T13:52:18.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "linux-open-source"
  - "KVM"
  - "Oracle"
  - "VirtualBox"
  - "virtualisation"
rss_source: Blog
url: https://korben.info/virtualbox-kvm-backend.html
note: 0
seen: false
---

<p>VirtualBox, le bon vieux logiciel de virtualisation d'Oracle, vient de franchir un cap plutôt inattendu. Le code de développement supporte désormais KVM comme backend sur Linux ! En gros, au lieu de s'appuyer uniquement sur son propre module noyau (qui, soyons honnêtes, a toujours été un poil galère à maintenir), l'outil de virtualisation peut maintenant <strong>utiliser l'hyperviseur natif de Linux</strong>.</p>
<p>Et c'est pas rien quand on sait que le logiciel d'Oracle et KVM se marchaient dessus depuis des années. C'était impossible de faire tourner les deux en même temps... Du coup, plutôt que de continuer à se battre, Oracle a décidé de faire copain-copain avec KVM. C'est pas bête !</p>
<p>L'idée vient à l'origine de
<a href="https://cyberus-technology.de/en/articles/vbox-kvm-public-release/">Cyberus Technology</a>
qui avait pondu une implémentation open source en 2024. Et aujourd'hui, c'est Oracle qui intègre le truc directement dans le code officiel. Alors pour l'instant, c'est dispo uniquement en version de dev dans les dépôts Git et les builds de test et ça fonctionne &quot;à peu près&quot;.</p>
<p>Vous pouvez dès à présent activer le backend KVM quand le module noyau classique de VirtualBox refuse de coopérer. C'est pratique mais attention par contre, si vous avez besoin du réseau NAT avancé ou du mode pont avec VLAN, ça passera pas encore via KVM... faudra rester sur le module maison.</p>
<p>Notez aussi que l'hyperviseur maison d'Oracle garde quand même des avantages notamment pour tout ce qui est modes réseau avancés, émulation précise pour les vieux OS, et émulation fine de périphériques.</p>
<p>Mais n'empêche, la tendance est claire, tout le monde converge vers l'hyperviseur du noyau Linux. Faut dire que
<a href="https://korben.info/quickemu.html">QEMU/KVM c'est devenu tellement solide</a>
ces dernières années que ça n'a plus trop de sens de réinventer la roue dans son coin.</p>
<p>Voilà, donc pour ceux qui utilisent l'outil d'Oracle au quotidien sur Linux, c'est une bonne nouvelle. Moins besoin de jongler avec le module vboxdrv, moins de conflits avec
<a href="https://korben.info/virtualx86-machine-virtuelle-navigateur.html">d'autres solutions de virtualisation</a>
, et surtout des mises à jour noyau qui cassent moins souvent.</p>
<p>Bref, gardez un œil sur les prochaines releases car Oracle a l'air d'y aller sérieusement. Le support KVM final et officiel devrait atterrir pour tous dans une version stable courant 2026. J'ai hâte !</p>
<p>
<a href="https://www.phoronix.com/news/VirtualBox-Upstream-With-KVM">Source</a>
</p>