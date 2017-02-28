/**
 * Created by Erin MacMillan on 2/11/2017.
 */

// ERIN these vars are used to validate project id length in addUser()/createProject()
$( function() {
    var dialog, form, MIN_ID_LEN = 5, MAX_ID_LEN = 10,

        // From http://www.whatwg.org/specs/web-apps/current-work/multipage/states-of-the-type-attribute.html#e-mail-state-%28type=email%29
        projectRegex = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
        projectID = $( "#project_id" ),
        allFields = $( [] ).add( projectID ),   // ERIN these var names can change later
        tips = $( ".validateTips" );            // ERIN these var names can change later
    // ERIN not a fucking clue what updateTips does...rolling with it
    function updateTips( t ) {
        tips
            .text( t )
            .addClass( "ui-state-highlight" );
        setTimeout(function() {
            tips.removeClass( "ui-state-highlight", 1500 );
        }, 500 );
    }
    // ERIN to validate length of text input
    function checkLength( o, n, min, max ) {
        if ( o.val().length > max || o.val().length < min ) {
            o.addClass( "ui-state-error" );
            updateTips( "Length of " + n + " must be between " +
                min + " and " + max + "." );
            return false;
        } else {
            return true;
        }
    }
    // ERIN validate regex
    function checkRegexp( o, regexp, n ) {
        if ( !( regexp.test( o.val() ) ) ) {
            o.addClass( "ui-state-error" );
            updateTips( n );
            return false;
        } else {
            return true;
        }
    }
    // ERIN create new project
    // ERIN**  update addUser ==> createProject()
    function createProject() {
        var valid = true;
        allFields.removeClass( "ui-state-error" );
        // ERIN validate length and regex val for project id entered by user
        // ERIN**
        valid = valid && checkLength( projectID, "Project ID", MIN_ID_LEN, MAX_ID_LEN );
        valid = valid && checkRegexp( projectID, /^[a-z]([0-9a-z_\s])+$/i, "Project ID may consist of a-z, 0-9, underscores, spaces and must begin with a letter." );

        // ERIN** if valid, hit db, grab proj info, pop form, add to users projects/tasks
        if ( valid ) {
            $( "#users tbody" ).append( "<tr>" +
                "<td>" + name.val() + "</td>" +
                "<td>" + email.val() + "</td>" +
                "<td>" + password.val() + "</td>" +
                "</tr>" );
            dialog.dialog( "close" );
        }
        return valid;
    }

    dialog = $( "#dialog-form" ).dialog({
        autoOpen: false,
        height: 400,
        width: 350,
        modal: true,
        buttons: {
            "CREATE": createProject,
            Cancel: function() {
                dialog.dialog( "close" );
            }
        },
        close: function() {
            form[ 0 ].reset();
            allFields.removeClass( "ui-state-error" );
        }
    });

    form = dialog.find( "form" ).on( "submit", function( event ) {
        event.preventDefault();
        createProject();
    });

    $( "#new-project" ).on( "click", function() {
        dialog.dialog( "open" );
        return false;
    });
} );
