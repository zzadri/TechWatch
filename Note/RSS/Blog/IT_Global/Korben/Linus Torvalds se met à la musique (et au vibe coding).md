---
title: "Linus Torvalds se met à la musique (et au vibe coding)"
author: "Korben"
date: 2026-01-12T13:51:10.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement"
  - "linux-open-source/logiciels-libres"
  - "audio"
  - "C"
  - "dsp"
  - "GitHub"
  - "Linus Torvalds"
  - "Python"
  - "vibe coding"
rss_source: Blog
url: https://korben.info/linus-torvalds-audionoise-audio-dsp.html
note: 0
seen: false
---

<p>Il y a quelques semaines,
<a href="https://korben.info/linus-torvalds-ia-vibe-coding-pragmatisme-dev.html">je vous parlais de la vision très pragmatique de Linus Torvalds</a>
sur l'IA et le &quot;vibe coding&quot;. Et bien figurez-vous que le créateur et mainteneur du noyau Linux ne fait pas que donner son avis, il met aussi les mains dans le cambouis (ou plutôt dans le code) avec un nouveau petit projet perso baptisé <strong>AudioNoise</strong>.</p>
<p>Alors calmez-vous tout de suite, il ne s'agit pas du prochain concurrent de Pro Tools ou d'Ableton Live. C'est un projet qu'il qualifie lui-même de &quot;silly&quot; (idiot), né de ses récentes expérimentations avec des pédales d'effets pour guitare. Après avoir joué avec le hardware et les circuits analogiques, Linus a décidé de voir ce que ça donnait côté numérique.</p>
<p>Le
<a href="https://github.com/torvalds/AudioNoise">dépôt GitHub</a>
contient des implémentations basiques en C d'effets audio : délais, phasers, et de filtres IIR (Infinite Impulse Response)... Bref, de quoi simuler des effets sans prétention.</p>
<p>Ce qui est marrant, c'est l'approche car Linus explique clairement dans le README qu'il n'y a rien de révolutionnaire là-dedans en terme d'algo mais juste des boucles de délai et des filtres simples. C'est du &quot;single sample in, single sample out&quot;, conçu pour apprendre les bases du traitement du signal (DSP).</p>
<p>Le projet inclut également un visualiseur en Python que Linus avoue avoir écrit en mode &quot;vibe-coding&quot;. En gros, comme il ne maîtrise pas vraiment Python, il a utilisé l'outil <strong>Google Antigravity</strong> pour générer le code à sa place. C'est du &quot;monkey-see-monkey-do&quot; assumé, où il a supprimé l'intermédiaire (lui-même cherchant sur Google) pour aller directement au but.</p>
<p>Bref, c'est toujours marrant de voir qu'un des devs les plus influents de la planète continue de coder des trucs &quot;juste pour le fun&quot;, sans se prendre la tête, et en utilisant les outils modernes comme un débutant curieux. Si vous voulez jeter un œil au code (ou l'utiliser pour vos propres bidouilles sonores), ça se passe sur
<a href="https://github.com/torvalds/AudioNoise">GitHub</a>
.</p>
<p>Merci à Lorenper pour le partage !</p>
<p>
<a href="https://linuxiac.com/linus-torvalds-shares-audionoise-a-personal-experiment-in-audio-dsp/">Source</a>
</p>