---
layout: post-read
title: 'Naked Objects'
author: 'Julien Sobczak'
date: '2013-10-02T09:00:00.002+02:00'
categories: read
tags:
read_authors: 'Richard Pawson'
read_note: 10
read_date_published: '2004-06-01'
read_number_of_pages: 223
read_roti: 2
read_time: 6
read_headline: "Une thèse assez digeste sur une idée originale."
---


Des entités, contenant uniquement des propriétés sans aucun comportement, manipulées par des services qui viennent les modifier à travers les accesseurs, çà vous parle La réponse est tristement oui. Martin Fowler introduit le nom de "Anemic domain model" pour décrire cette situation. Richard Pawson part du même constat et tente de comprendre les raisons qui ont conduit à en arriver là afin de proposer une approche nouvelle les Naked Objects.

Richard Pawson présente une approche où l'intégralité du code réside dans la couche domaine composée d'entités et de value objects. L'interface découle ensuite de ces objets et c'est là qu'un framework comme Apache Isis prend tout son sens. Je ne vais pas rentrer dans les détails mais pour donner une brève idée, il faut imaginer chaque entité représentée par une icône et chacune de ses méthodes devient une entrée du menu contextuel de l'icône. Les entités contiennent la logique métier comme le préconise une approche DDD. Cette génération des IHMs est assez surprenante mais je reste perplexe quant à son utilité. D'autres livres comme About Face me laisse penser que cela ne peut pas être la solution. La thèse le souligne d'ailleurs en détaillant les conditions favorables à cette approche et présente quelques projets où l'approche été conduite avec succès. Des études ont été menées sur les personnes impliqués sur ces projets (utilisateurs, développeur, etc) et les résultats sont très positifs. vous de vous faire votre propre avis.

Terminons en ajoutant que la préface est écrite par Trygve Reenskaug, à l'origine du pattern MVC et que Richard Pawson co-écrit peu de temps après un livre homonyme sur le sujet.

