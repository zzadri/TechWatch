---
title: "Un ingénieur a intégré la vérification d'âge dans Linux, et c'est la panique"
author: "Korben"
date: 2026-03-23T09:49:16.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business/legislation-juridique"
  - "linux-open-source"
  - "vie-privee-anonymat"
  - "Age"
  - "Linux"
  - "loi"
  - "systemd"
rss_source: Blog
url: https://korben.info/un-ingenieur-a-integre-la-verification-dage-dans-linux-et-cest-la-panique.html
note: 0
seen: false
---

<p>Un développeur américain a soumis en une semaine des modifications à trois projets Linux majeurs pour y ajouter un champ de date de naissance, au nom de lois californiennes et brésiliennes qui entreront en vigueur en janvier 2027.</p>
<p>Le plus gros morceau, systemd, a accepté la modification et refuse de revenir en arrière. La communauté open source est depuis en ébullition.</p>
<h2 id="un-développeur-solitaire-trois-projets-visés">Un développeur solitaire, trois projets visés</h2>
<p>Dylan M. Taylor, ingénieur DevOps basé en Caroline du Nord, a soumis des pull requests à systemd, Ubuntu et Arch Linux en mars 2026. Son objectif : ajouter un champ &quot;date de naissance&quot; dans la base de données utilisateur de chaque système, pour se conformer à trois lois qui entrent en vigueur le 1er janvier 2027.</p>
<p>La loi californienne AB-1043, la loi du Colorado SB26-051 et la loi brésilienne Lei 15.211 imposent aux systèmes d'exploitation de collecter l'âge des utilisateurs dès la création du compte, puis de transmettre cette donnée aux magasins d'applications via une API.</p>
<p>Le plus surprenant, c'est que personne ne lui a demandé de faire ça. Taylor a lu les textes de loi, estimé que Linux devait s'y conformer, et s'est mis au travail tout seul.</p>
<p>Il a lui-même reconnu dans sa pull request pour Arch Linux que le système serait &quot;totalement inefficace pour empêcher quiconque de mentir sur son âge&quot;. Il a qualifié sa propre fonctionnalité de &quot;hilarante d'inutilité&quot;, mais a quand même insisté pour l'intégrer.</p>
<h2 id="systemd-a-accepté-et-le-revert-a-été-refusé">systemd a accepté, et le revert a été refusé</h2>
<p>Côté systemd, la modification a été acceptée par Luca Boccassi, un mainteneur qui travaille chez Microsoft. La pull request a généré 945 commentaires. Quand un autre développeur a tenté de faire annuler la fusion, Lennart Poettering, le créateur de systemd (ancien Red Hat, passé par Microsoft), a personnellement rejeté la demande le 19 mars.</p>
<p>Son argument : le champ est optionnel, systemd ne force rien, et les distributions sont libres de l'utiliser ou non. Le champ date de naissance reste donc dans le code.</p>
<p>Côté Ubuntu, les deux pull requests sont restées à l'état de brouillon. Un vice-président de Canonical a précisé qu'il n'y avait &quot;aucun plan concret&quot; pour intégrer cette fonctionnalité.</p>
<p>Côté Arch Linux, le mainteneur a verrouillé la discussion en attendant un avis juridique. Et Artix Linux a pris la position la plus claire : jamais de vérification d'identité ni d'âge dans leur distribution.</p>
<h2 id="des-lois-qui-posent-un-vrai-problème-technique">Des lois qui posent un vrai problème technique</h2>
<p>Ces lois partent du principe que c'est au système d'exploitation de jouer le rôle de contrôleur d'identité. Sauf que Linux n'est pas Windows ou macOS : c'est un projet communautaire, maintenu par des bénévoles et des entreprises aux intérêts variés.</p>
<p>Collecter des données personnelles dans un système open source pour les transmettre à des magasins d'applications, c'est un changement de philosophie assez radical.</p>
<p>Un développeur d'Ubuntu a proposé une approche différente : une interface D-Bus optionnelle, sans stocker de date de naissance brute. Plus respectueux de la vie privée, mais ça ne fait pas non plus l'unanimité.</p>
<p>On a donc là un ingénieur qui admet que sa propre fonctionnalité ne sert à rien, et qui l'intègre quand même dans un des composants les plus utilisés de Linux. Le tout validé par un mainteneur employé chez Microsoft. Difficile de ne pas remarquer le problème.</p>
<p>Que des lois imposent la vérification d'âge aux systèmes d'exploitation, c'est une chose. Mais que ça passe par un bénévole qui pousse du code dans un projet open source sans que personne ne s'en rende compte avant la fusion, c'est un peu particulier quand même.</p>
<p>Source :
<a href="https://www.sambent.com/the-engineer-who-tried-to-put-age-verification-into-linux-5/">Sambent</a>
</p>