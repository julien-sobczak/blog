---
layout: post-read
title: 'Spring Data'
author: 'Julien Sobczak'
date: '2013-08-24T09:00:00.002+02:00'
categories: read
tags:
- big-data
- frameworks
- java
image: 'http://d.gr-assets.com/books/1350959510l/15808127.jpg'
read_authors: 'Mark Pollack, Oliver Gierke, Thomas Risberg, Jon Brisbin, Michael Hunger'
read_note: 14
read_date_published: '2012-10-31'
read_book_format: 'Paperback'
read_isbn: '1449323952'
read_number_of_pages: 316
read_roti: 4
read_time: 7
read_headline: "Une solide introduction sur un framework de qualité."
link_amazon: "http://www.amazon.com/gp/product/1449323952/"
link_goodreads: "http://www.goodreads.com/book/show/15808127-spring-data"
---


Un livre d'introduction pour comprendre les motivations derrière Spring Data. Les auteurs sont parfaitement qualifiés pour la tâche puisqu'ils travaillent sur le projet. Le livre est assez court avec environ 300 pages pour aborder les différentes solutions comme JPA, JDBC, Mongo DB, Redis, Neo4j, Hadoop, GemFire.

Avec autant de sujets abordés, je ne serai pas surpris de devoir rechercher de plus amples informations lors du l'utilisation du framework. Logiquement, le livre ne cherche pas à expliquer les différentes solutions de persistance et se contente d'une brève présentation à chaque fois. Les nombreux exemples illustrent eux très bien l'utilisation de Spring Data.

Concernant le framework lui-même, il est bien pensé. La réalisation est de qualité, pas étonnant pour un projet Spring. Toutefois, certaines appréhensions qui m'ont conduites à lire cet ouvrage persistent. L'utilisation QueryDSL ne me convainc guère. Pourquoi sacrifier la lisibilité pour être type-safe quand des tests automatisés nous protègent déjà d'oubli en cas de renommage de champ. L'avantage de pouvoir tester les requêtes sur une simple Collection est intéressante mais aurait très bien pu être déjà implémentée avec des requêtes HQL.

Pour la partie Repository, l'idée commence à dater depuis l'introduction de Ruby On Rails et autres déclinaisons. L'idée est séduisante mais pas révolutionnaire. Lorsque la convention de nommage des méthodes ne suffit pas, l'annotation @Query peut aider (tout en perdant le côté type-safe) ou alors vient la nécessité de créer une deuxième interface et implémentation. On ne peut malheureusement faire mieux en Java.

