---
title: "LACT - Le panneau de contrôle GPU qui manquait à Linux"
author: "Korben"
date: 2026-01-26T09:19:22.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy"
  - "linux-open-source/logiciels-libres"
rss_source: Blog
url: https://korben.info/lact-controle-gpu-amd-linux.html
note: 0
seen: false
---

<p>Si vous avez une carte graphique AMD sous Linux, vous savez que côté outils de contrôle, c'est pas vraiment la fête. AMD ne fournit rien d'officiel pour gérer l'overclocking ou les ventilateurs, du coup faut se débrouiller avec des solutions tierces. Et j'ai vu que
<a href="https://github.com/ilya-zlobintsev/LACT">LACT</a>
venait de sortir une nouvelle version estampillée 0.8.4 et franchement, elle a l'air vraiment pas mal.</p>
<p>Pour ceux qui débarquent, cet utilitaire open source permet de configurer et monitorer votre <strong>GPU AMD</strong> (et aussi Nvidia ou Intel dans une certaine mesure) directement depuis une interface graphique très bien fichue. Vous réglez vos courbes de ventilation, vous ajustez la puissance, vous undervoltez... tout ça sans passer par des lignes de commande cryptiques.</p>
<p>Et de ce que j'ai compris, la grosse nouveauté de cette version, c'est la refonte de la page d'overclocking. L'interface a été réorganisée avec les boutons déplacés dans l'en-tête, ce qui rend le tout plus lisible. D'ailleurs, le panneau de contrôle mémorise maintenant vos onglets entre les redémarrages, donc plus besoin de re-naviguer à chaque fois que vous lancez l'appli.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/lact-controle-gpu-amd-linux/lact-controle-gpu-amd-linux-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Côté hardware, y'a du nouveau aussi. De nouveaux capteurs de puissance sont exposés sur les cartes AMD, ce qui permet genre de séparer la consommation CPU et GPU. Pratique pour voir précisément ce qui bouffe le plus de watts dans votre config ! La lecture des métriques est aussi devenue plus efficace, donc moins de charge système pour afficher vos stats en temps réel.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/lact-controle-gpu-amd-linux/lact-controle-gpu-amd-linux-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Pour les serveurs headless, une image Docker est aussi disponible, du coup vous pouvez faire tourner le service sans interface graphique et gérer vos GPU à distance. Sympa pour les fermes de calcul ou les rigs de minage (si ça existe encore ??).</p>
<p>Les développeurs ont aussi corrigé pas mal de trucs notamment des fuites mémoire. Maintenant, si jamais ça crash, au lieu de se bloquer bêtement, l'appli affichera un jolie écran de plantage tout propre.</p>
<p>L'installation est dispo sur à peu près toutes les distros : Arch (directement dans les repos), Debian/Ubuntu en .deb, Fedora via Copr, openSUSE, et même en Flatpak pour les allergiques aux paquets natifs.</p>
<p>Voilà, si vous voulez vérifier la température de votre carte graphique sous Linux sans vous prendre la tête avec sensors et compagnie, c'est clairement la solution la plus user-friendly du moment.</p>
<p>
<a href="https://github.com/ilya-zlobintsev/LACT/releases/tag/v0.8.4">Source</a>
</p>