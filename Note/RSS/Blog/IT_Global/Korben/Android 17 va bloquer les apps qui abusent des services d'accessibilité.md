---
title: "Android 17 va bloquer les apps qui abusent des services d'accessibilité"
author: "Korben"
date: 2026-03-17T16:19:01.000Z
type: site
subject:
category: IT Global
tags:
  - "apple-mobile/android"
  - "cybersecurite/actualites-securite"
  - "accessibilite"
  - "Android"
  - "android17"
rss_source: Blog
url: https://korben.info/android-17-va-bloquer-les-apps-qui-abusent-des-services-daccessibilite.html
note: 0
seen: false
---

<p>Google durcit le ton avec Android 17. La prochaine version de l'OS mobile va empêcher les applications non certifiées d'accéder aux services d'accessibilité, une API très puissante et régulièrement détournée par les malwares pour espionner les utilisateurs et vider des comptes bancaires.</p>
<h2 id="ce-qui-change-avec-android-17">Ce qui change avec Android 17</h2>
<p>La nouveauté est apparue dans la Beta 2 d'Android 17, repérée la semaine dernière. Quand le mode Advanced Protection est activé, le système bloque automatiquement l'accès à l'API AccessibilityService pour toutes les apps qui ne sont pas de vrais outils d'accessibilité.</p>
<p>Seules les applications qui portent le marqueur technique isAccessibilityTool restent autorisées : lecteurs d'écran, outils de saisie vocale, systèmes d'entrée par contacteur et applications braille.</p>
<p>Les autres, et la liste est longue, sont mises de côté : antivirus, outils d'automatisation, assistants, nettoyeurs système, gestionnaires de mots de passe et lanceurs alternatifs.</p>
<p>Et si une de ces apps avait déjà l'autorisation, Android 17 la révoque automatiquement au moment où le mode Advanced Protection est activé. L'utilisateur ne peut pas non plus forcer l'accès manuellement tant que la protection est active.</p>
<h2 id="pourquoi-cest-un-vrai-sujet-">Pourquoi c'est un vrai sujet ?</h2>
<p>L'API AccessibilityService est l'une des plus sensibles d'Android. Elle permet de lire le contenu de l'écran, d'intercepter les frappes clavier, de cliquer sur des boutons à la place de l'utilisateur et d'accorder des autorisations sans que personne ne s'en rende compte.</p>
<p>Les malwares bancaires l'exploitent depuis des années pour voler des identifiants et vider des comptes. Google a longtemps fermé les yeux sur le problème, ou en tout cas laissé la porte grande ouverte. Avec ce mode, c'est un peu le retour à la raison.</p>
<p>Le mode Advanced Protection, lancé avec Android 16, regroupe aussi d'autres verrous : blocage du sideloading (l'installation d'apps en dehors du Play Store), restriction des transferts de données par USB et scan obligatoire via Google Play Protect.</p>
<p>Android 17 ajoute donc cette brique supplémentaire sur l'accessibilité. Côté développeurs, Google met à disposition une API AdvancedProtectionManager qui permet aux apps de détecter si le mode est actif et d'adapter leur comportement en conséquence.</p>
<p>On ne va pas se mentir, quand on utilise un iPhone, ce genre de problème ne se pose pas vraiment puisque iOS a toujours été bien plus restrictif sur ce que les apps peuvent faire en arrière-plan. Mais pour les utilisateurs Android, c'est une avancée qui était attendue depuis un moment. Le revers de la médaille, c'est que des apps tout à fait légitimes vont se retrouver bloquées.</p>
<p>Un émulateur de Dynamic Island comme dynamicSpot ne fonctionne plus avec le mode activé, et c'est le genre de petite frustration qui risque de pousser pas mal de monde à désactiver la protection. On espère que Google trouvera un juste milieu entre la sécurité et la flexibilité qui fait la force d'Android, en tout cas pour le moment ce n'est pas encore tout à fait ça.</p>
<p>Source :
<a href="https://thehackernews.com/2026/03/android-17-blocks-non-accessibility.html">The Hacker News</a>
</p>