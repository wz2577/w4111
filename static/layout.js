$(document).ready(function(){
    $("#form").submit(function(e){
      let input = $('#form :input').val();
      if(!(/^\s+$/.test(input)) && input.length != 0){
        return true;
      }
      else{
        $("#query").val("");
        $("#query").focus();
        return false;
      }
    });
  });