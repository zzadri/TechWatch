---
title: "8 façons de powner Claude Code - Attention à vos terminaux"
author: "Korben"
date: 2026-01-13T14:11:13.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/chatbots-llm"
  - "Claude Code"
  - "CVE-2025-66032"
rss_source: Blog
url: https://korben.info/pwning-claude-code-security-cve-2025-66032.html
note: 0
seen: false
---

<p>Alors, est ce que vous AUSSI, vous avez succombé à la tentation de Claude Code, le nouvel agent en ligne de commande d'Anthropic ?</p>
<p>J'suis sûr que oui !! Ahaha, C'est vrai que c'est hyper pratique de laisser une IA fouiller dans son repo pour corriger des bugs ou refactorer du code. Mais comme toujours avec ces outils qui ont un pied dans votre terminal et un autre dans le cloud, la question de la sécurité finit toujours par se poser.</p>
<p>Est-ce que Claude Code est vraiment sûr ?</p>
<p>Pour Anthropic, la réponse est un grand oui, avec tout son système de permissions basé sur une &quot;blocklist&quot; d'arguments dangereux...</p>
<p>Sauf que voilà,
<a href="https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/">RyotaK</a>
, un chercheur en sécurité chez GMO Flatt Security, a décidé d'aller voir sous le capot, et ce qu'il a trouvé devrait normalement, vous faire lever un gros sourcil.</p>
<p>En effet, le gars a dégoté pas moins de 8 façons différentes de faire exécuter n'importe quelle commande arbitraire à Claude Code, le tout sans que vous ayez à cliquer sur &quot;Approuver&quot;.</p>
<p>En fait, Claude Code autorise par défaut certaines commandes jugées &quot;inoffensives&quot; comme man, sort ou sed, parce qu'elles sont censées être en lecture seule. Et pour éviter les dérives, Anthropic filtre les arguments avec des expressions régulières.</p>
<p>C'est du classique mais RyotaK a montré que c'est un vrai champ de mines. Par exemple, sur la commande &quot;man&quot;, il suffisait d'utiliser l'option --html pour lui faire exécuter un binaire arbitraire chargé de &quot;formater&quot; la page.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">man --html=&#34;touch /tmp/pwned&#34; man
</span></span></code></pre><p>Pareil pour la commande &quot;sort&quot; qui, avec l'argument --compress-program, permet de lancer un shell qui va gentiment interpréter tout ce qu'on lui envoie sur l'entrée standard.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">sort --compress-program &#34;gzip&#34;
</span></span></code></pre><p>C'est vicieux parce que ce ne sont pas des bugs de Claude Code à proprement parler, mais juste des fonctionnalités légitimes d'outils Unix vieux de 30 ans que personne ne soupçonne d'être des vecteurs d'attaque ici...</p>
<p>Alors oui, pour ceux qui se demandent si Claude peut lire tout leur code, la réponse est oui, et c'est justement là que ça coince car si vous lancez l'outil sur un projet qui contient des fichiers malveillants (venant d'une PR douteuse ou d'un repo cloné à la va-vite), l'IA peut se faire piéger par ce qu'on appelle de l'injection de prompt indirecte.</p>
<p>Dans un des PoC, le chercheur utilise même les subtilités de Bash avec des trucs comme ${VAR@P} qui permettent d'interpréter le contenu d'une variable comme une invite de commande, exécutant ainsi du code caché. On est en plein dans la magie noire pour terminal et le pire, c'est que même git s'est fait avoir... En effet, Claude bloquait l'argument --upload-pack, mais comme git accepte les versions abrégées, il suffisait de taper --upload-pa pour passer à travers les mailles du filet !</p>
<p>Bref, c'est le jeu du chat et de la souris habituel, mais ici les enjeux sont énormes puisque l'agent a potentiellement accès à vos clés SSH, vos variables d'environnement et tout votre OS.</p>
<p>Après la bonne nouvelle (parce qu'il en faut bien de temps en temps...ahah), c'est qu'Anthropic a réagi au quart de tour et la faille, estampillée CVE-2025-66032, a bien été corrigée dans la version 1.0.93 de claude-code. Ils ont carrément abandonné l'approche par blocklist (trop permissive par nature) pour passer à une allowlist beaucoup plus stricte. Donc, si vous traînez encore sur une vieille version, un petit coup de npm install -g @anthropic-ai/claude-code ne vous fera pas de mal.</p>
<p>Voilà... C'est vrai que ces chouette tous ces assistants IA mais le prix à payer pour avoir un assistant qui bosse à votre place c'est que derrière, faut s'assurer aussi qu'il ne laisse pas la porte ouverte aux cambrioleurs en passant.</p>
<p>Après, ça ou un vrai employé qui tape dans la caisse
<a href="https://bitcoin.fr/sequestrations-et-home-jackings-le-fichier-du-fisc-au-service-des-braqueurs/">ou pire</a>
...</p>
<p>
<a href="https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/">Source</a>
</p>