---
layout: post-read
title: 'Data Model Patterns: Conventions of Thought'
author: 'Julien Sobczak'
date: '2014-04-23T09:00:00.002+02:00'
categories: read
tags:
- database
- design
image: 'http://d.gr-assets.com/books/1387732144l/981057.jpg'
read_authors: 'David C. Hay'
read_note: 10
read_date_published: '1996-01-01'
read_book_format: 'Hardcover'
read_isbn: '0932633293'
read_number_of_pages: 288
read_roti: 2
read_time: 8
read_headline: "La référence depuis déjà 20 ans sur la modélisation relationnelle. Indispensable pour passer de la théorie l'implémentation."
read_publisher: Dorset House
link_amazon: "http://www.amazon.com/gp/product/0932633293/"
link_goodreads: "http://www.goodreads.com/book/show/981057.Data_Model_Patterns"
---


Un livre qui ressemble beaucoup au [Analysis Patterns]({% post_url 2012-02-10-analysis-patterns-reusable-object-models %}) de Martin Fowler. Pas étonnant que ces deux livres soient sortis à quelques mois d'intervalle. Quelques différences tout de même. Martin Fowler propose des modèles orienté-objet alors que David C. Hay se concentre sur des modèles de données relationnels. Dans un monde de [Polyglot Persistence](http://martinfowler.com/bliki/PolyglotPersistence.html), il faut avouer que ce livre sérieusement vieilli et ce n'est pas le style d'écriture très rigoureux qui rendra la lecture plus agréable. Avantage donc à l'ouvrage de Martin Fowler.

Chapitre après chapitre, on se balade entre les différents domaines de l'entreprise (l'organisation, la comptabilité, les commandes, les stocks, etc). l'image du Analysis Patterns, les modèles sont construits progressivement, en étudiant les variations possibles, et à chaque fois, on découvre des subtilités qui nous aurait échappées. Les modèles proposés ont beaucoup à nous apprendre. Trop souvent, on cherche à tout modéliser dans le modèle relationnel alors que déporter certains points hors du modèle est souvent plus judicieux pour garantir son évolutivité. Quelle chance de pouvoir s'appuyer sur des modèles éprouvés !

