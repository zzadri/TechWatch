---
title: "Il charge TOUTES les extensions Firefox dans son navigateur"
author: "Korben ✨"
date: 2026-04-22T10:12:20.000Z
type: site
subject:
category: IT Global
tags:
  - "multimedia-culture/culture-geek"
  - "reseaux-internet/navigateurs-web"
  - "Firefox"
  - "Mozilla"
  - "vie privée"
  - "VPN"
rss_source: Blog
url: https://korben.info/jack-firefox-toutes-extensions.html
note: 0
seen: false
---

<p>Vous vous souvenez du mème &quot;<em>
<a href="https://knowyourmeme.com/memes/oh-you-love-x-name-every-y">Oh, tu aimes les extension Firefox ? Alors nomme les toutes !</a>
</em>&quot; ?</p>
<p>Bah
<a href="https://jack.cab">Jack</a>
s'est dit que plutôt que les nommer, autant toutes les installer. Oui, les 84 194 extensions d'un seul coup !</p>
<p>Sur le papier c'est pas si compliqué. Tu télécharges les <code>.xpi</code> depuis l'API publique Mozilla (aucune authentification requise), tu les colles dans le dossier <code>extensions/</code> d'un profil Firefox, tu édites <code>extensions.json</code> pour tout activer. Sauf que l'API de recherche plafonne à 600 pages max, soit environ 30 000 résultats. Du coup Jack a du combiner plusieurs tris pour contourner la limite et chopper les 84 235 extensions existantes, soit 49,3 Go de données au total.</p>
<p>Première tentative dans une VM Windows Tiny11 : le pagefile bouffe malheureusement tout le disque, Firefox gèle, et c'est la fin. Du coup, essai suivant sur Mac avec 6 heures de téléchargement, soit 400 Go d'écritures disque... la fenêtre Firefox s'ouvre mais ne répond jamais ! Entre 4 000 et 6 000 extensions actives certes mais les sites web ne chargent plus (une des extensions bloque tout mais laquelle ??). Bref, plus grand-chose ne répond à part le <code>about:addons</code>.</p>
<p>6 mois plus tard, Jack retente alors l'opération avec une VM. 84 194 extensions chargées, en 1h43 auquel s'ajoute 39 minutes pour que Firefox réécrive le fichier <code>extensions.json</code> (qui pèse du 189 Mo), +24 minutes avant que le navigateur affiche quoi que ce soit, avec une consommation mémoire stabilisée vers 32 Go. La cause du ralentissement est chirurgicale... En fait Firefox sérialise <code>extensions.json</code> en entier à chaque écriture donc ça marche nickel pour 15 extensions mais pour 84 194, c'est pas le même délire.</p>
<p>Le plus intéressant après, c'est pas la démarche elle-même, c'est surtout ce que ça révèle sur le store de Mozilla. En effet, après analyse, 34,3 % des extensions n'ont aucun utilisateur quotidien. 19 % sont totalement abandonnées, sans user, sans review ni capture écran, et encore moins une icône. Y'a aussi des contributeurs un peu chelous comme un certain &quot;Dr. B&quot; qui a publié à lui seul 84 extensions, toutes générées avec Grok 3.</p>
<p>Et puis il y a aussi des extensions de phishing crypto avec des
<a href="https://www.seqrite.com/fr/blog/homoglyph-attacks-lookalike-characters-cyber-deception/">homoglyphes cyrilliques</a>
. L'extension malveillante &quot;Іron Wаllеt&quot; par exemple récupère ses URLs depuis un
<a href="https://korben.info/nocodb-clone-airtable.html">NocoDB</a>
trois secondes après installation. Le groupe Innover Online Group contrôle à lui seul plus de 700 000 utilisateurs via un paquet d'extensions de spam affilié sur Yahoo Search. Mozilla en a pour le moment désactivé 3 dans la foulée.</p>
<p>Autre moment drôle : Windows Defender a flaggé
<a href="https://addons.mozilla.org/fr/firefox/addon/hacktools/">HackTools</a>
comme cheval de Troie alors que c'est légitime. Y'a aussi la plus grosse extension installée, <code>dmitlichess</code>, qui pèse 196 Mo car elle embarque 2 000 fichiers audio), et la plus petite fait 7 518 octets... sans contenir une seule ligne de code. Bref, y'a des pépites.</p>
<p>Et Jack a publié son
<a href="https://huggingface.co/datasets/jack5079/extensions">dataset en CC0 sur Hugging Face</a>
sans oublier que son code est dispo donc si vous avez 50 Go à cramer et envie de faire joujou avec l'
<a href="https://korben.info/glide-browser-firefox-fork-typescript-vim.html">écosystème Firefox</a>
, servez-vous !</p>
<p>Bref, un Firefox lancé avec TOUTES les extensions du store Mozilla, ça fonctionne techniquement, mais c'est loin d'être utilisable. Mais après pour faire de l'analyse et des stats, je trouve ça marrant.</p>
<p>
<a href="https://jack.cab/blog/every-firefox-extension">Source</a>
</p>