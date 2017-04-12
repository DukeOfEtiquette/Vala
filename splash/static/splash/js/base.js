/**
 * Created by Erin MacMillan on 2/11/2017.
 */

// ERIN these vars are used to validate project id length in addUser()/createProject()
$( function() {
    var dialog = $( "#dialog-form" ).dialog({
        autoOpen: false,
        height: 165,
        width: 350,
        modal: true,
    });

    $( "#new-project" ).on( "click", function() {
        dialog.dialog( "open" );
        return false;
    });
} );
