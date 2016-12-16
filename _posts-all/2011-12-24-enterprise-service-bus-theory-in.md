---
layout: post-read
title: 'Enterprise Service Bus: Theory in Practice'
author: 'Julien Sobczak'
date: '2011-12-24T09:00:00.002+02:00'
categories: read
tags:
- architecture
- soa
image: 'http://d.gr-assets.com/books/1328834348l/853977.jpg'
read_authors: 'David Chappell'
read_note: 9
read_date_published: '2004-07-2'
read_book_format: 'Paperback'
read_isbn: '0596006756'
read_number_of_pages: 276
read_roti: 2
read_time: 12
read_headline: "Le livre l'origine des ESBs. Peu convaincant, peu complet mais pas mal dépassé. Le livre ne mérite probablement pas le détour aujourd'hui."
link_amazon: "http://www.amazon.com/gp/product/0596006756/"
link_goodreads: "http://www.goodreads.com/book/show/853977.Enterprise_Service_Bus"
---


David Chappell, responsable SOA chez Oracle à l'époque, nous livre ici le tout premier livre à introduire véritablement les ESBs.

Après les échecs de Corba, RMI, et en s'appuyant sur les technologies actuelles de l'époque comme les JMS ou les WebServices, l'ESB s'annonce (en 2004) comme la solution tant attendue en matière d'intégration entre applications. Du moins, c'est ce que David Chappell veut que l'on retienne car en pratique, Enterprise Service Bus: Theory in Practice n'est guère convaincant. Beaucoup trop vendeur (les développeurs ne sont clairement pas une cible potentielle). Méfiance donc. Surtout qu'avant d'intégrer un ESB, je ne sais pas vous mais pour ma part, j'ai surtout besoin de comprendre ses limitations. L'auteur ne joue clairement pas le jeu sur ce point. Dommage. Il faudra se tourner par exemple sur la formidable présentation de Martin Fowler et Jim Webber au QCon 2008 [Does My Bus Look Big in This?]({% post_url 2014-02-07-does-my-bus-look-big-in-this %}) pour se faire une idée.

On peut souligner que l'auteur travaillé avec Gregory Hohpe, auteur de [Enterprise Integration Patterns]({% post_url 2012-05-30-enterprise-integration-patterns %}), publié quelques mois auparavant, de manière à avoir un vocabulaire commun. Un point appréciable pour le lecteur qui méritait d'être souligné.

10 années se sont presque écoulées depuis la parution de ce livre. Est-ce les ESB ont tenu leurs promesses Pas forcément mais une chose est sûre bon nombre d'entreprises ont suivi ou suivent seulement cette voie. Mais est-ce vraiment la voie à suivre ?

Il est facile de trouver des avantages à un ESB. Mais cela ne dispense pas de s'intéresser aux solutions alternatives. [Domain-Driven Design]({% post_url 2012-10-19-domain-driven-design-tackling %}) vous fera douter des Canonical Data Model, si important dans une approche SOA classique avec ESB. Les [MicroServices](http://martinfowler.com/articles/microservices.html) basés sur une [intégration par REST]({% post_url 2013-07-30-rest-in-practice %}), fortement découplés, ne sont-ils pas plus séduisants A vous d'en juger. L'essentiel est de faire un choix informé.

