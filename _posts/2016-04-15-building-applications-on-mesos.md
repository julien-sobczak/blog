---
layout: post-read
title: "Building Applications on Mesos: Leveraging Resilient, Scalable, and Distributed Systems"
shortTitle: "Building Applications on Mesos"
author: Julien Sobczak
date: '2016-04-15'
category: read
subject: Apache Mesos
headline: Valuable advices targeted to Mesos framework developers delivered in a poorly edited book
note: 8
tags:
  - data
  - architecture
image: 'https://images.gr-assets.com/books/1450041191l/27015346.jpg'
metadata:
  authors: David Greenberg
  publisher: "O'Reilly Media"
  datePublished: '2016-01-01'
  bookFormat: 'Paperback'
  isbn: '149192652X'
  numberOfPages: 164
links:
  amazon: 'https://www.amazon.com/Building-Applications-Mesos-Leveraging-Distributed/dp/149192652X/'
  goodreads: 'https://www.goodreads.com/book/show/27015346-building-applications-on-mesos'
---

Recently, Apache Mesos received a lot of attention, following the hype around containerization. With *Building Applications on Mesos*, O'Reilly and author David Greenberg succeed in publishing the first book on the subject but fails to deliver some of its promises.

The book perfectly introduces the framework by telling its history, why it was created and examples of company like Twitter who use it. It covers the two most popular framework above Mesos: Marathon and Chronos and quickly delves into building your own framework. But in such a thin book (140 pages), the author could only scratch the surface of these subjects. At the end of the book, you will have a good idea of what it means to work with Mesos to host your applications or to create a new framework but you will miss the big picture necessary to fully grasp the potential of the framework. Too often, the author could not resist the urge to talk about useless technical details. The overall style of the book is more like a list of key points than a technical book.

That being said, *Building applications on Mesos* is a good collection of information and if you plan to build a new production-ready framework on top of Mesos, this book will help you grasp the core concepts of the Mesos API. In contrast, if you plan to deploy a Mesos cluster to manage your datacenter, you should consider most recent books such as *Mesos in Action* (Manning).
