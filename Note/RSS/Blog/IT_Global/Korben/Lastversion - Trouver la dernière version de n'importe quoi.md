---
title: "Lastversion - Trouver la dernière version de n'importe quoi"
author: "Korben ✨"
date: 2026-04-23T12:37:49.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/terminal-shell"
  - "open source"
  - "tool linux"
  - "version"
rss_source: Blog
url: https://korben.info/lastversion-cli-derniere-version-github.html
note: 0
seen: false
---

<p>Vous bossez sur un Dockerfile et vous avez besoin de la dernière version de nginx. Vous ouvrez GitHub, vous cliquez sur Releases, vous copiez-collez. Et 3 minutes plus tard, rebelote pour curl. Puis pour PHP. Sans parler du fait que dans votre script d'auto-update, vous avez hardcodé une &quot;v3.2.1&quot; qui dort là depuis 2023 parce que personne n'a pris le temps de mettre à jour le fichier.</p>
<p>
<a href="https://github.com/dvershinin/lastversion">Lastversion</a>
, c'est le petit CLI Python signé Danila Vershinin qui remplace cette corvée par une seule ligne. Vous tapez <code>lastversion apache/incubator-pagespeed-ngx</code> et vous récupérez le numéro de la dernière version.</p>
<p>Le truc marche sur GitHub, GitLab, BitBucket, PyPI, Wikipédia, les flux RSS, les plugins WordPress, Helm charts, Gitea, SourceForge... et même sur des sites qui publient leurs versions comme ils veulent, genre nginx.org.</p>
<p>La beauté du bazar, c'est qu'il comprend les humains, parce que, c'est vrai, les mainteneurs font un peu n'importe quoi avec leurs tags. Ils étiquettent <code>release-1.2.3</code> au lieu de <code>1.2.3</code>, ils marquent des release candidates en stable sans le faire exprès, ils changent de format entre <code>v20150121</code> et <code>v2.0.1</code> sans prévenir. lastversion détecte toutes ces incohérences et vous renvoie la véritable dernière stable, celle que vous vouliez dès le départ. C'est pénible à gérer à la main quand vous avez vingt dépendances à suivre. Maintenant c'est réglé tout seul avec ce petit bidule.</p>
<p>Et les sources exotiques, c'est tout un délire. <code>lastversion windows</code> vous crache le build Windows en cours, <code>lastversion ios</code> pour iOS, <code>lastversion rocky</code> vous renverra 8.4 et <code>lastversion https://en.wikipedia.org/wiki/Rocky_Linux</code> aussi, parce que le bidule va carrément parser la page Wikipédia pour vous.</p>
<p>Alors certains d'entre vous me diront que ce n'est pas utile au quotidien. Peut-être jusqu'au jour où vous devez scripter une vérif de version d'OS sans dépendre d'un outil système. Par contre, si vous enchaînez cinquante requêtes par heure sur un token GitHub anonyme, faudra pas s'étonner de manger un rate limit dans la tronche.</p>
<p>Côté one-liners qui tuent, y'a déjà de quoi faire.</p>
<p><code>wget $(lastversion --assets mautic/mautic)</code> télécharge direct la dernière archive.</p>
<p><code>lastversion --pre Aircoookie/WLED --format assets --filter ESP32.bin -d ESP32.bin</code> récupère le dernier firmware ESP32 WLED.</p>
<p>Pour Nginx, <code>lastversion https://nginx.org --major stable</code> renvoie <code>1.16.1</code> pendant que <code>--major mainline</code> renvoie <code>1.17.9</code>.</p>
<p>Vous voyez l'idée, c'est du pipe-friendly pur jus.</p>
<p>Et le mode <code>install</code>, c'est un autre délire. Vous tapez <code>lastversion install mailspring</code> et hop, il récupère l'AppImage ou le RPM du dépôt, il l'installe, et c'est fini. Attention quand même, sur les dépôts un peu bordéliques il va parfois se vautrer sur le packaging et juste vous balancer le tarball brut. Bon, c'est pas la mort, vous dézippez à la main et vous passez à la suite...</p>
<p>Combiné avec cron, <code>@daily /usr/bin/lastversion install mailspring -y</code> et votre bureau sera toujours à jour sans passer par un store. Pour tous les outils qui ne sont ni dans apt, ni dans un snap, ni dans un flatpak, c'est l'alternative la plus propre à avoir sous la main.</p>
<p>L'install se fait via <code>pip install lastversion</code> sur à peu près tout, ou <code>yum install lastversion</code> après avoir ajouté le repo GetPageSpeed si vous êtes sur CentOS, RHEL, Rocky, Alma, Fedora ou Amazon Linux.</p>
<p>Le projet est publié sous licence BSD-2, codé en Python, et il y a aussi une API utilisable directement (<code>from lastversion import latest</code>) si vous préférez appeler ça dans vos scripts plutôt que de piper dans un subprocess.</p>
<p>Bref, un chouette outil à ranger entre vos
<a href="https://korben.info/redirections-bash-qui-sauvent-ta-vie.html">redirections bash</a>
et votre
<a href="https://korben.info/sshm-gestionnaire-ssh.html">gestionnaire SSH</a>
, catégorie petits trucs qui font gagner 10 minutes par semaine.</p>