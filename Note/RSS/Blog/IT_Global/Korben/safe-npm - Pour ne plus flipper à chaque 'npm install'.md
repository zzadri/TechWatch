---
title: "safe-npm - Pour ne plus flipper à chaque 'npm install'"
author: "Korben"
date: 2026-01-16T09:00:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/malwares-menaces"
  - "developpement/outils-developpement"
  - "Cybersécurité"
  - "JavaScript"
  - "malware"
  - "NPM"
  - "shai-hulud"
  - "supply chain"
rss_source: Blog
url: https://korben.info/safe-npm-protection-supply-chain-attack-javascript.html
note: 0
seen: false
---

<p>Après l'attaque massive de septembre 2025 qui a vérolé 18 packages ultra-populaires (coucou
<a href="https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised">debug et chalk</a>
) et la campagne
<a href="https://korben.info/npm-shai-hulud-scanner-attaque-supply-chain.html">Shai-Hulud</a>
2.0 qui a siphonné les credentials cloud de 25 000 dépôts GitHub, on peut le dire, on est officiellement dans la sauce. Surtout si vous êtes du genre à faire un <code>npm install</code> comme on traverse l'autoroute les yeux bandés ! Il est donc temps de changer vos habitudes parce qu'entre les crypto-stealers qui vident vos portefeuilles en 2 heures et les malwares qui exfiltrent vos clés AWS, l'écosystème JavaScript ressemble de plus en plus à un champ de mines.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/safe-npm-protection-supply-chain-attack-javascript/safe-npm-protection-supply-chain-attack-javascript-1.webp" alt="" loading="lazy" decoding="async">
<p><em>Le rayon d'action de la campagne Shai-Hulud 2.0 - une véritable moisson de secrets (
<a href="https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack">Source</a>
)</em></p>
<p>D'ailleurs, beaucoup se demandent comment savoir si un package npm est vraiment sûr. Et la réponse classique, c'est de lire le code de toutes les dépendances. Ahahaha... personne ne fait ça, soyons réalistes. Du coup, on se base sur la popularité, sauf que c'est justement ce qu'exploitent les attaques supply chain en ciblant les mainteneurs les plus influents pour injecter leurs saloperies.</p>
<p>C'est là qu'intervient <strong>
<a href="https://github.com/kevinslin/safe-npm">safe-npm</a>
</strong>, une petite pépite qui va vous éviter bien des sueurs froides. Cela consiste à ne jamais installer une version de package publiée depuis moins de 90 jours. Pourquoi ? Parce que l'Histoire nous apprend que la plupart des compromissions massives sont détectées et signalées par la communauté dans les premiers jours ou semaines. Ainsi, en imposant ce délai de &quot;quarantaine&quot;, vous laissez aux experts en sécurité le temps de faire le ménage avant que le malware n'arrive sur votre bécane.</p>
<p>Et hop, un souci en moins !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/safe-npm-protection-supply-chain-attack-javascript/safe-npm-protection-supply-chain-attack-javascript-1.jpg" alt="" loading="lazy" decoding="async">
<p><em>La supply chain npm, le nouveau terrain de jeu préféré des attaquants (
<a href="https://www.paloaltonetworks.com/blog/cloud-security/npm-supply-chain-attack/">Source</a>
)</em></p>
<p>Concrètement, si vous voulez <code>react@^18</code> et que la version 18.5.0 est sortie hier, safe-npm va poliment l'ignorer et installer la version précédente ayant passé le test des 90 jours.</p>
<p>Pour l'installer, c'est du classique :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npm install -g @dendronhq/safe-npm
</span></span></code></pre><p>Ensuite, vous l'utilisez à la place de votre commande habituelle. L'outil propose des options bien pratiques comme <code>--min-age-days</code> pour ajuster le délai, <code>--ignore</code> pour les packages que vous savez sains (ou critiques), et surtout un mode <code>--strict</code> parfait pour votre CI afin de bloquer tout build qui tenterait d'importer du code trop frais pour être honnête. Y'a même un <code>--dry-run</code> pour voir ce qui se passerait sans rien casser, c'est nickel.</p>
<p>Alors oui, ça veut dire que vous n'aurez pas la toute dernière feature à la mode dès la première seconde. Mais bon, entre avoir une nouvelle icône dans une lib de CSS et voir son compte AWS se faire siphonner par un groupe de hackers russes, le choix est vite fait, non ? Perso, je préfère largement ce filet de sécurité, surtout quand on voit que les attaquants utilisent maintenant Gemini ou Qwen pour réécrire leur code malveillant à la volée afin d'échapper aux antivirus.</p>
<p>Bien sûr, ça ne remplace pas un bon
<a href="https://korben.info/npm-shai-hulud-scanner-attaque-supply-chain.html">scanner de malware spécifique</a>
ou une lecture attentive des vulnérabilités, mais c'est une couche de protection supplémentaire qui coûte rien et qui peut sauver votre boîte. À coupler d'urgence avec les recommandations de la CISA comme la MFA résistante au phishing et la rotation régulière de vos credentials.</p>
<p>Bref, si vous voulez kiffer votre code sans avoir l'impression de jouer à la roulette russe à chaque dépendance ajoutée, safe-npm est clairement un indispensable à rajouter dans votre caisse à outils de dev paranoïaque.</p>
<p>Allez sur ce, codez bien et restez prudents (et gardez un œil sur vos
<a href="https://korben.info/code-ia-securite-vulnerabilites-copilot.html">backdoors générées par IA</a>
, on sait jamais ^^).</p>