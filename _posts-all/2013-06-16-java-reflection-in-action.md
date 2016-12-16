---
layout: post-read
title: 'Java Reflection in Action'
author: 'Julien Sobczak'
date: '2013-06-16T09:00:00.002+02:00'
categories: read
tags:
- java
image: 'http://d.gr-assets.com/books/1328837424l/1665018.jpg'
read_authors: 'Ira R. Forman, Nate Forman'
read_note: 15
read_date_published: '2004-10-1'
read_book_format: 'Paperback'
read_isbn: '1932394184'
read_number_of_pages: 273
read_roti: 4
read_time: 15
read_headline: "Un livre complet et abordable sur une API incontournable souvent méconnue."
link_amazon: "http://www.amazon.com/gp/product/1932394184/"
link_goodreads: "http://www.goodreads.com/book/show/1665018.Java_Reflection_in_Action"
---


Peu de livre aborde le sujet de la réflection. Pourtant, cela n'en reste pas moins un sujet intéressant. *Java Reflection in Action*, à travers de nombreux cas pratiques, montre l'utilité d'une API de réflection pour répondre à des besoins courants (loggers, converters, IOC container...), qui, sans une telle API, serait difficilement résolus de manière satisfaisante. D'un autre côté, il faut reconnaître que la plupart de ces problèmes sont affrontés par les frameworks que nous utilisons couramment (Hibernate, LogBack, Spring, ...) et que la nécessité de recourir à cette partie de l'API Java reste marginale.

Néanmois, si le cas de figure se présente, il a fort à parier que ce livre se révèle être d'une aide précieuse. Un exemple, l'objet Class propose deux méthodes getDeclaredMethods() et getMethods(). La première retourne toutes les méthodes déclarées par la classe courante, indépendamment de la visibilité des méthodes alors que la seconde retourne l'ensemble des méthodes déclarées et héritées mais de visibilité publiques uniquement. Cela est bien souligné dans la Javadoc. Toutefois, n'est-il pas plus judicieux de découvrir l'API à travers des exemples qui soulignent les particularités de l'API plutôt qu'en parcourant cette Javadoc à chaque question ou problème rencontré. Le livre met également en avant les limites de l'API notamment en terme d'intercession, c'est-à-dire les modifications possibles permettant de modifier la définition ou le comportement des objets. Il n'est, par exemple, pas possible d'ajouter dynamiquement une méthode à une classe, contrairement à d'autres langages comme Ruby.

En résumé, un livre bien écrit, très facile à comprendre mais réservé à ceux curieux de comprendre les subtilités de l'API ou ceux cherchant à découvrir l'utilité d'une telle API. Pour approfondir davantage les notions de réflection, le livre *Putting Metaclasses to Work* écrit par l'un des deux auteurs est conseillé, notamment par le créateur du langage Python, Guido van Rossum, comme en témoigne son commentaire sur Amazon.com.

