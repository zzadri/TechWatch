---
title: "pyinfra - Du Python au lieu du YAML pour gérer vos serveurs"
author: "Korben"
date: 2026-03-06T09:35:17.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/devops-infrastructure"
  - "developpement/langages-programmation"
  - "Ansible"
  - "automatisation"
  - "DevOps"
  - "open source"
  - "Python"
rss_source: Blog
url: https://korben.info/pyinfra-automatisation-infrastructure-python.html
note: 0
seen: false
---

<p>Ansible, c'est bien. Mais du YAML à perte de vue pour configurer trois serveurs c'est pas non plus l'idéal. Hé bien ça tombe bien car y'a maintenant
<a href="https://github.com/pyinfra-dev/pyinfra">pyinfra</a>
, qui fait tout pareil sauf qu'on écrit du Python. En gros, votre script de déploiement c'est juste du code Python normal avec des imports, des boucles, des conditions... tout ça, tout ça...</p>
<p>Ce projet existe depuis 2014, il est sous licence MIT et côté perfs, c'est de ce que j'ai lu, jusqu'à 10 fois plus rapide qu'Ansible sur des déploiements massifs (genre plusieurs milliers de machines). Bon, sur le papier c'est bien, mais en fait ça dépend surtout de votre infra SSH et de la latence réseau.</p>
<p>Alors ça marche comment ?</p>
<p>Hé bien vous installez le bazar avec <code>uv tool install pyinfra</code> et hop, vous pouvez déjà lancer des commandes sur vos serveurs comme ceci :</p>
<p><code>pyinfra mon-serveur.net exec -- echo &quot;hello world&quot;</code></p>
<p>Ça fonctionne en SSH sur le port 22, sur des conteneurs Docker, ou même en local. Le truc est complètement agentless, du coup pas besoin d'installer quoi que ce soit sur les machines cibles. Suffit d'un accès shell POSIX tout ce qu'il y a de plus classique et c'est réglé.</p>
<img src="https://korben.info/pyinfra-automatisation-infrastructure-python/pyinfra-automatisation-infrastructure-python-1.gif" alt="" loading="lazy" decoding="async">
<p>Bon, ça c'est pour l'ad-hoc mais en fait le vrai kiff, ce sont les opérations déclaratives. Je vous montre... Vous créez un fichier <code>deploy.py</code> et dedans, vous mettez ça :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">from pyinfra.operations import apt, systemd
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">apt.packages(
</span></span><span class="line"><span class="cl"> name=&#34;Install nginx&#34;,
</span></span><span class="line"><span class="cl"> packages=[&#34;nginx&#34;],
</span></span><span class="line"><span class="cl">)
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">systemd.service(
</span></span><span class="line"><span class="cl"> name=&#34;Ensure nginx is running&#34;,
</span></span><span class="line"><span class="cl"> service=&#34;nginx.service&#34;,
</span></span><span class="line"><span class="cl"> running=True,
</span></span><span class="line"><span class="cl"> enabled=True,
</span></span><span class="line"><span class="cl">)
</span></span></code></pre><p>C'est du bon vieux Python sans DSL bizarre (Domain-Specific Language), pas d'indentation YAML qui vous pète entre les doigts à 3h du mat parce qu'il manque un espace. Et si vous voulez une boucle ? bah <code>for</code>. Une condition ? bah <code>if</code>. Ou encore importer
<a href="https://pypi.org/project/boto3/">boto3 pour causer avec AWS</a>
depuis votre Debian 12 ? No problemo !</p>
<p>Et pour cibler vos machines, suffit de créer un fichier <code>inventory.py</code> comme ceci :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">targets = [&#34;@docker/ubuntu&#34;, &#34;mon-serveur.net&#34;, &#34;autre-serveur.net&#34;]
</span></span></code></pre><p>Puis ensuite un petit : <code>pyinfra inventory.py deploy.py</code> et c'est parti mon kiki. L'outil gère le parallélisme sur 50 serveurs, les diffs (pour voir ce qui va changer AVANT d'appliquer), et le mode dry-run pour les plus prudents.</p>
<p>Côté intégrations, ça cause avec Terraform, Docker, Vagrant... et comme c'est du Python, vous avez accès à tout l'écosystème. Genre, vous voulez checker l'état d'une API avant de déployer ? Un <code>import requests</code> et c'est plié. La doc sur
<a href="https://docs.pyinfra.com">docs.pyinfra.com</a>
est plutôt complète, et y'a même la gestion des secrets intégrée avec variables d'environnement, fichiers chiffrés, HashiCorp Vault ou AWS Secrets Manager.</p>
<p>Ça tourne depuis Linux et macOS (et Windows via WSL), mais les cibles doivent être des systèmes POSIX donc pas de déploiement natif sur Windows. Et si votre inventaire contient 3 000 machines avec des configs SSH différentes... bon courage pour le debug en cas de souci (le mode <code>-vvv</code> aide, mais bon...).</p>
<p>Bref, si vous en avez marre du YAML et que Python c'est votre truc, allez jeter un oeil.</p>
<p>Merci à Letsar pour la découverte !</p>