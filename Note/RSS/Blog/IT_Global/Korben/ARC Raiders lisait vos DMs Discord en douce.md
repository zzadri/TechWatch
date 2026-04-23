---
title: "ARC Raiders lisait vos DMs Discord en douce"
author: "Korben"
date: 2026-03-06T12:57:31.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "jeux-video/actualites-gaming"
  - "défense de la vie privée"
  - "faille"
rss_source: Blog
url: https://korben.info/arc-raiders-discord-sdk-fuite-donnees.html
note: 0
seen: false
---

<p>Le <strong>Discord Game SDK</strong>, c'est ce petit bout de code que les devs de jeux vidéo intègrent pour afficher votre statut, gérer les invitations entre potes... sauf que dans ARC Raiders, le truc ouvrait carrément une connexion complète au serveur Discord. Du coup, vos DMs privés se retrouvaient jusqu'il y a peu, logués en clair sur votre disque dur.</p>
<p>C'est Timothy Meadows, un ingénieur en sécurité, qui a découvert le pot aux roses. En fouillant dans les fichiers de log du jeu (le chemin exact c'est <code>AppData\Local\PioneerGame\Saved\Logs\discord.log</code>), il est tombé sur des conversations privées Discord en clair.</p>
<p>Et cerise sur le gâteau, le fichier contenait aussi le Bearer token d'authentification Discord du joueur. En gros, la clé qui donne accès à TOUT votre compte !</p>
<p>Le problème vient du fait que le SDK se connecte avec un token utilisateur complet, exactement comme le ferait l'app Discord elle-même. La gateway pousse alors tous les events vers cette connexion, y compris les messages privés.</p>
<p>Sauf que le jeu ne filtre rien et balance TOUT dans un fichier log sur le disque. Ce n'est donc pas une backdoor volontaire mais juste du code mal branlé qui ne trie pas ce qu'il reçoit.</p>
<p>Meadows a bien sûr tenté de signaler la faille à
<a href="https://timothymeadows.com/arc-raiders-discord-sdk-data-exposure/">Embark Studios</a>
un mois avant de rendre l'info publique. Mais comme d'hab, pas de réponse et pas de bug bounty non plus...</p>
<p>Du coup, il a publié tranquillou ses trouvailles sur son blog le 3 mars et Embark a réagi 2 jours plus tard avec un hotfix qui désactive enfin le logging du SDK.</p>
<p>Seuls les joueurs ayant lié leur compte Discord à ARC Raiders sont touchés et c'est peut-être votre cas.... Mais bon, vu que le jeu vous le propose dès l'installation, y'a probablement pas mal de monde dans le lot.</p>
<p>Le token Bearer avait une durée de validité d'environ 167 heures (en gros, une semaine), ce qui laisse une sacrée fenêtre pour quiconque aurait accès au fichier log. Un malware, un pote curieux, un PC partagé en LAN... les scénarios ne manquent pas... Suite à cela, Embark a sorti le communiqué classique en mode &quot;<em>vos données n'ont pas quitté votre machine, on n'a rien lu, on ne lira rien</em>&quot;. OK, cool story bro, sauf que le vrai souci c'est pas Embark en fait, c'est Discord car leur SDK donne un accès beaucoup trop large aux devs tiers.</p>
<p>Car quand vous liez votre compte à un jeu, vous pensez autoriser l'affichage de votre pseudo et de votre statut et pas du tout l'accès à vos DMs. D'ailleurs, après l'incident, la page d'autorisations du jeu est passée de &quot;<em>cette application ne peut PAS lire vos messages</em>&quot; à &quot;<em>cette application PEUT lire et envoyer des messages</em>&quot;. Hop, ni vu ni connu !</p>
<p>Côté protection, c'est pas la mer à boire, suffit de changer votre mot de passe Discord dans les réglages de l'app (ça invalide tous les tokens actifs), et désactivez l'intégration Discord dans les paramètres d'ARC Raiders, puis supprimez le fichier <code>discord.log</code> dans le dossier du jeu.</p>
<p>Attention, si vous êtes du genre parano, faites aussi le ménage dans vos autorisations Discord, parce que ARC Raiders est sûrement pas le seul jeu à avoir ce genre de problème...</p>
<p>Bref, méfiez-vous des jeux qui demandent à se connecter à votre Discord... c'est pas la première fois que ça tourne mal !</p>
<p>
<a href="https://timothymeadows.com/arc-raiders-discord-sdk-data-exposure/">Source</a>
</p>