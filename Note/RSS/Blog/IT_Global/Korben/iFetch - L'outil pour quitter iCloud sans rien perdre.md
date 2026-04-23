---
title: "iFetch - L'outil pour quitter iCloud sans rien perdre"
author: "Korben"
date: 2026-03-09T09:34:34.000Z
type: site
subject:
category: IT Global
tags:
  - "linux-open-source/logiciels-libres"
  - "tutoriels-guides"
  - "open source"
  - "Python"
  - "CLI"
  - "sauvegarde"
  - "icloud"
rss_source: Blog
url: https://korben.info/ifetch-telecharger-icloud-drive.html
note: 0
seen: false
---

<p><strong>iCloud, c'est sympa pour stocker vos photos et vos documents</strong>... jusqu'au jour où comme moi, vous décidez de vous barrer. Parce que récupérer vos 200 Go de fichiers en masse depuis le cloud d'Apple (plusieurs To pour moi), c'est pas vraiment ce qu'il y a de plus simple (genre, y'a pas de bouton &quot;tout télécharger&quot;). J'ai bien essayé de demander un export de mes datas à Apple et pour la partie iCloud Drive, j'ai juste eu des espèces de CSV bizarres mais pas mes documents.</p>
<p>Heureusement, pour s'extraire des griffes de l'entreprise de Cupertino, y'a un outil Python parfait pour ça.</p>
<p>
<a href="https://github.com/roshanlam/iFetch">iFetch</a>
, c'est un utilitaire en ligne de commande qui va se connecter à votre compte iCloud Drive et tout rapatrier en local. Le truc gère la 2FA (parce que bon, en 2026, si vous n'avez pas de 2FA activée quand c'est possible, vous méritez d'être envahi de puces de lit), les téléchargements parallèles avec 4 workers par défaut, et surtout les updates différentiels.</p>
<p>En gros, seuls les morceaux de fichiers qui ont changé sont re-téléchargés, du coup, sur un dossier de 50 Go déjà synchro, ça passe en quelques secondes au lieu de tout re-pomper. Et si ça plante au milieu, pas de panique, l'outil reprend là où il s'est arrêté grâce à un système de checkpointing.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ifetch-telecharger-icloud-drive/ifetch-telecharger-icloud-drive-2.png" alt="" loading="lazy" decoding="async">
<p>Y'a aussi un truc malin, c'est le système de profils. Vous créez un fichier JSON avec des règles d'inclusion et d'exclusion, genre &quot;<em>tous les PDF du dossier Documents sauf ceux du dossier Private</em>&quot; et hop, en une commande et c'est plié.</p>
<p>Le support des dossiers partagés est aussi de la partie (le fameux <code>--list-shared</code>), y'a un système de plugins pour ceux qui veulent étendre le bazar, et même un historique de versions avec rollback automatique. Pas mal pour un outil libre !</p>
<p>Pour l'installer, après c'est du classique. Virtualenv Python, <code>pip install pyicloud tqdm requests keyring</code>, et vous stockez vos identifiants via <code>icloud --username=votre@email.com</code> qui balance tout ça dans le trousseau système (Keychain sur macOS, libsecret sur Linux). D'ailleurs, si vous êtes du genre à
<a href="https://korben.info/sauvegardez-automatiquement-vos-fichiers-de-config-dotfiles-vers-icloud.html">sauvegarder vos dotfiles dans iCloud</a>
, c'est l'outil parfait pour faire le chemin inverse.</p>
<p>Côté utilisation, c'est super sobre :</p>
<p><code>python ifetch/cli.py Documents/Photos ~/Downloads/icloud-photos</code></p>
<p>...et ça mouline !! Vous pouvez même monter jusqu'à 8 workers pour aller plus vite (<code>--max-workers=8</code>), configurer les retries (<code>--max-retries=5</code>) ou juste lister le contenu sans rien télécharger avec <code>--list</code>. Attention, si vous avez des noms de fichiers avec des caractères spéciaux (genre des accents ou des espaces... merci macOS, groumpf), vérifiez bien que tout est passé après le transfert.</p>
<p>Alors oui, c'est CLI only, donc oubliez l'interface graphique. La doc mériterait un petit coup de polish et surtout, si votre session 2FA expire en plein transfert... faut relancer l'auth. Ça casse pas le téléchargement en cours, mais bon, c'est un peu &quot;chiant&quot;.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/ifetch-telecharger-icloud-drive/ifetch-telecharger-icloud-drive-3.png" alt="" loading="lazy" decoding="async">
<p>Bon au final, pour un projet open source sous licence MIT, c'est plutôt du solide. Et si vous voulez
<a href="https://korben.info/chiffrez-vos-sauvegardes-avant-de-les-envoyer-dans-le-cloud.html">chiffrer vos sauvegardes</a>
une fois récupérées en local, y'a des solutions pour ça aussi.</p>
<p>Bref, c'est simple, ça fait le job et c'est gratuit. Que demande le peuple à part du matos Apple moins cher, lool ?</p>
<p>Merci à Lorenper pour le lien !</p>