---
layout: post-read
title: 'Programming Google App Engine, 2nd Edition'
author: 'Julien Sobczak'
date: '2014-06-27T09:00:00.002+02:00'
categories: read
tags:
- java
- cloud
- big-data
- performance
image: 'http://d.gr-assets.com/books/1350397226l/13218129.jpg'
read_authors: 'Dan Sanderson'
read_note: 10
read_date_published: '2012-10-26'
read_book_format: 'Paperback'
read_isbn: '144939826X'
read_number_of_pages: 538
read_roti: 3
read_time: 12
read_headline: "Un guide très pratique pour comprendre les particularités de la plateforme comme sa solution NoSQL Datastore. La référence."
read_publisher: Google Press
link_amazon: "http://www.amazon.com/gp/product/144939826X/"
link_goodreads: "http://www.goodreads.com/book/show/7244453-programming-google-app-engine"
---


Il est désormais possible et très facile de créer une application web qui peut scaler à des millions d'utilisateurs de manière transparente (sauf pour notre budget :). Google App Engine nous ouvre les portes des Data Centers de Google. Beaucoup de possibilités et aussi de nombreuses contraintes à commencer par les langages supportés par la plateforme.

*Programming Google App Engine* choisit de documenter les deux principaux à savoir Python et Java, au détriment du Go et plus récemment du PHP. Un choix logique de l'auteur pour ne pas allonger un livre déjà volumineux. L'auteur commence souvent par discuter des généralités avant de plonger dans les implémentations Python et Java qui se révèlent souvent bien différentes. On constate un vrai effort de la part des développeurs de proposer un framework qui colle aux "standards" du langage respect de la spécification WSGI en Python, ou de JPA en Java, etc. Il en résulte un livre qui se lit sans problème de bout en bout, même si on peut se contenter des sections spécifiques à son langage de prédilection. Cela ne nous dispensera pas des nombreuses répétitions dont souffre ce livre au sein même des parties indépendantes des langages. Un peu dommage.

*Programming Google App Engine* se révèle plus proche d'une référence (même si l'auteur nous redirige souvent vers la documentation en ligne) que d'un livre d'introduction. L'auteur n'hésite pas à nous livrer assez tôt chapitres consécutifs sur la solution NoSQL (semblable BigTable). Les différents services (UrlFetch, Task, ...) nous faisant oublier le côté sandbox de la solution sont ensuite passés au crible tout comme la partie déploiement et monitoring, véritable force de la plateforme.

