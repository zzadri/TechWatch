---
title: "Une hacktiviste déguisée en Pink Ranger supprime des sites de nazis en live au 39C3"
author: "Korben"
date: Tue, 06 Jan 2026 18:47:47 +0100
type: site
subject:
category:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/hackers-celebres"
  - "39C3"
  - "Chaos Computer Club"
  - "DDoSecrets"
  - "hacktivisme"
  - "nazis"
  - "WhiteDate"
rss-source: Blog
url: https://korben.info/hacktiviste-pink-ranger-supprime-sites-nazis-39c3.html
seen: false
---

<p>Vous savez ce qui est encore mieux qu'un bon film de super-héros ?</p>
<p>Une hacktiviste déguisée en Pink Ranger des Power Rangers qui supprime en direct des sites de nazis devant une salle comble de hackers en délire. Et ce moment de liesse s'est passé fin décembre au
<a href="https://korben.info/chaos-computer-club-histoire-hackers-allemands.html">39C3</a>
, le Chaos Communication Congress à Hambourg. Mais avant d'en arriver là, il a fallu une sacrée investigation.</p>
<p>Tout commence avec <strong>WhiteDate</strong>, une sorte de Tinder pour suprémacistes blancs. À côté, deux autres sites du même acabit : <strong>WhiteChild</strong> (un truc glauque pour matcher des donneurs de sperme et d'ovules &quot;de race pure&quot;) et <strong>WhiteDeal</strong> (une marketplace pour embaucher uniquement des racistes). Ça devait être sympa l'ambiance, n'empêche !</p>
<p>Les stats de WhiteDate parlent d'elles-mêmes puisque le site comptait environ 3600 profils aux USA, 600 en Allemagne, et la France, le Canada et le UK loin derrière. Et surtout <strong>86% d'hommes</strong>. On imagine bien le niveau des conversations sur ce site de losers qui cherchent l'âme sœur aryenne dans un océan de testostérone frustrée.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/hacktiviste-pink-ranger-supprime-sites-nazis-39c3/hacktiviste-pink-ranger-supprime-sites-nazis-39c3-2.png" alt="" loading="lazy" decoding="async">
<p>Les trois sites étaient gérés par une certaine &quot;Liff Heide&quot;. Un pseudo un peu trop allemand pour être vrai. Deux journalistes, Eva Hoffmann (investigatrice freelance) et Christian Fuchs (qui couvre l'extrême droite depuis 20 ans), ont mené l'enquête pour Die Zeit et ont fini par identifier la vraie personne : <strong>Christiane Haar</strong>, 57 ans, qui vit près de Kiel en Allemagne.</p>
<p>Et comment l'ont-ils trouvée ? Hé bien par l'enregistrement de la marque déposée &quot;WhiteDeal&quot; au registre du commerce allemand. Parce que oui, quand tu montes un réseau clandestin de nazis, tu n'oublies pas de déposer ta marque à l'INPI local.</p>
<p>Le souci du détail administratif, c'est toujours magique.</p>
<p>Le parcours de Christiane Haar est d'ailleurs assez dingue. Ancienne pianiste prodige, elle a vécu à Paris dans les années 2000 où elle a épousé un banquier... dont le père avait survécu à la Shoah. Oui, vous avez bien lu... Son ex-mari a raconté aux journalistes qu'elle s'était radicalisée après 2014, persuadée que l'attentat de Charlie Hebdo était une &quot;opération false flag&quot;. La descente aux enfers conspirationniste classique. Et le brave homme a fini par divorcer &quot;pour raisons politiques&quot; après qu'elle ait pété un câble antisémite lors d'un dîner avec des amis.</p>
<p>Côté autorités allemandes, c'est la lose totale par contre. Le Verfassungsschutz (les services de renseignement intérieur) surveillait le dossier depuis 2019... sauf qu'ils ont passé des années à traquer <strong>la mauvaise personne</strong>. Il existe en effet une romancière qui s'appelle vraiment Liff Heide, et ces brillants enquêteurs ont confondu les deux femmes malgré des différences flagrantes : pas le même âge, pas la même couleur de cheveux, l'une vivait à Paris depuis des décennies, l'autre à Berlin. Résultat, la pauvre romancière a perdu son job dans une université berlinoise à cause de cette bourde monumentale.</p>
<p>C'est là qu'entre en scène Martha Root (un pseudo, évidemment), une hacktiviste qui a décidé de faire ce que les services de renseignement n'avaient pas réussi en six ans.</p>
<p>Pour infiltrer ces plateformes, elle a utilisé des chatbots IA (Llama et compagnie). Elle a créé un faux profil avec une photo générée par IA, et quand son compte a bugué à force de bidouiller les champs de texte, elle a contacté le support. Ces génies lui ont non seulement débloqué son compte, mais lui ont offert <strong>3 mois de premium gratuit</strong>. Merci les gars.</p>
<p>Mais le meilleur c'est quand Martha a demandé à une connaisseuse plus calée qu'elle de jeter un œil. Cinq minutes plus tard (pour de vrai), sa pote lui envoie la faille. Il suffisait de taper <code>WhiteDate.net/download-all-users</code> dans la barre d'adresse. C'est tout. Pas d'injection SQL sophistiquée, pas d'exploit zero-day... juste une URL en clair dans l'API WordPress. La &quot;race supérieure&quot; a oublié de protéger son endpoint JSON.</p>
<p>Comme l'a dit Martha Root : &quot;<em>Avant de vouloir dominer le monde, apprenez déjà à sécuriser un WordPress</em>&quot;. C'est drôle ^^.</p>
<p>Martha Root est donc montée sur scène au 39C3, déguisée en Pink Ranger, aux côtés des deux journalistes. Et au lieu de se contenter de slides PowerPoint bien sages, elle a décidé de passer à l'action : <strong>une suppression en direct des trois sites devant une salle en délire.</strong></p>
<p>Les données récupérées (100 Go quand même) ont été transmises à DDoSecrets, le collectif qui a pris la relève de WikiLeaks pour ce genre de fuites. Ils ont baptisé ça &quot;WhiteLeaks&quot; et le partagent avec les journalistes et chercheurs vérifiés. Comme le faisait
<a href="https://korben.info/histoire-anonymous-collectif-hacker-legendaire.html">Anonymous</a>
à la grande époque, le hacktivisme continue de faire le ménage là où les autorités traînent des pieds.</p>
<p>L'admin des sites a réagi sur X en pleurnichant que c'était du &quot;<em>cyberterrorisme</em>&quot; et en promettant des représailles. Elle envoie même chaque mois un fax (oui, un fax) aux journalistes pour réclamer de la thune en dédommagement. Ah oui, parce que supprimer des sites de nazis, c'est du terrorisme, mais matcher des donneurs de sperme pour la pureté raciale, c'est juste un hobby sympa entre amis.</p>
<p>Pour couronner le tout, le site WhiteDate était développé par une boîte IT en Inde, avec la comptabilité gérée depuis Madagascar. L'internationale brune qui sous-traite à l'étranger, ça ne s'invente pas, les amis...</p>
<p>Bref, ce que Martha a trouvé en quelques jours, toute l'infrastructure de renseignement allemande n'a pas réussi à le faire en six ans.</p>
<p>Encore raté.</p>
<p>
<a href="https://techcrunch.com/2026/01/05/hacktivist-deletes-white-supremacist-websites-live-on-stage-during-hacker-conference/">Source</a>
|
<a href="https://media.ccc.de/v/39c3-the-heartbreak-machine-nazis-in-the-echo-chamber">Vidéo du talk au 39C3</a>
</p>