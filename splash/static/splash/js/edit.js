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
  var row = event.currentTarget;
  console.log(row);

  //Grab the table ID
  var parentID = event.parentNode.parentNode.parentNode.id;

  //Grab the row that was selected
  var row = event.parentNode.parentNode;

  //Remove it from current table
  row.remove();

  //See if we are in the available equipment list, or the workbench
  if(parentID === "fileEquipmentList")
  {
    var workBench = $("#fileListBench");
    workBench.append(row);
    save_equip();

  }else {
    var equipList = $("#fileEquipmentList");
    equipList.append(row);
    row.checked = false;
    delete_equip(row);
  }
}

function equipOnClick(event) {
  var row = event.currentTarget;
  console.log(row);
  //Grab the table ID
  var parentID = event.parentNode.parentNode.parentNode.id;

  //Grab the row that was selected
  var row = event.parentNode.parentNode;
  //console.log(row);
  //Remove it from current table
  row.remove();

  //See if we are in the available equipment list, or the workbench
  if(parentID === "availEquipmentList")
  {
    var workBench = $("#equipListBench");
    workBench.append(row);
    save_equip();

  }else {
    var equipList = $("#availEquipmentList");
    equipList.append(row);
    row.checked = false;
    delete_equip(row);
  }
}

function delete_equip(row){
  var equipment_id = row.getElementsByClassName("equipID")[0].innerText;

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

function save_equip() {
  //Get the data we are sending over
  var list_of_ids = $('#equipListBench').find(".equipID");
  var list_of_names = $('#equipListBench').find(".equipName");

  //Get the project ID
  var entryId = getEntryId();

  //Initialize some arrays to hold the data to be saved
  var equipmentIDs = [];
  var equipmentNames = [];

  //Add data to a couple arrays
  for(var i = 0; i < list_of_ids.length; i++)
  {
    equipmentIDs.push(list_of_ids[i].innerText);
    equipmentNames.push(list_of_names[i].innerText);
  }

  // Get all elements with class="tablinks" and find out what tab we are on
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    if(tablinks[i].className.match(" active"))
    {
      activeTab = i;
    }
  }

  //Save the name of the active tab so we can construct our url
  if(activeTab != undefined) {
    var slug = tablinks[activeTab].innerHTML;
  }

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
    data: { entry_id: entryId,
            'equipmentIDs[]': equipmentIDs,
            'equipmentNames[]': equipmentNames }

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
      var newRow = "<li class='tableRow equipment-row'> " +
          "<span class='tableCell' id='equipCheckCell'><input type='checkbox' class='rowCheckBox' onclick='equipOnClick(this)'/></span> " +
          "<span class='tableCell equipID' id=" + equipID + ">" + equipID + "</span> "+
          "<span class='tableCell equipName'>" + equipName + "</span></li>";

      //Add the row to the task list
      $("#availEquipmentList").append(newRow);
    }
  }
}

function isEquipmentOnBench(equipId)
{
  //Get all equipment IDs already associated with this project
  var list_of_ids = $('#equipListBench').find(".equipID");

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
      var newRow = "<li class='tableRow file-row'> " +
          "<span class='tableCell' id='fileCheckCell'><input type='checkbox' class='rowCheckBox' onclick='equipOnClick(this)'/></span> " +
          "<span class='tableCell fileID' id=" + fileID + ">" + fileID + "</span> "+
          "<span class='tableCell fileName'>" + fileName + "</span></li>";

      //Add the row to the task list
      $("#availFileList").append(newRow);
    }
  }
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

      if(tableaving != undefined){
        var slug = tablinks[tableaving].innerHTML;
        console.log(slug);
        var csrf_token = getCookie('csrftoken');
      }

      // Show the current tab, and add an "active" class to the link that opened the tab
      document.getElementById(this.textContent).style.display = "inline-block";
      this.className += " active";
  });

  //TODO(Adam): Uncomment after Equipment tab demo
  //$(".tablinks").first().click();

  //TODO(Adam): Remove after Equipment tab demo
  $("a:contains('Equipment')").click();

});

