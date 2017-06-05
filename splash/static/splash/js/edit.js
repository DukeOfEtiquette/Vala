/**
 * Created by Adam DuQuette on 2/11/2017.
 */

function getEntryId(){
  //Get the project ID
  return $(".project_title > h1").attr("id");
}

function fileOnClick(r) {
  var row;

  //Hack(adam): When adding onclick event dynamically I wasn't sure how to pass
  //            "this" to the function like I do in the HTML
  if(typeof(event.parentNode) === "undefined"){
    row = event.path[1];
  }else{
    row = r;
  }

  var rowID = '#' + row.id;

  //Grab the table ID
  var parentID = row.parentNode.parentNode.id;

  var rowData, tableRow, benchTable, availTable;

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availFileList")
  {
    //Grab the table the row is moving OUT of
    availTable = $("#availFileList").DataTable();

    //Capture the rows data and remove from the table
    rowData = availTable.row(rowID).data();
    availTable.row(rowID).remove().draw();

    //Grab the table the row is moving INTO and add it
    benchTable = $("#fileListBench").DataTable();
    benchTable.row.add(rowData).draw();

    //Grab the row through datatables API
    tableRow = benchTable.row(rowID).node();

    //Save to database
    save_file(row);

  }else {
    benchTable = $("#fileListBench").DataTable();

    rowData = benchTable.row(rowID).data();
    benchTable.row(rowID).remove().draw();

    availTable = $("#availFileList").DataTable();
    availTable.row.add(rowData).draw();

    tableRow = availTable.row(rowID).node();

    delete_file(row);
  }

  //Add style and onclick event to row
  $(tableRow).addClass(" click-row").on("click", fileOnClick);

  //Add id and name classes to children
  $(tableRow).children()
      .first().addClass(" fileID")
      .next().addClass(" fileName");
}

function delete_file(row){
  //Get the data we are sending over
  var entryId = getEntryId();
  var file_id = row.getElementsByClassName("fileID")[0].innerText;

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
  //Get the data we are sending over
  var entryId = getEntryId();
  var file_id = row.id;
  var file_name = row.getElementsByClassName("fileName")[0].innerText;

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

function scientistOnClick(r) {
  var row;

  //Hack(adam): When adding onclick event dynamically I wasn't sure how to pass
  //            "this" to the function like I do in the HTML
  if(typeof(event.parentNode) === "undefined"){
    row = event.path[1];
  }else{
    row = r;
  }

  var rowID = '#' + row.id;

  //Grab the table ID
  var parentID = row.parentNode.parentNode.id;

  var rowData, tableRow, benchTable, availTable;

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availScientistList") {
    //Grab the table the row is moving OUT of
    availTable = $("#availScientistList").DataTable();

    //Capture the rows data and remove from the table
    rowData = availTable.row(rowID).data();
    availTable.row(rowID).remove().draw();

    //Grab the table the row is moving INTO and add it
    benchTable = $("#scientistListBench").DataTable();
    benchTable.row.add(rowData).draw();

    //Grab the row through datatables API
    tableRow = benchTable.row(rowID).node();

    //Save to database
    save_scientist(row);

  }else {
    benchTable = $("#scientistListBench").DataTable();

    rowData = benchTable.row(rowID).data();
    benchTable.row(rowID).remove().draw();

    availTable = $("#availScientistList").DataTable();
    availTable.row.add(rowData).draw();

    tableRow = availTable.row(rowID).node();

    delete_scientist(row);
  }

  //Add style and onclick event to row
  $(tableRow).addClass(" click-row").on("click", scientistOnClick);

  //Add id and name classes to children
  $(tableRow).children()
      .first().addClass(" sciUsername")
      .next().addClass(" sciName");
  return true;
}

function save_scientist(row) {
  //Get the data we are sending over
  var sci_username = row.id;

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
    url: "/save_scientist/",
    data: {
      entry_id: entryId,
      sci_username: sci_username
    }

  });

}

function delete_scientist(row) {
  //Get the data we are sending over
  var sci_username = row.id;

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
    url: "/delete_scientist/",
    data: {
      entry_id: entryId,
      sci_username: sci_username
    }

  });

}

function equipOnClick(r) {
  var row;

  //Hack(adam): When adding onclick event dynamically I wasn't sure how to pass
  //            "this" to the function like I do in the HTML
  if(typeof(event.parentNode) === "undefined"){
    row = event.path[1];
  }else{
    row = r;
  }

  var rowID = '#' + row.id;

  //Grab the table ID
  var parentID = row.parentNode.parentNode.id;

  var rowData, tableRow, benchTable, availTable;

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availEquipmentList") {
    //Grab the table the row is moving OUT of
    availTable = $("#availEquipmentList").DataTable();

    //Capture the rows data and remove from the table
    rowData = availTable.row(rowID).data();
    availTable.row(rowID).remove().draw();

    //Grab the table the row is moving INTO and add it
    benchTable = $("#equipListBench").DataTable();
    benchTable.row.add(rowData).draw();

    //Grab the row through datatables API
    tableRow = benchTable.row(rowID).node();

    //Save to database
    save_equip(row);

  }else {
    benchTable = $("#equipListBench").DataTable();

    rowData = benchTable.row(rowID).data();
    benchTable.row(rowID).remove().draw();

    availTable = $("#availEquipmentList").DataTable();
    availTable.row.add(rowData).draw();

    tableRow = availTable.row(rowID).node();

    delete_equip(row);
  }

  //Add style and onclick event to row
  $(tableRow).addClass(" click-row").on("click", equipOnClick);

  //Add id and name classes to children
  $(tableRow).children()
      .first().addClass(" equipID")
      .next().addClass(" equipName");

}

function save_equip(row){
  //Get the data we are sending over
  var equipment_id = row.id;
  var equipment_name = row.getElementsByClassName("equipName")[0].innerText;

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
  //Get the data we are sending over
  var entryId = getEntryId();
  var equipment_id = row.getElementsByClassName("equipID")[0].innerText;

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

  $('.tablinks').on('click', function() {

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

  $('.tablinks').first().click();

  $('#equipSummaryTable').DataTable();
  $('#equipListBench').DataTable();
  $('#fileListBench').DataTable();
  $('#fileSummaryTable').DataTable();

  $('#availScientistList').DataTable();
  $('#scientistListBench').DataTable();

});

function refreshSummary(){

  var summaryTable = $('#equipListBench').clone();
  summaryTable.attr("id", "equipSummaryTable");

  var $equipSummaryTable = $('#equipSummaryTable');
  var $EquipSummary = $('#EquipSummary');

  $equipSummaryTable.remove();
  $EquipSummary.empty();//remove all content in div
  $EquipSummary.append("<h3 class='tabHeader'>Equipment</h3>");//add header
  $EquipSummary.append(summaryTable);//add table

  //Remove listener from each row, and click-row styling
  summaryTable.find(".click-row").each(function(){
    $(this).removeClass("click-row");
    $(this).prop('onclick', null).off('click');
  });

  //If there are no elements in the table this will fail
  try{
    $('#equipSummaryTable').DataTable();//go go datatable
  }catch(e){
    console.log(e.message);
  }


  summaryTable = $('#fileListBench').clone();
  summaryTable.attr("id", "fileSummaryTable");

  var $fileSummaryTable = $('#fileSummaryTable');
  var $FileSummary = $('#FileSummary');

  $fileSummaryTable.remove();
  $FileSummary.empty();
  $FileSummary.append("<h3 class='tabHeader'>Files</h3>");
  $FileSummary.append(summaryTable);

  //Remove listener from each row, and click-row styling
  summaryTable.find(".click-row").each(function(){
    $(this).removeClass("click-row");
    $(this).prop('onclick', null).off('click');
  });

  try{
    $('#fileSummaryTable').DataTable();
  }catch(e){
    console.log(e.message);
  }

  summaryTable = $('#scientistListBench').clone();
  summaryTable.attr("id", "scientistSummaryTable");

  var $scientistSummaryTable = $('#scientistSummaryTable');
  var $ScientistSummary = $('#ScientistSummary');

  $scientistSummaryTable.remove();
  $ScientistSummary.empty();
  $ScientistSummary.append("<h3 class='tabHeader'>Scientist</h3>");
  $ScientistSummary.append(summaryTable);

  //Remove listener from each row, and click-row styling
  summaryTable.find(".click-row").each(function(){
    $(this).removeClass("click-row");
    $(this).prop('onclick', null).off('click');
  });

  try{
    console.log('holl');
    $('#scientistSummaryTable').DataTable();
  }catch(e){
    console.log(e.message);
  }
}
