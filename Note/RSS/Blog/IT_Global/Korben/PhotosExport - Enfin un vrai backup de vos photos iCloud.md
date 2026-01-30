---
title: "PhotosExport - Enfin un vrai backup de vos photos iCloud"
author: "Korben"
date: 2026-01-25T08:17:00.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "tutoriels-guides"
  - "Apple"
  - "backup"
  - "CLI"
  - "macOS"
  - "Photos"
  - "swift"
rss_source: Blog
url: https://korben.info/photosexport-backup-photos-icloud.html
note: 0
seen: false
---

<p>Si vous utilisez un Mac et un iPhone, vous savez que l'app Photos d'Apple c'est un peu beaucoup une prison dorée. C'est génial tant qu'on reste chez Apple, mais dès qu'on veut sortir ses photos pour en faire une vraie sauvegarde sur un NAS ou un disque externe, ça devient vite compliqué.</p>
<p>Y'a bien une option &quot;<em>Exporter les originaux non modifiés</em>&quot; qui fait le job, mais elle n'inclut pas vos retouches, vos recadrages et la structure des dossiers est souvent inexistante. Du coup, on se retrouve avec un vrac de fichiers IMG_1234.JPG pas très sexy.</p>
<p>Mais vous me connaissez, j'suis toujours dans les bons coup et j'ai une bonne nouvelle pour vous. Rui Carmo, un développeur qui en a eu marre (comme nous), a codé un petit outil en Swift baptisé <strong>
<a href="https://github.com/rcarmo/PhotosExport">PhotosExport</a>
</strong>. Ça fonctionne en ligne de commande et ça va piocher directement dans votre librairie Photos pour extraire vos fichiers proprement.</p>
<p>Par défaut, l'outil se concentre sur l'année en cours, mais avec les options <code>--year</code> et <code>--end-year</code>, vous pouvez remonter le temps et tout récupérer d'un coup.</p>
<p>PhotosExport crée une hiérarchie <code>Année/Mois</code> (genre <code>2024/01/</code>) et renomme chaque fichier avec un timestamp précis. Ça évite les collisions de noms (avec un petit suffixe si besoin) et ça met de l'ordre dans le chaos.</p>
<p>Ce qui est cool, c'est que si vous ajoutez l'option <code>--metadata</code>, il tente aussi d'exporter les infos (lieux, dates, données techniques...) dans un fichier JSON à côté de l'image. C'est du &quot;best effort&quot; (car il ne va pas forcément récupérer la reconnaissance des visages ou des trucs trop spécifiques à Apple), mais ça permet de garder une trace des infos essentielles si un jour vous changez de crémerie.</p>
<p>Attention quand même, il y a un petit prérequis : il faut être sous <strong>macOS 13 (Ventura) ou plus récent</strong>. Et au premier lancement, macOS va vous demander d'autoriser l'accès à vos Photos (le fameux TCC). C'est normal, c'est pour la sécurité.</p>
<p>L'installation se fait via <code>make build</code> si vous avez Xcode ou les outils de développement. Ensuite, vous lancez la commande, et hop, ça mouline. Le mode incrémental est pas mal aussi car il ignore les fichiers qui existent déjà dans le dossier de destination, ce qui permet de relancer l'outil sans tout réécrire.</p>
<p>Vous pouvez même imaginer scripter ça pour que ça tourne régulièrement vers votre NAS, à condition de bien gérer les permissions d'accès au niveau du terminal ou du script (ce qui peut être un peu sioux avec les sécurités d'Apple, mais ça se fait).</p>
<p>Si vous cherchez aussi à sécuriser le reste de votre vie chez Apple, jetez un œil à ma méthode pour
<a href="https://korben.info/backup-sauvegarde-apple-notes.html">sauvegarder vos données Apple Notes</a>
ou encore comment
<a href="https://korben.info/sauvegarde-iphone-disque-externe.html">sauvegarder votre iPhone sur un disque externe</a>
. C'est toujours mieux d'avoir une copie locale, car on ne sait jamais ce qui peut arriver à un compte iCloud (Genre si Donald Trump décide de tout couper...).</p>