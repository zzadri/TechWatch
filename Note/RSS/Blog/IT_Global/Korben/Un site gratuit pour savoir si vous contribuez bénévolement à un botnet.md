---
title: "Un site gratuit pour savoir si vous contribuez bénévolement à un botnet"
author: "Korben"
date: 2026-02-21T09:28:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/malwares-menaces"
  - "cybersecurite/outils-securite"
rss_source: Blog
url: https://korben.info/detecteur-botnet.html
note: 0
seen: false
---

<p>On s'imagine souvent que les botnets, c'est un truc réservé aux PC vérolés de gamers qui téléchargent n'importe quoi. Sauf que non ! Votre box, votre routeur, ou n'importe quel appareil connecté de votre réseau domestique peut très bien faire partie d'un réseau de machines zombies sans que vous le sachiez.</p>
<p>C'est pour lutter contre ça que les gens de chez GreyNoise (une boîte spécialisée dans l'analyse des menaces réseau) ont lancé un outil gratuit pour vérifier en quelques secondes si votre IP a été repérée dans des activités de scanning suspectes. Ça s'appelle
<a href="https://check.labs.greynoise.io/">IP Check</a>
, vous allez sur le site, vous cliquez, et hop, le verdict est immédiat.</p>
<p>Quatre verdicts sont alors possibles. Soit votre IP est &quot;<strong>Benign</strong>&quot; et vous pouvez dormir tranquille. Soit elle est marquée &quot;<strong>Malicious</strong>&quot; ou &quot;<strong>Suspicious</strong>&quot;, ce qui signifie qu'elle a été repérée en train de scanner Internet ou de participer à des activités louches. Soit c'est &quot;Unknown&quot;, ce qui veut dire qu'elle n'a tout simplement jamais été vue par leurs sondes. L'outil indique aussi si votre IP appartient à un service connu (VPN, cloud, entreprise) grâce à leur base de données RIOT.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/detecteur-botnet/detecteur-botnet-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Le truc c'est que si votre IP est flaguée, l'outil vous affichera une timeline sur 90 jours, soit de quoi faire un petit diagnostic pour voir depuis quand une activité suspecte a été observée sur votre connexion. Parce que oui, le risque c'est que des botnets peuvent utiliser les connexions de particuliers comme relais pour leurs saloperies, et votre IP peut alors se retrouver sur des listes de réputation douteuse. Du coup vous vous tapez des CAPTCHA à répétition, des refus d'accès sur certains sites, ou des restrictions bizarres sur les services de streaming.</p>
<p>Et pour les amateurs de ligne de commande, y'a même une API JSON qui renvoie le statut de l'IP appelante !</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -s https://check.labs.greynoise.io/api/v1/check | jq
</span></span></code></pre><p>Après si le résultat n'est pas glorieux, les recommandations dépendront du type d'appareil. Pour vos PC et mobiles, il faudra lancer un
<a href="https://korben.info/malwarebytes-5.html">bon scan anti-malware</a>
et pour votre routeur et vos objets connectés, faudra mettre à jour le firmware (celui que personne ne met jamais à jour ^^), changer les identifiants admin par défaut, et désactiver l'accès distant si vous ne l'utilisez pas. Enfin, pour ceux qui veulent
<a href="https://korben.info/securiser-telechargements-virustotal-vt4browser.html">sécuriser automatiquement leurs téléchargements</a>
, c'est aussi le moment d'y penser.</p>
<p>C'est gratuit, ça prend quelques secondes, et ça peut vous permettre de découvrir que votre Freebox fait partie d'une armée de cyber zombies.</p>
<p>À vous de vérifier maintenant !</p>