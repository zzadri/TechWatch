---
title: "MLX-Audio - Faites parler votre Mac sans le cloud"
author: "Korben"
date: 2026-03-11T13:41:28.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/ia-developpement"
  - "Apple Silicon"
  - "OpenAI Whisper"
  - "text-to-speech"
rss_source: Blog
url: https://korben.info/mlx-audio.html
note: 0
seen: false
---

<p>Faire de la
<a href="https://korben.info/synthese-vocale-linux-mac-windows.html">synthèse vocale</a>
, de la transcription et du voice cloning en local sur son Mac, sans envoyer le moindre octet dans le cloud... hey bien c'est possible mes petits foufous et en plus comme je sais que vous avez des oursins dans les poches, hé bien bonne nouvelle : C'est gratuit !</p>
<p>
<a href="https://github.com/Blaizzy/mlx-audio">MLX-Audio</a>
, c'est donc une bibliothèque Python qui exploite le framework MLX d'Apple pour faire tourner des modèles audio directement sur les puces M1, M2, M3, M4 et maintenant M5. Cette liste est trop longue, la prochaine fois, j'écrirais M* ou M1-5 ^^. Avec cette lib, du coup, tout se fait en local sur votre machine. Si je devais oser une comparaison un peu casse gueule, je dirais que c'est un peu le Ollama de l'audio.</p>
<p>Côté text-to-speech, y'a surtout du choix. Une dizaine de modèles sont disponibles, dont Kokoro pour du multilingue (français, anglais, japonais, chinois, espagnol...), Chatterbox qui gère 23 langues, ou encore Dia pour les dialogues. Et voici comment ensuite avec une commande dans le terminal, on peut faire parler la machine :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">mlx_audio.tts.generate --model mlx-community/Kokoro-82M-bf16 --text &#34;Salut les copains&#34; --lang_code f --play
</span></span></code></pre><p>Le truc sympa, c'est que ça ne s'arrête pas à la synthèse vocale. Côté transcription, on retrouve Whisper (le modèle d'OpenAI qui gère 99 langues), Parakeet de NVIDIA pour les langues européennes, et même VibeVoice-ASR de Microsoft qui fait de la diarization (identifier qui parle dans une conversation).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/mlx-audio/mlx-audio-2.png" alt="" loading="lazy" decoding="async">
<p>Pour transcrire un fichier audio, c'est donc tout aussi simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">python -m mlx_audio.stt.generate --model mlx-community/whisper-large-v3-turbo-asr-fp16 --audio meeting.wav --verbose
</span></span></code></pre><p>Y'a aussi le
<a href="https://korben.info/voicecraft-ia-revolutionne-edition-vocale-synthese.html">voice cloning</a>
avec CSM, où vous filez un fichier audio de référence et le modèle reproduit la voix. Perso, ça fait un peu flipper mais qui est carrément bluffant ! Sauf si vous avez une voix super particulière (trop de clope hein ^^), au final le résultat est assez bon.</p>
<p>Attention, tout ça a besoin de mémoire ! Heureusement, la bibliothèque gère la quantization (de 3 à 8 bits), du coup les modèles sont compressés pour tenir dans la mémoire unifiée des puces Apple Silicon. Le plus léger, Kokoro, fait 82M de paramètres et le plus costaud, Ming Omni, monte à 16.8 milliards de paramètres (mais en mixture-of-experts, donc seulement 3B activés à la fois). Pour ce dernier, faut donc un Mac avec pas mal de RAM.</p>
<p>D'ailleurs, si vous êtes développeur, la bibliothèque expose également une API REST compatible OpenAI. Ça veut dire que vos apps qui causent déjà avec l'API d'OpenAI peuvent basculer sur du local sans changer une ligne de code... enfin presque. Car faut quand même pointer vers localhost au lieu des serveurs d'OpenAI, mais c'est à peu près tout. Y'a même un package Swift pour intégrer ça dans une app iOS ou macOS native.</p>
<p>Voilà, pour ceux qui préfèrent une interface graphique, un mode web avec visualisation 3D de l'audio est même intégré. C'est super joli !</p>
<p>Ce projet est sous licence MIT, et le mainteneur, Prince Canuma, est un ancien ingénieur ML chez Arcee AI, donc pas un random qui a forké un truc un dimanche ^^.</p>
<p>Voilà, si vous avez un Mac et que l'audio IA en local vous branche, c'est open source, c'est gratuit et ça marche carrément bien !</p>