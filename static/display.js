$(document).ready(function(){
    $("#name").append(data["name"]);
    let genra = ""
    for (let i = 0; i < data["genra"].length; i++) {
      genra += data["genra"][i];
      if(i != data["genra"].length - 1){
          genra += ", "
      }
    }
    $("#genra").append(genra);
    $("#release_date").append(data["release_date"]);
    $("#about").append(data["about_this_game"]);
    let link_ref = "/patch/" + data["game_id"]
    let patch_link = $("<a />", {
        name : "link",
        href : link_ref,
        text : "Patch History"
    });
    $("#patch").append(patch_link);
    $("#rating").append(data["rating"]);

    let comments = data["comments"];
    for (let i = 0; i < comments.length; i++) {
        let comment_info = comments[i]
        let ref = "/userhomepage/" + comment_info["user_id"]
        let newLink = $("<a />", {
            name : "link",
            href : ref,
            text : comment_info["name"]
        });
        let name= $("<div class='name'>");
        name.html(newLink)

        let content= $("<div class='content'>");
        let content_text = comment_info["content"]
        content.text(content_text)

        let date= $("<div class='date'>");
        let date_text = comment_info["since"]
        date.text(date_text)

        $("#comments").append(name);
        $("#comments").append(content);
        $("#comments").append(date);
        $("#comments").append("<br/>");
    }
})