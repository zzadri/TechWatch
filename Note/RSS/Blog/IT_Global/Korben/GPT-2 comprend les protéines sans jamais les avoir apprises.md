---
title: "GPT-2 comprend les protéines sans jamais les avoir apprises"
author: "Korben"
date: 2026-01-27T09:48:24.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/science-recherche"
  - "intelligence-artificielle"
  - "biologie"
  - "protéines"
rss_source: Blog
url: https://korben.info/llm-biologie-decouverte-structurelle.html
note: 0
seen: false
---

<p>Des chercheurs viennent de trouver un truc complètement dingue. <strong>Un modèle de langage entraîné UNIQUEMENT sur de l'anglais</strong>, du texte humain basique quoi, est capable de <strong>comprendre la biologie moléculaire</strong> sans jamais avoir vu une seule séquence de protéines durant son entraînement.</p>
<p>En gros, GPT-2 qui fait de la paraphrase d'ordinaire est, sans le savoir, un expert en détection d'
<a href="https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_de_prot%C3%A9ines_par_homologie">homologie protéique</a>
. Je vous jure que c'est vrai !!</p>
<p>Liang Wang, chercheur à l'Université de Wuhan (les pangolins, tout ça tout ça, loool), a publié
<a href="https://www.biorxiv.org/node/5155480.full">une étude sur bioRxiv</a>
qui remet en question pas mal de certitudes. L'idée, c'est que la &quot;grammaire&quot; du langage humain et celle du vivant partagent une structure profonde commune. Du coup, un modèle qui apprend à distinguer des phrases qui ont le même sens mais avec des mots dans un ordre différent... développe aussi la capacité de reconnaitre les protéines qui sont de la même &quot;famille&quot;.</p>
<p>Perso, ça me retourne le cerveau parce qu'à la base, on parle &quot;juste&quot; d'un petit GPT-2 de 124 millions de paramètres, entraîné sur le dataset PAWS (des paires de phrases anglaises adverses), qui atteint 84% de précision sur la détection d'homologie protéique. Sans jamais avoir vu d'acides aminés ! C'est comme si votre chat, après avoir appris le français, se mettait soudainement à comprendre le chinois.</p>
<p>Et ça devient encore plus fou quand on scale. Les gros modèles comme Qwen-3 atteignent quasiment 100% de précision sur les benchmarks standards, mais le plus impressionnant, c'est leur performance dans la &quot;<strong>zone crépusculaire</strong>&quot; de l'évolution, là où les séquences protéiques ont moins de 25% d'identité entre elles. Dans ce régime où même les outils spécialisés comme
<a href="https://www.science.org/doi/10.1126/science.ade2574">ESM-2</a>
peinent à maintenir leurs performances, les LLM généralistes maintiennent 75% de précision.</p>
<p>Ils raisonnent là où les autres mémorisent !</p>
<p>D'ailleurs, si vous aimez l'actu IA et biologie, vous avez peut-être déjà lu mes articles sur
<a href="https://korben.info/evo-2-ia-genere-proteines-fonctionnelles.html">Evo 2</a>
ou
<a href="https://korben.info/apple-simplefold-ia-proteines-macbook.html">SimpleFold d'Apple</a>
. Ces outils-là sont entraînés sur des montagnes de données biologiques alors que dans le cas que je vous expose ici, c'est l'inverse. C'est un LLM tout ce qu'il y a de plus classique qui n'a pas BESOIN de ces données spécifiques pour comprendre la structure du vivant (enfin, ça doit encore être bien validé par d'autres équipes mais on verra bien).</p>
<p>Alors vous vous en doutez, curieux, les chercheurs ont analysé ce qui se passe dans la tête du modèle. Certaines &quot;
<a href="https://www.datacamp.com/fr/blog/attention-mechanism-in-llms-intuition">têtes d'attention</a>
&quot; du transformer deviennent des détecteurs universels de différences. La même tête qui repère une inversion sujet-objet dans une phrase anglaise va spontanément repérer les mutations d'acides aminés dans une protéine. Et voilà comment la syntaxe du langage humain et la syntaxe de la vie se retrouvent projetées sur le même &quot;manifold&quot; c'est à dire dans la même &quot;surface&quot; géométrique dans l'espace latent du modèle.</p>
<p>Et quand on demande aux gros modèles d'expliquer leur raisonnement via Chain-of-Thought (enchainement de pensées comme ce que propose ChatGPT 5.2 en mode thinking par exemple), ils font du &quot;mental folding&quot;. C'est à dire qu'ils imaginent la structure 3D des protéines à partir de la séquence 1D. Le modèle identifie explicitement des motifs structurels comme &quot;
<a href="https://fr.wikipedia.org/wiki/H%C3%A9lice-coude-h%C3%A9lice">Hélice-Coude-Hélice</a>
&quot; versus &quot;
<a href="https://fr.wikipedia.org/wiki/Tonneau_TIM">Tonneau TIM</a>
&quot; pour déterminer si deux protéines sont apparentées. Et tout ça sans jamais avoir reçu de coordonnées 3D en entrée.</p>
<p>Pour formaliser tout ça, l'équipe a donc créé BioPAWS, un benchmark qui évalue la capacité des modèles à transférer leur compréhension syntaxique du langage vers l'ADN, l'ARN et les protéines. Le dataset est dispo sur
<a href="https://huggingface.co/datasets/dnagpt/biopaws">Hugging Face</a>
pour ceux qui veulent jouer avec.</p>
<p>Bref, si la grammaire humaine et la grammaire biologique sont vraiment des manifestations d'une même structure universelle, ça change pas mal de choses sur comment on pourrait faire de la découverte scientifique à moindre coût. Plus besoin de datasets monstrueux pour chaque domaine, les patterns abstraits sont peut-être déjà là, encodés dans le langage qu'on utilise tous les jours.</p>
<p>
<a href="https://www.biorxiv.org/node/5155480.full">Source</a>
</p>