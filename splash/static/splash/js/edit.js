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

function getEntryId(){
  //Get the project ID
  var entryId = $(".project_title > h1").attr("id");

  return entryId;
}

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

function fileOnClick(event) {
  var row = event;

  //Grab the table ID
  var parentID = event.parentNode.parentNode.id;
  console.log(parentID);

  /*
  //Grab the row that was selected
  var row = event.parentNode.parentNode;
  console.log(row);*/

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availFileList")
  {
    var workBench = $("#fileListBench");
    workBench.append(row);
    save_file(row);

  }else {
    var equipList = $("#availFileList");
    equipList.append(row);
    row.checked = false;
    delete_file(row);
  }
}

function delete_file(row){
  var file_id = row.getElementsByClassName("fileID")[0].innerText;

  //Get the project ID
  var entryId = getEntryId();

  //Some kind of voodoo, remove this and ajax request won't work
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });

  //Make the AJAX post request
  $.ajax({
    type: "POST",
    url: "/delete_file/",
    data: {
      entry_id: entryId,
      file_id: file_id
    }

  });
}

function save_file(row) {
  var file_id = row.id;
  //Get the data we are sending over
  var list_of_ids = $('#fileListBench').find(".fileID");
  var list_of_names = $('#fileListBench').find(".fileName");

  var file_name = row.getElementsByClassName("fileName")[0].innerText;
  //Get the project ID
  var entryId = getEntryId();

  //Some kind of voodoo, remove this and ajax request won't work
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });

  //Make the AJAX post request
  $.ajax({
    type: "POST",
    url: "/save_file/",
    data: {
      entry_id: entryId,
      file_id: file_id,
      file_name: file_name
    }
  });
}

function equipOnClick(event) {
  var row = event;
  console.log("row: ");
  console.log(row);
  //Grab the table ID
  var parentID = row.parentNode.parentNode.id;
  console.log("ParentID: " + parentID)

  /*
  //Grab the row that was selected
  var row = event.parentNode.parentNode;
  //console.log(row);*/
  //Remove it from current table

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availEquipmentList")
  {
    var workBench = $("#benchEquipBody");
    console.log("appending...");
    console.log(row);
    console.log("to benchEquipBody...");
    console.log(workBench);
    workBench.append(row);
    save_equip(row);

  }else {
    var equipList = $("#availEquipBody");
    console.log("availEquipBody...");
    console.log(equipList);
    equipList.append(row);
    delete_equip(row);
  }
}

function save_equip(row){
  var equipment_id = row.id;
  console.log("ROW ID: " + equipment_id);

  console.log("Row...");
  console.log(row);
  var equipment_name = row.getElementsByClassName("equipName")[0].innerText;
  console.log("ROW NAME: " + equipment_name);

  //Get the project ID
  var entryId = getEntryId();

  //Some kind of voodoo, remove this and ajax request won't work
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });

  //Make the AJAX post request
  $.ajax({
    type: "POST",
    url: "/save_equipment/",
    data: {
      entry_id: entryId,
      equip_id: equipment_id,
      equip_name: equipment_name
    }

  });
}

function delete_equip(row){
  var equipment_id = row.getElementsByClassName("equipID")[0].innerText;
  console.log("ROW ID: " + row.id);

  //Get the project ID
  var entryId = getEntryId();

  //Some kind of voodoo, remove this and ajax request won't work
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });

  //Make the AJAX post request
  $.ajax({
    type: "POST",
    url: "/delete_equipment/",
    data: {
      entry_id: entryId,
      equip_id: equipment_id
    }

  });
}

// using jQuery, taken from Django documentation about AJAX post requests
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

//Makes an ajax request to get json data from a stub server and send it to a
//function that will format the data in the page
function populateEquipment(){
  $.ajax({
    type: "GET",
    dataType: 'json',
    url: "http://stubserver.us-west-2.elasticbeanstalk.com/Equipment/?format=json",
    success: function(data){
      addEquipmentData(data);
    }
  });
}

//Receives json data and adds it to the equipment table
function addEquipmentData(data){

  //console.log(data);
  for(var i = 0; i < data.count; i++)
  {
    //Get the equipmentId we are trying to add
    var equipID = data.results[i].serial_number;

    //Only add the equipment not already associated with this project
    if(!isEquipmentOnBench(equipID))
    {
      //Grab the equipment name now that we know it needs to be added
      var equipName = data.results[i].description;

      //Construct HTML for a row
      var dataRow = "<tr class='click-row' id="+equipID+" onclick='equipOnClick(this)'><td class='equipID'>"+equipID+"</td>" +
                     "<td class='equipName'>"+equipName+"</td></tr>";

      //Add the row to the task list
      $("#availEquipBody").append(dataRow);
    }
  }
  $('#availEquipmentList').DataTable();
}

function isEquipmentOnBench(equipId)
{
  //Get all equipment IDs already associated with this project
  var list_of_ids = $('#benchEquipBody').find(".equipID");

  //Iterate over each id...
  for(var i = 0; i < list_of_ids.length; i++)
  {
    //If the current id is already associated with this project return true
    if(list_of_ids[i].innerText == equipId){
      return true;
    }
  }

  //If it wasn't found then return false
  return false;

}

//Makes an ajax request to get json data from a stub server and send it to a
//function that will format the data in the page
function populateFiles(){
  $.ajax({
    type: "GET",
    dataType: 'json',
    url: "http://stubserver.us-west-2.elasticbeanstalk.com/Files/?format=json",
    success: function(data){
      addFileData(data);
    }
  });
}

//Receives json data and adds it to the files tab
function addFileData(data){

  //console.log(data);
  for(var i = 0; i < data.count; i++)
  {
    //Get the equipmentId we are trying to add
    var fileID = data.results[i].id;

    //Only add the equipment not already associated with this project
    if(!isFileOnBench(fileID))
    {
      //Grab the equipment name now that we know it needs to be added
      var fileName = data.results[i].key;

      //Construct HTML for a row
      var dataRow = "<tr class='click-row' id="+fileID+" onclick='fileOnClick(this)'><td class='fileID'>"+fileID+"</td>" +
          "<td class='fileName'>"+fileName+"</td></tr>";

      //Add the row to the task list
      $("#availFileBody").append(dataRow);
    }
  }
  $('#availFileList').DataTable();
}

function isFileOnBench(fileId)
{
  //Get all equipment IDs already associated with this project
  var list_of_ids = $('#fileListBench').find(".fileID");

  //Iterate over each id...
  for(var i = 0; i < list_of_ids.length; i++)
  {
    //If the current id is already associated with this project return true
    if(list_of_ids[i].innerText == fileId){
      return true;
    }
  }

  //If it wasn't found then return false
  return false;
}

$("document").ready(function() {

  //Populate the the Equipment pane from outside microservice
  populateEquipment();
  populateFiles();

  $(".tablinks").on('click', function() {
      // Declare all variables
      var i, tabcontent, tablinks, tableaving;

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "none";
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
          if(tablinks[i].className.match(" active"))
          {
            tableaving = i;
          }
          tablinks[i].className = tablinks[i].className.replace(" active", "");
      }

      // Show the current tab, and add an "active" class to the link that opened the tab
      document.getElementById(this.textContent).style.display = "inline-block";
      this.className += " active";

      if(this.innerHTML == "Summary")
        refreshSummary();
  });

  $(".tablinks").first().click();

  $('#equipSummaryTable').DataTable();
  $('#equipListBench').DataTable();
  $('#fileListBench').DataTable();
  $('#fileSummaryTable').DataTable();

});

function refreshSummary(){

  var summaryTable = $('#equipListBench').clone();
  summaryTable.attr("id", "equipSummaryTable");

  $('#equipSummaryTable').remove();
  $('#EquipSummary').empty();//remove all content in div
  $('#EquipSummary').append("<h3 class='tabHeader'>Equipment</h3>");//add header
  $('#EquipSummary').append(summaryTable);//add table

  //Remove listener from each row, and click-row styling
  console.log(summaryTable.find(".click-row").each(function(){
    $(this).removeClass("click-row");
    $(this).prop('onclick', null).off('click');
  }));
  $('#equipSummaryTable').DataTable();//go go datatable


  summaryTable = $('#fileListBench').clone();
  summaryTable.attr("id", "fileSummaryTable");

  $('#fileSummaryTable').remove();
  $('#FileSummary').empty();
  $('#EquipSummary').append("<h3 class='tabHeader'>Files</h3>");
  $('#FileSummary').append(summaryTable);

  //Remove listener from each row, and click-row styling
  console.log(summaryTable.find(".click-row").each(function(){
    $(this).removeClass("click-row");
    $(this).prop('onclick', null).off('click');
  }));
  $('#fileSummaryTable').DataTable();
}
