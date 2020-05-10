
// Enable Masonry effect
var postList = document.getElementById('post-list');
if (postList) {
  new AnimOnScroll(postList, {
	  minDuration: 0.4,
	  maxDuration: 0.7,
	  viewportFactor: 0.4
  });
}

window.addEventListener('load', (event) => {
  
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
  window.addEventListener('scroll', () => {
    const scrollPos = document.documentElement.scrollTop || document.body.scrollTop;
    if (scrollPos > 100) {
      document.body.classList.add('affix');
    } else {
      document.body.classList.remove('affix');
    }
  }, false);

});


