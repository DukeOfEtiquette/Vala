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
    val = $(this).children("span:first").text();
    var location = "/edit/" + val;
    window.location.href = location;
  });
  $("#id_project_id").bind('input propertychange', function() {
    value = this.value;
    var reg = new RegExp('^[A-z]{2}-[0-9]+$');
    eval = value.match(reg);
    if( eval ){
      $('#id_project_id').css('border','3px solid green');
        $('#create-project').prop('disabled', false);
    }else{
      $('#id_project_id').css('border','3px solid red')
        $('#create-project').prop('disabled', true);
    }
  })
});
