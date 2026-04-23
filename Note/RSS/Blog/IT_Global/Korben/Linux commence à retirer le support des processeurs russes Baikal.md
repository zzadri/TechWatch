---
title: "Linux commence à retirer le support des processeurs russes Baikal"
author: "Korben"
date: 2026-04-16T16:20:00.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business"
  - "actualites-business/legislation-juridique"
  - "linux-open-source/distributions-linux"
  - "baikal"
  - "CPU"
  - "Russie"
rss_source: Blog
url: https://korben.info/linux-commence-a-retirer-le-support-des-processeurs-russes-baikal.html
note: 0
seen: false
---

<p>Le noyau Linux est en train de retirer le support matériel des processeurs Baikal, fabriqués par Baikal Electronics en Russie. Pas juste les mainteneurs cette fois, le code lui-même. Les drivers et le support de la plateforme MIPS Baikal-T1 sont en cours de suppression dans les sources du noyau, après des années de tensions autour des sanctions internationales.</p>
<p>Pour remettre en contexte, le support du Baikal-T1 (un CPU MIPS double coeur P5600 cadencé à 1,2 GHz) et du SoC BE-T1000 avait été intégré au noyau Linux à partir de la branche 5.8. Baikal Electronics travaille sur des processeurs domestiques russes, en MIPS et en ARM, pensés pour réduire la dépendance de la Russie aux puces étrangères.</p>
<p>Le problème, c'est que l'entreprise est directement sanctionnée par les États-Unis, l'Union européenne et d'autres pays, avec le soupçon que ses puces puissent finir dans du matériel militaire.</p>
<p>En octobre 2024, une première étape avait été franchie. Onze mainteneurs russes avaient été retirés du fichier MAINTAINERS du noyau, dont Serge Semin, responsable du driver Baikal-T1 PVT et de la plateforme MIPS Baikal-T1.</p>
<p>Linus Torvalds avait tranché clairement : &quot;C'est parfaitement clair pourquoi le changement a été fait, il ne sera pas annulé.&quot; Greg Kroah-Hartman, de son côté, avait invoqué des &quot;exigences de conformité&quot; liées aux sanctions américaines OFAC.</p>
<p>Mais à l'époque, le code restait. Les mainteneurs partaient, les drivers non. Du coup, un développeur de chez Baikal pouvait toujours soumettre un patch, même si trouver quelqu'un pour le merger devenait compliqué.</p>
<p>Jakub Kicinski, mainteneur du sous-système réseau du noyau, avait d'ailleurs refusé publiquement d'accepter des patches venant d'employés de Baikal Electronics, en invoquant un malaise personnel face à la situation.</p>
<p>L'étape en cours va plus loin. C'est le support matériel lui-même qui est en train d'être retiré. Concrètement, ça veut dire que les futures versions du noyau ne compileront plus pour cette plateforme, et que les distributions qui montent en version perdront le support natif de ces puces.</p>
<p>Pour les quelques machines qui tournent sur du Baikal-T1 en dehors de Russie (il y en a très peu), ça implique de rester sur un noyau ancien ou de maintenir un fork.</p>
<p>Côté Russie, Baikal Electronics maintient son propre fork du noyau Linux sur GitHub. Le projet n'est pas mort, il est juste découplé de l'upstream. Ça pose quand même une vraie question sur la viabilité long terme d'un fork désormais très isolé, sans les contributions de la communauté internationale.</p>
<p>Bref, Linux tranche dans le dur cette fois. Plus de mainteneurs, et bientôt plus de code non plus.</p>
<p>Source :
<a href="https://www.phoronix.com/news/Linux-Dropping-Baikal-CPUs">Phoronix</a>
</p>