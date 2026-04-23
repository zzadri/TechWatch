---
title: "PinMe - Le web immuable en une commande"
author: "Korben"
date: 2026-02-27T08:07:28.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "linux-open-source/self-hosting"
  - "auto-hébergement"
  - "IPFS"
  - "web décentralisé"
rss_source: Blog
url: https://korben.info/pinme-site-web-permanent-ipfs.html
note: 0
seen: false
---

<p>Les 404, c'est la plaie du web... J'en sais quelque chose, je fais la chasse à ça en permanence sur mon propre site. C'est vrai que c'est relou parce que vous bookmarkez un projet cool, vous y retournez trois mois après... et pouf, ça a disparu. Le dev n'a pas renouvelé son nom de domaine, l'hébergeur a fermé boutique, le contenu s'est évaporé ou que sais-je encore... En fait, sur le web, <strong>RIEN n'est permanent</strong>.</p>
<p>
<a href="https://github.com/glitternetwork/pinme">PinMe</a>
prend le problème à l'envers en collant vos fichiers directement sur
<a href="https://korben.info/ipfs-le-web-permanent.html">IPFS</a>
. En gros, au lieu de dépendre d'un serveur unique qui peut tomber n'importe quand, vos pages sont distribuées sur un réseau décentralisé et identifiées par un hash CID unique. Du coup, tant que le réseau tourne, votre contenu existe. Pas besoin de renouveler quoi que ce soit, pas besoin de payer un hébergeur... ça fonctionne tout seul.</p>
<p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pinme-site-web-permanent-ipfs/pinme-site-web-permanent-ipfs-2.png" alt="" loading="lazy" decoding="async">
</p>
<p>L'installation se fait en une ligne :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npm install -g pinme
</span></span></code></pre><p>Pour déployer votre site statique, c'est hyper simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-gdscript3" data-lang="gdscript3"><span class="line"><span class="cl"><span class="n">pinme</span> <span class="n">upload</span> <span class="n">dist</span><span class="o">/</span>
</span></span></code></pre><p>L'outil détecte le dossier de build, ou plutôt il le devine tout seul selon votre framework : <code>dist/</code> pour Vite et Vue, <code>build/</code> pour Create React App, <code>out/</code> pour Next.js en export statique. Ça évite d'avoir à se palucher de la config.</p>
<p>Côté limites, on est sur 200 Mo par fichier et 1 Go au total ce qui est largement suffisant pour une landing page ou une démo ! Et c'est GRATUIT. Pour ceux qui veulent un domaine lisible plutôt qu'un hash cryptique, y'a aussi des domaines ENS (les <code>.eth</code> sur Ethereum) ou des sous-domaines en <code>.pinit.eth.limo</code>. Après pour les domaines custom faudra un compte VIP par contre.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pinme-site-web-permanent-ipfs/pinme-site-web-permanent-ipfs-3.png" alt="" loading="lazy" decoding="async">
<p>Le truc sympa c'est que vos fichiers restent accessibles via n'importe quelle passerelle IPFS, genre dweb.link ou w3s.link. Ainsi, si votre hébergeur ferme ou que votre domaine expire comme je le disais en intro, on s'en fiche ! Le contenu est toujours là, épinglé quelque part sur le réseau. C'est du stockage immuable, basé sur le contenu lui-même... du coup personne ne peut modifier ou supprimer ce que vous avez publié. (Et en fait vous non plus, faut le savoir.)</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/pinme-site-web-permanent-ipfs/pinme-site-web-permanent-ipfs-4.png" alt="" loading="lazy" decoding="async">
<p>Et y'a aussi des commandes pour exporter en fichiers CAR et réimporter ailleurs, ce qui est pratique pour archiver ou migrer entre passerelles.</p>
<p>Voilà c'est gratuit pour 1 Go de stockage, c'est open source (licence MIT) et
<a href="https://pinme.eth.limo/">c'est par là</a>
. Merci à Lorenper pour la découverte !</p>