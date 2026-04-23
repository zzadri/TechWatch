---
title: "Le Royaume-Uni cherche un développeur C++ pour maintenir un logiciel vieux de 15 ans qui gère tout son trafic aérien"
author: "Korben"
date: 2026-03-12T16:08:39.000Z
type: site
subject:
category: IT Global
tags:
  - "actualites-business"
  - "developpement/langages-programmation"
  - "aeroport"
  - "aviation"
  - "C++"
  - "londres"
  - "Programmation"
  - "uk"
rss_source: Blog
url: https://korben.info/le-royaume-uni-cherche-un-developpeur-c-pour-maintenir-un-logiciel-vieux-de-15-ans-qui-gere-tout-son-trafic-aerien.html
note: 0
seen: false
---

<p>Le ministère des Transports britannique vient de publier un appel d'offres pour trouver un développeur C++ capable de maintenir le NAPAM, le modèle qui prédit la répartition des passagers dans les aéroports du pays. Le programme tourne sur 10 000 lignes de code avec Excel comme interface. Budget prévu : 100 000 livres sur trois ans.</p>
<h2 id="10-000-lignes-de-c-et-un-fichier-excel">10 000 lignes de C++ et un fichier Excel</h2>
<p>Le NAPAM (pour National Aviation Passenger Allocation Model), est le logiciel qui permet au gouvernement britannique de prévoir comment les passagers se répartissent entre les aéroports du pays. Il couvre 29 aéroports britanniques qui gèrent des vols internationaux, plus quatre hubs à l'étranger : Amsterdam, Dubaï, Francfort et Paris.</p>
<p>Le programme tourne dans un environnement .NET en C++ et se nourrit de données via des fichiers Excel. Il effectue des calculs itératifs jusqu'à atteindre certains seuils définis par l'utilisateur, comme la capacité maximale de passagers d'un aéroport donné. Le tout tient en 10 000 lignes de code. Pour un outil qui influence les décisions de politique aérienne du Royaume-Uni, on est sur quelque chose d'assez artisanal.</p>
<h2 id="un-appel-doffres-à-budget-serré">Un appel d'offres à budget serré</h2>
<p>Cet appel d'offres a été lancé pour un contrat de trois ans, avec un budget de 100 000 livres, soit l'équivalent de 120 000 euros. Le poste consiste à fournir un support technique ad hoc aux analystes et économistes de l'équipe Aviation Appraisal and Modelling.</p>
<p>Le modèle existe depuis au moins 2010 et a été mis à jour en 2017, 2022 et 2024. Le précédent contrat de maintenance avait été attribué au cabinet américain Jacobs, qui avait facturé environ 97 000 livres rien que pour les mises à jour de 2020. Le ministère précise quand même que le budget est « non engageant » et qu'il ne garantit ni le volume de travail ni les dépenses.</p>
<h2 id="un-cas-décole-du-logiciel-legacy">Un cas d'école du logiciel legacy</h2>
<p>Ce genre de situation est un classique dans les administrations : un outil développé il y a quinze ans par un prestataire, maintenu au fil de l'eau par un consultant externe, et dont personne en interne ne maîtrise vraiment le code.</p>
<p>Le NAPAM est quand même utilisé pour orienter les investissements aéroportuaires et les projections de trafic du pays. Si le développeur sous contrat décide de partir à la retraite ou de changer de métier, c'est tout le modèle de prévision qui se retrouve en difficulté.</p>
<p>Et avec 10 000 lignes de C++ legacy plus des macros Excel, on imagine la joie du prochain développeur qui reprendra le dossier.</p>
<p>C'est quand même un peu vertigineux de se dire que les prévisions du trafic aérien d'un pays du G7 dépendent d'un programme en C++ maintenu par un seul prestataire pour 33 000 livres par an.</p>
<p>Avec ce budget, on est à peine sur le tarif d'un développeur junior à mi-temps à Londres. On ne dit pas que le modèle est mauvais, mais la dépendance à une seule personne sur du code legacy avec Excel comme interface, ça fait quand même un peu froid dans le dos.</p>
<p>Source :
<a href="https://www.theregister.com/2026/03/12/100k_tender_napam/">The Register</a>
</p>