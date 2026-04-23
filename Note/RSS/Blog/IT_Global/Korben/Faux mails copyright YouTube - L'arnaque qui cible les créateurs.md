---
title: "Faux mails copyright YouTube - L'arnaque qui cible les créateurs"
author: "Korben"
date: 2026-04-19T07:08:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "vie-privee-anonymat"
  - "copyright"
  - "créateur de contenu"
  - "DMCA"
  - "phishing"
  - "scam"
rss_source: Blog
url: https://korben.info/scam-phishing-youtube-copyright-createurs-3.html
note: 0
seen: false
---

<p>Attention les amis, si vous avez une chaîne YouTube, vous allez probablement recevoir ce mail d'un certain &quot;Edward Evans&quot; ou autre qui vous explique très poliment que vous avez utilisé sa musique dans une vidéo, qu'il a déposé une plainte, et qu'il serait ravi de résoudre ça &quot;peacefully&quot;.</p>
<p>Surtout ne répondez pas !</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scam-phishing-youtube-copyright-createurs-3/scam-phishing-youtube-copyright-createurs-3-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>J'en ai reçu un hier sur ma boite mail... Un message courtois où le type explique qu'il y a eu une petite incompréhension et qu'on va arranger ça entre gens biens. Sauf que ce mail, c'est en fait le premier étage d'une arnaque bien ficelée qui a pour but final de dérober votre compte Google et de détourner votre chaîne.</p>
<p>Le premier red flag qui saute tout de suite quand on clique sur le nom de l'expéditeur c'est le display name qui affiche &quot;Edward Evans&quot;, mais dont l'adresse réelle derrière est <code>sigourneyphoebe1847@gmail.com</code>. Deux prénoms féminins + 4 chiffres au pif, c'est très typique d'un Gmail jetable créé pour la campagne.</p>
<p>Perso, je m'en fous qu'un ayant droit utilise Gmail, car ça arrive. Par contre, un nom totalement différent entre ce qui est affiché et la vraie boîte mail, ça c'est un premier signal probable qu'on vous balade !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scam-phishing-youtube-copyright-createurs-3/scam-phishing-youtube-copyright-createurs-3-3.png" alt="" loading="lazy" decoding="async">
<p>Le deuxième truc qui trahit l'arnaque, c'est le vide complet du mail. Aucune URL de la vidéo incriminée, aucun nom de morceau, aucun timestamp... juste &quot;<em>my audio track/music</em>&quot; bien générique. Le problème, c'est qu'un vrai détenteur de droits qui contacte en direct fournit généralement la vidéo exacte, l'œuvre concernée avec son numéro d'enregistrement et le passage précis.</p>
<p>Là, y'a rien.</p>
<p>Le mail est en fait volontairement flou pour maximiser les réponses, peu importe le contenu réel de votre chaîne. Par acquit de conscience, je suis allé chercher le gars sur GitHub, Twitter, Reddit, Gravatar, et compagnie mais zéro trace nulle part. C'est un pur Gmail fantôme créé juste pour l'occasion.</p>
<p>Et si vous répondez un truc du genre &quot;<em>bonjour, quelle vidéo exactement ?</em>&quot;, ce que j'ai failli faire avant de me raviser, vous recevrez un deuxième mail avec un lien vers un prétendu dossier de preuve. Le hic, c'est que le lien pointe vers <code>dmca-notification[.]info</code> ou une variante, un site documenté récemment par
<a href="https://www.malwarebytes.com/blog/threat-intel/2026/04/fake-youtube-copyright-notices-can-steal-your-google-login">Malwarebytes</a>
.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scam-phishing-youtube-copyright-createurs-3/scam-phishing-youtube-copyright-createurs-3-1.webp" alt="" loading="lazy" decoding="async">
<p>En fait le site clone l'interface YouTube, récupère votre vraie photo de profil, vos vrais subs, votre dernière vidéo, et vous invite très naturellement à vous connecter avec Google pour &quot;<em>consulter la réclamation</em>&quot;. Et peu importe que vous soyez sur macOS, Windows ou Linux, le piège fonctionnera dans n'importe quel navigateur. Et si vous tombez dans le panneau, BAM, ça part en credentials volés, et donc en compte Google récupéré, et dont la chaîne est ensuite souvent renommée, pillée et détournée, tout ça en quelques heures !</p>
<p>L'arnaque fonctionne en mode Phishing-as-a-Service. Plusieurs attaquants partagent le même backend, chacun avec son affiliate ID. Un peu comme Uber Eats, mais pour l'extorsion... sympa hein ? Selon l'analyse Malwarebytes, le kit cible spécifiquement les chaînes sous les 3 millions d'abonnés plutôt que les gros YouTubeurs, parce qu'au-dessus les créateurs ont des contacts directs chez YouTube et le kit se fait démonter trop vite. Du coup, attention si vous bossez sur votre chaîne sans équipe juridique derrière comme moi, vous êtes clairement pile dans la cible.</p>
<p>Voici donc ce qu'il faut faire si vous recevez ce mail. Premier réflexe, ne pas répondre et signaler comme phishing directement dans Gmail. Ensuite, il faut bloquer l'expéditeur pour couper les relances. Enfin, vérifiez que votre compte Google a bien la double authentification activée, idéalement avec une clé physique type YubiKey au lieu d'un SMS (plus costaud parce qu'un SIM swap, ça peut se faire en quelques minutes avec un minimum d'ingénierie sociale.</p>
<p>Allez faire aussi un tour sur
<a href="https://myaccount.google.com/security">myaccount.google.com/security</a>
pour lister les sessions actives et les apps autorisées, et virez tout ce que vous ne reconnaissez pas. Ne zappez pas non plus les gestionnaires tiers sur votre chaîne dans YouTube Studio, y'a souvent des vieilles autorisations qui traînent.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/scam-phishing-youtube-copyright-createurs-3/scam-phishing-youtube-copyright-createurs-3-4.png" alt="" loading="lazy" decoding="async">
<p>Et n'oubliez pas, LA source de vérité pour tout problème de copyright, c'est YouTube Studio, dans l'onglet Contenu, colonne Restrictions. Si y'a pas de restriction affichée en Studio, alors le mail c'est du phishing de merde, point.</p>
<p>Voilà, si vous avez une chaîne ou pas, parlez-en aussi à vos potes créateurs autour de vous car cette arnaque tourne fort en ce moment.</p>
<p>
<a href="https://www.malwarebytes.com/blog/threat-intel/2026/04/fake-youtube-copyright-notices-can-steal-your-google-login">Source</a>
</p>
<p></p>