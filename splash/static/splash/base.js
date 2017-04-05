/**
 * Created by Erin MacMillan on 2/11/2017.
 */

$(window).on("load", function () {
// ERIN these vars are used to validate project id length in addUser()/createProject()
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

