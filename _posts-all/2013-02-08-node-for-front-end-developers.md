---
layout: post-read
title: 'Node for Front-End Developers'
author: 'Julien Sobczak'
date: '2013-02-08T09:00:00.002+02:00'
categories: read
tags:
- frameworks
- javascript
image: 'http://d.gr-assets.com/books/1328240521l/13227091.jpg'
read_authors: 'Garann Means'
read_note: 10
read_book_format: 'Paperback'
read_isbn: '1449318835'
read_number_of_pages: 60
read_roti: 4
read_time: 1
read_headline: "Une très courte introduction Node, ses modules phares (Connect, Socket.io, Express) ou encore des frameworks/librairies (Redis, Jade, Require.JS, Backbone). Le tout en 45 pages... Peu convaincant."
link_amazon: "http://www.amazon.com/gp/product/1449318835/"
link_goodreads: "http://www.goodreads.com/book/show/13227091-node-for-front-end-developers"
---


Parmi les grands éditeurs, O'Reilly est le seul à proposer des livres aussi courts comme *Node for Front-End Developers* totalisant seulement 45 pages. J'avoue ne pas être hyper emballé par ce format mais il est vrai qu'une seule heure aura suffit pour monter en compétence sur Node.js.

Seul prérequis à ce livre, une bonne expérience en JavaScript côté client est indispensable.

Garann Means nous propose chapitres :

- Chapitre 1: installation de l'environnement Node et premier programme avec l'utilitaire REPL (équivalent à l'outil irb en Ruby)

- Chapitre 2: création d'un serveur Web servant des fichiers statiques, juste avec le module http dans un premier temps, puis avec l'excellent module connect qui fait tomber le serveur à lignes de code...

- Chapitre : gestion des requêtes GET et POST à nouveau avec le minimum de modules (querystring) puis c'est le retour du module connect accompagné de socket.io qui nous simplifient bien la vie.

- Chapitre : séparation des vues à l'aide du système de templating Mustache.

- Chapitre : persistance des données avec Redis et introduction de Pub/Sub, indispensable côté serveur

- Chapitre : utilisation du pattern MVC à l'aide du module Express ou d'une solution courante côté client, Backbone.js. Beaucoup de codes dans ce chapitre qui vise surtout à rallonger le livre suffisamment pour être "publiable". Notons que la création de modules, probablement la clé du succès de Node, est également abordée mais en une seule page... Dommage mais pas indispensable.

Le point positif du livre est que l'auteur nous montre souvent comment faire en Node sans introduire de modules (ce qui nous permet de mieux comprendre son fonctionnement) avant de nous montrer les modules indispensables que nous devrons utiliser pour ne pas réinventer sans cesse la roue.

Le côté négatif, c'est qu'à être si court, tout est survolé à une vitesse folle, sans jamais rentré dans les détails, de quoi se demander sérieusement si on ne devrait pas aller chercher le même niveau de contenu ailleurs comme sur des blogs.

