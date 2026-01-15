---
title: "Ehud Tenenbaum - L'ado qui a hacké le Pentagone"
author: "Korben"
date: 2026-01-14T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/hackers-celebres"
  - "analyzer"
  - "Cybersécurité"
  - "Ehud Tenenbaum"
  - "Pentagone"
rss_source: Blog
url: https://korben.info/ehud-tenenbaum-analyzer-hacker-pentagon.html
note: 0
seen: false
---


<em>Cet article fait partie de
<a href="https://korben.info/collections/hackers/">ma série spéciale hackers</a>
. Bonne lecture !</em>
<p>FLASH SPÉCIAL : Un ado de <strong>18 ans</strong> vient de cracker la sécurité du Pentagone américain. Ah non pardon, c'est pas une news, c'est de l'histoire ancienne. Mais franchement, quelle histoire ! Ehud Tenenbaum, alias <strong>The Analyzer</strong>, a réussi ce que bien des services secrets n'osaient même pas rêver : infiltrer les réseaux non classifiés du Département de la Défense américain depuis sa chambre d'adolescent à Hod HaSharon.</p>
<p>Vous savez ce qui m'a plu dans cette histoire ? C'est qu'à l'époque, en 1998, j'étais moi-même en train de bidouiller mes premiers scripts sur mon Pentium 200 MHz, et pendant que je galérais à faire fonctionner tout ça, ce gamin faisait trembler l'oncle Sam. En plus, en février 1998, les USA sont en pleine opération Desert Fox contre l'Irak alors quand le DoD a détecté les intrusions, la première réaction a été la panique... et si c'était Saddam Hussein qui contre-attaquait ? Bah non, c'était juste un ado avec son clavier.</p>
<p>Mais alors qui était ce gamin ?</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-1.jpg" alt="" loading="lazy" decoding="async">
<p>Ehud &quot;Udi&quot; Tenenbaum naît le 29 août 1979 à Hod HaSharon, une petite ville tranquille d'Israël. Rien ne prédestinait ce môme à devenir l'un des hackers les plus célèbres de la planète. D'ailleurs, il souffrait de dyslexie, un handicap qui aurait pu le freiner, sauf qu'Ehud avait un truc en plus : <strong>des capacités dingues en math et en sciences</strong>. À 15 ans, il s'auto-forme au hacking armé de sa curiosité, et une connexion internet.</p>
<p>À 18 ans, Ehud fait ensuite son service militaire obligatoire dans Tsahal. Mais bon, l'armée et lui, ça fait pas bon ménage. Suite à un accident de voiture, il est libéré de ses obligations militaires. Et c'est là que tout va basculer.</p>
<p>Car Ehud ne travaille pas seul. Il monte une petite équipe avec d'autres hackers : deux adolescents en Californie (connus sous les pseudos Makaveli et Stimpy) et possiblement d'autres contacts en Israël. Tenenbaum joue le rôle de mentor technique, le cerveau qui orchestre l'opération et petit détail qui tue : <strong>
<a href="https://korben.info/solar-sunrise-1998-cyberattaque-pentagone-histoire-complete.html">Solar Sunrise</a>
</strong>, c'est pas le nom que le groupe s'est donné mais le nom de code que les autorités ont attribué à l'enquête. Solar comme Solaris, l'OS qu'ils ont hacké.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-2.png" alt="" loading="lazy" decoding="async">
<p>Pendant que le monde entier suit l'affaire Monica Lewinsky, pendant que les États-Unis bombardent l'Irak, Ehud et ses complices préparent discrètement l'une des <strong>cyberattaques</strong> les plus audacieuses de l'histoire.</p>
<p>Pour arriver à leurs fins, ils exploitent une faille dans <strong>Solaris 2.4</strong>, précisément dans le service rpc.statd qui tourne avec les privilèges root. Le truc foufou (ou flippant selon comment on voit les choses) c'est que cette vulnérabilité était <strong>connue depuis décembre 1997</strong>. Les patchs étaient disponibles, mais personne ne les avait appliqués.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-3.png" alt="" loading="lazy" decoding="async">
<p>Leur attaque se déroule en quatre phases ultra-méthodiques : reconnaissance des cibles, exploitation de la faille, déploiement de backdoors, et exfiltration de données. Ils ne frappent pas une cible après l'autre comme dans les films. Non, ils propagent leur intrusion <strong>simultanément</strong> sur plusieurs sites : bases de l'Air Force, de la Navy, systèmes de la NASA, universités sous contrat militaire, et des systèmes du DoD. Au total, plus de 500 systèmes infiltrés.</p>
<p>Heureusement, ils n'ont pas pénétré les systèmes <strong>les plus secrets</strong> du Pentagone mais uniquement des réseaux non classifiés. Mais même sur des systèmes non classifiés, vous avez des informations opérationnelles sensibles. Des backdoors installées, des sniffers qui capturent les mots de passe, des accès qui auraient pu être exploités autrement... John Hamre, le Deputy Defense Secretary de l'époque, qualifiera l'attaque de &quot;<em>la plus organisée à ce jour</em>&quot; contre les systèmes militaires américains.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-4.png" alt="" loading="lazy" decoding="async">
<p>Mais tout faux empire finit par s'effondrer.</p>
<p>Le FBI, la NSA, l'Air Force OSI et le Shin Bet israélien unissent leurs forces. Et vous le savez, les intrusions laissent des traces. Des serveurs intermédiaires, des rebonds, des adresses IP qui finissent par pointer vers Israël. La coopération internationale se met alors en place.</p>
<p>Le 18 mars 1998, Ehud Tenenbaum se réveille dans son appartement de Hod HaSharon. Sauf que ce matin-là, il ne se réveille pas avec une envie de pisser. Il se réveille avec la police israélienne dans son salon. Fin de l'aventure pour The Analyzer.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-2.jpg" alt="" loading="lazy" decoding="async">
<p>La réaction médiatique est immédiate. D'abord, le soulagement : ce n'est pas une attaque étatique irakienne. Mais ensuite, le choc : des adolescents ont paralysé les défenses informatiques du DoD. Et cette affaire va contribuer à la création de la Presidential Decision Directive/NSC-63, la politique de cybersécurité nationale des États-Unis.</p>
<p>L'affaire met trois ans à arriver devant les tribunaux. En 2001, Ehud Tenenbaum plaide coupable. La sentence initiale ? Six mois de travaux d'intérêt général. Léger, non ? Le procureur fait appel et en <strong>juin 2002</strong>, le tribunal alourdit la peine : 18 mois de prison. Mais grâce au système de libération conditionnelle israélien, qui permet une libération après environ 50% de la peine purgée, Ehud ne purge qu'environ 8 mois.</p>
<p>Sorti de prison, Ehud tente de se ranger. En 2003, il fonde <strong>2XS Security</strong>, une société de conseil en sécurité et son idée c'est d'utiliser sa notoriété pour faire du consulting. Le hacker devenu consultant, c'est un classique, mais la tentation revient. Toujours.</p>
<ol start="2008">
<li>Ehud Tenenbaum, désormais âgé de 29 ans, monte un nouveau coup. Ce qu'il veut c'est hacker les systèmes d'institutions financières américaines et canadiennes, voler des informations de cartes bancaires par milliers, les charger sur des cartes prépayées, puis utiliser un réseau international de &quot;mules&quot; pour retirer l'argent aux distributeurs.</li>
</ol>
<p>Sa cible principale est <strong>Direct Cash Management</strong>, une boîte de Calgary, en Alberta. Et sa technique c'est une bonne vieille <strong>injection SQL</strong> pour accéder à la base de données. Classique mais efficace.</p>
<p>Le butin ? Environ <strong>1,8 million de dollars canadiens</strong> (soit ~1,7 million USD) rien que pour Direct Cash Management. Mais l'opération visait aussi d'autres cibles américaines : OmniAmerican Credit Union au Texas, Global Cash Card. Au total, les pertes estimées dépassent les <strong>10 millions de dollars</strong>.</p>
<p>Ehud travaille avec des complices, dont sa fiancée <strong>Priscilla Mastrangelo</strong> à Calgary. Les charges contre elle seront finalement abandonnées, mais son implication reste floue.</p>
<p>De leur côté, le FBI et la GRC (Gendarmerie royale du Canada) ne chôment pas. Et en <strong>septembre 2008</strong>, Ehud Tenenbaum est arrêté au Canada et détenu au <strong>Calgary Remand Centre</strong>, en Alberta. L'extradition vers les États-Unis va prendre du temps.</p>
<p>En 2012, après quatre ans de procédure, Ehud accepte un <strong>plea bargain</strong>. La sentence ? Le temps déjà passé en détention (time served), <strong>503 000 dollars de restitution</strong> et trois ans de mise à l'épreuve. Fin de l'affaire américaine.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ehud-tenenbaum-analyzer-hacker-pentagon/ehud-tenenbaum-analyzer-hacker-pentagon-3.jpg" alt="" loading="lazy" decoding="async">
<p>Toutefois, l'histoire ne s'arrête pas là car en <strong>novembre 2013</strong>, Ehud Tenenbaum est de nouveau arrêté en Israël, cette fois pour blanchiment d'argent à grande échelle. Quand est-il rentré en Israël ? Ça, les archives publiques ne le disent pas, quand à l'issue de cette affaire, c'est un mystère total. Certaines sources évoquent une condamnation à sept ans de prison, d'autres restent floues. Ce qui est sûr, c'est que l'issue de cette troisième arrestation reste dans le brouillard des archives publiques accessibles.</p>
<p>Au final, quel est l'héritage d'Ehud Tenenbaum ? Solar Sunrise a été le premier grand wake-up call cybersécurité pour les États-Unis. Il a prouvé que des adolescents pouvaient paralyser une infrastructure militaire. Il a forcé le DoD à prendre la cybermenace au sérieux. Et il a contribué à façonner la politique de cybersécurité nationale américaine.</p>
<p>Tenenbaum était un génie technique incontestable. Un mec capable de détecter les failles que personne ne voyait, de comprendre les systèmes mieux que leurs créateurs. Et pourtant, il n'a jamais pu résister à la tentation. Comme d'autres hackers légendaires tels que
<a href="https://korben.info/kevin-mitnick-hacker-legende-fbi.html">Kevin Mitnick</a>
ou
<a href="https://korben.info/gary-mckinnon-hacker-nasa-pentagone-ufo.html">Gary McKinnon</a>
, Tenenbaum illustre également cette trajectoire fascinante où le génie technique côtoie l'incapacité à s'arrêter.</p>
<p>
<a href="https://en.wikipedia.org/wiki/Ehud_Tenenbaum">Source</a>
|
<a href="https://nsarchive.gwu.edu/briefing-book/cyber-vault/2018-03-23/solar-sunrise-1998-pentagons-first-cyberwar">National Security Archive - Solar Sunrise Collection</a>
|
<a href="https://www.theregister.com/2001/06/15/solar_sunrise_hacker_analyzer_escapes/">The Register</a>
|
<a href="https://www.cbc.ca/news/canada/calgary">CBC News Calgary</a>
|
<a href="https://www.controleng.com/throwback-attack-three-teens-stoke-fears-of-a-cyber-war-with-the-solar-sunrise-attack/">Control Engineering</a>
</p>