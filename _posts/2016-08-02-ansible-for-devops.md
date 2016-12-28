---
layout: post-read
title: "Ansible for DevOps"
author: Julien Sobczak
date: '2016-08-02'
category: read
subject: DevOps
headline: Learn Ansible and DevOps best practices with this well-written and technically excellent guide
note: 16
tags:
  - tool
  - devops
image: 'https://images.gr-assets.com/books/1444973445l/27111284.jpg'
metadata:
  authors: Jeff Geerling (Goodreads Author)
  publisher: 'Midwestern Mac, LLC'
  datePublished: '2015-10-10'
  bookFormat: 'Paperback'
  numberOfPages: 398
links:
  amazon: 'https://www.amazon.com/gp/search/'
  goodreads: 'https://www.goodreads.com/book/show/27111284-ansible-for-devops'
---

If you are interested in both development and operations, and have basic familiarity with the command line, *Ansible for DevOps* will provide you with a beginner to expert-level understanding of Ansible and how you can use it to manage your infrastructure.

One of Ansible's greatest strength is its exhaustive documentation. This book is meant as a supplement to it, providing an easy-to-follow step-by-step guide to learn this popular tool. The first 4 chapters (70 pages) are enough to get you started but remaining chapters are recommended to truly grasp the potential of Ansible. Among the most valuable chapters, the chapter 6 covers playbook organization using roles and includes to keep your playbooks maintenance, reusable, and powerful. A must to scale smoothly with your infrastructure. Chapter 8 synthesizes everything we've gone over in the previous chapters, and show how Ansible is applied to real-world infrastructure management scenarios, such as a highly-available infrastructure using redundancy, then provisioned on either local Vagrant VMs, DigitalOcean droplets, or AWS EC2 instances. You will even manage your local workstation with Ansible itself. Chapter 9 discusses deployment strategies: single-server, zero-downtime with rolling upgrade, and blue-green deployments to test your new infrastructure, and automatically cut over to the new instances. This book is the perfect showcase of all the impressive Ansible features.

What I appreciate the most about this book is its excellent style. The text is clear and concise, and the examples are outstanding. The only drawback I found is the author covers exclusively its own playbooks that are simpler than the official playbooks (elasticsearch, apache), so you will probably need to adjust the samples in your own projects.

Ansible was built by developers and sysadmins who know the command line - a lot of guys, judging the popularity of the project on GitHub. I recommend this book to anyone interested in Ansible, and wanting to learn all the benefits such a tool could bring to your infrastructure, using the current industry best practices.
