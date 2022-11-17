$(document).ready(function(){
    $.each(data, function(index, value){
        let ref = "/display/" + value["game_id"]
        let newLink = $("<a />", {
            name : "link",
            href : ref,
            text : value["name"]
        });
        $("#content").append(newLink);
        $("#content").append("<br/>");
    });
})