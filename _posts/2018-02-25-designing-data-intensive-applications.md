---
layout: post-read
title: "Book Review: Designing Data-Intensive Applications"
shortTitle: "Designing Data-Intensive Applications"
author: Julien Sobczak
date: '2018-02-25'
category: read
subject: Data
headline: Undeniably one of the best books published in the last years
note: 19
tags:
  - data
  - architecture
image: 'https://images.gr-assets.com/books/1415816873l/23463279.jpg'
metadata:
  authors: Martin Kleppmann
  publisher: "O'Reilly"
  numberOfPages: 562
links:
  amazon: 'https://www.amazon.com/s/'
  amazon_review: 'https://www.amazon.com/review/R34HPJHT4Y1FAG/'
  goodreads: 'https://www.goodreads.com/book/show/23463279-designing-data-intensive-applications'
---

You probably don't need to know the underlying implementation details to use relational and distributed databases, but as data volume increases, using the right product in the right way could really make the difference. Armed with the knowledge present in this book, you will be in a better position to understand the compromises behind each solution (single-leader vs leaderless replication, which transactional isolation level, consistency vs availability, consensus algorithms), and almost all, how to combine them to solve complex problems.

Clearly, *Designing Data-Intensive Applications* ranks among the best publications in the last decade. There is so much experiences and personal researches distilled in a remarkably written book that it would be unconceivable not to devote just a few hours of your time to read it. The book really fills a gap in the literature. There are so many books to explain why you should choose such storage system and how to use it. With *Designing Data-Intensive Applications*, you get a solid understanding of decades of researches (including SSTables, LVM, Paxos) in an approachable manner, and in just one book.

It's a highly theoretical book with almost no details about how to use existing technologies; that is in my opinion, a really good point. The book is here to stay a long time on our bookshelves. It would have been so easy to spend pages explaining how to use technologies, but Martin Kleppmann chose the hard path by focusing on the timeless principles, using only famous products to discuss algorithms and their tradeoffs. In the end, the book help you develop a good intuition for how these systems are working under the hood.

This book have to be read carefully, cover to cover (and probably several times) to get through the vast and rich content. A required reading for every backend developer of scalable, highly available applications facing a high volume of data (web, mobile apps, IoT), or just because you are curious about how most popular websites serve billions of customers daily.

A last word to say drawings/maps at the start of each chapter are just incredible, and while not indispensable, these drawings reflect the devotion of the author to publish one of the most successful technical books I had the opportunity to read.
