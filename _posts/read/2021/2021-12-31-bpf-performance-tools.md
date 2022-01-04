---
layout: post-read
title: "Book Review: BPF Performance Tools"
shortTitle: "BPF Performance Tools"
author: Julien Sobczak
date: '2021-12-31'
category: read
subject: Linux
headline: Linux performance analysis made easier
note: 15
stars: 4
tags:
  - devops
unofficialTags:
  - performance
image: 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1563239967l/51635102._SX318_SY475_.jpg'
metadata:
  authors: Brendan Gregg
  publisher: "Addison-Wesley Professional"
  datePublished: '2019-12-23'
  isbn: '0136554822'
  numberOfPages: 880
links:
  amazon: 'https://www.amazon.com/gp/product/0136554822/'
  goodreads: 'https://www.goodreads.com/book/show/51635102-bpf-performance-tools'
  goodreads_review: 'https://www.goodreads.com/review/show/4449015301'
---

eBPF is gaining more and more attention for good reasons. eBPF turns Linux into a "programmable" kernel, improving its observability, networking, and security.

If you work closely with Linux systems, learning about eBPF is indispensable, and _BPF Performance Tools_ is the best resource. This book is written by Brendan Gregg, one of the main contributors on this subject, and author of the excellent _Systems Performance_.

The first part is an introduction to eBFP to understand its history and how it works under the hood. The second part is by far the largest one. It contains one or several chapters for every topic—CPUs, memory, filesystems, disk I/Os, networking, security, languages, applications, containers, and hypervisors. Each chapter starts with a gentle introduction, before introducing the traditional Linux commands and the BPF tools that complement them.

As a software developer, I found the book easy to follow, even without a solid background in Linux programming. The explanations are concise, clear, and remarkably illustrated. The commands used in examples are well-chosen and the comments really help to understand their output.

This book was invaluable during my last performance issues. Running commands to debug issues is easy. Knowing which command to run and understanding which statistics to read is far more challenging. This book will help you too.
