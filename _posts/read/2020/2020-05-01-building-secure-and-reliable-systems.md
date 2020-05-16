---
layout: post-read
title: "Book Review: Building Secure and Reliable Systems: Best Practices for Designing, Implementing, and Maintaining Systems"
shortTitle: "Building Secure and Reliable Systems"
author: Julien Sobczak
date: '2020-05-01'
category: read
subject: Security
headline: The SRE book series welcomes a long-awaited guest to the party.
note: 12
stars: 3
tags:
  - architecture
image: 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1583200803l/52362720.jpg'
metadata:
  authors: Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield
  publisher: "O'Reilly Media"
  datePublished: '2020-03-31'
  isbn: '1492083127'
  numberOfPages: 541
links:
  amazon: 'https://www.amazon.com/gp/product/1492083127/'
  goodreads: 'https://www.goodreads.com/book/show/52362720-building-secure-and-reliable-systems'
  goodreads_review: 'https://www.goodreads.com/review/show/3339604076'
---

Google fills a gap in its SRE book series by integrating security into the reliability equation. As a reliable system is only  useful as long as its security is guaranteed, if you have read the SRE book(s), you should definitely read this one too. But I admit I didn’t like it as much as its predecessors. 

The format is similar to other Google’s SRE books (we can also cite _Software Engineering at Google_). We retrieve a clear separation between principles and practices. The book contributors capture how security is managed at Google but present solutions in a way that makes it possible to adapt to your infrastructure, context, and culture. But the devil is in the details.

The first problem is that by trying to abstract principles in the second part, I found chapters suffer from a lack of clarity, which impedes comprehension. That’s bad. The subjects covered by those chapters are important and you will find valuable insights, but their development is too long, too verbose. Even if there are more practical sections later in the book to illustrate these principles, I don’t think it’s acceptable to depend on later chapters to clarify the meaning. I consider it would not be a problem to put more explanations about how it works at Google even in the most abstract chapters. It will not make the book less widely applicable, quite the contrary.

The second problem concerns the scope that is probably too large. The book is massive with almost 600 pages but I think editors must have had a hard time deciding what to include, and what to leave out. They decided to focus on building secure applications. You will not find much information about network or physical security in this book. But nevertheless, it’s still too much for a single book when you have so much to bring to the table as Google has.

Don't get me wrong. This book is a great addition in the software literature. It contains many valuable lessons. I appreciate how the book draws the parallel between security and reliability, two disciplines that don't have to be treated separately. It’s just that I found this book not as great as previous Google's books.
