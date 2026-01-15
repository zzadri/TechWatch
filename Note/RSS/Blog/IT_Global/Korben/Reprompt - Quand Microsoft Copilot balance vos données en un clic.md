---
title: "Reprompt - Quand Microsoft Copilot balance vos données en un clic"
author: "Korben"
date: 2026-01-15T14:52:34.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/chatbots-llm"
  - "Copilot"
  - "IA"
  - "Microsoft"
  - "sécurité"
  - "Varonis"
rss_source: Blog
url: https://korben.info/reprompt-copilot-vol-donnees-varonis.html
note: 0
seen: false
---

<p>Vous vous souvenez d'
<a href="https://korben.info/echoleak-vulnerabilite-zero-click-microsoft-copilot.html">EchoLeak, cette faille zero-click dans Microsoft Copilot</a>
dont je vous parlais l'année dernière ? Eh bien accrochez-vous, parce que les chercheurs de <strong>Varonis</strong> viennent de remettre le couvert avec une nouvelle technique baptisée &quot;<strong>Reprompt</strong>&quot;. Et cette fois, un simple clic suffit pour que l'assistant IA de Microsoft balance toutes vos données sensibles à un attaquant.</p>
<p>Je vous explique le principe... Dolev Taler, chercheur chez Varonis Threat Labs, a découvert que l'URL de l'assistant Microsoft intègre un paramètre &quot;<code>q</code>&quot; qui permet d'injecter directement des instructions dans le prompt.</p>
<p>Du coup, n'importe qui peut vous envoyer un lien piégé du style <code>copilot.microsoft.com/?q=INSTRUCTION_MALVEILLANTE</code> et hop, votre assistant exécute ce qu'on lui demande dès que vous cliquez.</p>
<p>Et là où c'est vraiment pas drôle, c'est que Varonis a identifié trois techniques d'exploitation. La première, &quot;Double-Request&quot;, contourne les garde-fous en demandant à l'IA de répéter deux fois la même action. La deuxième, &quot;Chain-Request&quot;, enchaîne les instructions côté serveur pour exfiltrer vos données sans que vous ne voyiez rien. Et la troisième combine les deux pour un effet maximal.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/reprompt-copilot-vol-donnees-varonis/reprompt-copilot-vol-donnees-varonis-2.png" alt="" loading="lazy" decoding="async">
<p><em>Les trois techniques d'attaque Reprompt : P2P Injection, Double-Request et Chain-Request (
<a href="https://www.varonis.com/blog/reprompt">Source</a>
)</em></p>
<p>Via cette faille, un attaquant peut récupérer vos emails récents, vos fichiers OneDrive, votre historique de recherche, et tout ça en arrière-plan pendant que vous pensez juste avoir cliqué sur un lien anodin. Ça craint hein !</p>
<p>Petite précision importante quand même, cette faille ne touche que la version Personal de l'assistant Microsoft, et pas la version Enterprise qui bénéficie de protections supplémentaires. Si vous utilisez la version pro au boulot, vous pouvez respirer. Par contre, si vous utilisez la version grand public pour vos trucs perso, c'était open bar jusqu'au patch du 13 janvier dernier.</p>
<p>Parce que oui, bonne nouvelle quand même, <strong>Microsoft a confirmé avoir corrigé le problème</strong>. Mais ça pose une vraie question sur la sécurité des assistants IA qui ont accès à nos données car entre EchoLeak et Reprompt, ça commence à faire beaucoup pour un seul produit.</p>
<p>Et surtout au niveau de la sécurité, moi ce que je comprends pas, c'est pourquoi le niveau de sécurité est un argument marketing ? Au nom de quoi la version personnelle devrait être moins sûre que la version personnelle ? Je pense que les données personnelles des gens n'ont pas moins de valeur...</p>
<p>Pour moi le niveau de sécurité devrait être exactement le même sur les deux versions du service.</p>
<p>Bref, l'IA c'est pratique, mais c'est aussi un nouveau terrain de jeu pour les attaquants alors méfiez-vous des liens bizarres, même s'ils pointent vers des services Microsoft légitimes !</p>
<p>
<a href="https://www.varonis.com/blog/reprompt">Source</a>
</p>