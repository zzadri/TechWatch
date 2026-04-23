---
title: "osxphotos - Sauvegardez automatiquement votre photothèque Apple"
author: "Korben"
date: 2026-02-23T12:39:58.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "tutoriels-guides/astuces-productivite"
  - "backup"
  - "macOS"
  - "open source"
  - "Photos"
rss_source: Blog
url: https://korben.info/osxphotos-backup-photos-apple-automatique.html
note: 0
seen: false
---

<p>Vos photos dans iCloud, c'est une synchronisation, et pas un backup et même si la nuance est mince, quand on s'en rend compte, il est souvent trop tard... C'est pourquoi même si vous avez une confiance aveugle en Apple, si demain votre compte est supprimé pour une raison ou une autre, vous perdrez l'accès à vos précieuses photos. Et ça, on ne le veut pas ! Alors aujourd'hui, on va apprendre à en faire une sauvegarde.</p>
<p>Pour cela, on va utiliser
<a href="https://github.com/RhetTbull/osxphotos">osxphotos</a>
, une bibliothèque Python open source (MIT) qui lit directement la base SQLite de Photos.app pour en exporter tout le contenu. Ça tourne sur macOS de Sierra à Sequoia, et même sur Linux.</p>
<p>L'installation :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew tap RhetTbull/osxphotos
</span></span><span class="line"><span class="cl">brew install osxphotos
</span></span></code></pre><p>Et pour exporter tout votre catalogue de photos vers un disque externe il suffit d'entrer la commande suivante :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">osxphotos</span> <span class="k">export</span> <span class="o">/</span><span class="n">Volumes</span><span class="o">/</span><span class="n">MonDisque</span><span class="o">/</span><span class="n">Photos</span> <span class="o">--</span><span class="n">download</span><span class="o">-</span><span class="n">missing</span> <span class="o">--</span><span class="n">update</span>
</span></span></code></pre><p><code>--download-missing</code> forcera le téléchargement depuis iCloud des photos pas encore présentes en local et <code>--update</code> fera le boulot incrémental, ne retraitant que les nouvelles photos ou celles modifiées depuis le dernier lancement.</p>
<p>Du coup, le premier export peut prendre des heures, et les suivants quelques secondes. L'outil génère d'ailleurs un <code>.osxphotos_export.db</code> dans le dossier de destination pour tracker ce qui a déjà été exporté. Je trouve ça un peu plus simple que d'exporter toute la grosse photothèque <em>.photoslibrary</em> à chaque coup.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/osxphotos-backup-photos-apple-automatique/osxphotos-backup-photos-apple-automatique-2.png" alt="" loading="lazy" decoding="async">
<p>Ensuite, pour automatiser, un cron suffit (vérifiez votre chemin avec <code>which osxphotos</code> - <code>/opt/homebrew/bin/</code> sur Apple Silicon, <code>/usr/local/bin/</code> sur Intel) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="mi">0</span> <span class="mi">3</span> <span class="o">*</span> <span class="o">*</span> <span class="o">*</span> <span class="o">/</span><span class="n">opt</span><span class="o">/</span><span class="n">homebrew</span><span class="o">/</span><span class="n">bin</span><span class="o">/</span><span class="n">osxphotos</span> <span class="k">export</span> <span class="o">/</span><span class="n">Volumes</span><span class="o">/</span><span class="n">MonDisque</span><span class="o">/</span><span class="n">Photos</span> <span class="o">--</span><span class="n">download</span><span class="o">-</span><span class="n">missing</span> <span class="o">--</span><span class="n">update</span>
</span></span></code></pre><p>Moi je l'ai mis tous les jours à 3h du mat ! Mais attention, disque non monté = 0 export, 0 erreur visible. Donc à moins que vous ayez un script de vérification du montage, vérifiez les logs de temps en temps. Pour une gestion plus propre des conditions de montage, <code>launchd</code> est quand même préférable, mais pour commencer, le cron fera très bien l'affaire.</p>
<p>Après si vous n'utilisez pas Photos.app mais juste iCloud depuis votre iPhone, regardez plutôt du côté de
<a href="https://korben.info/sauvegarde-iphone-disque-externe.html">la sauvegarde iPhone sur disque externe</a>
. Et si vous voulez aussi mettre en sécurité vos
<a href="https://korben.info/backup-sauvegarde-apple-notes.html">données Apple Notes</a>
, ou les migrer sur Obsidian, c'est possible aussi.</p>