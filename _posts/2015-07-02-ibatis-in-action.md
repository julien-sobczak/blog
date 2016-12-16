---
layout: post-read
title: iBatis in Action
author: Julien Sobczak
date: '2015-07-02'
categories: read
tags:
- frameworks
- java
image: 'http://d.gr-assets.com/books/1442410340l/332070.jpg'
read_authors: Clinton Begin, Brandon Goodin, Larry Meadors
read_note: 12
read_roti: 3
read_time: 7
read_publisher: 'Manning Publications'
read_date_published: '2007-01-17'
read_book_format: 'Paperback'
read_isbn: '1932394826'
read_number_of_pages: 350
read_headline: Still a good reference to understand concepts behind MyBatis.
link_goodreads: 'http://www.goodreads.com/book/show/332070.iBatis_in_Action'
link_amazon: 'http://www.amazon.com/iBatis-Action-Clinton-Begin/dp/1932394826/'
---

Why read a book about a retired project today ? Because iBatis shares a lot with MyBatis, its successor : same developers and same initial codebase. This explains why no reference book was published about this new framework. So, *iBatis in Action*, written by the creators of the two frameworks, is probably the best resource if you want to have a solid knowledge about it.

The book is well organized. We begin with a good introduction to the framework and its motivations. The second part explains in detail the most important topic, how to map a Java method to a SQL query. The third part talks about advanced concepts like caching or related subjects like the pattern DAO. The last part presents best practices and the indispensable sample application to understand how iBatis fits in a typical web application.

*iBatis in Action* is relatively well-written, filled with dozen of examples. The audience is the Java developer having basic knowledge of SQL. No experience with an ORM or JDBC is expected (the authors explains the different transaction types, the ACID properties, the DAO pattern...). If these concepts are not new to you, you could safely skim over some parts of the book.

The less useful chapter is probably the one on best practices. These best practices are too general (write unit tests, respect naming conventions and good project organization) and will be only useful to a novice programmer. The last chapter presenting a fully working application was certainly very interesting when the book was publishing but today, we regret that the authors does not have made the good choice concerning the technologies used (Ant, Struts). A solution based on Maven/Spring would have better stood the test of time.

I found the two chapters about the pattern DAO too lengthy and lacking of subjectivity about technologies like Hibernate or Spring. The authors cite Hibernate several times in the book but does not provide a true comparison of the two approaches. The reader will have to resort on his own judgement for that. Not a bad thing in my opinion. The authors present also raw JDBC code without comparing the same code with the Spring `JDBCTemplate`, maybe the closest solution to iBatis.

In definitive, *iBatis in Action* was the reference guide of this popular framework. Now largely outdated, this book is still useful to gain insights about why this framework was born and how it does to offer a great alternative between pure JDBC and full ORM like Hibernate. But prepare you to skim most of the content.