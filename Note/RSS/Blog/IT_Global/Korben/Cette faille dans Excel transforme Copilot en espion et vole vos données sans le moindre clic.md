---
title: "Cette faille dans Excel transforme Copilot en espion et vole vos données sans le moindre clic"
author: "Korben"
date: 2026-03-11T12:47:27.000Z
type: site
subject:
category: IT Global
tags:
  - "cybersecurite/failles-vulnerabilites"
  - "intelligence-artificielle/actualites-ia"
  - "Copilot"
  - "faille"
  - "Microsoft"
rss_source: Blog
url: https://korben.info/cette-faille-dans-excel-transforme-copilot-en-espion-et-vole-vos-donnees-sans-le-moindre-clic.html
note: 0
seen: false
---

<p>Microsoft vient de corriger 79 failles de sécurité dans son Patch Tuesday de mars 2026. Parmi elles, une vulnérabilité critique dans Excel qui permet d'utiliser l'agent Copilot pour exfiltrer des données sensibles, le tout sans aucune interaction de la victime. Oui oui, zéro clic.</p>
<h2 id="une-faille-xss-qui-détourne-copilot">Une faille XSS qui détourne Copilot</h2>
<p>Cette faille répondant au doux nom de CVE-2026-26144 est une vulnérabilité de type cross-site scripting dans Microsoft Excel, et elle a un petit truc en plus qui la rend franchement inquiétante : elle est capable de détourner le mode Agent de Copilot pour envoyer des données vers l'extérieur, via ce que Microsoft appelle un &quot;unintended network egress&quot;. </p>
<p>Traduction : l'IA qui est censée vous aider à rédiger vos tableaux et vos formules devient, l'air de rien, un canal d'exfiltration de données.</p>
<p>Pas besoin que la victime clique sur quoi que ce soit. Pas besoin non plus d'élévation de privilèges. Il suffit d'un accès réseau. Les données qui peuvent fuiter sont loin d'être anodines : documents financiers, propriété intellectuelle, données opérationnelles. Dustin Childs, de la Zero Day Initiative, a qualifié cette faille de &quot;fascinante&quot;. On veut bien le croire.</p>
<h2 id="deux-autres-failles-office-à-ne-pas-oublier">Deux autres failles Office à ne pas oublier</h2>
<p>Ce Patch Tuesday de mars n'apporte pas que la CVE-2026-26144. Microsoft a aussi corrigé deux failles d'exécution de code à distance dans Office (CVE-2026-26110 et CVE-2026-26113) qui peuvent être exploitées via le simple volet de prévisualisation.</p>
<p>Ce qui veut dire qu'il suffit de survoler un fichier piégé dans l'explorateur pour déclencher l'attaque, sans même l'ouvrir.</p>
<p>Au total, ce sont 79 vulnérabilités corrigées ce mois-ci, dont trois classées critiques. Bonne nouvelle quand même : c'est le premier Patch Tuesday en six mois sans faille activement exploitée dans la nature. Après les épisodes avec APT28 et la CVE-2026-21509 exploitée par des groupes liés à la Russie en début d'année, ça fait une petite pause bienvenue.</p>
<p>Le truc un peu agaçant dans cette histoire, c'est que Microsoft pousse Copilot dans tous ses logiciels, et que PAF, une faille XSS permet de transformer cet assistant IA en mouchard.</p>
<p>C'est d'autant plus gênant que beaucoup d'entreprises ont activé Copilot sans forcément mesurer ce que ça implique en termes de surface d'attaque. Avec un agent IA qui a accès à vos fichiers et à votre réseau, le moindre trou dans la raquette prend une autre dimension.</p>
<p>Si vous utilisez Excel avec Copilot activé en entreprise, la mise à jour de mars est à installer sans traîner.</p>
<p>Source :
<a href="https://cyberscoop.com/microsoft-patch-tuesday-march-2026/">Cyberscoop</a>
</p>