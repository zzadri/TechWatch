---
title: "RustFS - L'alternative Rust à MinIO"
author: "Korben"
date: 2026-02-27T07:41:35.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/langages-programmation"
  - "linux-open-source/self-hosting"
  - "alternative open source"
  - "Docker"
  - "Rust"
  - "S3"
  - "self-hosting"
rss_source: Blog
url: https://korben.info/rustfs-stockage-objet-distribue-rust.html
note: 0
seen: false
---

<p><strong>MinIO</strong>, tout le monde ou presque connaît car c'est LE truc quand on veut du stockage objet S3-compatible auto-hébergé sous Linux. Sauf que voilà... la licence AGPL, ça pique pour pas mal de boîtes qui ne veulent pas se retrouver à devoir ouvrir leur code.</p>
<p>Du coup, y'a un nouveau projet qui débarque dans le tiek et qui devrait en intéresser plus d'un. C'est
<a href="https://github.com/rustfs/rustfs">RustFS</a>
, codé en Rust (comme le nom le laisse deviner mes petits Sherlock) et 100% compatible S3. En gros, vous prenez votre stack MinIO existante, vous remplacez par ce truc, et en fait tout continue de fonctionner pareil... Vos buckets, vos applis, vos scripts Python, boto3... tout pareil !</p>
<div class="video-container" id="video-container-rustfs-stockage-objet-distribue-rust-1.mp4">
<video controls preload="metadata" >
<source src="https://korben.info/rustfs-stockage-objet-distribue-rust/rustfs-stockage-objet-distribue-rust-1.mp4" type="video/mp4" />
Votre navigateur ne supporte pas la lecture de vidéos HTML5. Voici un
<a href="https://korben.info/rustfs-stockage-objet-distribue-rust/rustfs-stockage-objet-distribue-rust-1.mp4">lien vers la vidéo</a>.
</video>
<div>
<p>La licence c'est de l'Apache 2.0 comme ça y'a pas de contrainte virale, vous faites ce que vous voulez avec. Et c'est d'ailleurs sûrement la raison numéro un pour laquelle le projet cartonne.</p>
<p>Côté perfs, les devs annoncent 2,3x plus rapide que MinIO sur des petits objets de 4 Ko (testé sur un modeste 2 coeurs Xeon avec 4 Go de RAM). Bon, c'est un benchmark maison, à prendre avec des pincettes hein... mais finalement Rust pour du I/O intensif, ça se tient comme argument, car y'a pas de garbage collector qui vient foutre le bazar.</p>
<p>Pour l'installer, Docker en une ligne :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
</span></span></code></pre><p>Et voilà, l'API tourne sur le port 9000 et la console web sur le 9001 (identifiants par défaut : rustfsadmin/rustfsadmin, changez-les vite fait hein). Y'a aussi du Kubernetes via Helm, un script d'install one-click, du Nix, ou un bon vieux git clone pour compiler vous-même (attention, sur macOS faut un ulimit à 4096 sinon ça ne marche pas).</p>
<p>Le conteneur Docker tourne en non-root (UID 10001), donc c'est plutôt propre niveau sécu. Pensez juste à faire un petit <code>chown -R 10001:10001 data logs</code> sur vos répertoires avant de lancer, sinon ça casse au démarrage.</p>
<p>Petit bonus appréciable, y'a aussi de la détection de corruption intégrée, et même du versioning de buckets pour les plus méfiants côté intégrité des données. D'ailleurs, côté monitoring, c'est déjà câblé pour envoyer vos métriques dans Grafana, vos traces dans Jaeger et le reste dans Prometheus. Un petit <code>docker compose --profile observability up -d</code> et c'est plié.</p>
<p>Par contre, on est encore en alpha et le mode distribué et le KMS sont en phase de test. Donc c'est PAS le genre de truc que vous mettrez en prod demain matin pour vos données critiques... mais pour du dev, du lab, ou des tâches pas trop sensibles... ça tourne impecc !</p>
<p>Bref, si l'AGPL de MinIO vous gave et que vous cherchez une alternative S3-compatible, en Rust, sous licence + permissive, allez jeter un œil à RustFS.</p>
<p>Merci à Lorenper pour le partage !</p>