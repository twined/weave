    $(function(){
        var $container = $('.portfolio');
        $container.imagesLoaded( function(){
            $('#loading-images').slideUp();
            $container.fadeIn().isotope({
                itemSelector : '.pfwrap',
                layoutMode: 'masonry'
            });
        });

        $container.infinitescroll({
            // selector for the paged navigation
            navSelector  : '#page_nav',
            // selector for the NEXT link (to page 2)
            nextSelector : '#page_nav a',
            // selector for all items you'll retrieve
            itemSelector : '.pfwrap',
            loading: {
                msgText: 'Loading next set of images..',
                finishedMsg: 'No more images to load.',
                img: 'http://i.imgur.com/qkKy8.gif',
                speed: 0
              }
            },
            // call Isotope as a callback
            function( newElements ) {
                //var $newElems = $(newElements);
                var $newElems = $(newElements).css({opacity: 0});
                $newElems.imagesLoaded(function() {

                    $container.isotope('appended', $newElems);
                    $newElems.animate({ opacity: 1 });
                });
            }
        );
    });