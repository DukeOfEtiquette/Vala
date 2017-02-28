/**
 * Created by Adam DuQuette on 2/11/2017.
 */

/**
 * Found this beauty at http://stackoverflow.com/questions/20729823/jquery-string-format-issue-with-0
 */
String.prototype.format = function() {
  var str = this;
  for (var i = 0; i < arguments.length; i++) {
    var reg = new RegExp("\\{" + i + "\\}", "gm");
    str = str.replace(reg, arguments[i]);
  }
  return str;
};

$(function() {
   $('.sub').accordion();
});

$( window ).on( "load", function() {
    function removeButton(){
        var parent = document.getElementById("file_list");
        var child = document.getElementById("file1");
        parent.removeChild(child);
    }

    function addFileButton(evt){
        var addButton = document.createElement("INPUT");
        addButton.setAttribute("type", "file");
        var x = document.getElementById("file_list");
        x.prepend(addButton);
    }

});

function deleteRow(r) {
  var i = r.parentNode.parentNode.rowIndex;
  document.getElementById("taskList").deleteRow(i);
}

//onclick event for the submit button in the Add Equipment Dialog box
function equipSubmit() {

  //For each row that is checked in the dialog box...
  $('.tableRowDialog').find('input.rowCheckbox').filter(':checked').each(function(){

    // Parent2     Parents1   $this
    // tableRow -> td ->     checkBox
    var row = $(this).parent().parent();

    //Get the equipments ID number from within the row selected
    var equipID = row.find('td.equipID')[0].innerHTML;

    //If the item has already been added, then skip
    if($("#" + equipID).length > 0)
    {
      //Uncheck before leaving
      $(this).prop('checked', false);
      return;
    }

    //Get the selected equipment name
    var equipName = row.find('td.equipName')[0].innerText;

    //Construct HTML for a row
    var newRow = "<tr class='tableRow'> " +
        "<td><input type='button' value='x' onclick='deleteRow(this)'/></td> " +
        "<td class='equipID' id=" + equipID + "> " + equipID + " </td> " +
        "<td class='equipName'> " + equipName + " </td></tr>"

    //Add the row to the task list
    $("#taskList").append(newRow);

    //Uncheck row
    $(this).prop('checked', false);

  });

  //Close the dialog box
  $( "#addEquipDialog" ).dialog( "close" );
}

$("document").ready(function() {

  $(".tablinks").on('click', function() {
      // Declare all variables
      var i, tabcontent, tablinks;

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "none";
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
          tablinks[i].className = tablinks[i].className.replace(" active", "");
      }

      // Show the current tab, and add an "active" class to the link that opened the tab
      document.getElementById(this.textContent).style.display = "inline-block";
      this.className += " active";
  });

  //TODO(Adam): Uncomment after Equipment tab demo
  //$(".tablinks").first().click();

  //TODO(Adam): Remove after Equipment tab demo
  $("a:contains('Equipment')").click();


  $(function() {
    $( "#addEquipButt" ).click(function() {
      $( "#addEquipDialog" ).dialog( "open" );

    });

    $( "#addEquipDialog" ).dialog({
      draggable: true,
      modal: true,
      width: 500,
      height: 300,
      autoOpen: false,
    });

    return false;

    /*$( "#addEquipDialog" ).dialog("widget").position({
      my: 'center',
      at: 'center'
    });*/
  });

});

function selectExperiment(experimentType) {
    console.log(experimentType);
   $('.experiment_options option:contains({0})'.format(experimentType)).prop('selected', true);
}