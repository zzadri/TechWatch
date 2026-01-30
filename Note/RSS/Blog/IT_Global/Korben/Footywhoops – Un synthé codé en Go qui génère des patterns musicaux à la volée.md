---
title: "Footywhoops – Un synthé codé en Go qui génère des patterns musicaux à la volée"
author: "Korben"
date: 2026-01-29T09:21:00.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture/musique"
  - "audio"
  - "dsp"
  - "Go"
  - "musique électronique"
  - "open source"
  - "portaudio"
  - "sequenceur"
  - "synthétiseur"
rss_source: Blog
url: https://korben.info/footywhoops-synthetiseur-go-portaudio-dsp.html
note: 0
seen: false
---

<p>Faire du bruit avec du code, c'est un peu le graal pour tout dev qui aime la musique. On connaît tous les gros trucs en C++ ou les frameworks spécialisés, mais voir débarquer un synthé complet codé en <strong>Go</strong>, c'est toujours une petite surprise qui se déguste sans modération.</p>
<p>Son nom : <strong>
<a href="https://github.com/system32-ai/footywhoops?tab=readme-ov-file">Footywhoops</a>
</strong>.</p>
<p>C'est un couteau suisse sonore que vous pilotez directement depuis votre terminal et qui permet de générer des séquences de batterie, des lignes de basse (un mode &quot;Acid Bass&quot; bien gras avec sub-oscillateur et enveloppes ADSR est de la partie), des arpèges et des mélodies. Le tout peut être calé sur différentes gammes musicales (majeure, mineure, dorienne, blues, etc.) pour éviter de finir avec une cacophonie insupportable. On est un peu dans l'esprit du live coding musical comme ce que propose
<a href="https://korben.info/strudel-live-coding-music-browser.html">Strudel</a>
ou
<a href="https://korben.info/dittytoy-live-coding-musique-navigateur.html">Dittytoy</a>
, mais version ligne de commande.</p>
<div class="audio-container">
<audio controls preload="metadata">
<source src="https://korben.info/footywhoops-synthetiseur-go-portaudio-dsp/footywhoops-synthetiseur-go-portaudio-dsp-1.wav" type="audio/mpeg" />
Votre navigateur ne supporte pas l'élément audio.
</audio>
<p>Sous le capot, c'est du sérieux niveau DSP (<em>Digital Signal Processing</em>) puisqu'on y trouve une réverbération de type <strong>Schroeder</strong> pour donner de l'espace, plusieurs algorithmes de distorsion (Tanh, Atan, hard clipping) pour salir le signal, et un filtre passe-bas pour sculpter la tonalité. Et pour ceux qui se demanderaient quel est le meilleur langage pour la programmation audio, le C++ reste le roi pour la performance pure, mais Go s'en sort étonnamment bien ici grâce à sa gestion efficace de la concurrence (coucou les goroutines) et l'utilisation de <strong>PortAudio</strong> pour l'I/O audio. On a d'ailleurs vu d'autres outils sympas en Go récemment, comme
<a href="https://korben.info/sshm-manager-ssh-tui-go-bubble-tea.html">SSHM</a>
qui utilise le framework Bubble Tea pour son interface terminal.</p>
<p>Le truc est super léger et s'installe en deux minutes si vous avez l'environnement Go prêt sur votre machine. Vous pouvez même enregistrer vos expérimentations directement en WAV (dry ou wet) sans avoir besoin de passer par une DAW (<em>Digital Audio Workstation</em>). D'ailleurs, si vous cherchez des ressources pour faire de la musique sous pingouin, n'hésitez pas à consulter ce
<a href="https://korben.info/linuxdaw-catalogue-audio-linux.html">catalogue audio pour Linux</a>
.</p>
<p>Et si vous avez envie de tester ce petit monstre, voici comment vous lancer.</p>
<p>Pour commencer, vous aurez besoin de <strong>Go 1.19</strong> ou plus et des bibliothèques de développement de <strong>PortAudio</strong> sur votre système.</p>
<p><strong>1. Installation des dépendances</strong></p>
<p>Sur <strong>macOS</strong> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">brew install portaudio
</span></span></code></pre><p>Sur <strong>Ubuntu/Debian</strong> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">sudo apt-get install portaudio19-dev
</span></span></code></pre><p><strong>2. Compilation du projet</strong></p>
<p>Récupérez le code et compilez l'exécutable :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://github.com/system32-ai/footywhoops
</span></span><span class="line"><span class="cl">cd footywhoops
</span></span><span class="line"><span class="cl">go build
</span></span></code></pre><p><strong>3. Exemples d'utilisation</strong></p>
<p>Pour lancer une génération automatique de mélodie et de batterie (le mode &quot;standalone&quot;) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./footywhoops -mode synth
</span></span></code></pre><p>Si vous voulez utiliser Footywhoops comme un processeur d'effets (par exemple pour traiter le son de votre micro ou d'une guitare branchée sur votre interface) :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./footywhoops -mode fx -dist 0.8 -reverb 0.5
</span></span></code></pre><p>Vous pouvez évidemment jouer avec plein de paramètres en CLI pour ajuster le son (fréquence du filtre, type de distorsion, taille de la réverb, etc.). Pour voir toutes les options disponibles, un petit <code>./footywhoops -help</code> et voilà, vous avez la liste complète.</p>
<p>Je pense que j'ai fait le tour... si vous aimez le mélange entre code et synthèse sonore, Footywhoops est un super terrain de jeu. C'est brut, c'est sale, et c'est expérimental mais ça permet de s'amuser un peu !</p>