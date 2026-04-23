---
title: "Notepad++ - Votre éditeur de texte préféré a été piraté"
author: "Korben"
date: 2026-02-02T12:13:42.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/actualites-securite"
  - "cybersecurite/failles-vulnerabilites"
  - "alertes de sécurité informatique"
  - "Notepad++"
rss_source: Blog
url: https://korben.info/notepad-votre-editeur-de-texte-prefere-a-ete-pirate.html
note: 0
seen: false
---

<p>Si vous utilisez Notepad++, faut que vous sachiez qu'il s'est passé un truc moche. Entre juin et décembre 2025, les serveurs de mise à jour de votre éditeur de texte préféré ont été carrément piratés. Et c'est carrément une opération d'espionnage probablement menée par un groupe parrainé par l'État chinois. Ouin 🥲.</p>
<p>En gros, les attaquants ont réussi à compromettre l'infrastructure de l'ancien hébergeur du projet. Du coup, ils ont pu détourner le trafic de mise à jour pour rediriger certains utilisateurs vers des serveurs malveillants. Ces serveurs envoyaient ensuite des fichiers de mise à jour vérolés au lieu des vrais binaires. C'est le genre de nouvelle qui file des frissons dans le dos quand on sait que des millions de dev utilisent ce logiciel quotidiennement.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/notepad-votre-editeur-de-texte-prefere-a-ete-pirate/notepad-votre-editeur-de-texte-prefere-a-ete-pirate-2.png" alt="" loading="lazy" decoding="async">
<p>Les hackers ont exploité une vulnérabilité dans le script <code>getDownloadUrl.php</code> et ont gardé un accès interne jusqu'au 2 décembre dernier. Heureusement, Notepad++ a depuis migré vers un nouvel hébergeur beaucoup plus costaud et sécurisé.</p>
<p>Donc si vous avez fait une mise à jour durant cette période, y'a de fortes chances que vous soyez concernés. L'outil de mise à jour WinGup manquait apparemment de contrôles de vérification suffisants, ce qui a permis cette redirection.</p>
<p>C'est moche de voir un outil open source aussi iconique se faire cibler de la sorte.</p>
<h2 id="comment-protéger-votre-système-">Comment protéger votre système ?</h2>
<p>Heureusement, l'équipe de développement a réagi. Voici donc ce qu'il faut faire pour dormir tranquille :</p>
<ul>
<li>Mettez à jour Notepad++ vers la version 8.8.9 au minimum. Cette version intègre déjà des premières protections.</li>
<li>Attendez la version 8.9.2 (prévue dans un mois) qui va carrément verrouiller le truc avec une vérification stricte des certificats XMLDSig.</li>
<li>Si vous avez un doute, désinstallez votre version actuelle et téléchargez la dernière mouture directement sur le nouveau site officiel.</li>
<li>Changez vos mots de passe (SSH, FTP, base de données) si vous les utilisiez avec cet outil pendant la période critique.</li>
</ul>
<p>Ensuite, un petit coup de nettoyage avec un antivirus ne fera pas de mal et si vous cherchez des alternatives le temps que ça se tasse, vous pouvez jeter un œil à
<a href="https://korben.info/notepads-un-nouvel-editeur-texte-open-source-pour-windows-10.html">Notepads</a>
ou même
<a href="https://korben.info/notepadnext-notepad-cross-platform.html">NotepadNext</a>
qui font du super boulot.</p>
<p>Bref, restez vigilants et ne traînez pas pour faire le ménage sur votre PC !</p>
<p>
<a href="https://notepad-plus-plus.org/news/hijacked-incident-info-update/">Source</a>
&amp;
<a href="https://www.neowin.net/news/how-to-protect-your-system-following-the-notepad-update-server-compromise/">Source</a>
</p>