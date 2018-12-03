---
layout: post-read
title: "Book Review: Hadoop: The Definitive Guide"
shortTitle: "Hadoop: The Definitive Guide"
author: Julien Sobczak
date: '2015-12-19'
category: read
subject: Hadoop
headline: Excellent style, clear and understandable examples. Useful both as a guide and as a reference. Still the best book on Hadoop
note: 15
tags:
  - data
unofficialTags:
  - big-data
image: 'https://images.gr-assets.com/books/1470664545l/31372333.jpg'
metadata:
  authors: Tom White
  publisher: "O'Reilly"
  bookFormat: 'Hardcover'
  isbn: '9781491901'
  numberOfPages: 756
links:
  amazon: 'https://www.amazon.com/Hadoop-Definitive-Storage-Analysis-Internet/dp/1491901632/'
  goodreads: 'https://www.goodreads.com/book/show/31372333-hadoop'
---

I feel lost when I started to learn Hadoop. It's inner workings seems complex, a mixture of distributed systems theory and practical engineering. But it doesn't need to be like this. This book aims to help the beginners understand what the technology is capable of, where it excels and how to use it and the numerous tools built on top of it (Hive, HBase, Spark, Flume, ...).

The book is divided into five main parts: Parts I to III are about core Hadoop, Part IV covers related projects in the Hadoop ecosystem, and Part V contains Hadoop case studies. I really appreciate the gentle introduction (chapter I) to the topic explaining what Hadoop is and is not compared to other technologies like database, grid computing, or volunteer computing. More generally, Part I is really excellent and provides a solid foundation of Hadoop.

I found the book particularly well-written for such a massive book. The author introduces each term at the right time even if the subject is covered extensively later in the book, and includes many helpful and relevant examples. He even explains log output. A very well edited book to read from cover to cover.

The fourth edition covers Hadoop 2 (Yarn) exclusively and includes two new case studies: one on how Hadoop is used in Heathcare systems, and another on using Hadoop technologies for genomics data processing. A really great way to close the book by providing a high-level view of the Hadoop ecosystem.

One downside I found is some chapters such as those on Pig and Hive are a little too long. As new tools emerges constantly in the Hadoop ecosystem, I think future editions of this book should stop covering these tools with this level of details. What would be more interesting are chapters organized by topic (batch processing, stream processing, CEP, security, governance, ...) and presenting the history and differences between the majors tools in each one of these domains, the pros and the cons related to each option, with some recommendations and best practices (what the book *Hadoop Application Architecture* try to do with moderate success).

In definitive, I strongly recommend this book especially for beginners that will learn the motivations behind Yarn, how MapReduce works under the hood, the principal configuration properties and when to customize them. You will also get a good overview of the Hadoop landscape, the beginning of a fascinating journey into the Hadoop world.
