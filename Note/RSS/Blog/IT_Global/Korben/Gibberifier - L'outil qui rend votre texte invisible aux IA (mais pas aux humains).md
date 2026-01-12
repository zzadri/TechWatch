---
title: "Gibberifier - L'outil qui rend votre texte invisible aux IA (mais pas aux humains)"
author: "Korben"
date: 2026-01-12T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "intelligence-artificielle/chatbots-llm"
  - "anti-ia"
  - "Chrome Extension"
  - "Firefox"
  - "IA"
  - "open source"
  - "protection"
  - "texte"
  - "Unicode"
rss_source: Blog
url: https://korben.info/gibberifier-texte-invisible-anti-ia-unicode.html
note: 0
seen: false
---

<p>Vous connaissez sans doute la stéganographie, l'art de planquer des messages secrets un peu partout, mais avez-vous déjà entendu parler de la stéganographie inversée ? Non ? Eh bien, laissez-moi vous présenter <strong>
<a href="https://github.com/GeneploreAI/gibberifier">Gibberifier</a>
</strong>.</p>
<p>L'idée est géniale puisqu'il s'agit de rendre un texte totalement illisible pour une IA (ChatGPT, Claude, Gemini, et consorts) tout en le laissant parfaitement clair pour nous, pauvres humains. C'est un peu comme parler une langue que les machines ne comprennent pas.</p>
<p>Le secret de cette technique réside dans l'utilisation de caractères Unicode de largeur zéro (comme le fameux <code>U+200B</code>) qui sont des caractères qui existent informatiquement mais qui ne prennent aucune place à l'écran. Gibberifier en insère aléatoirement entre les lettres de votre texte. Pour vos yeux, &quot;Bonjour&quot; reste &quot;Bonjour&quot;. Mais pour une IA, ça ressemble à un truc comme ça &quot;B\u200Bo\u200Bn\u200Bj\u200Bo\u200Bu\u200Br&quot; en indécodable.</p>
<p>Et voilà comme le tokenizer de l'IA (la partie qui découpe le texte en morceaux digestes) panique complètement. Lors de mes tests avec ChatGPT, celui-ci est à la ramasse, quand à Claude, pas moyen qu'il accepte le message, ça le fait bugger... c'est assez jouissif à voir.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gibberifier-texte-invisible-anti-ia-unicode/gibberifier-texte-invisible-anti-ia-unicode-2.png" alt="" loading="lazy" decoding="async">
<p>L'outil a été développé par <strong>GeneploreAI</strong> et le code est dispo en open source sur GitHub (licence GPL-3.0) et c'est pas juste un script python obscur, ils ont sorti des extensions pour
<a href="https://chromewebstore.google.com/detail/gibberifier/cmlaplmipnmfpfcgmegjobhobehjiagn?authuser=0&amp;hl=en">Chrome</a>
et
<a href="https://addons.mozilla.org/en-US/firefox/addon/gibberifier/">Firefox</a>
, et même une version web pour tester rapidement. J'ai testé avec ChatGPT et il galère un peu..</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/gibberifier-texte-invisible-anti-ia-unicode/gibberifier-texte-invisible-anti-ia-unicode-3.png" alt="" loading="lazy" decoding="async">
<p>Mais avant que vous ne partiez chiffrer tout votre blog, une petite mise en garde quand même : Ce n'est pas fait pour des romans entiers. L'auteur recommande de l'utiliser sur des passages courts (environ 500 caractères). C'est idéal pour protéger une &quot;formule secrète&quot;, un prompt spécifique ou un paragraphe clé que vous ne voulez pas voir aspiré par les scrapers d'entraînement.</p>
<p>Certains se demandent peut-être si c'est dangereux. En soi, non, ce sont juste des caractères standard mais c'est une belle démonstration de la fragilité actuelle des LLM. Un simple grain de sable Unicode suffit à enrayer la machine la plus sophistiquée du monde.</p>
<p>Bref, si vous voulez troller un peu les bots ou protéger un snippet de code, c'est l'outil qu'il vous faut.</p>