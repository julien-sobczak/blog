---
layout: post-read
title: 'MapReduce Design Patterns'
author: 'Julien Sobczak'
date: '2013-06-28T09:00:00.002+02:00'
categories: read
tags:
- big-data
- design-patterns
image: 'http://d.gr-assets.com/books/1344723076l/14514285.jpg'
read_authors: 'Donald Miner, Adam Shook'
read_note: 11
read_date_published: '2012-12-22'
read_book_format: 'Paperback'
read_isbn: '1449327176'
read_number_of_pages: 230
read_roti: 2
read_time: 10
read_headline: "Un livre correct pour découvrir le sujet. Une simple introduction en attendant d'autres livres plus complets..."
link_amazon: "http://www.amazon.com/gp/product/1449327176/"
link_goodreads: "http://www.goodreads.com/book/show/14514285-mapreduce-design-patterns"
---


Depuis la publication du papier par Google, le terme MapReduce se manifeste de plus en plus souvent. De plus en plus de frameworks l'implémentent (Hadoop, MongoDB, ...) mais la documentation reste limitée sur le sujet. On trouve souvent dans les ouvrages de ces solutions un chapitre consacré à l'utilisation de MapReduce. Mais cela reste limité à quelques exemples ciblés.

Quelles est l'étendue des domaines auxquels un framework comme MapReduce peut s'appliquer et surtout comment l'utiliser judicieusement sont deux questions que je voulais approfondir.

*MapReduce Design Patterns* apporte ces réponses mais pas complètement. Les patterns restent basiques et peu nombreux, les exemples tous centrés sur Hadoop (même si cela peut se comprendre), d'où mon appréciation générale mitigée sur l'ouvrage. Toutefois, il faut bien reconnaître que le livre comble un manque au niveau de la littérature sur MapReduce et faute d'autres livres à comparer, *MapReduce Design Patterns* reste un ouvrage à recommandé sur le sujet.

Le livre fait souvent le parallèle avec le langage SQL et Pig, ce qui appréciable pour la compréhension des patterns. Le livre montre aussi comment Pig implémenté ces différents patterns pour proposer une solution de plus haut niveau d'abstraction, plus facile à prendre en main et plus succinct que l'écriture des fonctions map et reduce. Grâce à Pig, on peut exploiter le framework MapReduce sans même sans rendre compte mais est-ce une bonne chose De même qu'utiliser Hibernate ne dispense pas de comprendre son fonctionnement pour bien l'appréhender, je pense que comprendre la logique MapReduce est indispensable pour utiliser les différentes solutions développées au dessus du framework.

