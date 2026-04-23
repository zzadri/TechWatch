---
title: "CATAI - Des chats pixel art boostés à l'IA sur votre dock"
author: "Korben"
date: 2026-04-07T13:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "intelligence-artificielle/chatbots-llm"
  - "IA locale"
  - "Ollama"
  - "pixel art"
rss_source: Blog
url: https://korben.info/catai-chats-pixel-art-ia-ollama-macos.html
note: 0
seen: false
---

<p>Des chats en pixel art qui se baladent sur votre dock macOS et qui causent grâce à un LLM local... non vous ne rêvez pas car c'est ce qu'on peut obtenir avec
<a href="https://github.com/wil-pe/CATAI">CATAI</a>
, qui vous fera adopter 6 matous virtuels avec chacun sa personnalité.</p>
<p>En gros, c'est le Tamagotchi de votre dock, sauf qu'au lieu de biper quand il a faim, il vous cite du Nietzsche. Vous lancez l'app, et hop, un chat orange débarque. Il marche, il mange, il dort, il s'énerve... soit 368 sprites dessinés à la main (c'est devenu assez rare pour le souligner !!). Et quand le dock est masqué, le chat se téléporte directement sur le bord supérieur de votre fenêtre active. Parce que vous le savez, un chat, ça squatte toujours les rebords les plus improbables.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/catai-chats-pixel-art-ia-ollama-macos/catai-chats-pixel-art-ia-ollama-macos-1.jpeg" alt="" loading="lazy" decoding="async">
<p>Vous pouvez en coller jusqu'à 6 en même temps, chacun avec sa couleur et son caractère. Le noir (Ombre) est philosophe et vous pose des questions existentielles, le blanc (Neige) s'exprime en vers, le gris (Einstein) vous balance des faits scientifiques et le brun (Indiana) raconte des aventures. De temps en temps, ils miaulent tout seuls dans des bulles pixel art. &quot;Mrrp !&quot;, &quot;Prrr...&quot;, &quot;ronronronron&quot;. Perso, je trouve ça craquant.</p>
<p>Et quand vous cliquez sur un chat, ça ouvre une bulle de discussion connectée à
<a href="https://korben.info/ollama-web-search-api-tutoriel-ia-locale.html">Ollama</a>
(le moteur d'IA locale que vous connaissez sûrement). Si vous avez déjà un modèle qui tourne, votre matou vous répond alors avec sa propre personnalité. La mémoire de conversation est même persistante entre les sessions (max 20 messages par chat, pour garder un contexte de conversation raisonnable).</p>
<p>Comme c'est du Swift pur, juste les Command Line Tools suffisent pour compiler le fichier source :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">swiftc -O -o cat cat.swift -framework AppKit -framework Foundation
</span></span></code></pre><p>La compilation prend genre 3 secondes sur un M1, et le binaire pèse dans les 500 Ko, soit moins qu'une photo iPhone. Y'a aussi un <code>build.sh</code> qui crée un <code>.app</code> propre avec son icône si vous préférez.</p>
<p>Les plus anciens d'entre vous se souviendront peut-être de Neko, le petit chat qui courait après votre curseur, porté sur Mac en 1989 par Kenji Gotoh. L'un des premiers desktop pets connus. Sauf que là, comme on est en 2026, le chat vous fait la conversation via un LLM local. Si vous bidouillez déjà avec Ollama ou que vous avez découvert
<a href="https://korben.info/apfel-ia-mac-apple-silicon.html">le LLM caché de votre Mac</a>
, c'est un usage auquel vous n'aviez probablement pas pensé.</p>
<p>Notez que sans Ollama, ça fonctionne, les chats se baladent mais restent muets (ce qui est déjà sympa en soi). Et si vous collez un modèle trop lourd genre un 70B, ça va ramer vu que le streaming passe par localhost. Un petit Qwen 2.5 ou Llama 3.2 3B fait largement le taf pour des réponses de chat en 2-3 phrases.</p>
<p>Merci à William pour la découverte.</p>