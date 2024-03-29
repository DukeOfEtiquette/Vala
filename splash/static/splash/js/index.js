/**
 * Created by Adam DuQuette on 2/6/2017.
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
        var location = "";
        if (viewAll === "True"){
            location = "/project/" + val;
        }else{
            location = "/edit/" + val;
        }
        window.location.href = location;
    });

    // implementation of dataTable tool for task list
    $(document).ready(function(){
        $('#taskList').DataTable();
    });

//these functions are used to validate project id length in addUser()/createProject()
    $(function () {
        var dialog = $("#dialog-form").dialog({
            autoOpen: false,
            height: 165,
            width: 350,
            modal: true,
        });

        $("#new-project").on("click", function () {
            dialog.dialog("open");
            return false;
        });
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





