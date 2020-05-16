---
layout: post-read
title: "Book Review: Software Engineering at Google: Lessons Learned from Programming Over Time"
shortTitle: "Software Engineering at Google"
author: Julien Sobczak
date: '2020-04-05'
category: read
subject: Software Engineering
headline: Following the success of the SRE book series, an inside look on the other side of the looking-glass.
note: 15
stars: 4
tags:
  - tools
image: 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1576579607l/48816586.jpg'
metadata:
  authors: Titus Winters, Tom Manshreck, Hyrum Wright
  publisher: "O'Reilly Media"
  datePublished: '2020-03-17'
  isbn: '1492082791'
  numberOfPages: 602
links:
  amazon: 'https://www.amazon.com/gp/product/1492082791/'
  goodreads: 'https://www.goodreads.com/book/show/48816586-software-engineering-at-google'
  goodreads_review: 'https://www.goodreads.com/review/show/3339563138'
---

Google is unique and few companies have to address engineering problems at Google scale. All programmers, however, will learn valuable lessons acquired during two decades where Google built some of the most innovative applications, and the underlying platform to make them come to life.

The book reintroduces the term engineering with a new definition: programming integrated over time, or how to make software programs stand the test of time. You will find in this book how tens of thousands of engineers collaborates across the same codebase, in an quite unusual way.

The first part is relatively short and focuses on Google engineering culture.

The second part is about processes and presents common software development practices, like automated testing. I found few things that are not already discussed elsewhere in the literature, even if Google’s scale presents new challenges. These chapters are extremely well written and clarify many misunderstood points like the usage of test doubles. I hope that having Google printed on the book cover helps those practices spread even further.

The last part is about internal tools used by Googlers. This is the largest part, and also the part I found the most interesting. The chapter on dependency management is really excellent and does a remarkable job in introducing their monorepo approach. More diagrams, screenshots, or pictures (like a Testing on the Toilet flyer) would have been appreciated (especially concerning the chapters about CI/CD and large-scale changes).

It’s a large book with almost no code, as it has more to do with engineering than programming. It’s a book about Google. You may not want to apply the same techniques in your organization, and that’s totally fine. But you cannot ignore fresh perspectives on our discipline to help us deliver even better software. I liked this book and I would like other large-scale companies to put on paper their practices too.