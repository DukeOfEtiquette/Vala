/**
 * Created by peacock on 5/24/17.
 */

//Once document is ready...
$(window).on("load", function () {

    //Change what nav bar item is selected
    $(".nav-bar ul li").click(function () {
        $(".nav-bar .active").removeClass('active');
        $(this).addClass('active');

    });

    $(".click-row").click(function () {
        val = $(this).children("td:first").text();
        var location = "/edit/" + val;
        window.location.href = location;
    });

     // implementation of dataTable tool for query list
    $(document).ready(function(){
        $('#queryList').DataTable();
    });

    // IN PROGRESS...function to redirect user to project summary from query page
    $(".click-row").click(function () {
        val = $(this).children("td:first").text();
        var location = "/project/" + val;
        window.location.href = location;
    });

    $("#id_project_id").bind('input propertychange', function () {
        value = this.value;
        var reg = new RegExp('^[A-z]{2}-[0-9]+$');
        eval = value.match(reg);
        if (eval) {
            $('#id_project_id').css('border', '3px solid green');
            $('#create-project').prop('disabled', false);
        } else {
            $('#id_project_id').css('border', '3px solid red')
            $('#create-project').prop('disabled', true);
        }
    });
});





