---
title: "sudo-rs - 40 ans de silence cassés par des astérisques"
author: "Korben"
date: 2026-02-27T08:33:54.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source"
  - "tutoriels-guides/tutoriels-avances"
  - "Rust"
  - "sécurité"
  - "sudo"
  - "terminal"
  - "Ubuntu"
rss_source: Blog
url: https://korben.info/sudo-rs-password-feedback-asterisques.html
note: 0
seen: false
---

<p>Si vous utilisez Ubuntu 26.04, vous avez peut-être remarqué un truc bizarre dernièrement en tapant votre mot de passe sudo... Ouiiiiii, y'a des petites étoiles qui apparaissent !! Pas de panique, c'est &quot;normal&quot;. Enfin, c'est nouveau...</p>
<p>En effet, <strong>sudo-rs</strong>, la réécriture en Rust de la bonne vieille commande sudo, a décidé d'activer <code>pwfeedback</code> par défaut. En gros, quand vous faites un <code>sudo apt install bidule</code>, au lieu du trou noir habituel, vous voyez maintenant des <code>*****</code> défiler pendant la saisie du mot de passe. C'est un changement qui casse une convention vieille de 40 ans... et ça, forcément, ça fait du bruit !</p>
<p>Pour rappel, Ubuntu a basculé sur sudo-rs (le remplaçant en Rust du bon vieux sudo en C) depuis la version 25.10. Ça fait partie du même mouvement de réécriture des outils système en Rust,
<a href="https://korben.info/rust-coreutils-base64-bat-gnu.html">comme les coreutils</a>
dont je vous avais parlé. Et la 26.04 vient de &quot;cherry-picker&quot; comme on dit, un patch upstream <strong>qui active le feedback visuel par défaut.</strong></p>
<p>Un bug report sur Launchpad (
<a href="https://bugs.launchpad.net/ubuntu/&#43;source/rust-sudo-rs/&#43;bug/2142721">#2142721</a>
) est bien sûr arrivé direct, en mode vénère genre &quot;*ÇA FAIT DES DÉCENNIES qu'on n'affiche pas la longueur du mot de passe pour empêcher le shoulder surfing ! C'est quoi ce bordel !!?? *&quot;</p>
<p>Et la réponse des devs : <strong>Won't Fix</strong>. Circulez les relous !</p>
<p>En fait, leur argument c'est que le bénéfice sécurité est &quot;infinitésimal&quot;. Parce que bon, votre mot de passe sudo c'est le même que celui de votre session (celui que vous tapez à l'écran de login, devant tout le monde). Et le bruit des touches trahit déjà la longueur de toute façon. Du coup, ils ont préféré régler le problème UX qui paume les débutants depuis le début des années 80.</p>
<p>D'ailleurs,
<a href="https://korben.info/des-etoiles-lors-de-la-saisie-dun-mot-de-passe-dans-le-terminal.html">en 2013 je vous expliquais comment activer ces étoiles manuellement</a>
avec <code>sudo visudo</code> (ça date de fou !!) et maintenant c'est l'inverse, faut expliquer comment les virer ! Linux Mint avait d'ailleurs déjà sauté le pas de son côté depuis un moment.</p>
<p>Perso, le truc qui me gonfle c'est pour les tutos vidéo. Quand vous faites un screencast, les astérisques révèlent la longueur de votre mot de passe à tous vos spectateurs. Du coup faut aller reparamétrer chaque machine avant de filmer ou faire du masquage en post prod. C'est pas la fin du monde, mais bon, la flemme...</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/sudo-rs-password-feedback-asterisques/sudo-rs-password-feedback-asterisques-2.png" alt="" loading="lazy" decoding="async">
<p>Alors pour désactiver ces jolies zétoiles :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">sudo visudo
</span></span></code></pre><p>Et ajoutez cette ligne à la fin de <code>/etc/sudoers</code> :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">Defaults !pwfeedback
</span></span></code></pre><p>Sauvegardez (Ctrl+X sous nano), et c'est réglé. Attention, ne touchez à rien d'autre dans ce fichier, une erreur de typo et sudo ne marchera plus. Grâce à cette manip, ce sera retour au trou noir ! Youpi !</p>
<p>
<a href="https://www.phoronix.com/news/sudo-rs-password-feedback">Source</a>
</p>