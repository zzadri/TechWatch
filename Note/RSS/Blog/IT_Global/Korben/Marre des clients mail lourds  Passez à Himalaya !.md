---
title: "Marre des clients mail lourds ? Passez à Himalaya !"
author: "Korben"
date: 2026-02-20T09:25:00.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/terminal-shell"
  - "reseaux-internet/email"
  - "CLI mail"
  - "himalaya"
rss_source: Blog
url: https://korben.info/marre-des-clients-mail-lourds-passez-a-himalaya.html
note: 0
seen: false
---

<p>Envie de gérer vos emails sans sortir de votre terminal ? Si vous êtes du genre à passer votre vie dans une console (genre pour les mecs comme moi quoi...), vous savez que les clients mails classiques sont souvent des usines à gaz qui mangent de la RAM pour rien.</p>
<p>C'est là qu'intervient <strong>
<a href="https://github.com/pimalaya/himalaya">Himalaya CLI</a>
</strong>.</p>
<p>C'est un client email écrit en Rust, donc autant vous dire que ça envoie du bois niveau rapidité et sécurité. L'idée, c'est de proposer un outil qui fait une seule chose mais qui la fait bien à savoir gérer vos courriers électroniques directement en ligne de commande, sans chichi.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/marre-des-clients-mail-lourds-passez-a-himalaya/marre-des-clients-mail-lourds-passez-a-himalaya-1.jpeg" alt="" loading="lazy" decoding="async">
<p>Le truc cool, c'est qu'il est super polyvalent. Il gère le multi-compte sans broncher (Gmail, Outlook, iCloud, Protonmail...), supporte l'IMAP et le SMTP, mais peut aussi bosser avec des boîtes locales au format Maildir ou Notmuch. Pour les paranoïaques de la sécurité, le support PGP est de la partie pour chiffrer vos échanges, et il s'intègre même avec le trousseau de clés de votre OS pour stocker vos mots de passe proprement.</p>
<p>Pour l'installer en tant que user, c'est archi-simple :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | PREFIX=~/.local sh
</span></span></code></pre><p>Et une fois en place, je vous conseille de lancer l'assistant de configuration qui va vous guider pas à pas (sans vous prendre la tête). Pour cela, lancez simplement :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">himalaya
</span></span></code></pre><p>Vous pourrez ensuite lister vos messages, les lire, ajouter des pièces jointes et même composer vos réponses dans votre éditeur de texte préféré (Vim, Emacs, ou même Nano si vous n'avez pas encore vu la lumière). Et si vous voulez automatiser des trucs, sachez qu'il peut cracher du JSON, ce qui est parfait pour faire de la bidouille terminal avec d'autres scripts.</p>
<p>D'ailleurs, si vous kiffez les outils en Rust pour votre console, je vous avais déjà parlé de
<a href="https://korben.info/doxx-terminal-viewer-word-rust.html">Doxx pour lire des fichiers Word</a>
ou de
<a href="https://korben.info/geary-client-mail-leger-pour-gnome.html">Geary si vous préférez quand même une petite interface légère</a>
.</p>
<p>Bref, encore un excellent outil pour reprendre le contrôle de sa boîte mail tout en restant dans son environnement préféré.</p>
<p>
<a href="https://terminaltrove.com/himalaya/">Source</a>
</p>