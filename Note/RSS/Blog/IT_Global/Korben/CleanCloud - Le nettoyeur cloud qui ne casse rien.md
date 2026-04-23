---
title: "CleanCloud - Le nettoyeur cloud qui ne casse rien"
author: "Korben"
date: 2026-03-06T13:09:20.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "linux-open-source/logiciels-libres"
  - "AWS"
  - "azure"
  - "DevOps"
rss_source: Blog
url: https://korben.info/cleancloud-nettoyeur-cloud-aws-azure.html
note: 0
seen: false
---

<p>Le gaspillage du cloud, c'est un peu le secret de polichinelle du devops. Tout le monde sait qu'il y a des volumes EBS détachés qui traînent, des snapshots vieux de 6 mois, des Elastic IP à 3,65 $/mois qui servent à rien... mais bon, on nettoie pas. Parce qu'on a trop les miquettes de casser un truc en prod. Mais entre le volume de 500 Go &quot;temporaire&quot; créé en 2024 et le NAT Gateway qui facture 32 $/mois dans le vide, ça chiffre assez vite.</p>
<p>
<a href="https://github.com/cleancloud-io/cleancloud">CleanCloud</a>
va vous permettre de remédier à ça. Il s'agit d'un petit CLI Python compatible Linux, macOS et Windows (dispo via <code>pip</code> ou <code>pipx</code>) qui va scanner vos comptes AWS et Azure pour débusquer toutes ces ressources orphelines. Le truc, c'est qu'il tourne uniquement en lecture seule, donc pas de mutation, pas de suppression, et zéro modification de tags. Lui se contente de regarder, de prendre des notes, et de vous sortir un bon vieux <code>report.json</code> ou CSV avec tout le détail.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/cleancloud-nettoyeur-cloud-aws-azure/cleancloud-nettoyeur-cloud-aws-azure-2.png" alt="" loading="lazy" decoding="async">
<p>Du coup, côté permissions IAM, c'est le strict minimum... 14 permissions en lecture seule type <code>ec2:Describe*</code>, <code>s3:List*</code> ou <code>rds:DescribeDBInstances</code>. C'est d'ailleurs bien fichu puisque le code vérifie statiquement via AST qu'aucun appel en écriture ne passe. Donc pas besoin de filer vos clés IAM à un outil tiers, et ça c'est plutôt rassurant pour les équipes sécu qui flippent (à juste titre) dès qu'on parle d'accès cloud.</p>
<p>L'outil embarque 20 règles de détection. 10 pour AWS, 10 pour Azure. Côté AWS, ça scanne comme vous l'aurez deviné les volumes EBS non attachés, les vieux snapshots, les logs CloudWatch en rétention infinie, les Elastic IP orphelines, les ENI détachées, les AMI créées en 2022 qui traînent, les NAT Gateways au repos, les instances RDS à l'arrêt...etc.</p>
<p>Côté Azure, même combat avec les disques managés, les IP publiques inutilisées, les VMs stoppées qui continuent de bouffer du stockage Premium SSD.</p>
<p>Pour chaque trouvaille, vous avez un score de confiance (LOW, MEDIUM, HIGH) et une estimation du coût mensuel gaspillé en dollars. En fait c'est assez bien foutu, le rapport vous donne le type de ressource, la région, l'âge du truc et combien ça vous coûte.</p>
<p>Hop, un <code>pipx install cleancloud</code> et c'est parti :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cleancloud scan --provider aws --all-regions
</span></span></code></pre><p>Y'a même un mode démo sans aucun credential requis, histoire de voir la tête du rapport JSON avant de brancher vos vrais comptes. Perso, je trouve ça bien pour voir à quoi ça ressemble :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">cleancloud demo
</span></span></code></pre><p>Et pour ceux qui veulent aller plus loin, le scanner s'intègre dans vos pipelines CI/CD. GitHub Actions, Azure DevOps, Docker CI, peu importe. Vous collez un <code>--fail-on-cost 100</code> (exit code 2 si le gaspillage dépasse 100 $/mois) ou un <code>--fail-on-confidence HIGH</code> et hop, le build pète si y'a du déchet. De quoi automatiser le ménage. Vous mettez juste cette commande dans votre CI et c'est plié.</p>
<p>D'ailleurs, la config supporte aussi le filtrage par tags. Vous créez ce fichier <code>cleancloud.yaml</code> à la racine de votre projet, vous excluez vos ressources de prod tagguées <code>env:production</code>, et le scan ignore ce qui doit l'être. Attention par contre, si vos ressources sont mal tagguées (et on sait tous que c'est souvent le cas...), le filtre ne servira à rien.</p>
<p>Côté sécurité, l'outil ne fait aucun appel vers des serveurs tiers et cause uniquement avec les API AWS et Azure de vos propres comptes, et supporte aussi l'auth OIDC avec des credentials temporaires. Voilà même si c'est un projet super jeune encore, c'est plutôt bien pensé pour les environnements corporate. C'est sous licence MIT et le code Python est sur GitHub donc tout est vérifiable.</p>
<p>Bref, si votre facture cloud vous pique les yeux, un <code>pip install cleancloud</code> et comme ça, vous en saurez plus... C'est gratuit, c'est open source, et surtout ça ne casse rien !</p>