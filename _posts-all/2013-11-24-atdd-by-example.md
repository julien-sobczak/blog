---
layout: post-read
title: 'ATDD by Example: A Practical Guide to Acceptance Test-Driven Development'
author: 'Julien Sobczak'
date: '2013-11-24T09:00:00.002+02:00'
categories: read
tags:
- agile
- testing
image: 'http://d.gr-assets.com/books/1355045558l/13705173.jpg'
read_authors: 'Markus Gärtner'
read_note: 10
read_date_published: '2012-06-26'
read_book_format: 'Paperback'
read_isbn: '0321784154'
read_number_of_pages: 212
read_roti: 3
read_time: 5
read_headline: "Un livre intéressant, qui présente beaucoup de notions différentes. Probablement le livre le plus rapide pour débuter mais pas indispensable"
link_amazon: "http://www.amazon.com/gp/product/0321784154/"
link_goodreads: "http://www.goodreads.com/book/show/13705173-atdd-by-example"
---


Le livre reprend les mêmes idées qui ont fait le succès de [TDD By Example]({% post_url 2011-10-18-test-driven-development-by-example %}) de Kent Beck mais en les appliquant à un sujet tout aussi important ATTD. Le livre de Kent Beck permet d'écrire un code simple et évolutif ("the code right") alors que le livre de Markus Gärtner vous aidera à écrire un code qui répond aux exigences fonctionnelles ("the right code").

Le livre est divisé en parties :

- Un premier exemple, sur la gestion des prix d'un parking d'aéroport, utilise Ruby et Cucumber branché directement sur l'IHM Web à l'aide de Selenium (en utilisant le Page Object Pattern qui ne sera pas cité avant les annexes...). Cet exemple montre également la collaboration entre le développeur, le testeur et l'expert métier à travers les Specification Workshops introduites par Gojko Adzic.

- Un second exemple, sur la gestion d'un feu tricolore en Allemagne, utilise Java et FitNesse, mais cette fois ci, branché sur les services. Le besoin, bien que plus poussé, présente moins de risque de confusion, et c'est l'occasion de mettre un peu de côté les Specification Workshops pour laisser entrevoir l'harmonie entre ATDD, TDD et Refactoring. Cela est très fait bien.

- Une troisième partie, bien plus théorique, où l'influence de Gokjo Adzic est une nouvelle fois omniprésente. Pour ceux qui ont déjà eu la chance de lire ses ouvrages, cette troisième partie se révélera décevante. Markus Gärtner reformule les mêmes idées de manière plus concise et pas toujours très claire. Cela me laisse perplexe sur l'intérêt de ces chapitres pour quelqu'un débutant sur le sujet. Contrairement aux deux exemples qui apportent un vrai plus pour débuter avec les tests d'acceptance, je pense qu'il est préférable de se tourner ensuite vers Bridging the communication Gap et d'ignorer cette troisième partie.

Un avantage du livre est de confronter plusieurs outils comme FitNesse et Cucumber et les différents formats d'exemple (Given-When-Then, Tabular, Keywork).

