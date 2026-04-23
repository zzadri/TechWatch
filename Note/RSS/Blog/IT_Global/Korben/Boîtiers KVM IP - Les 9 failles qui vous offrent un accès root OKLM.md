---
title: "Boîtiers KVM IP - Les 9 failles qui vous offrent un accès root OKLM"
author: "Korben"
date: 2026-03-18T14:50:38.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "linux-open-source/administration-serveur"
  - "IP-KVM"
  - "KVM"
  - "KVM IP"
  - "NanoKVM"
rss_source: Blog
url: https://korben.info/9-failles-ip-kvm-prise-controle-serveurs.html
note: 0
seen: false
---

<p>Les boîtiers KVM IP, c'est le genre de matos qu'on branche dans un rack et qu'on oublie dans un coin pendant des années. Hé bien va falloir vous souvenir de où vous les avez mis les copains parce que des chercheurs d'Eclypsium viennent de retourner de fond en comble 4 modèles populaires... et c'est pas joli joli. A l'intérieur il y on trouvé pas moins de 9 failles, dont une qui score à 9.8 sur 10 en gravité CVSS. Autant dire qu'on n'est plus dans le &quot;petit bug rigolo oh oh&quot; qui fait marrer votre admin sys.</p>
<p>Pour ceux qui débarquent, ces petits appareils dont l'acronyme veut dire &quot;Kernel-based Virtual Machine&quot;, permettent de contrôler un serveur à distance via le réseau, clavier, souris et écran compris, comme si vous étiez physiquement devant la machine. Hyper pratique donc pour gérer un homelab ou une salle serveur, et ça coûte entre 50 et 200 euros sur Amazon. Du coup, y'en a partout !!!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/9-failles-ip-kvm-prise-controle-serveurs/9-failles-ip-kvm-prise-controle-serveurs-2.png" alt="" loading="lazy" decoding="async">
<p>Les chercheurs Paul Asadoorian et Reynaldo Vasquez Garcia ont passé au crible le GL-iNet Comet RM-1, le JetKVM, le Sipeed NanoKVM et l'Angeet ES3 et ça fait mal : authentification manquante sur des fonctions critiques, injection de commandes OS, ports UART qui filent un accès root direct, et des firmwares qu'on peut remplacer sans aucune vérification de signature. En gros, c'est la fête du slip côté sécu !</p>
<p>Le truc vraiment relou avec ce type d'appareils, c'est qu'en fait ils opèrent en dessous de votre OS. Pas d'antivirus, pas d'EDR, rien ne les voit. Un attaquant qui compromet votre switch de contrôle distant peut alors injecter des frappes clavier, booter depuis une clé USB (bye bye le chiffrement de disque et le Secure Boot), contourner l'écran de verrouillage, et planquer une backdoor directement dans le firmware du boîtier. Tout ça sans que votre machine ne bronche car un KVM compromis, c'est pas un stupide gadget IoT de plus sur votre réseau... Là je vous parle vraiment d'un accès direct et silencieux à toutes les machines qu'il contrôle.</p>
<p>Et c'est pas juste théorique puisqu'en 2025, des travailleurs nord-coréens infiltrés dans des boîtes américaines utilisaient des PiKVM et TinyPilot pour contrôler à distance les laptops d'entreprise depuis des &quot;laptop farms&quot;. Voilà le genre de scénario qu'on rend possible quand le firmware n'a même pas de signature. C'est un peu comme
<a href="https://korben.info/doom-camera-iot-securite-vulnerabilites.html">ces caméras IoT bourrées de failles</a>
sur lesquelles un chercheur faisait tourner DOOM... sauf qu'ici, l'attaquant prend le contrôle de vos serveurs, pas d'un flux vidéo.</p>
<p>Et histoire de parfaire le tableau, côté correctifs c'est la jungle intégral !! JetKVM a patché en v0.5.4, Sipeed en v2.3.1, GL-iNet promet un fix en v1.8.1 beta et pour l'Angeet ES3, qui cumule les 2 failles les plus sévères (scores 9.8 et 8.8), y'a aucun correctif prévu. Oupsy oups...</p>
<p>Donc si vous avez un de ces boîtiers qui traîne, voilà ce qu'il faut faire. D'abord isolez-le sur un VLAN de management dédié (jamais sur le réseau principal), coupez-lui l'accès Internet, activez le MFA si c'est supporté, et vérifiez que votre appareil n'est pas
<a href="https://korben.info/scanner-iot.html">exposé publiquement</a>
via un scan de votre IP. Mettez également le firmware à jour, sauf si c'est un Angeet... là, franchement, faut débrancher.</p>
<p>Bref, si vous avez un de ces machins dans votre rack, traitez-le comme un point d'accès critique... parce que c'en est un !</p>
<p>
<a href="https://thehackernews.com/2026/03/9-critical-ip-kvm-flaws-enable.html">Source</a>
</p>