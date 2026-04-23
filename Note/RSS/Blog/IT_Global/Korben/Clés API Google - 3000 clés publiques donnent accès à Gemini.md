---
title: "Clés API Google - 3000 clés publiques donnent accès à Gemini"
author: "Korben"
date: 2026-02-26T08:31:20.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "developpement/api-services"
  - "API"
  - "gemini"
rss_source: Blog
url: https://korben.info/google-api-keys-gemini-secrets.html
note: 0
seen: false
---

<p><strong>Les clés API Google</strong> que vous collez dans votre JavaScript pour afficher une carte Maps... hé bien elles ne sont plus si inoffensives. Car depuis que Gemini est entré dans la danse, ces mêmes clés donnent maintenant accès à vos fichiers privés et surtout à votre facture IA.</p>
<p><strong>Et personne ne nous a prévenu...</strong></p>
<p>En gros, Google utilise un format de clé unique, les fameuses <code>AIza...</code>, aussi bien pour Maps et Firebase (public, collé dans le HTML, tout le monde s'en fout) que pour
<a href="https://korben.info/google-gemini-pouvoir-monopole-privacy.html">Gemini</a>
(privé, accès aux fichiers, facturation). Le problème c'est que quand vous activez l'API Gemini sur un projet Google Cloud, TOUTES les clés existantes de ce projet héritent automatiquement de l'accès Gemini. Sans warning, sans notification, sans rien... Ouin !</p>
<p>Les chercheurs de
<a href="https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules">TruffleSecurity</a>
ont ainsi trouvé presque 3000 clés API Google valides dans le dataset Common Crawl de novembre 2025. Des clés qui trainent dans du code JavaScript, des pages HTML, des repos GitHub publics... et qui fonctionnent sur l'endpoint Gemini. Il suffit d'un simple <code>curl</code> avec une clé Maps récupérée sur un site web, et hop, vous accédez à l'API Gemini du propriétaire. Fichiers privés, contenu en cache, facturation sur son compte.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/google-api-keys-gemini-secrets/google-api-keys-gemini-secrets-2.png" alt="" loading="lazy" decoding="async">
<p>Et parmi les victimes, on trouve des institutions financières, des boîtes de cybersécurité, et... Google eux-mêmes (oui oui, vraiment).</p>
<p>Le 21 novembre 2025, TruffleSecurity signale donc le problème et la réponse de Google le 25 novembre c'est : &quot;<em>intended behavior</em>&quot; (comportement normal)... Sauf que le 2 décembre, Google a reclassifié ça en bug, puis le 13 janvier 2026, ça passe finalement en Tier 1. On est donc passé du &quot;c'est normal les frérots&quot; à &quot;ah oui quand même, oupsi oups&quot;, en 7 semaines.</p>
<p>Maintenant, pour ceux qui se demandent si leurs clés API Google sont concernées, direction
<a href="https://console.cloud.google.com/">console.cloud.google.com</a>
, section &quot;APIs &amp; Services&quot; puis &quot;Identifiants&quot;.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/google-api-keys-gemini-secrets/google-api-keys-gemini-secrets-3.png" alt="" loading="lazy" decoding="async">
</p>
<p>Si vous voyez l'API &quot;
<a href="https://ai.google.dev/api/all-methods">Generative Language</a>
&quot; de Gemini API activée sur un projet avec des clés non restreintes... attention, c'est le moment de faire le ménage. Ajoutez des restrictions IP ou HTTP referrer, et surtout, utilisez des comptes de service plutôt que des clés API pour tout ce qui touche à Gemini (sauf si vous aimez les surprises sur votre facture ^^).</p>
<img src="https://korben.info/google-api-keys-gemini-secrets/google-api-keys-gemini-secrets-1.avif" alt="" loading="lazy" decoding="async">
<p>Le truc tordu, c'est que la doc Firebase dit noir sur blanc que les clés API ne sont pas des secrets. Google Maps vous dit carrément de les coller dans votre HTML. Et maintenant, ces mêmes clés donnent accès à une IA qui peut lire vos fichiers. Du
<a href="https://cwe.mitre.org/data/definitions/1188.html">CWE-1188</a>
pur et dur ! Et c'est pas la première fois que Google se fait taper sur les doigts pour ce genre de
<a href="https://korben.info/promptflux-malware-gemini-llm-runtime-generation.html">souci avec Gemini</a>
.</p>
<p>Du coup, Google a annoncé des nouvelles mesures, du scoped defaults, du blocage de clés fuités, des notifications proactives...etc. Reste donc à voir si ça arrivera avant que les presque 3000 clés exposées soient exploitées par des gens moins bien intentionnés.</p>
<p>Bref, dix ans à dire que c'est public, et hop, aujourd'hui c'est devenu top secret. Bien joué Google !!</p>
<p>
<a href="https://simonwillison.net/2026/Feb/26/google-api-keys/">Source</a>
</p>