---
title: "Windows a enfin sa CLI pour les développeurs d'apps"
author: "Korben"
date: 2026-01-23T08:08:27.000Z
type: site
subject:
category: IT Global
tags:
  - "developpement/outils-developpement"
  - "windows/powershell-scripting"
  - "développement web"
rss_source: Blog
url: https://korben.info/windows-a-enfin-sa-cli-pour-les-developpeurs-dapps.html
note: 0
seen: false
---

<p>Développer une application pour Windows quand on n'utilise pas Visual Studio, c'est un peu comme essayer de monter un meuble Conforama sans la notice et avec des outils en plastique.</p>
<p>Faut jongler avec les SDK, se battre avec des manifestes XML (l'enfer sur Terre ces trucs), générer des certificats dans tous les sens... Bref, c'est souvent la croix et la bannière. Et Microsoft, dans sa grande bonté (si si, ça arrive), s'est dit qu'il était temps d'arrêter de torturer les développeurs.</p>
<p>Du coup, ils viennent d'annoncer en petite pompe la sortie en preview publique de <strong>winapp</strong>, un nouveau CLI open source conçu pour simplifier tout ce bazar.</p>
<p>Avouez que vous avez lu Winamp ? Ahahah, hé bien non !</p>
<p>Avec ce truc, que vous soyez un développeur Web à fond dans Electron, un vétéran du C++ qui vit dans CMake, ou que vous bossiez en Rust ou Dart, cet outil va grave vous mâcher le travail.</p>
<p>Exit la configuration manuelle de l'environnement qui prend trois plombes, notamment grâce à la commande <code>winapp init</code>.</p>
<p>
<img src="https://korben.info/windows-a-enfin-sa-cli-pour-les-developpeurs-dapps/windows-a-enfin-sa-cli-pour-les-developpeurs-dapps-1.gif" alt="" loading="lazy" decoding="async">
</p>
<p>Cet outil s'occupe de tout, c'est fou : il télécharge les SDK nécessaires, génère les projections (C++/WinRT pour commencer) et configure votre projet. Hop, c'est réglé. Je trouve ça quand même plus sympa que de se taper toutes les étapes à la main avec le risque de se foirer tous les deux clics.</p>
<p>Mais là où c'est vraiment cool, c'est pour le débogage.</p>
<p>Vous savez ces API modernes de Windows telles que les notifications ou les fonctions IA qui nécessitent que votre application ait une &quot;identité de paquet&quot; (ça me rappelle une blague de Bigard, tiens..) ? Hé bien avant, pour tester ça, il fallait empaqueter et installer l'application complète. C'était une perte de temps monumentale.</p>
<p>Mais maintenant, avec <code>winapp create-debug-identity</code>, vous injectez cette identité directement dans votre exécutable. Ça vous permet de continuer à coder et de déboguer votre code spaghetti normalement, sans casser votre boucle de développement. Rien que pour ça, ça vaut le détour !</p>
<div class="youtube-container">
<iframe
src="https://www.youtube-nocookie.com/embed/WsUaymVnLGY?rel=0&modestbranding=1"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
</iframe>
<div>
<p>Bienvenue au XXIe siècle les dev M$ !</p>
<p>L'outil gère aussi la création des manifestes et des certificats de développement. Plus besoin de chialer durant des heures devant un fichier <code>appxmanifest.xml</code> invalide. Vous pouvez même générer un certificat auto-signé en une commande pour tester vos paquets localement.</p>
<p>Et pour les amis qui font de l'Electron, Microsoft a pensé à vous avec un paquet npm dédié.</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">npm install --save-dev @microsoft/winappcli
</span></span></code></pre><p>Ça permet d'intégrer des fonctionnalités natives ou de l'IA directement dans votre app Electron, et de lancer le tout avec un simple <code>npm start</code> qui gère l'identité du paquet via <code>winapp node add-electron-debug-identity</code>. C'est propre, hein ?</p>
<p>Maintenant, pour installer la bête sur votre machine, un petit coup de WinGet :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">winget install microsoft.winappcli
</span></span></code></pre><p>Et vous m'en direz des nouvelles. Alors bien sûr, c'est encore en preview ET c'est dev par Microsoft, donc il y a sûrement des petits bugs qui traînent, mais l'intention est là et ça fait plaisir de les voir s'ouvrir un peu plus aux workflows qui sortent de leur écosystème fermé habituel.</p>
<p>Voilà, si vous voulez tester,
<a href="https://github.com/microsoft/WinAppCli">le code est dispo sur GitHub</a>
et ils attendent vos retours.</p>
<p>Amusez-vous bien !</p>
<p>
<a href="https://blogs.windows.com/windowsdeveloper/2026/01/22/announcing-winapp-the-windows-app-development-cli/">Source</a>
</p>