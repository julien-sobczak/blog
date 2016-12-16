---
layout: post-read
title: 'Refactoring Databases: Evolutionary Database Design'
author: 'Julien Sobczak'
date: '2012-06-24T09:00:00.002+02:00'
categories: read
tags:
- refactoring
- database
image: 'http://d.gr-assets.com/books/1348015290l/161302.jpg'
read_authors: 'Scott W. Ambler, Pramod J. Sadalage'
read_note: 14
read_date_published: '2006-03-3'
read_book_format: 'Hardcover'
read_isbn: '0321293533'
read_number_of_pages: 384
read_roti: 4
read_time: 10
read_headline: "Un livre qui marque un tournant dans la communauté relationnelle. L'agilité travers le refactoring fait son entrée, mais si on tire un premier bilan après les quelques années écoulées depuis la parution de l'ouvrage, il faut reconnaître qu'il ne s'agit pas d'une entrée fracassante comme celle survenue dans le monde Java il a déjà plus de 10 ans."
link_amazon: "http://www.amazon.com/gp/product/0321293533/"
link_goodreads: "http://www.goodreads.com/book/show/161302.Refactoring_Databases"
---


Il aura fallu attendre ans après la parution du Refactoring de Martin Fowler pour que la communauté du monde relationnel réagisse avec la sortie de ce livre. *Refactoring Databases: Evolutionary Database Design* été l'élément déclencheur qui aidé au développement d'outils comme Liquibase ou Flyway et qui nous aide aujourd'hui à les utiliser correctement.

Les auteurs nous livrent ici les enseignements acquis durant des années à naviguer de part et d'autre de la séparation si forte en développeurs et DBAs. L'essentiel du livre est organisé logiquement sous forme d'un catalogue de refactorings/transformations (rename table, drop column, ...), pas forcément très plaisant à lire car on retrouve le style "baby steps" une succession d'étapes minuscules garantissant qu'entre chacune d'entre elles, tout continue de fonctionner. Cette partie fait davantage office de référence qu'on consultera de multiples fois au besoin.

Un des apports notables de ce livre est la reconnaissance que le schéma doit évoluer de manière incrémentale et itérative. Le monde Java aura su s'engouffrer dans la vague provoquée par l'agilité. Le monde relationnel, lui, préféré rester très procédural. Le refactoring de base de données est compliqué mais ce livre nous montre que c'est possible.

