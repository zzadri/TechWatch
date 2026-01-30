---
title: "jq-quest - Apprenez à maîtriser jq sans vous prendre la tête"
author: "Korben"
date: 2026-01-28T06:46:31.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "tutoriels-guides/tutoriels-avances"
rss_source: Blog
url: https://korben.info/jq-quest-apprendre-jq-tuto.html
note: 0
seen: false
---

<p>Si vous avez déjà
<a href="https://www.tiktok.com/@korbeninfo/video/7201447995383172358">croisé la route de jq</a>
, c'est probablement parce que vous vous la touchez un peu dans le terminal et que vous avez déjà joué avec du format JSON (logs, APIs, config...).</p>
<p>Jq, tout le monde l'adore parce que ça filtre, ça mappe et surtout ça transforme du JSON directement depuis le terminal. Mais la syntaxe de ce truc, aïe aïe aïe, c'est comme faire de la Regex. C'est de l'apprentissage sur le tas surtout. Faut copier coller des trucs en provenance de RIP-StackOverflow ou de ChatGPT-le-sang-de-la-veine. Et le pire c'est que 2 jours après, on a tout oublié !!! Puis lire la doc officielle, m'en parlez pas, c'est comme lire autre chose que mon site... c'est pas le criss de fun ^^.</p>
<p>Heureusement, pour ceux qui veulent vraiment monter en compétence sans s'endormir, il existe <strong>
<a href="https://codeberg.org/gturri/jq-quest">jq-quest</a>
</strong>.</p>
<p>C'est un petit projet sympa hébergé sur Codeberg qui propose une approche &quot;<em>learning by doing</em>&quot; (apprendre en faisant, pour les anglophobes). Au début, je pensais que c'était juste un QCM basique, mais en fait non puisqu'il faut vraiment taper les commandes et se salir les mains.</p>
<p>Pour essayer, suffit de cloner le dépôt, vous lancez le script, et on vous donne un input JSON et l'output attendu. À vous ensuite de trouver la bonne commande jq pour passer de l'un à l'autre.</p>
<p>Il vous faudra juste jq d'installé sur votre machine. Attention par contre, si vous êtes sous Windows, il faudra passer par WSL ou Git Bash, parce que le script .sh ne va pas aimer PowerShell.</p>
<p>Ça s'installe donc en deux secondes comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">git clone https://codeberg.org/gturri/jq-quest.git
</span></span></code></pre><div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cd jq-quest
</span></span></code></pre><p>Ensuite, vous lancez votre premier exercice :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./jq-quest.sh 1-pretty-print.json
</span></span></code></pre><p>Le script va alors vous afficher l'instruction, le JSON d'entrée et ce qu'il attend en sortie :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">INSTRUCTION: Pretty print the json
</span></span><span class="line"><span class="cl">INPUT: {&#34;k1&#34;: &#34;v1&#34;, &#34;k2&#34;:[1, 3, 7]}
</span></span><span class="line"><span class="cl">EXPECTED OUTPUT: {
</span></span><span class="line"><span class="cl"> &#34;k1&#34;: &#34;v1&#34;,
</span></span><span class="line"><span class="cl"> &#34;k2&#34;: [
</span></span><span class="line"><span class="cl"> 1,
</span></span><span class="line"><span class="cl"> 3,
</span></span><span class="line"><span class="cl"> 7
</span></span><span class="line"><span class="cl"> ]
</span></span><span class="line"><span class="cl">}
</span></span></code></pre><p>Vous tapez votre proposition de filtre, et il vous dit si c'est bon ou pas. Pour proposer une solution, suffit de taper :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./jq-quest.sh 1-pretty-print.json &#39;SOLUTION&#39;
</span></span></code></pre><p>Si vous séchez (et croyez-moi, ça va arriver), vous pouvez demander un indice avec :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./jq-quest.sh 1-pretty-print.json hint
</span></span></code></pre><p>Ou carrément la solution si vous êtes au bout du rouleau :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">./jq-quest.sh 1-pretty-print.json solution
</span></span></code></pre><p>Mais rassurez vous, les exercices sont progressifs, ça commence par du &quot;pretty print&quot; basique (le truc qu'on fait tous), puis on attaque les filtres simples, les clés spéciales, les tableaux, et petit à petit on arrive sur des trucs bien plus costauds comme les itérations sur objets, le slicing ou les opérations mathématiques.</p>
<p>Ce genre de tuto interactif c'est top parce que jq, c'est hyper puissant, mais la courbe d'apprentissage est un peu raide au début. Là, en une petite heure, vous pouvez plier les exercices et avoir enfin compris la logique du truc au lieu de tâtonner à chaque fois.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/jq-quest-apprendre-jq-tuto/jq-quest-apprendre-jq-tuto-2.png" alt="" loading="lazy" decoding="async">
<p>D'ailleurs, si vous aimez ce genre d'outils pour parser de la donnée, je vous rappelle qu'il existe aussi
<a href="https://korben.info/fq-extraire-donnees-structurees-binaires.html">fq pour les fichiers binaires</a>
ou encore
<a href="https://korben.info/htmlq-extraire-texte-html.html">htmlq pour le HTML</a>
. J'aurais pu vous parler d'outils graphiques pour faire ça, mais franchement, rien ne vaut la ligne de commande pour comprendre ce qu'on fait. Et si vous êtes plutôt Python, jetez un oeil à
<a href="https://korben.info/convertir-sortie-commande-format-json.html">jc</a>
qui convertit la sortie des commandes classiques en JSON.</p>
<p>Bref, si vous voulez arrêter de souffrir à chaque fois que vous devez extraire un champ d'un JSON interminable, faites un tour sur jq-quest, ça va vous dérouiller les neurones.</p>
<p>Si vous êtes dev et que ce genre de tuto vous parle,
<a href="https://www.linkedin.com/company/korben-info/">suivez Korben sur LinkedIn</a>
pour d'autres découvertes.</p>
<p>Un grand merci à Guillaume pour la découverte.</p>