
// Enable Masonry effect
var postList = document.getElementById('post-list');
if (postList) {
  new AnimOnScroll(postList, {
	  minDuration: 0.4,
	  maxDuration: 0.7,
	  viewportFactor: 0.4
  });
}

(function($) {
    "use strict"; // Start of use strict

    var $window = $(window);

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-default',
        offset: 51
    });

    // Highlight the top nav as scrolling occurs
    $('.body').scrollspy({
        target: '.navbar-default',
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function(){
        $('.navbar-toggle:visible').click();
    });

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    });

    $('#mainNav button').click(function() {
        $('#mainNav .navbar-collapse').toggleClass('expanded');
    });


    // Inspired by https://www.sitepoint.com/scroll-based-animations-jquery-css3/
    // Un-blur figures when first appearing on screen
    var $animation_elements = $('figure img');
    $window.on('scroll resize', check_if_in_view);
    $window.trigger('scroll');
    function check_if_in_view() {
      var window_height = $window.height();
      var window_top_position = $window.scrollTop();
      var window_bottom_position = (window_top_position + window_height);

      $.each($animation_elements, function() {
        var $element = $(this);
        var element_height = $element.outerHeight();
        var element_top_position = $element.offset().top;
        var element_bottom_position = (element_top_position + element_height);

        // check to see if this current container is within viewport
        if ((element_bottom_position >= window_top_position) &&
            (element_top_position <= window_bottom_position)) {
          $element.addClass('in-view');
        } //else {
        //  $element.removeClass('in-view');
        //}
      });
    }

    // Reading progress bar
    // Inspired by https://codepen.io/haroldjc/pen/GZaqWa
    var readingBar = document.getElementById("reading-bar");
    addEventListener("scroll", function(event) {
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


    // Activate the sunshine effect on the main label list
    $('#labels .label').hover(
      function() {
        $(this).addClass('hover');
      },
      function() {
        var label = $(this);
        window.setTimeout(function() {
          label.removeClass('hover');
        }, 500);
      }
    );

    // Make Aside sticky on blog post
    var stickySidebar = $('.sticky');
    var stickyContainer = $('.sticky-container');
    if (stickySidebar.length > 0) {
      var stickyHeight = stickySidebar.outerHeight(),
          sidebarTop = stickySidebar.offset().top;
      // Use the max height as reference
      stickySidebar.each(function() {
        var eachStickyHeight = $(this).outerHeight();
        if (eachStickyHeight > stickyHeight) {
          stickyHeight = eachStickyHeight;
        }
      });
    }
    var mainNav = $('#mainNav');
    // on scroll move the sidebar
    $(window).scroll(function () {
      if (stickySidebar.length > 0) {
        var scrollTop = $(window).scrollTop();

        if (sidebarTop < scrollTop) {
          stickySidebar.css('top', scrollTop - sidebarTop);

          // stop the sticky sidebar at the footer to avoid overlapping
          var stickyStop = stickyContainer.offset().top + stickyContainer.outerHeight();
          stickySidebar.each(function() {
            var eachStickySidebar = $(this);
            var stickyHeight = eachStickySidebar.outerHeight();
            var sidebarBottom = stickySidebar.offset().top + stickyHeight;
            var optionalSidebar = eachStickySidebar.hasClass('optional');

            if (optionalSidebar) {
              if (scrollTop - sidebarTop > 100) {
                eachStickySidebar.css('opacity', "100");
              } else {
                eachStickySidebar.css('opacity', "0");
              }
              if (stickyStop - ($(window).height() / 2) < sidebarBottom) {
                eachStickySidebar.css('opacity', "0");
              }
            }

            if (stickyStop < sidebarBottom) {
              var stopPosition = stickyContainer.outerHeight() - stickyHeight;
              eachStickySidebar.css('top', stopPosition);
            }
          });
        }
        else {
          stickySidebar.css('top', '0');
        }
      }
    });
    // Do not forget to listen resize
    $(window).resize(function () {
      if (stickySidebar.length > 0) {
        stickyHeight = stickySidebar.outerHeight();
      }
    });


    // Add menu for lengthy post
    $("#toc").tocify({
       "context": "#page-post article",
       "scrollTo": 150,
       "theme": "none",
       "selectors": "h2,h3,h4"
    });

})(jQuery); // End of use strict



// Easter-egg
window.addEventListener('load', (event) => {
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
});


