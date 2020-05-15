window.addEventListener('load', (event) => {
  
  document.body.classList.add('loaded');

  //
  // Easter-egg
  // Based on https://gomakethings.com/how-to-create-a-konami-code-easter-egg-with-vanilla-js/
  //

  // The hidden element to reveal...
  const easterEgg = document.getElementById('easter-egg');
  // ...when the following sequence is completed:
  const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
  // Current position in the above sequence
  let current = 0;

  // Listen for keypress
  document.addEventListener('keydown', (event) => {
    // If the key isn't in the pattern, or isn't the current key in the pattern, reset
    if (konamiCode.indexOf(event.key) < 0 || event.key !== konamiCode[current]) {
      current = 0;
      return;
    }

    // Update how much of the pattern is complete
    current++;

    // Complete
    if (konamiCode.length === current) {
      current = 0;
      easterEgg.classList.add('active');
    }

  }, false);

  // Mask when the user click on the revealed element
  easterEgg.addEventListener('click', () => {
    easterEgg.classList.remove('active');
  });


  //
  // Reading bar
  // Inspired by https://codepen.io/haroldjc/pen/GZaqWa
  //

  var readingBar = document.getElementById("reading-bar");
  document.addEventListener("scroll", () => {
    if (!readingBar) return;
    var total = document.body.scrollHeight - window.innerHeight;
    var percent = (window.scrollY / total) * 100;

    if (percent > 5) {
      readingBar.style.width = percent + "%";
    } else {
      readingBar.style.width = "0%";
    }

    if (percent == 100) {
      readingBar.className = "finished";
    } else {
      readingBar.className = "";
    }
  });


  // 
  // Nav Links Highlighting
  // Inspired by https://codepen.io/jonasmarco/pen/JjoKNaZ
  // 

  // Make nav link be active on scroll when their section is on screen
  const navLinks = document.querySelectorAll('.nav-link');

  for (let n in navLinks) {
    if (navLinks.hasOwnProperty(n)) {
      navLinks[n].addEventListener('click', e => {
        e.preventDefault();
        document.querySelector(navLinks[n].hash).scrollIntoView({ behavior: "smooth" });
      });
    }
  }
  
  const sections = document.querySelectorAll('section[id]');
  const highlightCurrentNavLink = () => {
    const scrollPos = document.documentElement.scrollTop || document.body.scrollTop;
    const accuracy = window.innerHeight / 2; // Heighlight the section represents 50% of the viewport 

    for (let s in sections) {
      if (sections.hasOwnProperty(s) && sections[s].offsetTop - accuracy <= scrollPos) {
        const id = sections[s].id;
        const sectionLink = document.querySelector(`a[href*=${id}]`);
        const sectionPreviousLink = document.querySelector('nav li.active');
        // Remove highlight on previous link
        if (sectionLink && sectionPreviousLink) sectionPreviousLink.classList.remove('active');
        // Add highlight on current link
        if (sectionLink) sectionLink.parentNode.classList.add('active');
      }
    }
  };
  window.addEventListener('scroll', highlightCurrentNavLink, false);
  highlightCurrentNavLink(); // Force on page load 
  
  
  // Affix effect (reduce the menu size on scroll)
  const labels = document.getElementById('labels');
  const footer = document.getElementById('footer');
  window.addEventListener('scroll', () => {
    const scrollPos = document.documentElement.scrollTop || document.body.scrollTop;
    const labelsPos = (labels && labels.offsetTop) || Number.MAX_SAFE_INTEGER;
    const footerPos = (footer && footer.offsetTop) || Number.MAX_SAFE_INTEGER;
    if (scrollPos > 500 && scrollPos < Math.min(labelsPos, footerPos) - 100) {
      document.body.classList.add('affix');
    } else {
      document.body.classList.remove('affix');
    }
  }, false);


  // Mansory effect 
  var grid = document.querySelector('.grid-view');
  if (grid) {
    new Colcade(grid, {
      columns: '.grid-col',
      items: '.grid-item',
    });
  }

  // Filters on posts list
  const filterByRating = stars => {
    const itemStars1 = [...document.querySelectorAll(".item-stars-1")];
    const itemStars2 = [...document.querySelectorAll(".item-stars-2")];
    const itemStars3 = [...document.querySelectorAll(".item-stars-3")];
    const itemStars4 = [...document.querySelectorAll(".item-stars-4")];
    const itemStars5 = [...document.querySelectorAll(".item-stars-5")];
    itemStars1.map(e => e.classList.remove('hidden'));
    itemStars2.map(e => e.classList.remove('hidden'));
    itemStars3.map(e => e.classList.remove('hidden'));
    itemStars4.map(e => e.classList.remove('hidden'));
    itemStars5.map(e => e.classList.remove('hidden'));
    if (stars >= 2) {
      itemStars1.map(e => e.classList.add('hidden'));
    }
    if (stars >= 3) {
      itemStars2.map(e => e.classList.add('hidden'));
    }
    if (stars >= 4) {
      itemStars3.map(e => e.classList.add('hidden'));
    }
    if (stars >= 5) {
      itemStars4.map(e => e.classList.add('hidden'));
    }
  }
  const filterStar1 = document.getElementById('filter-star-1');
  const filterStar2 = document.getElementById('filter-star-2');
  const filterStar3 = document.getElementById('filter-star-3');
  const filterStar4 = document.getElementById('filter-star-4');
  const filterStar5 = document.getElementById('filter-star-5');
  if (filterStar1) {
    filterStar1.addEventListener('click', () => filterByRating(1));
    filterStar2.addEventListener('click', () => filterByRating(2));
    filterStar3.addEventListener('click', () => filterByRating(3));
    filterStar4.addEventListener('click', () => filterByRating(4));
    filterStar5.addEventListener('click', () => filterByRating(5));
  }

  // Support multiple view modes
  const filterGrid = document.getElementById('filter-grid-mode');
  const filterList = document.getElementById('filter-list-mode');
  if (filterGrid) {
    const showListView = () => {
      document.querySelector('.grid-view').classList.add('hidden');
      document.querySelector('.list-view').classList.remove('hidden');
      localStorage.setItem('view','list');
    };
    const showGridView = () => {
      document.querySelector('.list-view').classList.add('hidden');
      document.querySelector('.grid-view').classList.remove('hidden');
      localStorage.setItem('view','grid');
    };
    // Register Event Listeners 
    filterGrid.addEventListener('click', showGridView);
    filterList.addEventListener('click', showListView);
    
    // Check preferences
    let preferredView = localStorage.getItem('view');
    if (preferredView && preferredView == "list") {
      showListView();
    } else {
      showGridView();
    }
  }

  // Support a zen mode on long post
  const zenButtonIn = document.getElementById('zen-mode-in');
  const zenButtonOut = document.getElementById('zen-mode-out');
  if (zenButtonIn) {

    const enableZenMode = () => {
      document.body.classList.add('zen');
      zenButtonOut.classList.add('visible');
      localStorage.setItem('zen','enable');
    };
    const disableZenMode = () => {
      document.body.classList.remove('zen');
      zenButtonOut.classList.remove('visible');
      localStorage.setItem('zen','disable');
    };
    zenButtonIn.addEventListener('click', enableZenMode);
    zenButtonOut.addEventListener('click', disableZenMode);

    let zenMode = localStorage.getItem('zen');
    if (zenMode === 'enable') {
      enableZenMode();
    }
  }
});


