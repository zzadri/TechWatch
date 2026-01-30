---
title: "Pourquoi votre vieux serveur Windows est une bombe à retardement, et comment la désamorcer"
author: "Korben"
date: 2026-01-16T05:52:11.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "windows/securite-windows"
  - "NTLM"
rss_source: Blog
url: https://korben.info/net-ntlmv1-danger-windows-server-rainbow-tables.html
note: 0
seen: false
---

<p>Les amis, si vous administrez encore des serveurs Windows avec des configurations &quot;d'époque&quot; (qui sentent la naphtaline quoi...), il faut qu'on parle.</p>
<p>Google Cloud (via son équipe Mandiant) vient de sortir un papier assez creepy sur <strong>Net-NTLMv1</strong>, ce vieux protocole d'authentification qu'on croyait enterré mais qui survit encore dans pas mal d'infrastructures. Verdict implacable : <strong>c'est une véritable bombe à retardement !!</strong></p>
<p>BOOM <strong>💥</strong> !</p>
<p>En gros, si vous avez encore du NTLMv1 activé quelque part sur votre réseau, un attaquant positionné sur votre réseau peut récupérer le matériel cryptographique nécessaire pour casser vos comptes. <strong>Le problème avec Net-NTLMv1</strong>, c'est qu'il s'agit d'un protocole d'authentification challenge-response qui date des années 90. C'était l'époque de Windows NT, de 2Pac et des modems 56k sauf que contrairement à la musique, la sécurité a <em>un peu</em> évolué depuis.</p>
<p>Le souci, c'est que ce protocole utilise l'algorithme DES (Data Encryption Standard) pour chiffrer ses challenges. Et le DES, aujourd'hui, c'est aussi solide qu'une porte en papier mâché.</p>
<p>Concrètement, un attaquant peut donc forcer un échange d'authentification (via des outils comme Responder) et, grâce à des <strong>Rainbow Tables</strong> (des tables arc-en-ciel), retrouver la clé de chiffrement. Une fois qu'il a cette clé, il peut reconstruire le hash NTLM et s'authentifier sur vos serveurs comme s'il était vous (attaque <em>Pass-the-Hash</em>).</p>
<p>Maintenant, la nouveauté qui va vous faire mal, c'est que Mandiant vient de publier <strong>un jeu complet de Rainbow Tables</strong> spécifiquement pour ça. Avant, il fallait les générer soi-même ou fouiller sur des sites communautaires comme
<a href="https://freerainbowtables.com/">FreeRainbowTables.com</a>
.</p>
<p>Le concept des RainbowTables c'est que plutôt que de recalculer les hashs à chaque fois, on pré-calcule des milliards de combinaisons possibles et on les stocke. Et Mandiant explique qu'avec ce dataset et du matériel grand public (moins de 600 $ de GPU), on peut désormais casser des clés NTLM en <strong>moins de 12 heures</strong>.</p>
<p>Soit une demi-journée pour transformer votre serveur &quot;sécurisé&quot; en moulin à vent... Alors <strong>comment savoir si vous êtes concerné ?</strong> Hé bien c'est là que ça devient sauvage car même si vous pensez être en NTLMv2 (la version plus sécurisée), il suffit qu'un seul équipement mal configuré, genre une vieille imprimante réseau ou un vieux logiciel force le &quot;downgrade&quot; vers NTLMv1 pour exposer des identifiants.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/net-ntlmv1-danger-windows-server-rainbow-tables/net-ntlmv1-danger-windows-server-rainbow-tables-2.png" alt="" loading="lazy" decoding="async">
<p>Heureusement, Windows permet d'auditer ça !</p>
<p>Vous pouvez aller fouiller dans les journaux d'événements (Event Viewer) et chercher l'ID <strong>4624</strong>. Si vous voyez &quot;<strong>Authentication Package: NTLM</strong>&quot; et &quot;<strong>Package Name (NTLM only): NTLM V1</strong>&quot;, c'est que vous avez un gros problème.</p>
<p><strong>Pour le guide de survie</strong>, pas de panique, on peut désamorcer le truc mais il va falloir être méthodique pour ne pas casser la prod (ce qui vous ferait passer pour un admin en carton, et on veut éviter ça).</p>
<ol>
<li><strong>Auditez d'abord</strong> : Activez les logs d'audit pour le NTLM. Ça se passe dans les GPO (Group Policy Object). <code>Computer Configuration -&gt; Windows Settings -&gt; Security Settings -&gt; Local Policies -&gt; Security Options -&gt; Network security: Restrict NTLM: Audit NTLM authentication in this domain</code></li>
<li><strong>Identifiez les coupables</strong> : Repérez les machines qui utilisent encore la v1. Souvent, ce sont de vieux serveurs 2003 qui traînent, des NAS non mis à jour ou des applis métier codées avec les pieds il y a 15 ans.</li>
<li><strong>Forcez le NTLMv2</strong> : Une fois que vous avez tout nettoyé, modifiez la GPO : <code>Network security: LAN Manager authentication level</code>. Passez-la à <strong>&quot;Send NTLMv2 response only. Refuse LM &amp; NTLM&quot;</strong>.</li>
</ol>
<p>C'est radical, mais c'est une étape indispensable pour assainir votre réseau.</p>
<p>Voilà si je vous en parle c'est pas pour vous faire paniquer mais ne laissez pas traîner ça. Comme d'hab, la sécurité, c'est souvent de la maintenance de l'existant, et virer ces vieux protocoles tout nuls est probablement l'action la plus rentable que vous puissiez faire cette semaine pour la sécurité de votre boite.</p>
<p>Et si vous cherchez d'autres moyens de sécuriser vos accès, jetez un œil à ce que j'écrivais sur
<a href="https://korben.info/windows-faille-critique-vol-mots-de-passe-ntlm.html">les failles critiques NTLM</a>
y'a un peu plus d'un an, ça reste d'actualité.</p>
<p>
<a href="https://cloud.google.com/blog/topics/threat-intelligence/net-ntlmv1-deprecation-rainbow-tables?hl=en">Source</a>
</p>