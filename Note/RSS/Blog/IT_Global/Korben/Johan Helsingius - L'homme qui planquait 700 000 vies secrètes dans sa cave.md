---
title: "Johan Helsingius - L'homme qui planquait 700 000 vies secrètes dans sa cave"
author: "Korben"
date: 2026-01-23T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hackers-celebres"
  - "vie-privee-anonymat"
  - "anon.penet.fi"
  - "anonymat"
  - "internet pionnier"
  - "remailer"
  - "Scientologie"
  - "Tor"
  - "trolling"
rss_source: Blog
url: https://korben.info/johan-helsingius-anonymiseur-internet.html
note: 0
seen: false
---


<em>Cet article fait partie de
<a href="https://korben.info/collections/hackers/">ma série spéciale hackers</a>
. Bonne lecture !</em>
<p>Imaginez un monde sans Google, sans Facebook, où pour se connecter, il faut débrancher le téléphone et écouter la symphonie stridente d'un modem 56k. Nous sommes en 1992... Quelque part à Helsinki, dans une cave mal ventilée, un ingénieur finlandais s'apprête à lancer un petit script Perl qui va faire trembler la planète entière. Johan Helsingius, ou &quot;Julf&quot; pour les intimes, vient de créer le premier grand service d'anonymat du Web : <strong>anon.penet.fi</strong>.</p>
<p>J'ai toujours eu une fascination pour ces pionniers qui ont bâti le Web avec trois bouts de ficelle et Julf est l'archétype du héros cypherpunk. Ce type, qui a étudié la musique avant de devenir un pilier du réseau, a notamment fondé <strong>EUnet Finlande</strong>, le premier FAI commercial du pays. Et tenez-vous bien, c'est lui qui a aussi aidé à tirer les premiers câbles pour connecter l'Union Soviétique à Internet. Rien que ça !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/johan-helsingius-anonymiseur-internet/johan-helsingius-anonymiseur-internet-2.png" alt="" loading="lazy" decoding="async">
<p>En 1992, alors qu'il traîne sur les newsgroups Usenet (l'ancêtre de Reddit ^^), une discussion éclate : <strong>doit-on obligatoirement signer ses messages de son vrai nom ?</strong> Pour Julf, c'est un &quot;non&quot; ferme et définitive, alors plutôt que de débattre pendant des heures, il fait ce que tout bon hacker fait et il code une solution. Il lance son serveur en octobre 1992 et c'est ce qu'on appelle un &quot;<em>remailer de type 0</em>&quot;.</p>
<p>Concrètement, vous envoyez un mail à &quot;pingouin@anon.penet.fi&quot;, le serveur efface votre nom et votre IP, vous attribue un pseudo genre &quot;an1234&quot; et transfère le message. Et voilà, le tour est joué !</p>
<p>Et la vraie révolution, c'est surtout que ça marchait dans les deux sens... Ainsi, si on répondait à &quot;an1234&quot;, le serveur renvoyait le courrier dans votre vraie boîte. C'était la première fois qu'on pouvait avoir une conversation suivie tout en restant un fantôme.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/johan-helsingius-anonymiseur-internet/johan-helsingius-anonymiseur-internet-3.png" alt="" loading="lazy" decoding="async">
<p><em>Le genre de bécane qui faisait tourner le monde en 93</em></p>
<p>Le succès de son service a été immédiat et assez violent. En quelques mois, le petit serveur gérait plus de 10 000 messages par jour. Et au moment de sa fermeture, on comptait pas moins de <strong>700 000 comptes enregistrés</strong>. C'est énorme pour l'époque ! On y trouvait des gens qui voulaient juste discuter tranquillement, mais aussi des victimes de violences conjugales, des groupes de soutien et des lanceurs d'alerte.</p>
<p>Perso, je trouve ça dingue quand on y repense. Et c'est là que les emmerdes arrivent car parmi les utilisateurs les plus actifs, on trouvait les critiques de l'Église de Scientologie. En 1995, la secte contre-attaque avec l'affaire &quot;<em>Miss Blood</em>&quot;. Ils affirment qu'un utilisateur (identifié sous le pseudo &quot;-AB-&quot;) a volé des fichiers secrets. Ils mettent alors Interpol et la police finlandaise dans la boucle et les flics débarquent chez Julf le geek juste parce qu'une secte américaine a fait son petit caprice.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/johan-helsingius-anonymiseur-internet/johan-helsingius-anonymiseur-internet-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>
<a href="https://en.wikipedia.org/wiki/Project_Chanology?utm_source=chatgpt.com">source</a>
</em></p>
<p>Car oui, le système de Julf avait une faille mortelle : <strong>c'était un système centralisé</strong>. Pour que ça marche, le serveur devait garder une table de correspondance entre les vrais mails et les pseudos donc s'il donnait la base, il grillait 700 000 personnes. Julf a tenu bon et a négocié comme un chef, acceptant de ne révéler qu'une seule identité pour sauver toutes les autres. Mais la leçon était apprise : <strong>l'anonymat centralisé ne peut pas résister à la pression légale.</strong></p>
<p>Comme si ça ne suffisait pas, la presse s'en est mêlée avec un article délirant de The Observer accusant le service d'héberger 90% de la pédopornographie mondiale. C'était techniquement impossible car le serveur avait une limite de <strong>16 Ko par message</strong>, pile de quoi bloquer les images binaires de l'époque mais le mal était fait.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/johan-helsingius-anonymiseur-internet/johan-helsingius-anonymiseur-internet-4.png" alt="" loading="lazy" decoding="async">
<p><em>
<a href="https://pet3rpan.medium.com/before-bitcoin-pt-3-90s-cryptowars-e857915fab82?utm_source=chatgpt.com">source</a>
</em></p>
<p>Alors le 30 août 1996, Julf annonce la fermeture. Le service s'arrête définitivement en septembre, laissant un vide immense mais pavant la voie aux outils modernes comme <strong>Tor</strong>. D'ailleurs, si vous voulez creuser le sujet, j'avais publié
<a href="https://korben.info/un-guide-pour-apprendre-a-creer-votre-relai-tor.html">un guide pour créer votre relais Tor</a>
ou encore comment utiliser
<a href="https://korben.info/torbirdy-pour-utiliser-thunderbird-au-travers-du-reseau-tor.html">Tor avec Thunderbird</a>
.</p>
<p>Et aujourd'hui, Julf continue de bosser dans la tech, mais son héritage le plus fort reste ces trois années folles. Alors la prochaine fois que vous utilisez un VPN ou Signal, ayez une petite pensée pour l'homme qui, seul avec son 486 dans une cave finlandaise, a offert un masque à des centaines de milliers de visages juste par principe.</p>
<p>
<a href="https://en.wikipedia.org/wiki/Johan_Helsingius">Source</a>
</p>