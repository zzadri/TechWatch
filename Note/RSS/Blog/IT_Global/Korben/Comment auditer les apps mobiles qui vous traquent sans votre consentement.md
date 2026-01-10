---
title: "Comment auditer les apps mobiles qui vous traquent sans votre consentement"
author: "Korben"
date: 2026-01-09T16:18:30.000Z
type: site
subject:
category: IT Global
tags:
  - "vie-privee-anonymat"
  - "Android"
  - "RGPD"
  - "TrackerControl"
  - "Tracking"
  - "vie privée"
rss_source: Blog
url: https://korben.info/apps-mobiles-tracking-rgpd-audit.html
note: 0
seen: false
---

<p>Si vous avez installé une app récemment, vous avez surement remarqué le petit popup RGPD qui vous demande votre consentement pour les cookies et le tracking. Vous cliquez évidemment sur &quot;Refuser&quot; en vous disant que c'est réglé... Ben en fait... non.</p>
<p>Des chercheurs ont passé au crible 400 applications mobiles populaires (200 sur Android, 200 sur iOS) et résultat, 100% d'entre elles violent au moins une exigence du RGPD. Et près de la moitié de ces apps continuent à contacter des trackers MÊME APRÈS que vous ayez dit non.</p>
<p>Sympa le &quot;consentement&quot; !</p>
<p>Du coup, plutôt que de vous laisser vous faire gauler par ces mouchards, je vous propose un petit guide pour auditer vous-même les apps que vous utilisez. Sans vous prendre la tête, promis.</p>
<h2 id="ce-quil-vous-faut">Ce qu'il vous faut</h2>
<ul>
<li>Un téléphone Android (iOS, c'est plus compliqué, Apple verrouille tout)</li>
<li>
<a href="https://f-droid.org/fr/packages/net.kollnig.missioncontrol.fdroid/">TrackerControl</a>
, l'outil d'audit qu'on va utiliser</li>
<li>10 minutes de votre temps</li>
<li>L'option &quot;Sources inconnues&quot; activée dans les paramètres sécurité d'Android (l'app n'est pas sur le Play Store...)</li>
</ul>
<h2 id="étape-1--installer-trackercontrol">Étape 1 : Installer TrackerControl</h2>
<p>TrackerControl est donc un outil open source développé par des chercheurs. La bestiole analyse le trafic réseau de chaque app pour détecter les connexions vers des serveurs de tracking.</p>
<p>Rendez-vous sur
<a href="https://github.com/TrackerControl/tracker-control-android">le GitHub du projet</a>
et téléchargez l'APK. Installez-le en autorisant temporairement les sources inconnues.</p>
<h2 id="étape-2--lancer-laudit">Étape 2 : Lancer l'audit</h2>
<p>Une fois installé, TrackerControl se comporte comme un VPN local (vos données ne sortent pas de votre téléphone, rassurez-vous). Activez-le et lancez l'app que vous voulez auditer.</p>
<p>L'outil va alors intercepter toutes les connexions sortantes et les classer : publicité, analytics, tracking social, fingerprinting... Y'a de quoi faire le tri !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/apps-mobiles-tracking-rgpd-audit/apps-mobiles-tracking-rgpd-audit-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface de TrackerControl - sobre mais efficace (
<a href="https://github.com/TrackerControl/tracker-control-android">Source</a>
)</em></p>
<h2 id="étape-3--interpréter-les-résultats">Étape 3 : Interpréter les résultats</h2>
<p>Ce qu'il faut surveiller :</p>
<ul>
<li><strong>Connexions AVANT toute action</strong> : Si l'app contacte des trackers dès son lancement, avant même que vous ayez vu un popup de consentement, c'est une violation du critère &quot;Prior consent&quot;</li>
<li><strong>Connexions APRÈS refus</strong> : Relancez l'app après avoir refusé le tracking. Si des connexions partent quand même vers Google Analytics, Facebook ou autres... bingo !</li>
<li><strong>Le nombre de domaines contactés</strong> : Une app de lampe torche qui contacte 15 serveurs différents, c'est suspect (oui ça existe)</li>
</ul>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/apps-mobiles-tracking-rgpd-audit/apps-mobiles-tracking-rgpd-audit-3.png" alt="" loading="lazy" decoding="async">
<p><em>Détail des trackers détectés - on voit tout ce qui sort (
<a href="https://github.com/TrackerControl/tracker-control-android">Source</a>
)</em></p>
<h2 id="les-6-critères-rgpd-que-les-apps-violent">Les 6 critères RGPD que les apps violent</h2>
<p>
<a href="https://dl.acm.org/doi/fullHtml/10.1145/3600160.3605079">L'étude suivante</a>
a identifié six types de violations :</p>
<ul>
<li><strong>Prior</strong> : L'app collecte VOS données avant de vous demander votre avis</li>
<li><strong>Informed</strong> : On vous dit pas vraiment ce qu'on fait avec vos données</li>
<li><strong>Freely-given</strong> : Pas le choix, c'est &quot;accepte ou dégage&quot;</li>
<li><strong>Specific</strong> : Le consentement est trop vague, genre &quot;améliorer nos services&quot;</li>
<li><strong>Unambiguous</strong> : L'interface est conçue pour vous faire cliquer sur &quot;Accepter&quot;</li>
<li><strong>Revocable</strong> : Vous dites non, mais ça continue quand même (près de la moitié des apps)</li>
</ul>
<p>C'est flippant, non ? Comme je vous l'expliquais dans
<a href="https://korben.info/smartphone-espionnage-publicite-ciblee-mythe-realite.html">mon article sur le mythe du smartphone espion</a>
, le vrai problème n'est pas le micro qui vous écoute... c'est ce réseau de data brokers qui aspire tout ce qu'ils peuvent.</p>
<h2 id="dépannage">Dépannage</h2>
<p>Et si TrackerControl ne détecte rien, vérifiez que le &quot;VPN&quot; est bien actif (icône de clé dans la barre de notifications). Certaines apps détectent les VPN et changent leur comportement, du coup relancez plusieurs fois pour être sûr.</p>
<p>Pour aller plus loin dans la protection de vos données, j'ai publié également
<a href="https://korben.info/supprimer-donnees-personnelles-internet-guide-2025.html">ce guide sur la suppression de vos données personnelles</a>
qui vous donnera quelques pistes.</p>
<p>Voilà, maintenant vous avez les outils pour aller à la pêche aux trackers. De quoi regarder vos apps d'un autre œil, j'imagine !</p>
<p>
<a href="https://dl.acm.org/doi/fullHtml/10.1145/3600160.3605079">Source</a>
</p>