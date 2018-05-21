---
layout: post-read
title: "Book Review: Systems Performance: Enterprise and the Cloud"
shortTitle: "Systems Performance"
author: Julien Sobczak
date: '2017-05-07'
category: read
subject: Systems Performance
headline: ???
note: 15
tags:
  - performance
image: 'https://images.gr-assets.com/books/1372681832l/18058001.jpg'
metadata:
  authors: Brendan Gregg
  publisher: "Prentice Hall"
  datePublished: '2013-10-26'
  isbn: '0133390098'
  numberOfPages: 735
links:
  amazon: 'https://www.amazon.com/gp/product/0133390098/'
  goodreads: 'https://www.goodreads.com/book/show/18058001-systems-performance'
---

The main focus of this book is the study of systems performance, with tools, examples, and tunable parameters from Linux- and Solaris-based operating systems used as examples.

Many performance features for Linux covered in this book have been developed in the past five years 

Does it cover the background behind each tool? (concept)  yes. Chapters 1 to 4 cover essential backgrounds and latter chapters focus on specific topics (CPU, memory, file system, disk, network, cloud). 
Is that a reference book? Maybe not. Advanced performance analysis topics are summarized so that you are aware of their existence and can then study them from additional sources. Maybe yes. [This book has been written to provide value for many years, by focusing on background and methodologies for the systems performance analyst.] Chapters are splitted in two parts: theory and implementation. The latter will become out-of-date, but will still be useful as examples. 
Does it help is Solving performance of Virtual Machine-based languages? 

The author is the lead performance engineer at a cloud computing provider (Joyent), and writes the book primarily for systems administrators, but developers (DevOps or SRE)  will find the book valuable too. 

CPU, memory, file system, disk, network. Each chapter consists of five parts, the first three (concepts and architecture) providing the basis and the last two (commands and tuning) showing its practical application to Linux- and Solaris-based systems. 

A straight to the goal style, a highly structured book. The perfect book to start on the subject of system performance. List many commands but not many examples of each of them. Do not contains too much commands (you will have to investigate by yourself but resources are numerous online). The DTrace use is a advanced. 

The books ends with a case study that provides an over-the-shoulder view of how  performance engineers approaches an issue, and glues together the book content by showing how tools and metholodoes applies in practice. 
