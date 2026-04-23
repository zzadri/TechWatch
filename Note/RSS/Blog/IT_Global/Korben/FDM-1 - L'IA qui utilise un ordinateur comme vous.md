---
title: "FDM-1 - L'IA qui utilise un ordinateur comme vous"
author: "Korben"
date: 2026-02-26T13:59:34.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "intelligence-artificielle/automatisation-ia"
  - "agent IA"
  - "automatisation"
  - "IA"
rss_source: Blog
url: https://korben.info/fdm1-modele-action-informatique-general.html
note: 0
seen: false
---

<p>
<a href="https://si.inc/posts/fdm1/">Standard Intelligence</a>
vient d'annoncer <strong>FDM-1</strong>, un modèle IA capable de contrôler n'importe quel ordinateur... en regardant l'écran et en cliquant. Comme nous !!</p>
<p>En gros le modèle regarde des pixels, comprend l'interface et exécute des actions. Clics, mouvements de souris, saisie clavier... et ça tourne à 30 FPS avec 11 ms de latence. Donc c'est beaucoup plus réactif que la plupart des français devant un formulaire administratif, quoi... ^^</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-2.png" alt="" loading="lazy" decoding="async">
<p>Concrètement, vous pourriez lui demander de remplir vos tableurs Excel ou Google Sheets, de naviguer dans SAP, Salesforce ou n'importe quel logiciel métier sous Windows, macOS ou Linux, ou d'automatiser ces clics débiles que vous faites 200 fois par jour. Attention, c'est pas un bot Selenium ou un macro AutoHotkey hein. C'est vraiment un truc qui comprend ce qu'il voit à l'écran.</p>
<p>Du coup, ça se compose de 3 blocs. Un encodeur vidéo qui compresse le flux visuel, un modèle de dynamique inverse, entraîné sur 40 000 heures de données humaines, qui relie les actions aux changements d'écran, et bien sûr le modèle d'action, qui prédit le prochain clic.</p>
<p>Le truc carrément dingue, c'est l'échelle d’entrainement de ce modèle... 11 millions d'heures de vidéo d'entraînement, 80 000 machines virtuelles en parallèle, un seul GPU NVIDIA H100 qui pilote 42 VMs à la fois. Ça représente plus d'un million de simulations par heure. Y'a de quoi faire donc !</p>
<p>Et les applications vont loin... Par exemple, CAO sur Blender 3D, conduite autonome avec moins d'une heure de vidéo à 1080p, et même du fuzzing d'applications bancaires (Ahaha, je sais ça va vous plaire ça !).</p>
<div class="video-container" id="video-container-fdm1-modele-action-informatique-general-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-1.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-1.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Si vous connaissez déjà des agents comme
<a href="https://korben.info/bytebot-agent-prend-controle-votre-ordinateur.html">ByteBot</a>
ou
<a href="https://korben.info/skyvern-automatisation-web-ia-vision-ordinateur.html">Skyvern</a>
, FDM-1 joue dans une autre catégorie. Ces outils s'appuient sur des LLMs pour comprendre ce qu'ils voient mais FDM-1, lui, fonctionne sans aucun modèle de langage. En fait, c'est du pur apprentissage visuel sans aucun GPT en dessous. C'est un
<a href="https://korben.info/open-computer-agent-robot-virtuel-ia-test.html">agent IA autonome</a>
sous stéroïdes, quoi.</p>
<div class="video-container" id="video-container-fdm1-modele-action-informatique-general-2.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-2.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-2.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Et comparé aux solutions RPA classiques genre UiPath ou Automation Anywhere, la différence est radicale. Le RPA traditionnel, c'est des scripts qui cassent dès qu'un bouton bouge de 3 pixels. Mais l'agent de Standard Intelligence lui s'en fiche puisqu'il comprend visuellement ce qu'il voit et saura s'adapter en quelques minutes. Je sens que les scrapers qui me lisent vont mouiller leur culotte...</p>
<p>Par contre, c'est maintenant le moment où je vous déçois <em>un peu</em> car le truc n'est pas encore dispo publiquement et aucune date n'est annoncée. Et les démos viennent de l'équipe elle-même... donc voilà, je reste prudent.</p>
<div class="video-container" id="video-container-fdm1-modele-action-informatique-general-3.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-3.mp4" type="video/mp4" />
<pre><code>Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
&lt;a href=&quot;/fdm1-modele-action-informatique-general/fdm1-modele-action-informatique-general-3.mp4&quot;&gt;lien vers la vidéo&lt;/a&gt;.
</code></pre>
</video>
<div>
<p>Et côté sécurité, y'a de quoi flipper un peu car un agent capable de cliquer partout sur n'importe quelle interface, ça ouvre la porte au phishing automatisé ou au clickjacking à grande échelle, sauf si des garde-fous sérieux sont mis en place (et pour l'instant, j'en vois pas).</p>
<p>Bref, c'est du lourd sur le papier mais reste à voir quand on pourra y toucher.</p>