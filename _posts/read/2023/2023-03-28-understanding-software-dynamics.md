---
layout: post-read
title: "Book Review: Understanding Software Dynamics"
shortTitle: "Understanding Software Dynamics"
author: Julien Sobczak
date: '2023-03-28'
category: read
subject: Performance
headline: Lessons learned after 55 years spent living at the intersection of hardware and software.
note: 17
stars: 4
tags: []
image: /posts_resources/covers/understanding-software-dynamics.png
metadata:
  authors: "Richard L. Sites"
  isbn: '9780137589739'
---

Software has rarely demonstrated the same gain of performance as hardware. Understanding the performance of complex software is difficult. "Without a good picture of reality, programmers are reduced to guessing and _trying things_ to reduce long delays and improve performance," declares the author. "This book is about not guessing, but knowing."

The author has worked with giants such as Frances Allen, Fred Brooks, John Cocke, and Don Knuth and has co-designed the DEC industry, worked on Adobe Photoshop and improved the performance of Google services like Gmail. It's one of these rare books that result from a unique experience of more than five decades at the intersection of hardware and software. For sure one of the most important programming books published in the last decade. For a limited audience…

You will learn what happens when you run instructions on a CPU that read and write from memory, disks or the network, from the lowest viewpoint, and most importantly, how to reason when facing a problem affecting the long tail latency (= the few abnormal slow requests) using common commands, logging, profiling, and tracing. Examples are written in C or C++ and running on Linux. Not all code examples are included in the text and must be downloaded, which sometimes makes comprehension difficult.

This book is a great complement to _Systems Performance_ by Brendan Gregg. It's (maybe) less practical but (maybe) more timeless as more focused on principles than the tools at hand. A great book for curious developers and an indispensable resource for performance engineers.
    