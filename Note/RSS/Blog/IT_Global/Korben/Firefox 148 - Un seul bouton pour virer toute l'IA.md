---
title: "Firefox 148 - Un seul bouton pour virer toute l'IA"
author: "Korben"
date: 2026-02-26T14:18:50.000Z
type: site
subject:
category: IT Global
tags:
  - "intelligence-artificielle/actualites-ia"
  - "linux-open-source/logiciels-libres"
  - "Brave"
  - "Chrome"
  - "Firefox"
  - "IA"
  - "kill switch"
  - "Mozilla"
  - "vie privée"
rss_source: Blog
url: https://korben.info/firefox-148-ia-kill-switch.html
note: 0
seen: false
---

<p>Vous voulez désactiver l'IA dans votre navigateur ? Bonne chance pour les couillons qui utilisent Chrome... faut passer par 5 réglages planqués dans chrome://settings et chrome://flags, tripatouiller des flags expérimentaux, bref, c'est un vrai parcours du combattant. <strong>Firefox 148</strong>, de son côté, a eu une idée folle : <strong>Mettre UN bouton</strong>. Hop, terminé.</p>
<p>Mozilla vient en effet de sortir la
<a href="https://www.firefox.com/en-US/firefox/148.0/releasenotes/">version 148 de Firefox</a>
et le gros morceau, c'est la section &quot;Contrôles de l'IA&quot; dans les paramètres (about:preferences#ai). Un seul toggle &quot;<strong>
<a href="https://korben.info/firefox-kill-switch-ia-desactiver-fonctionnalites.html">Bloquer les améliorations IA</a>
</strong>&quot; et paf, toutes les fonctions IA du navigateur sont coupées d'un coup. Traductions automatiques, regroupement d'onglets, previews de liens, texte alternatif des PDF, et même les chatbots de la barre latérale (ChatGPT, Claude, Gemini, Copilot, Le Chat). Tout dégage !</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/firefox-148-ia-kill-switch/firefox-148-ia-kill-switch-2.png" alt="" loading="lazy" decoding="async">
<p>C'est le top pour les fragilous qui refusent le progrès ^^... Roohh ça va je blague ! Et le vrai intérêt du truc, c'est que ça verrouille les futures fonctions IA aussi. Du coup, si Mozilla ajoute de nouvelles features IA plus tard, elles seront automatiquement bloquées. Pas besoin de revenir fouiller dans les paramètres à chaque update. D'ailleurs, toutes les fonctions IA sont déjà désactivées par défaut... faut donc les activer manuellement si vous en voulez.</p>
<p>Et attention, ça ne bloque pas les extensions tierces qui intègrent leur propre IA, genre les &quot;résumeurs&quot; de page ou les assistants de rédaction. Le toggle, lui, garantit uniquement que les fonctions NATIVES restent coupées quoi qu'il arrive.</p>
<p>Et maintenant comparons avec la concurrence, parce que c'est là que ça pique les yeux.</p>
<p>Comme je vous le disais dans mon intro trollesque, chez Google,
<a href="https://korben.info/firefox-controles-ia.html">désactiver l'IA dans Chrome</a>
(et ses dérivés) relève carrément du sport extrême. Faut couper Gemini (chrome://settings/ai), désactiver le mode IA et Help Me Write (chrome://flags), bloquer la recherche IA dans l'historique, et pour les AI Overviews... ben y'a pas vraiment de bouton.</p>
<p>Brave fait un peu mieux heureusement ! Leur assistant Leo est opt-in par défaut, tourne dans un profil isolé qui ne peut pas accéder à vos données de navigation, et applique une politique zéro log. Même leur mode &quot;agentic AI&quot; en Nightly est désactivé de base. C'est propre, mais y'a pas de kill switch global comme Firefox. Du coup, si vous voulez la solution radicale plutôt que du cas par cas, Firefox gagne.</p>
<p>Et pour ceux qui se demandent pourquoi Firefox investit dans l'IA tout en permettant de la couper... en fait, Mozilla joue la carte de la transparence. Les modèles locaux utilisés par Firefox sont supprimés du disque quand vous désactivez les fonctions et tout est vérifiable dans about:processes si vous êtes du genre parano.</p>
<p>Au passage, cette version corrige également une quarantaine de failles de sécurité et embarque la
<a href="https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer">Sanitizer API</a>
, ce qui est une première parmi les navigateurs. Et si vous êtes encore sur Firefox ESR, ça ne marchera pas... faudra donc attendre la prochaine ESR pour en profiter.</p>
<p>Voilà, si l'IA dans votre navigateur vous gave, vous savez où aller -&gt; <strong>Firefox, tout simplement.</strong></p>
<p>
<a href="https://www.techspot.com/news/111453-firefox-148-rolls-out-promised-ai-kill-switch.html">Source</a>
</p>