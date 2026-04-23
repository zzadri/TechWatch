---
title: "Dorso - L'app Mac qui floute votre écran quand vous faites le dos rond"
author: "Korben"
date: 2026-03-16T10:20:51.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/macos"
  - "tutoriels-guides/astuces-productivite"
  - "AirPods"
  - "app macos"
  - "ergonomie"
  - "open source"
  - "posture"
rss_source: Blog
url: https://korben.info/dorso-posture-mac-flou-ecran.html
note: 0
seen: false
---

<p>En ce moment, j'ai une sciatique qui me rend dingue ! Du coup, entre deux grimaces sur ma chaise de bureau ergonomique, je me suis retrouvé à chercher des trucs pour améliorer ma posture devant l'écran... et je suis tombé sur <strong>Dorso</strong>, une petite app macOS qui surveille votre posture en temps réel et qui floute progressivement l'écran quand vous commencez à vous avachir.</p>
<p>Ainsi, votre Mac vous punit si vous vous tenez mal ! Vous lancez l'app, vous vous asseyez bien droit devant votre clavier, vous cliquez sur le bouton de calibration (aïe, mes vertèbres), et ensuite Dorso surveille votre position via la webcam de votre MacBook ou iMac grâce au framework Vision d'Apple.</p>
<p>Dès que votre tête commence à piquer du nez, l'écran se floute. Plus vous &quot;slouchez&quot;, plus c'est flou. Du coup, soit vous vous redressez, soit vous bossez dans le brouillard comme un moine copiste myope. En tout cas, c'est redoutablement efficace pour corriger sa posture.</p>
<div class="video-container" id="video-container-dorso-posture-mac-flou-ecran-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/dorso-posture-mac-flou-ecran/dorso-posture-mac-flou-ecran-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/dorso-posture-mac-flou-ecran/dorso-posture-mac-flou-ecran-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Sauf que la webcam, c'est pas le seul mode de détection. Si vous avez des AirPods Pro, Max ou 3e génération, Dorso peut utiliser les capteurs de mouvement de vos écouteurs pour détecter l'inclinaison de votre tête. Pas besoin de caméra, pas besoin de lumière... vos AirPods deviennent votre &quot;coach posture&quot; et quand vous les retirez des oreilles, l'app se met en pause toute seule. Par contre, attention, le mode AirPods nécessite macOS 14 minimum et l'autorisation &quot;Motion &amp; Fitness Activity&quot; dans les réglages Confidentialité.</p>
<p>Côté vie privée, tout se passe en local sur votre machine. Aucune image n'est enregistrée, aucune donnée ne quitte votre Mac. Le flux vidéo de la webcam est traité en temps réel puis immédiatement supprimé et pour le flou, l'app utilise une API privée de CoreGraphics pour agir au niveau système, ce qui permet de flouter tous vos écrans d'un coup si vous avez un setup multi-moniteurs.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dorso-posture-mac-flou-ecran/dorso-posture-mac-flou-ecran-2.png" alt="" loading="lazy" decoding="async">
<p>L'installation, c'est un
<a href="https://github.com/tldev/dorso">brew install --cask dorso</a>
et hop, c'est réglé. Au premier lancement, il faudra autoriser l'accès caméra (mode webcam) ou Motion &amp; Fitness (mode AirPods) dans les Réglages Système.</p>
<p>L'app se loge ensuite dans la barre de menu à côté de l'icône Bluetooth et vous pouvez régler la sensibilité sur 5 niveaux via un petit panneau de préférences. Y'a même une &quot;dead zone&quot; configurable pour que ça ne se déclenche pas au moindre mouvement de tête (genre quand vous regardez votre téléphone 2 secondes). Sans cette dead zone, la moindre gorgée de café vous vaut un écran tout flou, donc c'est indispensable !!</p>
<p>L'app s'appelait &quot;Posturr&quot; à l'origine mais une app iOS portait déjà ce nom et comme c'est complétement FDP de voler le nom des autres, il a trouvé un autre nom en lançant 30 agents Claude en parallèle pendant une heure... mais pour rien puisque c'est finalement lui qui a trouvé &quot;Dorso&quot; (Claude avait suggéré &quot;Posturn&quot;, bof quoi). Comme quoi, même avec 30 IA qui bossent pour vous, le cerveau humain a encore son mot à dire !!</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dorso-posture-mac-flou-ecran/dorso-posture-mac-flou-ecran-3.png" alt="" loading="lazy" decoding="async">
<p>Perso, vu l'état de mon dos en ce moment,
<a href="https://korben.info/jai-teste-le-poste-de-travail-ergonomique-travaillerdebout-sante.html">mon bureau debout</a>
ne suffit plus. Si vous aussi vous passez vos journées courbé devant votre écran comme Gollum devant son précieux, Dorso pourrait bien vous éviter de finir chez le kiné à 60 balles la séance. L'app tourne sous macOS 13+ (Intel et Apple Silicon), c'est sous licence MIT, et c'est gratuit !</p>
<p>Bref, y'a plus qu'à se redresser. Enfin... à essayer.</p>