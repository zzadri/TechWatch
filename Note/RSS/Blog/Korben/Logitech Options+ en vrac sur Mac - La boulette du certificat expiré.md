---
title: "Logitech Options+ en vrac sur Mac - La boulette du certificat expiré"
author: "Korben"
date: Wed, 07 Jan 2026 13:08:30 +0100
type: site
subject:
category:
  - "apple-mobile/macos"
  - "cybersecurite/actualites-securite"
  - "bug"
  - "certificat"
  - "Logitech"
  - "macOS Big Sur"
rss-source: Blog
url: https://korben.info/logitech-options-mac-certificat-expire.html
seen: false
---

<p>Vous le savez, j'aime bien mon petit matos Logitech, surtout la gamme MX qui sauve pas mal de poignets de développeurs. Mais alors là, ce qui arrive aux utilisateurs de Mac, c'est hyper relou.</p>
<p>Si vous avez essayé de lancer <strong>Logitech Options+</strong> ce matin sur votre bécane à la pomme, vous avez sûrement eu droit à un message d'erreur bien sec de macOS vous expliquant que l'application ne peut pas être ouverte. Et non, c'est pas votre installation qui a sauté d'un coup sans prévenir.</p>
<p>Le coupable c'est surtout un stupide certificat de développeur Apple qui est arrivé à expiration.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/logitech-options-mac-certificat-expire/logitech-options-mac-certificat-expire-1.webp" alt="" loading="lazy" decoding="async">
</p>
<p>C'est le genre de truc qui arrive même aux meilleurs (enfin, surtout à ceux qui oublient de mettre un rappel dans leur calendrier), mais là ça bloque carrément le lancement de l'utilitaire. Et comme Gatekeeper, le gardien de prison de macOS, ne rigole pas avec la sécurité, il voit un certificat périmé et il verrouille tout.</p>
<p>D'ailleurs, ça me rappelle un peu les discussions sur
<a href="https://korben.info/apple-espionne-ocsp.html">la manière dont Apple vérifie la signature des apps via OCSP</a>
. Quand ça coince, plus rien ne bouge.</p>
<p>Bref, Logitech a fini par se réveiller et a sorti un petit patch. Le souci, c'est que l'updater intégré à l'appli est lui aussi aux fraises à cause du certificat. Il faut donc repasser
<a href="https://www.logitech.com/fr-fr/software/logi-options-plus.html">par la case téléchargement manuel</a>
sur leur site pour réinstaller une version propre.</p>
<p>Pour ceux qui n'ont pas envie de tout re-télécharger ou qui sont pressés, y'a aussi une petite bidouille de sioux qui consiste à changer la date système de votre Mac pour revenir quelques jours en arrière (genre au 5 janvier). Vous lancez l'appli, elle s'ouvre nickel, et vous pouvez remettre la bonne date dans la foulée. Bon, attention, ça peut quand même faire tousser iCloud ou vos connexions SSL pendant quelques secondes, mais ça dépanne.</p>
<p>Une autre option consiste à désinstaller proprement la version actuelle (avec un petit coup d'AppCleaner pour ne pas laisser de déchêts) et à remettre une version un peu plus ancienne, comme la 1.60.495862, qui semble passer entre les mailles du filet.</p>
<p>C'est quand même dingue qu'une boîte comme Logitech se prenne les pieds dans le tapis sur un truc aussi basique. Mais bon, au moins la solution est là.</p>
<p>De rien, je vous en prie !</p>
<p>
<a href="https://www.neowin.net/news/expired-certificate-breaks-logitech-options-on-mac/">Source</a>
</p>