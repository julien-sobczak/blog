---
layout: post-read
title: 'Patterns of Enterprise Application Architecture'
author: 'Julien Sobczak'
date: '2011-01-28T09:00:00.002+02:00'
categories: read
tags:
- architecture
- classics
- design-patterns
image: 'http://d.gr-assets.com/books/1388197686l/70156.jpg'
read_authors: 'Martin Fowler'
read_note: 17
read_date_published: '2002-11-5'
read_book_format: 'Hardcover'
read_isbn: '0321127420'
read_number_of_pages: 533
read_roti: 4
read_time: 25
read_headline: "Un des meilleurs catalogues de patterns. Il a peu de chance que vous soyez amené les implémenter mais il a fort parier que vous les utiliser déjà au quotidien. Le livre vous en révélera toutes leurs subtilités et leur regroupement au sein d'un même livre apporte une certaine cohérence très intéressante."
link_amazon: "http://www.amazon.com/gp/product/0321127420/"
link_goodreads: "http://www.goodreads.com/book/show/70156.Patterns_of_Enterprise_Application_Architecture"
---


Un des catalogues de patterns les plus connus et les plus souvent cités.

Martin Fowler s'attaque ici aux patterns d'architecture. L'ouvrage commence par une première partie narrative, très réussie, qui permet d'obtenir une vison globale de l'ouvrage et de mieux situer les patterns entre eux. Martin Fowler décrit ce qu'est une application d'entreprise sans en donner de définition exacte, mais plutôt ses caractéristiques système de grande envergure, nombreux écrans, besoin de persister de nombreuses données accédées de manière concurrente, etc.

Vient ensuite le catalogue de patterns qui constitue le cœur du livre. Il est important de préciser que ces patterns ne sont pas forcément très utiles en pratique. Par exemple, le livre comprend un nombre conséquent de patterns liés à la problématique d'ORM (les stratégies pour gérer l'héritage, Identity Map, Unit of Work, etc).

Quel est donc l'intérêt du livre pour la majorité des lecteurs ?

En effet, la plupart des patterns du livre sont repris dans les frameworks que nous connaissons tous (Hibernate, Struts, etc). Découvrir ces patterns aident donc à mieux comprendre ces frameworks qui les implémentent. Utiliser un framework ne dispense pas, selon moi, de comprendre son fonctionnement. Bien au contraire, ne pas s'y intéresser, c'est prendre le risque de ne pas profiter pleinement du framework et de le subir. Hibernate est le parfait exemple. Ne pas comprendre les notions derrière un ORM se traduit généralement par une mauvaise utilisation et des performances déplorables, souvent imputées injustement au framework. Autre exemple, Hibernate propose la stratégie de lock optimiste. Comment savoir si son utilisation est justifiée sans comprendre le pattern Optimist Lock et les solutions alternatives comme Pessimistic Lock. Vous l'aurez compris, le livre garde donc un réel intérêt.

