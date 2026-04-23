---
title: "QRTape - De la musique en QR codes sur papier"
author: "Korben"
date: 2026-03-07T10:30:00.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/insolite-wtf"
  - "hardware-diy/arduino-electronique"
  - "Arduino"
  - "audio"
  - "DIY maker"
  - "QR Code"
rss_source: Blog
url: https://korben.info/qrtape-qr-code-audio-bande-papier.html
note: 0
seen: false
---

<p>Les bandes de papier perforé, ça vous parle ? C'est les trucs qui sortaient des mainframes dans les années 60... Hé bien, y'a un mec qui a décidé de remettre ça au goût du jour, sauf qu'au lieu de petits trous, lui il utilise des QR codes. Et au lieu d'y stocker des données binaires, il y stocke de la musique.</p>
<p>Le projet (un peu old c’est vrai 😜) s'appelle <strong>
<a href="https://github.com/aarossig/qrtape">QRTape</a>
</strong> et le principe c'est que vous prenez un fichier audio, vous le compressez en Opus à 12 kbps (fichier .opus de quelques Ko), vous découpez le résultat en morceaux de 2 331 octets, et chaque morceau devient un QR code imprimé sur un ruban de papier continu.</p>
<p>Une webcam Logitech C920 branchée en USB lit alors les codes un par un sur /dev/video0 pendant qu'un moteur pas-à-pas fait défiler la bande, et hop, ça joue du son !</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/gbtqU8awzWg?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Le plus beau dans l'histoire, c'est le côté bricolage total car la structure du &quot;magnétophone&quot; est faite en carton, les bobines sont des rouleaux d'essuie-tout avec des embouts en carton, et l'entraînement c'est un élastique (oui, un élastique !). Le moteur NEMA 17 est piloté par un Arduino Uno qui fait défiler 1 à 2 QR codes par seconde devant la caméra. C'est pas une hi-fi, mais ça marche très bien sur un Raspberry Pi 3 !</p>
<p>Côté logiciel, c'est la bibliothèque ZBar (libzbar0 sous Linux) qui décode les QR codes en temps réel. Chaque code contient un identifiant de séquence sur 2 octets, la taille du chunk, les données audio et un checksum CRC16 pour détecter les erreurs. Du coup si un code est illisible (froissé, mal imprimé), le système le skippe et passe au suivant sans couper la lecture.</p>
<p>D'ailleurs, le format choisi c'est du QR version 40, le plus gros possible, avec correction d'erreur moyenne. Ça donne 2 331 octets exploitables par code (le reste étant de la correction d'erreur). Attention par contre, si votre bande de papier se froisse ou prend l'humidité, c'est mort... le CRC16 détecte l'erreur mais ne corrige rien.</p>
<p>Et une fois imprimé, il obtient un morceau de 4 minutes 21 qui tient sur 157 QR codes, soit une bande de papier de quelques mètres.</p>
<p>Si vous aimez ce genre de projets rétro-futuristes, je vous invite à jeter aussi un oeil à
<a href="https://korben.info/qart-qr-code-art-generator.html">QArt Coder qui génère des QR codes artistiques</a>
ou encore aux
<a href="https://korben.info/recycler-cassette-audio-proteger-raspberry-pi.html">boîtiers Raspberry Pi en cassette audio recyclée</a>
. Y'a clairement une communauté de gens qui kiffent mélanger le vintage et le numérique et vous en faites peut-être partie ? !</p>
<p>Après on va pas se mentir, la qualité audio à 12 kbps mono c'est pas non plus du FLAC mais ça reste écoutable. Et le simple fait d'entendre de la musique sortir d'une bande de papier qui défile dans un truc en carton... c'est quand même la classe !</p>
<p>Du coup si vous avez une imprimante à étiquettes et un Arduino qui traîne, vous savez quoi faire ce dimanche.</p>