---
layout: post-read
title: "Book Review: Pro Puppet"
shortTitle: "Pro Puppet"
author: Julien Sobczak
date: '2016-07-21'
category: read
subject: Puppet
headline: A messy collection of advanced Puppet code. Valuable information delivered in a poorly organized book
note: 5
tags:
  - devops
image: 'https://images.gr-assets.com/books/1379334130l/17919001.jpg'
metadata:
  authors: Spencer Krum, William Van Hevelingen, Ben Kero, James Turnbull, Jeffrey McCune
  publisher: 'Apress'
  datePublished: '2013-12-19'
  bookFormat: 'Paperback'
  isbn: '1430260408'
  numberOfPages: 332
links:
  amazon: 'https://www.amazon.com/gp/product/1430260408/'
  goodreads: 'https://www.goodreads.com/book/show/17919001-pro-puppet'
---

Let me lay it on the line, this book was a painful reading. Puppet was new to me and I know this is a "Pro" book but the description of the book mentions you don't need previous Puppet experience. That's not true!

*Pro Puppet* is a completely disorganized collection of code samples on advanced Puppet topics. There is almost no explanation or introduction text about the different concepts. For example, modules are introduced by showing the code of a Puppet module for SSH, Postfix, and MySQL. Moreover, you still doesn't have grasp the Puppet concepts that you are already installing an Apache server to scale Puppet using multiple masters behind a load balancer. That's not all. Explanations about related subjects such as Git or Apache are very laborious. The authors probably preferred avoid talking too much about these out of scope subjects but, in definitive, the reader with no prior experience on these topics will completely miss the point.

So, is this book useful to the experienced Puppet user? Maybe not...

One thing is certain, *Pro Puppet* covers many advanced topics like how to configure a randomized time between two Puppet agent refreshes to avoid overwhelming the Puppet master, how to scale your Puppet masters, how to configure monitoring with Nagios, and so on. But I do not recommend you to read Pro Puppet cover to cover but instead use it as a reference to find specific information.

This second edition was updated to cover the now obsolete Puppet 3, and clearly lacks a chapter on Puppet best practices like the Roles and Profiles pattern (Note: O'Reilly is publishing a new book on this subject). The covering of hiera files was surely a late addition to this book (this is the last chapter) and there is every reason to believe that the book was pushed to press before the upcoming Puppet 4 release.

In definitive, if you want to discover DevOps practices or to learn Puppet, this is definitely not the right book. If you want to expand your Puppet knowledge, it's our call but check the recent O'Reilly publications first (I do not have read them).
