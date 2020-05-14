---
layout: post-read
title: "Book Review: SonarQube in Action"
shortTitle: SonarQube in Action
author: Julien Sobczak
date: '2015-08-04'
category: read
subject: SonarQube
headline: A thorough, in-depth guide to Code Inspection with SonarQube
note: 17
stars: 4
tags:
  - tools
  - craftsmanship
image: 'https://d.gr-assets.com/books/1415174686l/23502608.jpg'
metadata:
  authors: Patroklos P. Papapetrou
  publisher: Manning Publications
  datePublished: '2013-04-28'
  bookFormat: 'Paperback'
  numberOfPages: 392
links:
  goodreads: 'https://www.goodreads.com/book/show/16028082-sonar-in-action'
  amazon: 'https://www.amazon.com/SonarQube-Action-G-Ann-Campbell/dp/1617290955/'
---

Could a book about a graphical tool like SonarQube be enjoyable to read? The answer is yes. *SonarQube in Action* is not a succession of screenshots explaining what each menu entry does but a book about code quality: why the quality is not an option but an essential factor for a project be successful, what are the metrics to collect. The book is organized around the Seven Axes of Quality, which are: potential bugs, coding rules, tests, duplications, comments, architecture and design, and complexity. But of course, *SonarQube in Action* is also about how SonarQube helps us to track these metrics and watch their evolutions

Written by two active members of the SonarQube project, their expertise serves to make this book a trusted reference. The authors share a lot of best practices, showing you how to exploit the tool to make it fit your context. They introduces numerous plugins after each chapter, doing an excellent job of putting them in context. Sonar integration with our CI Server, our IDE, and our security policy is discussed in detail.

The book devotes a whole chapter to writing your own plugin. However, the authors only scratches the surface of the topic. A discussion about the SSLR (SonarSource Language Recognizer) and how to make your own custom rules would have been welcome.

The only drawback is a book already outdated. The tool continues to evolve (multi-language support, departure from historical tools like PMD, FindBugs, Checkstyle toward the Sonar Way, new look-and-feel, ElasticSearch database to store file contents...).

In definitive, *SonarQube in Action* is not a manual or an administrative guide but a thorough introduction to Continuous Code Inspection with the best Open Source tool out there. I recommend it to any developer, tech leader, or project manager concerned about quality, but still not using SonarQube.
