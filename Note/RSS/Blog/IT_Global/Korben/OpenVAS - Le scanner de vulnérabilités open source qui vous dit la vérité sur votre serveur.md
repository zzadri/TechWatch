---
title: "OpenVAS - Le scanner de vulnérabilités open source qui vous dit la vérité sur votre serveur"
author: "Korben"
date: 2026-02-15T09:47:00.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/outils-securite"
  - "tutoriels-guides/tutoriels-avances"
  - "audit serveur"
  - "Cybersécurité"
  - "Docker"
  - "Greenbone"
  - "OpenVAS"
  - "scanner vulnérabilités"
  - "sécurité"
rss_source: Blog
url: https://korben.info/openvas-scanner-vulnerabilites-gratuit-audit-secur.html
note: 0
seen: false
---

<p>Vous avez un serveur, un NAS, quelques services qui tournent chez vous ou au boulot, et vous vous demandez si tout ça est bien sécurisé ? Alors plutôt que d'attendre qu'un petit malin vous le fasse savoir de manière désagréable, autant prendre les devants avec un scanner de vulnérabilités.</p>
<p><strong>Attention :</strong> si vous scannez le réseau de votre boulot, demandez toujours une autorisation écrite avant car scanner sans permission, c'est illégal et ça peut vous coûter cher. Et ne comptez pas sur moi pour vous apporter des oranges en prison.</p>
<p><strong>OpenVAS</strong> (Open Vulnerability Assessment Scanner), c'est l'un des scanners open source les plus connus, maintenu par Greenbone. Une fois en place sur votre réseau, il scanne vos services exposés et vous balance un rapport avec ce qui craint : Ports ouverts, services mal configurés, failles connues, certificats expirés... De quoi repérer une bonne partie de ce qu'un attaquant pourrait exploiter.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/openvas-scanner-vulnerabilites-gratuit-audit-secur/openvas-scanner-vulnerabilites-gratuit-audit-secur-2.png" alt="" loading="lazy" decoding="async">
<p><em>L'interface principale d'OpenVAS</em></p>
<p>Ce qui est cool, c'est que vous restez en mode défensif. C'est pas un outil de pentest offensif ou de hacking pur et dur mais juste un audit de votre propre infra pour savoir où vous en êtes. Et ça tourne avec un feed de vulnérabilités (le Greenbone Community Feed) qui est régulièrement mis à jour, ce qui permet de détecter les failles récentes.</p>
<p>Pour l'installer, une des méthodes c'est de passer par Docker. Greenbone fournit une stack complète avec docker-compose. Après vous cherchez plutôt à analyser spécifiquement vos images de conteneurs,
<a href="https://korben.info/analyse-vulnerabilites-conteneurs-docker-avec-grype.html">Grype pourrait aussi vous intéresser</a>
.</p>
<p>Pour OpenVAS, vous créez un répertoire, vous téléchargez leur fichier de config (jetez toujours un œil dedans avant de l'exécuter, c'est une bonne pratique), et hop :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">mkdir -p ~/greenbone-community-container
</span></span><span class="line"><span class="cl">cd ~/greenbone-community-container
</span></span><span class="line"><span class="cl">curl -f -O -L https://greenbone.github.io/docs/latest/_static/docker-compose.yml
</span></span><span class="line"><span class="cl">docker compose pull
</span></span><span class="line"><span class="cl">docker compose up -d
</span></span></code></pre>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/openvas-scanner-vulnerabilites-gratuit-audit-secur/openvas-scanner-vulnerabilites-gratuit-audit-secur-3.png" alt="" loading="lazy" decoding="async">
<p><em>L'assistant de configuration initiale</em></p>
<p>Après ça, vous accédez à l'interface web via <code>http://localhost:9392</code>.</p>
<p>Et pour le login, attention, car sur les versions récentes du conteneur communautaire, le mot de passe admin est <strong>généré aléatoirement</strong> au premier démarrage. Il faut donc aller voir les logs pour le récupérer (<code>docker compose logs -f</code>). Si ça ne marche pas, tentez le classique admin/admin, mais changez-le direct.</p>
<p>La première synchro des feeds peut prendre un moment, le temps que la base de vulnérabilités se télécharge. Vous avez le temps d'aller vous faire un café, c'est pas instantané.</p>
<p>Niveau config machine, la documentation recommande au moins 2 CPU et 4 Go de RAM pour que ça tourne, mais pour scanner un réseau un peu costaud, doublez ça (4 CPU / 8 Go) pour être à l'aise. Et une fois connecté, direction la section scans pour créer une cible avec votre IP ou plage d'adresses. Ensuite vous pouvez lancer un scan avec le profil de votre choix :</p>
<p>Le mode &quot;<strong>Discovery</strong>&quot; se contente de lister les services et ports ouverts tandis que le mode &quot;<strong>Full and Fast</strong>&quot; lance une batterie complète de tests de vulnérabilités. Il est conçu pour être &quot;safe&quot; (ne pas planter les services), mais le risque zéro n'existe pas en réseau donc évitez de scanner votre prod en pleine journée sans prévenir.</p>
<p>Les résultats arrivent sous forme de rapport avec un score de criticité comme ça vous avez le détail de ce qui pose problème et souvent des pistes pour corriger. Genre si vous avez un service SSH avec une config un peu lâche ou un serveur web trop bavard, le rapport vous le dira.</p>
<p>Par contre, c'est vrai que l'interface est assez austère comparée à des solutions commerciales comme Nessus mais c'est gratuit, c'est open source, et ça fait le taf pour un audit interne. La version Community a quand même quelques limitations (feed communautaire vs feed entreprise, support, etc.), mais pour surveiller son infra perso ou sa PME, c'est déjà très puissant.</p>
<p>Du coup, si vous voulez savoir ce qui traîne sur votre réseau avant que quelqu'un d'autre le découvre, OpenVAS est un excellent point de départ. Et c'est toujours mieux de découvrir ses failles soi-même que de les lire dans un mail de rançon... enfin, je pense ^^.</p>
<p>
<a href="https://www.greenbone.net/en/openvas-free/">A découvrir ici !</a>
</p>