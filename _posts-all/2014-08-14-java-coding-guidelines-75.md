---
layout: post-read
title: 'Java Coding Guidelines: 75 Recommendations for Reliable and Secure Programs'
author: 'Julien Sobczak'
date: '2014-08-14T09:00:00.002+02:00'
categories: read
tags:
- security
- java
- clean-code
image: 'http://d.gr-assets.com/books/1375059831l/17350057.jpg'
read_authors: 'Fred Long, Dhruv Mohindra, Robert C. Seacord, Dean F. Sutherland, David Svoboda'
read_note: 13
read_date_published: '2013-08-30'
read_book_format: 'Paperback'
read_isbn: '032193315X'
read_number_of_pages: 277
read_roti: 3
read_time: 5
read_headline: "Une lecture abordable pour sensibiliser et initier les développeurs Java la sécurité."
read_publisher: Addison-Wesley Professional
link_amazon: "http://www.amazon.com/gp/product/032193315X/"
link_goodreads: "http://www.goodreads.com/book/show/17350057-java-coding-guidelines"
---


75 guidelines pour accroître la sécurité de vos programmes Java.

Quelques généralités (ex SQL Injection). Quelques points plus pointus (ex Security Manager). L'accent est mis sur la sécurité mais également sur l'écriture de code robuste, fiable, et tout aussi maintenable (Difficile de sécuriser un code que l'on ne comprend pas).

Les exemples sont l'atout principal de ce livre. Les auteurs présentent à chaque fois des exemples "non-compliant" et "compliant". Tellement facile d'apprendre de cette manière. Les auteurs vont même jusqu'à nous exposer des exemples de failles du JDK et comment Oracle les résolues. Un vrai plus.

Les guidelines ne concernent pas du tuning de JVM ou d'infrastructures réseau. Elles concernent toutes l'écriture de code Java et on retrouvera de nombreux points en commun avec l'excellent [Effective Java]({% post_url 2009-04-10-effective-java-2nd-edition %}). Les guidelines reposent fortement sur *The CERT Oracle Secure Coding Standard for Java*, livre publié dans la même série ans plus tôt par ces mêmes auteurs dont le contenu est disponible [en ligne](https://www.securecoding.cert.org/confluence/display/java/The+CERT+Oracle+Secure+Coding+Standard+for+Java.).

Contrairement à d'autres avis, *Java Coding Guidelines* s'adresse selon moi exclusivement à des développeurs Java. Les guidelines conduisent souvent à recommander telle classe en défaveur d'une autre, ou dépendent du fonctionnement de la JVM. Oui, les idées sont généralisables à d'autres langages mais j'imagine qu'il a d'autres supports tout aussi réussis qui leurs sont consacrés.

