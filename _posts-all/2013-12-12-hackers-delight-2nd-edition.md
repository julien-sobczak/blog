---
layout: post-read
title: "Hacker's Delight, 2nd Edition"
author: 'Julien Sobczak'
date: '2013-12-12T09:00:00.002+02:00'
categories: read
tags:
- classics
image: 'http://d.gr-assets.com/books/1385216522l/276079.jpg'
read_authors: 'Henry S. Warren Jr.'
read_note: 17
read_date_published: '2002-07-17'
read_book_format: 'Hardcover'
read_isbn: '0201914654'
read_number_of_pages: 320
read_roti: 1
read_time: 20
read_headline: "Un livre soit indispensable, soit inutile."
link_amazon: "http://www.amazon.com/gp/product/0201914654/"
link_goodreads: "http://www.goodreads.com/book/show/276079.Hacker_s_Delight"
---


La première édition de Hacker's Delight est citée dans de nombreux livres et, plus surprenant, dans de très nombreux codes source, comme en témoigne la Javadoc de la classe Integer. Ce n'est donc pas surprenant de voir Guy Steele et Josh Bloch faire l'éloge du livre.

Mais que se cache donc derrière un tel titre ?

Hacker's Delight décrit des algorithmes liés à la manipulation de bits calculer le nombre de bits à 1, la différence entre deux mots, les additions, les multiplications, les divisions, les nombres premiers, ... Différents algorithmes sont généralement confrontés en terme du nombres instructions et du nombre de branches. Le livre s'intéressent (à l'exception d'un chapitre) aux nombres entiers (signés ou non). Les exemples sont généralement écrits en ou en langage machine (plus rare). Bref, on est vraiment sur du très bas niveau.

Hacker's Delight contient de très nombreux algorithmes et constitue davantage une référence sur le sujet qu'un livre vraiment destiné à être compris par un grand nombre de lecteurs. Pour ma part, je n'ai pas compris grand chose. Vous pouvez jeter un oeil à la méthode numberOfLeadingZeros dans la classe Integer de Java pour avoir un aperçu de ce qui vous attend (tout en sachant que les choses deviennent bien vite plus compliquées que cela...).

Pour la plupart des développeurs actuels dont je fais partie, nous avons appris à raisonner en nombres plutôt qu'en bits avec les subtilités que cela soulève (shifting, overflow, signed vs unsigned). Le livre nous ramène à la réalité, loin de notre zone de confort des langages de haut niveau. Etes-vous intéressé par un voyage dans ce monde dangereux Un conseil. N'oubliez pas l'assurance annulation car il a fort à parier que vous reposez le livre avant même la fin...

Je ne doute pas de la qualité du livre mais je vous invite à réfléchir par deux fois avant de l'entamer. moins de travailler sur un compilateur (peu probable) qui doit produire du code vraiment optimisé (encore moins probable), il a peu de chance que vous ayez à appliquer les techniques décrites. Pour cette cible restreinte, le livre constituera une vraie merveille et pourront remercier Addison Wesley de publier des livres d'exception mais dont le nombre d'exemplaires vendus ne sera jamais exceptionnel.

