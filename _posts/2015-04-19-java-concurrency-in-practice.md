---
layout: post-read
title: Java Concurrency in Practice
author: Julien Sobczak
date: '2015-04-19'
categories: read
tags:
- java
- performance
image: 'http://d.gr-assets.com/books/1349044077l/127932.jpg'
read_authors: Brian Goetz, Tim Peierls, Joshua Bloch, Joseph Bowbeer, David Holmes, Doug Lea
read_note: 19
read_roti: 5
read_time: 15
read_publisher: 'Addison-Wesley Professional'
read_date_published: '2006-05-1'
read_book_format: 'Paperback'
read_isbn: '0321349601'
read_number_of_pages: 403
read_headline: java.util.concurrent demystified by its creators. One of my top 3 most important book on the Java language.
link_goodreads: 'http://www.goodreads.com/book/show/127932.Java_Concurrency_in_Practice'
link_amazon: 'http://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601/'
---

Does anyone ever try to write concurrent code and looks their code does weird things in production, at the worst possible time, under heavy load? With *Java Concurrency in Practice*, this time is over, at least for us, the fortunate readers of this exceptional book.

When *Java Concurrency in Practice* was published, multicore processors was just becoming inexpensive enough for desktop systems. Today, multicore processors are present everywhere, even in our smartphones. So, we have no choice but learn the principles of concurrent programming.

The authors are uniquely qualified to write about the topic. Brian Goetz and all the authors are the primary members of the JCP Expert Group that created these facilities. Moreover, the authors do an excellent job of explaining in a clear manner a subject considered as a subject for advanced users only. With this book, novice programmers on the subject (like me) will be confident in writing concurrent code.

To give you a glimpse of the content:

- Part I: Fundamentals. You will learn the basic concepts: thread safely, immutability, safe publication, and the creation of thread-safe class by composing existing thread-safe building blocks.
- Part II: Structuring Concurrent Applications. You will learn how concurrency improves the throughput and responsiveness of your applications by executing and scheduling tasks concurrently.
- Part III: Liveness, Performance, and Testing. You will learn how to ensure that concurrent programs do what their are expected to do with acceptable performance.
- Part IV: Advanced Topics. The most experienced readers will learn more about atomic variables, non blocking algorithms and creating their own synchronizers.

What I love the most about this book is the numerous examples of "bad" code and how the authors rework them to do what they are initially supposed to do. Learning is so much easier that way. Moreover, no prior concurrent programming experience is required.

Finally, Java Concurrency in Practice is well written, probably one of the best technical book ever published. Too often, technical books confused the readers as soon the difficulty rises. This book is an exception, being enjoyable to read and always clear and to the point.

A very important book. Everyone should (re-)read it.