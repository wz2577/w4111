$(document).ready(function(){
    $("#search_query").append(query);

    if(data.length == 0){
        $("#content").append(" No Results Found ");
    }
    else{
        $.each(data, function(index, value){
        let name = value["name"]
        let id = value["game_id"]
        let ref = "/display/" + id
        let newLink = $("<a />", {
            name : "link",
            href : ref,
            text : name
        });
        $("#content").append(newLink);
        $("#content").append("<br/>");
    });
    }
})