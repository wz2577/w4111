$(document).ready(function(){
    if(data.length == 0){
        $("#patch_notes").append("No Patch Notes Found ");
    }
    else{
        $.each(data, function(index, value){
        let name = "Patch Name: " + value["patch_name"]
        let note = "Patch Note: " + value["patch_notes"]
        let date = "Release Date: " + value["release_date"]
        $("#patch_notes").append(name)
        $("#patch_notes").append("<br/>")
        $("#patch_notes").append(note)
        $("#patch_notes").append("<br/>")
        $("#patch_notes").append(date)
        $("#patch_notes").append("<br/>")
        $("#patch_notes").append("<br/>")
    });
    }
})