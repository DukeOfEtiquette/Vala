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
        location = "/view/"+val;
        console.log(locaton);
        window.location.href = location;
    });
});

function removeFile(){
    var parent = document.getElementById("file_list");
    var child = document.getElementById("file1");
    parent.removeChild(child);
}

var nItem = 1;

function addFileButton(){
    var fileItem = document.createElement('li');
    fileItem.setAttribute("id", nItem.toString());
    nItem++;

    var str = "File: <input type=\'file\'><button type=\'button\' onclick=\'removeFile()\' class=\'remove_file\'>X</button>";
    fileItem.innerHTML = str;

    //var addButton = document.createElement("INPUT");
    //addButton.setAttribute("type", "".concat("file", nItem.toString()));

    var x = document.getElementById("file_list");
    x.append(fileItem);

    //openTab(evt, "files");
}

function openTab(evt, cityName) {
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
    document.getElementById(cityName).style.display = "inline-block";
    evt.currentTarget.className += " active";
}
