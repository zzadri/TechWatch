---
title: "Voicebox - Clonez des voix en local sans passer par le cloud"
author: "Korben"
date: 2026-03-20T11:22:27.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "intelligence-artificielle/chatbots-llm"
  - "linux-open-source/logiciels-libres"
  - "alternative open source"
  - "text-to-speech"
rss_source: Blog
url: https://korben.info/voicebox-clonage-vocal-open-source.html
note: 0
seen: false
---

<p>Si vous cherchez un moyen de faire du clonage vocal en local sans filer vos fichiers audio à un service cloud,
<a href="https://voicebox.sh">Voicebox</a>
devrait vous plaire. C'est un studio de
<a href="https://korben.info/synthese-vocale-linux-mac-windows.html">synthèse vocale</a>
open source et gratuit qui tourne entièrement sur votre machine, et qui n'a rien à envier à ElevenLabs.</p>
<p>Concrètement, vous téléchargez l'app (dispo macOS, Windows et Docker), vous importez un extrait audio d'à peine 3 secondes minimum et hop, la voix est clonée. Pas besoin de compte, pas de limite d'utilisation, pas de &quot;crédits&quot; qui fondent comme neige au soleil !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/voicebox-clonage-vocal-open-source/voicebox-clonage-vocal-open-source-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Voicebox embarque 5 moteurs TTS différents plutôt que de tout miser sur un seul. Par exemple, Qwen3-TTS gère 10 langues avec des instructions en langage naturel du genre &quot;parle lentement&quot; ou &quot;chuchote&quot;. Chatterbox Multilingual couvre 23 langues, de l'arabe au swahili en passant par le finnois.</p>
<p>LuxTTS lui est ultra-léger... genre 1 Go de VRAM et 150x plus rapide que le temps réel même sur CPU (anglais uniquement par contre) ! Et avec Chatterbox Turbo, vous pouvez injecter des tags comme [laugh], [sigh] ou [gasp] directement dans le texte pour que la voix rigole ou soupire à la demande (anglais aussi). Franchement, c'est pas mal du tout.</p>
<p>Tenez voici ce que ça donne avec ma voix (J'ai utilisé Qwen3)</p>
<div class="audio-container">
<audio controls preload="metadata">
<source src="https://korben.info/voicebox-clonage-vocal-open-source/voicebox-clonage-vocal-open-source-1.wav" type="audio/mpeg" />
Votre navigateur ne supporte pas l'élément audio.
</audio>
<p>Et pour ceux qui aiment bidouiller, y'a une API REST complète sur localhost:17493. Du coup, on peut intégrer la synthèse vocale dans ses propres scripts, automatiser la génération de podcasts ou monter un pipeline perso avec ffmpeg. Parce que bon, avoir un moteur vocal sans pouvoir l'utiliser dans ses projets, ça n'a pas d'intérêt.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/voicebox-clonage-vocal-open-source/voicebox-clonage-vocal-open-source-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Côté post-production, 8 effets audio sont dispos (pitch shift, reverb, delay, chorus, compression...) propulsés par pedalboard, la lib audio de Spotify. On peut aussi sauvegarder des presets et les appliquer par profil vocal. Y'a même un éditeur multi-pistes pour composer des conversations ou des narrations avec plusieurs voix sur une timeline.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/voicebox-clonage-vocal-open-source/voicebox-clonage-vocal-open-source-4.png" alt="" loading="lazy" decoding="async">
<p>Attention par contre, le projet est assez récent (c'est sorti en janvier) et côté Linux, y'a pas encore de binaires pré-compilés, faudra donc compiler from source mais je sais que vous adorez ça, les barbus ^^. Et le problème avec 5 moteurs différents, c'est que chacun a ses propres dépendances, donc ça prend pas mal en espace disque.</p>
<p>Sous le capot, c'est codé en Rust, ça utilise Tauri (pas Electron) car personne ne veut un genre de Chromium de 500 Mo pour lancer un simple outil audio. Sur Mac Apple Silicon, l'inférence passe par MLX et le Neural Engine et sur Windows et Linux, c'est CUDA, ROCm pour AMD, DirectML et même Intel Arc. D'ailleurs si vous voulez exploiter
<a href="https://korben.info/perspective-intelligence-web-community.html">l'IA locale sur Mac</a>
pour d'autres usages, les Foundation Models d'Apple s'y prêtent aussi.</p>
<p>Si vous avez déjà joué avec
<a href="https://korben.info/mlx-audio.html">MLX-Audio</a>
pour faire de la synthèse vocale en ligne de commande, Voicebox c'est finalement la version &quot;app complète&quot; avec interface graphique, gestion de profils vocaux et file d'attente de génération. C'est un peu le Ollama de la voix.</p>
<p>Voilà, si le clonage vocal en local vous branche, c'est sous licence MIT, c'est gratuit et ça tourne nickel ! Ah et si vous êtes un escroc qui cherche à cloner des voix pour arnaquer des gens, sachez que je viens de vous jeter un mauvais sort à travers la lecture de cet article. Attendez-vous à avoir des cheveux qui vous poussent sur la langue et des verrues dans les yeux, d'ici quelques semaines.</p>
<p>Merci à Lorenper pour la découverte.</p>