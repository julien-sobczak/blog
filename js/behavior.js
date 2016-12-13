// Freelancer Theme JavaScript

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


    // Spongbob easteregg
    $(document).easteregg({
      callback: function () {
        console.log('ici!!!!!!!!!!!!!!!');
        // Add a CSS class to trigger animations
        $('.easter-egg-party').addClass('active').addClass('go');

        var goBackToBlog = function() {
          $('.easter-egg-party').removeClass('active').removeClass('go');
          $(document).unbind('keydown', goBackToBlog);
          $(document).unbind('click', goBackToBlog);
        };

        // Remove everything when any key is pressed
        $(document).on('keydown', goBackToBlog);
        $(document).on('click', goBackToBlog);
      }
    });


})(jQuery); // End of use strict
