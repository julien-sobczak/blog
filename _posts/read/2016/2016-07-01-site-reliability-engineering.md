---
layout: post-read
title: "Book Review: Site Reliability Engineering: How Google Runs Production Systems"
shortTitle: Site Reliability Engineering
author: Julien Sobczak
date: '2016-07-01'
category: read
subject: Reliability
headline: Fantastic contribution to the operational field. One of the most important book published the last years
note: 18
stars: 5
tags:
  - devops
  - architecture
image: 'https://images.gr-assets.com/books/1459115220l/27968891.jpg'
metadata:
  authors: Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy
  publisher: O'Reilly Media
  datePublished: '2016-04-16'
  bookFormat: 'Paperback'
  isbn: '149192912X'
  numberOfPages: 552
links:
  amazon: 'https://www.amazon.com/gp/product/149192912X/'
  goodreads: 'https://www.goodreads.com/book/show/27968891-site-reliability-engineering'
---

In this collection of essays and articles, key members of Google's Site Reliability Engineering teams explain how they build, deploy, monitor and maintain large scale and ever changing applications like Gmail with great reliability.

What really surprise me is the openness of the authors. I was afraid of a highly theorical book, not delving enough inside the Google infrastructure. I was definitely wrong. This book offers a true immersion inside the Google infrastructure: how the hardware and software architecture looks like, the technologies and projects developed internally (outage tracker, time series database Borgmon, cluster operating systems such as Borg, Omega, etc).

One could argue that the content is of little interest in practice for most of us but the Docker/Mesos/Kubernetes' unprecedented popularity suggest the opposite. Furthermore, this book is not about targeting a 100% SLA. As the authors mention, 100% is the wrong reliability target for basically everything. With this book, you will learn the principles, practices and patterns - architectural and cultural - to run your application to the reliability target matching the profile of your service.

Organized like a conference proceedings where each chapter is written by a different author, I found the book remarkably edited. You could read it in any particular order or even not read the whole book but if, like, me, you decide to read it cover to cover, you will enjoy a pleasant reading.

The only word of caution: the second half of the book requires higher technical knowledge. For example, the chapter on distributed consensus algorithms (Paxos) is very detailed but not always easy to follow for someone new to distributed systems, but if you take the time to read it at your own pace, the results are worth it. A must-read book!
