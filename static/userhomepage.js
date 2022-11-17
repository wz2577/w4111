$(document).ready(function(){
    $("#name").append(data["user_name"]);


    let buys = data["buys"];
    for (let i = 0; i < buys.length; i++) {
        let buy_info = buys[i]
        let ref = "/display/" + buy_info["game_id"]
        let newLink = $("<a />", {
            name : "link",
            href : ref,
            text : buy_info["game_name"]
        });
        let name= $("<div class='name'>");
        name.html(newLink)

        let score= $("<div class='score'>");
        let score_text = "This person gives " + buy_info["score"] + " to this game!"
        score.text(score_text)

        $("#buy").append(name);
        $("#buy").append(score);
        $("#buy").append("<br/>");
    }
    // let keywords = video["key_word"]
    // $.each(keywords, function(index, value){
    //     keyword = value;
    //     if(index != keywords.length-1){
    //         keyword = keyword + ", ";
    //     }
    //     $("#keywords").append(keyword);
    // });
})