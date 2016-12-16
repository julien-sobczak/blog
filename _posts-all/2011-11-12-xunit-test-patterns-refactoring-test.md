---
layout: post-read
title: 'xUnit Test Patterns: Refactoring Test Code'
author: 'Julien Sobczak'
date: '2011-11-12T09:00:00.002+02:00'
categories: read
tags:
- design-patterns
- testing
image: 'http://d.gr-assets.com/books/1348288284l/337302.jpg'
read_authors: 'Gerard Meszaros'
read_note: 16
read_date_published: '2007-05-21'
read_book_format: 'Hardcover'
read_isbn: '0131495054'
read_number_of_pages: 944
read_roti: 5
read_time: 15
read_headline: "Un des livres qui s'est avéré le plus pratique dans mon travail. Il s'agit d'une vraie référence sur son sujet mais ne s'attaque pas toutes les problématiques de tests automatisés comme le travail sur du code legacy. Un livre indispensable pour enfin écrire des tests qui documentent votre code !"
link_amazon: "http://www.amazon.com/gp/product/0131495054/"
link_goodreads: "http://www.goodreads.com/book/show/337302.xUnit_Test_Patterns"
---


Peu de livres auront changé notablement ma manière de coder. <br/> xUnit Test Patterns en fait partie. J'ai constaté une réelle différence sur ma manière de voir et d'écrire mes tests unitaires, ou plus généralement, mes tests automatisés avec JUnit. Le catalogue de patterns est complet et très clair. Le sujet n'est pas non plus très compliqué mais il faut bien reconnaître que le travail de Gerard Meszaros est remarquable.

L'organisation du livre n'est pas sans rappeler d'autres livres comme of EAA (pour la première partie plus narrative) ou Refactoring (pour les "test smells" qui rappellent les fameux "code smells").

Le contenu du livre est très varié et contient une partie forte intéressante qui clarifie et définit des termes parfois mal utilisés Test Double, Stub, Spy, Mock, Fake. Le livre s'aventure même dans des patterns utilisés par les frameworks de test. Instructif sans être indispensable.

Un des manques du livre, c'est l'absence de patterns autour de l'utilisation des mocks (Mockito, JMock, etc), car en pratique, ces frameworks indispensables, rendent parfois les tests difficilement maintenables. D'un autre côté, le problème provient souvent d'une violation du principe SRP qu'aucun pattern ne pourra venir compenser.

Le principal problème du livre vient de sa taille. 800 pages, c'est long. Surtout si vous lisez le livre du début à la fin, car comme tout catalogue de patterns, les répétitions sont choses courantes, ce qui peut, soit ennuyer, soit aider à mieux retenir :).

