---
title: "DNS-collector - Pour comprendre enfin ce qui se passe sur votre réseau"
author: "Korben"
date: 2026-02-07T07:38:01.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/administration-serveur"
  - "reseaux-internet/dns-domaines"
  - "DNS"
  - "DNS tunneling"
  - "open source"
rss_source: Blog
url: https://korben.info/dns-collector.html
note: 0
seen: false
---

<p>Le DNS, c'est un peu la tuyauterie planquée d'Internet. Tout le monde l'utilise, mais personne ne regarde vraiment ce qui se passe dans les tuyaux... jusqu'à ce que ça pète ou qu'un petit con s'en serve pour exfiltrer des données. Et là, bon courage pour fouiller dans les logs en mode brutasse pour comprendre qui a fait quoi sur votre réseau.</p>
<p>En fait, pour ceux qui se demandent encore qu'est-ce que le DNS (Domain Name System), c'est simplement l'annuaire qui traduit les noms de domaine comme korben.info en adresses IP. Sans lui, on serait tous en train de mémoriser des suites de chiffres à la con.</p>
<p>Et il y a quelques jours, j'ai reçu un mail de Denis, un fidèle lecteur (qui traîne sur le blog depuis 2005, ça nous rajeunit pas !) qui m'a écrit pour me présenter son projet sur lequel il bosse depuis 5 ans :
<a href="https://github.com/dmachard/DNS-collector">DNS-collector</a>
.</p>
<p>DNS-collector, c'est un outil écrit en Go qui sert de &quot;chaînon manquant&quot; entre vos serveurs DNS et votre pile de données. En gros, il capture le trafic DNS, le nettoie, l'enrichit et l'envoie là où vous en avez besoin. C'est l'outil parfait pour ceux qui ont la flemme de se palucher des fichiers PCAP de 4 Go à la main ou de debugger des flux DNStap illisibles.</p>
<p>Le point fort de DNS Collector, c'est sa flexibilité. Côté entrées, ça avale tout : du DNStap via socket Unix ou TCP (le protocole standard utilisé par BIND, Unbound ou PowerDNS), du sniffing réseau classique avec AF_PACKET ou même XDP pour la très haute performance. Attention quand même, pour XDP, apparemment le kernel Linux doit être récent (version 5.x minimum) et les drivers réseau doivent suivre, sinon ça va faire pshitt. Ensuite, par défaut, le bousin écoute pépouze sur le port UDP/6000 en attendant ses flux.</p>
<img src="https://korben.info/dns-collector/dns-collector-1.gif" alt="" loading="lazy" decoding="async">
<p>Mais là où ça devient vraiment balaise, c'est dans le traitement des données. DNS-collector embarque des &quot;Transformers&quot; (rien à voir avec Optimus Prime hein ^^) qui font tout le boulot ingrat à votre place dans le pipeline de traitement. Hop, ça normalise les noms de domaine en minuscules (le fameux qname-lowercase dans le fichier de config), ça ajoute la géolocalisation via GeoIP (genre MaxMind ou IP2Location), et on peut même détecter les trucs louches.</p>
<p>Il peut aussi détecter le tunneling DNS ou les domaines générés par algorithme (DGA) qui sont souvent les signes d'une infection sur une machine. Petit bémol cependant, pour la géolocalisation, pensez à télécharger vos bases GeoIP au préalable (fichiers .mmdb), sinon l'outil va vous faire une petite grimace au démarrage.</p>
<p>Vous pouvez aussi protéger la vie privée de vos utilisateurs en anonymisant les adresses IP via un hachage SHA1 ou du masquage. C'est propre, ça respecte le RGPD, et ça permet de garder des stats utiles (genre le top des ASN consultés) sans fliquer tout le monde. Les données sortent proprement en JSON ou en Protobuf, prêtes à être ingérées.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/dns-collector/dns-collector-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>Une fois que vos données sont propres, vous les envoyez où vous voulez. J'ai choisi de vous citer ClickHouse ou InfluxDB car c'est parfait pour stocker des millions de requêtes sans mettre votre serveur à genoux, mais la liste est longue : Prometheus pour les métriques, ElasticSearch, Kafka, Redis, ou même Slack via des webhooks pour être alerté en temps réel quand un domaine louche pointe le bout de son nez.</p>
<p>Alors si ça vous chauffe, comment récupérer cet outil et le mettre en place ?</p>
<p>Hé bien c'est hyper fastoche comme d'hab puisque le projet est dispo en binaire ou via Docker. Ensuite, vous lancez la commande <code>./dnscollector -config config.yml</code>, vous branchez vos sources, et roule ma poule. Taaadaaaa ! DNS-collector s'occupera du reste sans vous bouffer toute votre RAM (contrairement à certaines usines à gaz Java qui demandent un sacré paquet de mémoire vive ^^).</p>
<p>Voilà, perso, je trouve l'approche très saine. C'est léger, modulaire et ça répond à un vrai besoin pour les admins sys qui veulent enfin &quot;voir&quot; ce qui transite par leurs serveurs. Le bousin encaisse des milliers de requêtes par seconde sans broncher... enfin sauf si votre serveur est une patate de 2012, là je garantis rien.</p>
<p>Mortecouille, c'est quand même mieux d'avoir des logs lisibles avec un simple <code>tail -f /var/log/syslog</code>, non ? Et d'ailleurs, le projet est déjà adopté par pas mal d'acteurs de la sécu, donc vous pouvez y aller sereinement.</p>
<p>Merci Denis !</p>