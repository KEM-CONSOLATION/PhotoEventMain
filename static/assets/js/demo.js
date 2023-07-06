   

$(document).ready(function() {
    'use strict';

    /*-------------------------------------
      Back to top
    -------------------------------------*/

    $('.back-to-top').click(function(){ 
        $("html, body").animate({ scrollTop: 0 }, 600); 
        return false; 
    });

    /*--  Side Bar Sticky js Start--*/
    // var sidebarSticky = $(".sidebar");
    // if (sidebarSticky.length) {
    //     var sidebar = new StickySidebar(".sidebar", {
    //         topSpacing: 20,
    //         bottomSpacing: 20,
    //         containerSelector: ".main-content",
    //         innerWrapperSelector: ".sidebar__inner",
    //     });
    // }

    var sidebarSticky = $(".main-content");
    if (sidebarSticky.length) {
        let content = document.querySelector(".main-content");
        let sidebarContent = content.querySelector(".sidebar__inner");
        var sidebar = sidebarSticky.find(".sidebar");
        var sidebarInner = sidebar.find(".sidebar__inner");
        $(window).on("scroll", function () {
            var y = window.scrollY;
            var x = sidebarSticky.offset().top;
            let h = content.offsetHeight;
            let sh = sidebarContent.offsetHeight;
            let tmp = x + h - sh;

            if (y > x) {
                sidebar.addClass("active");
                sidebarInner.css("position", `fixed`);
                sidebarInner.css("top", `20px`);
                sidebarInner.css("transform", `unset`);
                if (tmp < y) {
                    sidebar.removeClass("active");
                    let tmph = h - sh;
                    sidebarInner.css("position", `relative`);
                    sidebarInner.css("transform", `translate3d(0px, ${tmph}px, 0px)`);
                }
            } else {
                sidebarInner.css("position", `relative`);
                sidebarInner.css("top", `0px`);
                sidebarInner.css("transform", `unset`);
            }
        });
    }
    /*--  Side Bar Sticky js End --*/

        /*-- banner-img-scroll-effect-js start --*/
        var bannerImg = $(".banner-img");
        if (bannerImg.length) {
            $(window).on("scroll", function () {
                var CardImage = $(".banner-img");
                var y = window.scrollY;
                var x;
                x = CardImage.offset().top;
                x = x - 400;
    
                let animationValue = 0;
                animationValue = (y - x) / 2;
    
                let animationStop = 300;
    
                if (animationValue < 0) {
                    animationValue > 0;
                }
    
                if (animationValue > animationStop) {
                    animationValue = animationStop;
                }
    
                CardImage.css("transform", `translateY(${animationValue}px)`);
            });
        }
        /*-- banner-img-scroll-effect-js End --*/

    /*-------------------------------------
      Isotope
    -------------------------------------*/

    var $grid = $('.isotope-item').isotope({
        // options...
        itemSelector: '.item',
        layoutMode:'fitRows'

    });

    $grid.imagesLoaded().progress(function () {
        $grid.isotope('layout');
    });


    $('.nav-item').click(function(){
       $('.nav-item').removeClass('active');
       $(this).addClass('active');
       var selector=$(this).attr('data-filter');
       $('.isotope-item').isotope({
         filter:selector
       });
       return false;
    });

        // Select all links with hashes
    $('a[href*="#"]')
        // Remove links that don't actually link to anything
        .not('[href="#"]')
        .not('[href="#0"]')
        .click(function(event) {
            // On-page links
            if (
                location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                location.hostname == this.hostname
            ) {
                // Figure out element to scroll to
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                // Does a scroll target exist?
                if (target.length) {
                    // Only prevent default if animation is actually gonna happen
                    event.preventDefault();
                    $('html, body').animate({
                        scrollTop: target.offset().top
                    }, 500, function() {
                        // Callback after animation
                        // Must change focus!
                        var $target = $(target);
                        $target.focus();
                        if ($target.is(":focus")) { // Checking if the target was focused
                            return false;
                        } else {
                            $target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
                            $target.focus(); // Set focus again
                        };
                    });
                }
            }
        });


})

