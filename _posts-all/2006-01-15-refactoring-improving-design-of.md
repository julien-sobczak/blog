---
layout: post-read
title: 'Refactoring: Improving the Design of Existing Code'
author: 'Julien Sobczak'
date: '2006-01-15T09:00:00.002+02:00'
categories: read
tags:
- java
- refactoring
image: 'http://d.gr-assets.com/books/1386925632l/44936.jpg'
read_authors: 'Martin Fowler, Kent Beck, Don Roberts'
read_note: 19
read_date_published: '1999-06-28'
read_book_format: 'Hardcover'
read_isbn: '0201485672'
read_number_of_pages: 464
read_roti: 5
read_time: 15
read_headline: "Exceptionnel/Excellent. Incontournable/Indispensable. Un des rares livres qui profondément changé ma manière de développer."
link_amazon: "http://www.amazon.com/gp/product/0201485672/"
link_goodreads: "http://www.goodreads.com/book/show/44936.Refactoring"
---


Refactoring. Un terme sorti de nulle part et pourtant devenu si familier.

Le livre débute par quelques chapitres d'introduction vraiment excellents avant d'entamer une liste tout aussi excellente de Bad Smells (destinée à mettre le doigt sur les endroits où un refactoring s'impose). Arrive ensuite le coeur du livre un catalogue de refactorings qui va nous permettre de remédier à tout cela.

Pour chaque refactoring, un exemple en Java est présenté ainsi que les différentes étapes pour mener à bien ce refactoring. Ces étapes sont de très bas niveau et tellement évidentes que vous serez probablement tenté de les survoler. Pourtant, travailler de la sorte en baby steps, c'est la garantie qu'à tout moment, le code continue de fonctionner. Cela diffère de l'approche qu'on connait tous, où, par un soudain excès de confiance, une grande partie de code est modifiée, avec l'application qui cesse de fonctionner le temps des changements, au risque de ne plus fonctionner du tout....

Le livre achevé, on peut se dire que le contenu est vraiment simpliste mais en prenant un peu de recul, on mesure pleinement le potentiel du refactoring. Associé aux tests unitaires que Martin Fowler présente également à travers JUnit, le refactoring est redoutable d'efficacité avec le fameux "TDD mantra" red/green/refactor.

