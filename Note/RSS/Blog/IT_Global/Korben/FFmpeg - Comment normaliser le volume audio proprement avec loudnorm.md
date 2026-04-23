---
title: "FFmpeg - Comment normaliser le volume audio proprement avec loudnorm"
author: "Korben"
date: 2026-02-17T09:25:00.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture"
  - "tutoriels-guides/tutoriels-avances"
  - "actualité"
  - "Cybersécurité"
  - "Docker"
  - "ffmpeg"
  - "sécurité"
rss_source: Blog
url: https://korben.info/ffmpeg-normaliser-volume-audio-lufs-loudnorm.html
note: 0
seen: false
---

<p>Vous avez déjà remarqué comment le volume varie d'une vidéo à l'autre sur YouTube, ou pire, comment certaines pubs sont 10 fois plus fortes que le contenu ? Bah c'est parce que tout le monde n'utilise pas la même norme de volume. Et si vous produisez du contenu audio/vidéo, c'est le genre de détail qui fait la différence entre un truc amateur et un rendu pro.</p>
<p>La bonne nouvelle, c'est que <strong>FFmpeg</strong> intègre déjà un filtre qui s'appelle loudnorm et qui gère tout ça automatiquement. La norme utilisée, c'est le LUFS (Loudness Units Full Scale), qui est devenue le standard de l'industrie, et YouTube, Spotify, les TV... tout le monde utilise ça maintenant pour mesurer et normaliser le volume audio.</p>
<p>D'ailleurs, si vous débutez complètement avec cet outil, je vous conseille de jeter un œil à mon guide
<a href="https://korben.info/ffmpeg-pour-les-nuls.html">FFmpeg pour les nuls</a>
pour bien piger les bases de la ligne de commande.</p>
<p>Allez, c'est partiii ! <strong>Temps estimé :</strong> 2-5 minutes par fichier (selon la méthode choisie)</p>
<p>Mais, avant de se lancer dans les commandes, un petit point sur les paramètres qu'on va manipuler. Le filtre loudnorm utilise trois valeurs principales. D'abord I (Integrated loudness), c'est le volume moyen global mesuré en LUFS. La valeur standard pour le streaming, c'est -16 LUFS pour YouTube et Spotify, ou -23 LUFS pour la diffusion broadcast. Ensuite TP (True Peak), le niveau maximal que le signal ne doit jamais dépasser. On met généralement -1.5 dB pour avoir une marge de sécurité. Et enfin LRA (Loudness Range), qui définit la plage dynamique autorisée, généralement autour de 11 dB.</p>
<h2 id="méthode-1--normalisation-simple-single-pass">Méthode 1 : Normalisation simple (single-pass)</h2>
<p>C'est la méthode la plus rapide, parfaite pour du traitement à la volée :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">ffmpeg -i entree.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 -ar 48000 sortie.wav
</span></span></code></pre><p><strong>Pourquoi ces valeurs :</strong> -16 LUFS c'est le standard YouTube/Spotify, -1.5 dB de true peak évite le clipping, et 11 dB de range dynamique garde un son naturel.</p>
<p>Le truc c'est que cette méthode fait une analyse en temps réel et ajuste à la volée. C'est bien, mais pas parfait. Pour un résultat vraiment précis, y'a mieux.</p>
<h2 id="méthode-2--normalisation-en-deux-passes-dual-pass">Méthode 2 : Normalisation en deux passes (dual-pass)</h2>
<p>Cette méthode analyse d'abord le fichier complet, puis applique les corrections exactes. C'est plus long mais beaucoup plus précis.</p>
<p>Première passe, on analyse :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">ffmpeg -i entree.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -
</span></span></code></pre><p>FFmpeg va vous sortir un bloc JSON avec les mesures du fichier (input_i, input_tp, input_lra, input_thresh). Notez-les bien, car vous allez les injecter dans la deuxième passe.</p>
<p>Deuxième passe, on applique avec les valeurs mesurées (remplacez les chiffres par ceux obtenus à l'étape précédente) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">ffmpeg -i entree.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=-24.35:measured_TP=-2.15:measured_LRA=8.54:measured_thresh=-35.21:offset=0:linear=true -ar 48000 sortie.wav
</span></span></code></pre><p><strong>Pourquoi cette méthode ?</strong> En fait, en passant les valeurs mesurées, FFmpeg sait exactement de combien ajuster. L'option linear=true force une normalisation linéaire plutôt que dynamique, ce qui préserve mieux la dynamique originale.</p>
<h2 id="pour-les-fichiers-vidéo">Pour les fichiers vidéo</h2>
<p>Le principe est le même, on ajoute juste <code>-c:v copy</code> pour garder la vidéo intacte sans la ré-encoder :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">ffmpeg -i video.mp4 -c:v copy -af loudnorm=I=-16:TP=-1.5:LRA=11 -ar 48000 video_normalise.mp4
</span></span></code></pre><p>D'ailleurs, pour ceux qui veulent automatiser ça à l'extrême, j'avais parlé de
<a href="https://korben.info/ffmpegfs-un-systeme-de-fichiers-qui-convertit-vos-videos-automatiquement.html">FFmpegfs</a>
, un système de fichiers qui transcode automatiquement ce que vous déposez dessus. C'est pratique si vous avez une grosse bibliothèque à gérer.</p>
<h2 id="traitement-par-lots-avec-ffmpeg-normalize">Traitement par lots avec ffmpeg-normalize</h2>
<p>Si vous avez plein de fichiers à traiter, y'a un outil Python qui automatise la méthode dual-pass :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pip install ffmpeg-normalize
</span></span><span class="line"><span class="cl">ffmpeg-normalize *.wav -o output_folder/ -c:a pcm_s16le
</span></span></code></pre><p>Cet outil fait automatiquement les deux passes et supporte le traitement parallèle. Pratique pour normaliser une bibliothèque entière.</p>
<h2 id="et-en-cas-de-problème-">Et en cas de problème ?</h2>
<p><strong>Erreur &quot;No such filter: loudnorm&quot;</strong> : Votre version de FFmpeg est trop ancienne (il faut la 3.1 minimum). Mettez à jour votre binaire.</p>
<p><strong>Le son est distordu après normalisation</strong> : Le fichier source était probablement déjà saturé. Essayez de baisser le target (-18 LUFS au lieu de -16) ou augmentez le headroom du true peak (-2 dB au lieu de -1.5).</p>
<p>Voilà, maintenant vous n'avez plus d'excuse pour avoir des niveaux audio qui varient dans tous les sens. Le LUFS c'est le standard, FFmpeg gère ça nativement, et ça prend 30 secondes.</p>
<p>Vos auditeurs vous remercieront.</p>
<p>
<a href="https://ffmpeg.org/ffmpeg-filters.html#loudnorm">Source</a>
</p>