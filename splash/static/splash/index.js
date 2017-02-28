/**
 * Created by Adam DuQuette on 2/6/2017.
 */
//Once document is ready...
$( window ).on( "load", function() {

    //Change what nav bar item is selected
    $(".nav-bar ul li").click(function(){
        $(".nav-bar .active").removeClass('active');
        $(this).addClass('active');

    });

    $(".click-row").click( function(){
        val = $(this).children("span:first").text();
        var location = "/edit/"+val;
        window.location.href = location;
    });
});
