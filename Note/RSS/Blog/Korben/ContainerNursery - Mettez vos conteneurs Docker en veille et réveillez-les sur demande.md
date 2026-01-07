---
title: "ContainerNursery - Mettez vos conteneurs Docker en veille et réveillez-les sur demande"
author: Korben
date: Wed, 07 Jan 2026 15:18:53 +0100
type: site
subject: 
category: IT
rss-source: Blog
url: https://korben.info/containernursery-mise-veille-conteneurs-docker.html
seen: false
---


<p>Voilà un outil qui va faire plaisir aux possesseurs de homelabs qui surveillent leur consommation de ressources comme le lait sur le feu !</p>
<p>Car si vous êtes comme moi, vous avez probablement <strong>une ribambelle de conteneurs qui tournent H24</strong> sur votre bécane. Et je vous raconte pas tous ceux qui tournent alors que je m'en sers qu'une fois par an... breeeef...</p>
<p>Car même si un processus en &quot;idle&quot; ne consomme pas forcément grand-chose, c'est quand même un peu moisi de laisser tourner des services pour rien, non ? (oui, j'ai une âme d'écologiste de la ressource système).</p>
<p>C'est là qu'intervient
<a href="https://github.com/ItsEcholot/ContainerNursery">ContainerNursery</a>
, un petit utilitaire écrit en Node.js qui se comporte comme un reverse proxy intelligent qui va tout simplement stopper vos instances Docker quand aucune requête HTTP ou connexion WebSocket n'est détectée pendant un certain temps, et les redémarrer d'un coup de baguette magique dès qu'une nouvelle requête pointe le bout de son nez.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/containernursery-mise-veille-conteneurs-docker/containernursery-mise-veille-conteneurs-docker-2.png" alt="" loading="lazy" decoding="async">
<p>Pour ceux qui se demandent s'il est possible de mettre en pause un conteneur proprement, sachez que ContainerNursery va plus loin que le simple <code>docker pause</code>. Il arrête carrément le conteneur pour libérer la RAM et éviter les réveils CPU inutiles. Et il ne fait pas ça à la sauvage puisqu'il vérifie par exemple s'il n'y a pas de connexions WebSocket actives proxifiées avant de tout couper.</p>
<p>Hé oui, quand on n'est pas un connard, on évite de déconnecter un utilisateur en plein milieu de sa session.</p>
<div class="video-container" id="video-container-containernursery-mise-veille-conteneurs-docker-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/containernursery-mise-veille-conteneurs-docker/containernursery-mise-veille-conteneurs-docker-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/containernursery-mise-veille-conteneurs-docker/containernursery-mise-veille-conteneurs-docker-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>D'ailleurs, pour ne pas faire fuir vos visiteurs pendant que le conteneur sort de sa sieste, l'outil affiche une page de chargement sympa qui se rafraîchit toute seule dès que votre serveur est prêt à envoyer la sauce.</p>
<p>Côté bidouille, on reste sur du classique. Tout se règle dans un fichier <code>config.yml</code>.</p>
<p>En plus des domaines et des noms de conteneurs, vous devrez spécifier le <code>proxyHost</code> et le <code>proxyPort</code> pour que l'aiguillage se fasse correctement. Vous définissez ensuite le timeout au bout duquel tout le monde doit aller au dodo. Vous pouvez même lui dire de ne pas couper si l'utilisation moyenne du CPU dépasse un certain seuil (exprimé en pourcentage de 0 à 100 × le nombre de cœurs), histoire de ne pas flinguer un calcul lourd en cours.</p>
<p>Pour le lancer, rien de plus simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">docker</span> <span class="n">run</span> \
</span></span><span class="line"><span class="cl"> <span class="o">--</span><span class="n">name</span><span class="o">=</span><span class="s1">&#39;ContainerNursery&#39;</span> \
</span></span><span class="line"><span class="cl"> <span class="o">-</span><span class="n">v</span> <span class="o">/</span><span class="k">var</span><span class="o">/</span><span class="n">run</span><span class="o">/</span><span class="n">docker</span><span class="o">.</span><span class="n">sock</span><span class="p">:</span><span class="o">/</span><span class="k">var</span><span class="o">/</span><span class="n">run</span><span class="o">/</span><span class="n">docker</span><span class="o">.</span><span class="n">sock</span> \
</span></span><span class="line"><span class="cl"> <span class="o">-</span><span class="n">v</span> <span class="o">/</span><span class="n">mnt</span><span class="o">/</span><span class="n">ContainerNursery</span><span class="o">/</span><span class="n">config</span><span class="p">:</span><span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">src</span><span class="o">/</span><span class="n">app</span><span class="o">/</span><span class="n">config</span> \
</span></span><span class="line"><span class="cl"> <span class="n">ghcr</span><span class="o">.</span><span class="n">io</span><span class="o">/</span><span class="n">itsecholot</span><span class="o">/</span><span class="n">containernursery</span><span class="p">:</span><span class="n">latest</span>
</span></span></code></pre><p>Petit rappel de sécurité quand même... Essayez de placer un autre reverse proxy (genre Nginx ou Traefik) devant ContainerNursery pour gérer le HTTPS proprement, car ce dernier écoute en HTTP par défaut.</p>
<p>Quant au gain sur votre facture d'électricité, il dépendra évidemment de la charge réelle évitée, mais sur une grosse machine avec des dizaines de services, ça finit par compter.</p>
<p>Bref, c'est le genre de petit outil qui ne paie pas de mine mais qui permet de gagner pas mal de temps et surtout d'optimiser ses ressources sans se prendre la tête. On garde bien sûr la vieille carabine de pépé sous le lit pour les urgences, mais pour le reste, on laisse <strong>ContainerNursery</strong> gérer la crèche.</p>
<p>Un grand merci à Mickaël pour l'info !</p>
