---
title: "Axios, l'une des bibliothèques les plus populaires de npm, piratée pour installer un cheval de Troie"
author: "Korben"
date: 2026-04-01T07:02:28.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "cybersecurite/malwares-menaces"
  - "axios"
  - "cheval de Troie"
  - "NPM"
rss_source: Blog
url: https://korben.info/axios-lune-des-bibliotheques-les-plus-populaires-de-npm-piratee-pour-installer-un-cheval-de-troie.html
note: 0
seen: false
---

<p>La bibliothèque JavaScript Axios, téléchargée plus de 100 millions de fois par semaine, a été compromise. Un attaquant a détourné le compte du mainteneur principal pour y glisser un malware multiplateforme qui vise aussi bien macOS que Windows et Linux.</p>
<h2 id="un-compte-piraté-deux-versions-vérolées">Un compte piraté, deux versions vérolées</h2>
<p>Tout est parti du compte npm de jasonsaayman, le mainteneur principal d'Axios. L'attaquant a réussi à prendre le contrôle du compte, a changé l'adresse mail vers un ProtonMail anonyme, et a publié deux versions malveillantes : axios 1.14.1 et axios 0.30.4.</p>
<p>Les deux ont été mises en ligne en l'espace de 39 minutes, et pas via le processus habituel. Au lieu de passer par GitHub Actions, le pipeline d'intégration continue du projet, les paquets ont été poussés directement avec la ligne de commande npm. Un détail qui aurait pu alerter plus tôt, mais qui est passé entre les mailles du filet pendant deux à trois heures avant que npm ne retire les versions concernées.</p>
<h2 id="un-malware-bien-préparé-avec-auto-destruction">Un malware bien préparé, avec auto-destruction</h2>
<p>Le plus vicieux dans l'affaire, c'est la méthode. Plutôt que de modifier directement le code d'Axios, l'attaquant a ajouté une dépendance fantôme appelée plain-crypto-js. Elle n'est jamais importée dans le code source, son seul rôle est d'exécuter un script d'installation qui fonctionne comme un programme d'installation de malware. </p>
<p>Ce qui veut dire que dès que vous faites un npm install, le script contacte un serveur de commande en moins de deux secondes et télécharge un programme malveillant adapté à votre système : un daemon déguisé sur macOS, un script PowerShell sur Windows, une porte dérobée en Python sur Linux. Et une fois le malware déployé, le script se supprime, remplace son propre fichier de configuration par une version propre, et fait comme si de rien n'était. Même un npm list affiche alors un numéro de version différent pour brouiller les pistes.</p>
<h2 id="une-attaque-attribuée-à-la-corée-du-nord">Une attaque attribuée à la Corée du Nord</h2>
<p>StepSecurity et Socket.dev ont été les premiers à repérer la compromission. Selon Ashish Kurmi, CTO de StepSecurity, ce n'est pas du tout une attaque opportuniste. La dépendance malveillante avait été préparée 18 heures à l'avance, trois programmes malveillants différents étaient prêts pour trois systèmes d'exploitation, et les deux branches de publication ont été touchées en moins de 40 minutes.</p>
<p>Elastic a de son côté relevé que le binaire macOS présente des similitudes avec WAVESHAPER, une porte dérobée en C++ déjà documentée par Mandiant et attribué à un acteur nord-coréen identifié sous le nom UNC1069. Pour les chercheurs en sécurité, le message est clair : si vous avez installé axios 1.14.1 ou axios 0.30.4, considérez votre machine comme compromise. Il faut supprimer la dépendance, faire tourner les identifiants, et dans certains cas, réinstaller la machine.</p>
<p>Franchement, c'est le genre d'attaque qui fait froid dans le dos. Axios, c'est une brique de base pour à peu près tous les projets JavaScript qui font des appels réseau. Et là, en deux heures, un attaquant a réussi à transformer cette brique en porte d'entrée pour un cheval de Troie, y compris sur Mac.</p>
<p>Le plus déroutant, c'est que le système de publication npm permet encore de pousser un paquet manuellement sans que personne ne bronche. Bon par contre, il faut reconnaître que StepSecurity et Socket.dev ont fait du bon boulot en détectant le problème aussi vite.</p>
<p>Sans eux, la fenêtre d'exposition aurait pu être bien plus large, c'est faramineux quand on y pense. Et quand on sait que la piste nord-coréenne revient de plus en plus souvent dans ce genre d'opérations, on se dit que la sécurité de la chaîne logicielle mérite qu'on s'y intéresse de près.</p>
<p>Source :
<a href="https://www.theregister.com/2026/03/31/axios_npm_backdoor_rat/">The Register</a>
</p>