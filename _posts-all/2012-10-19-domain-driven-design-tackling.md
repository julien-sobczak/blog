---
layout: post-read
title: 'Domain-Driven Design: Tackling Complexity in the Heart of Software'
author: 'Julien Sobczak'
date: '2012-10-19T09:00:00.002+02:00'
categories: read
tags:
- architecture
- classics
- ddd
image: 'http://d.gr-assets.com/books/1287493789l/179133.jpg'
read_authors: 'Eric Evans'
read_note: 18
read_date_published: '2003-08-20'
read_book_format: 'Hardcover'
read_isbn: '0321125215'
read_number_of_pages: 529
read_roti: 5
read_time: 25
read_headline: "Exceptionnel. Un livre pas suffisamment connu. Quand les grands noms citent leurs livres les plus influents, DDD répond toujours présent. Laissez vous intriguer par ce livre. Accrochez vous. La récompense n'en sera que plus grande !"
link_amazon: "http://www.amazon.com/gp/product/0321125215/"
link_goodreads: "http://www.goodreads.com/book/show/179133.Domain_Driven_Design"
---


Une fois ce livre achevé, on sait pertinemment qu'on ne concevra plus les applications de la même manière. L'approche Domain-Driven Design ne doit pas être appliquée dans tous les cas. Eric Evans est parfaitement clair sur ce point. Il sera toutefois très difficile d'oublier les idées de ce livre tant elles sont remarquables.

Le livre est présenté comme un catalogue de patterns mais bien moins structuré que les autres classiques. Ce choix judicieux permet d'introduire progressivement les grandes lignes de cette approche.

Dans [PoEAA]({% post_url 2011-01-28-patterns-of-enterprise-application %}), Martin Fowler nous présentait le pattern Domain Model, très répandu en Java. Trop souvent, ce même domaine présente les symptômes néfastes décrit toujours par ce même Martin Fowler, sous le nom de [Anemic domain model](http://www.martinfowler.com/bliki/AnemicDomainModel.html). Nos objets métiers deviennent POJO et nos services accueillent alors la logique métier. On connait tous cette approche procédurale qui, au final, ne nous aide pas à affronter la complexité du domaine métier.

Domain-Driven Design, c'est rendre à la programmation orientée-objet ses lettres de noblesse. La première partie consacrée aux Building Blocks (Value Object, Entity, Specification, Domain Service, Repository, etc) est incontournable. Tellement incontournable que bon nombre de lecteurs ne retiennent que cela alors que l'approche bien plus à nous offrir.

Dans un [talk du QCon 2009]({% post_url 2013-12-30-what-ive-learned-about-ddd-since-book %}), Eric Evans exprimait le regret de ne pas avoir commencé son ouvrage par l'autre partie Strategic Design. Grâce à des patterns comme Ubiquitous Language ou Bounded Context, l'approche DDD prend alors une toute autre dimension qui vous aide à modéliser la logique entre les différentes applications. 10 ans après la parution du livre, on continue de retrouver ces notions au coeur des architectures ROA comme les [MicroServices](http://martinfowler.com/articles/microservices.html). La preuve que le livre est plus que jamais d'actualité.

Malheureusement, Domain-Driven Design, n'est pas le livre le plus digeste, d'autant plus avec ses 500 pages. Face à l'importance du sujet, on oubliera ce petit détail et c'est changé qu'on reposera ce livre avec beaucoup de questions en suspens, notamment en terme d'implémentation. Il aura fallu attendre 10 ans pour que Vaughn Vernon répondent avec l'excellent [Implementing Domain-Driven Design]({% post_url 2013-04-04-implementing-domain-driven-design %}). Deux livres qui sont pour moi inséparables et incontournables.

