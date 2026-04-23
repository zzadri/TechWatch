---
title: "Flipbook - Le web où chaque page est une image IA"
author: "Korben ✨"
date: 2026-04-23T07:03:52.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/generation-images"
  - "reseaux-internet/navigateurs-web"
  - "génération d'images"
  - "génération vidéo"
  - "GPU"
  - "IA"
  - "IA générative"
  - "navigateur"
rss_source: Blog
url: https://korben.info/flipbook-page-wiki-visuel-ia-infinite.html
note: 0
seen: false
---

<p><strong>Flipbook</strong> est un navigateur web génératif où aucune page n'existe avant que vous ne la demandiez. Pas de HTML, pas de boutons, pas de liens... A la place, vous tapez simplement un mot ou un sujet dans la barre de recherche (ou vous uploadez une image), et hop, ça vous pond une image en direct façon &quot;infographie&quot; qui explique ce sujet.</p>
<p>Ensuite, vous cliquez n'importe où sur cette image, et une nouvelle image apparaît qui creuse ce que vous venez de cliquer. En gros, faut imaginer Wikipedia mais avec aucun article pré-écrit puisque chaque page est dessinée par une IA pendant que vous patientez. C'est un genre d'Infinite Wiki en version 100% visuelle !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/flipbook-page-wiki-visuel-ia-infinite/flipbook-page-wiki-visuel-ia-infinite-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>La page que Flipbook m'a sortie quand j'ai tapé mon nom. Tout ce que vous voyez est une seule image générée par le modèle, y compris le texte.</em></p>
<p>Perso, j'ai juste tapé mon pseudonyme ce matin pour tester et comme résultat, j'ai obtenu une page intitulée &quot;Korben: The French Tech Influence&quot;, avec mon vrai nom Manuel Dorne, le lancement de korben.info noté en 2004, RemixJobs cité et même cette citation : &quot;<em>A cornerstone of the French-speaking web for over two decades</em>&quot; écrit en bas.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/flipbook-page-wiki-visuel-ia-infinite/flipbook-page-wiki-visuel-ia-infinite-2.jpeg" alt="" loading="lazy" decoding="async">
<p>Ne vous inquiétez pas pour mes chevilles, c'est pas moi qui le dit mais l'IA qui a chopé ces infos très précises et pour la majorité exacte. Le système de Flipbook fait une vraie recherche web agentique, et pas juste de l'hallucination pure à partir de son modèle. Les créateurs l'expliquent d'ailleurs dans leur FAQ.</p>
<p>Ensuite, il suffit de cliquer sur des éléments de l'image pour qu'une nouvelle image soit générée avec d'autres informations plus précises selon ce sur quoi vous avez cliqué.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/flipbook-page-wiki-visuel-ia-infinite/flipbook-page-wiki-visuel-ia-infinite-3.jpeg" alt="" loading="lazy" decoding="async">
<p>Mais le détail qui tue, c'est que TOUT le texte affiché à l'écran est rendu par le modèle d'image lui-même ! Aucune superposition HTML, aucun overlay texte. Les titres, les labels, les légendes, les flèches... tout est dessiné pixel par pixel au moment de la génération, comme si Photoshop crachait une infographie complète à chaque requête.</p>
<p>Le hic c'est que parfois ça bug (le modèle écrit un mot au mauvais endroit, ou fait une petite faute de frappe), mais c'est le choix assumé de l'équipe, qui ne souhaite aucune couche de rendu HTML classique. Sous le capot en fait, y'a LTX Studio (le modèle vidéo de Lightricks) qui anime les transitions en stream vidéo live, et Modal Labs pour l'infra GPU serverless qui encaisse la charge.</p>
<div class="video-container" id="video-container-flipbook-page-wiki-visuel-ia-infinite-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/flipbook-page-wiki-visuel-ia-infinite/flipbook-page-wiki-visuel-ia-infinite-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/flipbook-page-wiki-visuel-ia-infinite/flipbook-page-wiki-visuel-ia-infinite-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>Après comme d'hab avec ce genre d'outils c'est que les hallucinations factuelles sont invisibles pour l'utilisateur, puisqu'il n'y a pas de source citée, ni de lien à cliquer pour vérifier.</p>
<p>Et Zain Shah, l'un des créateurs, l'admet lui-même dans son thread de lancement sur X, Flipbook est aujourd'hui limité aux explications visuelles. Donc pas forcément adapté pour du vrai mode interactif (coder, réserver un truc, stocker de la data). Il faudra donc attendre que les modèles d'image et de vidéo deviennent plus rapides, plus précis, et surtout capables de conserver leur état pour assurer une cohérence dans le contenu (texte et images).</p>
<p>Bref, ça vaut le coup de
<a href="https://flipbook.page">tester</a>
, tapez votre nom ou votre animal préféré et voyez ce qui en sort !</p>
<p>
<a href="https://x.com/zan2434/status/2046982383430496444">Source</a>
</p>