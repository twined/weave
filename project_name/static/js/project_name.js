// application global js

$(document).ready(function() {
    $('.carousel').carousel();

    $(".alert").alert();

    $("a[href='#top']").click(function(e) {
        $("html, body").animate({ scrollTop: 0 }, "fast");
        e.preventDefault();
    });

    $.waypoints.settings.scrollThrottle = 30;
    $('#nav-container').waypoint(function(event, direction) {
        $(this).toggleClass('sticky', direction === "down");
        event.stopPropagation();
    });
});