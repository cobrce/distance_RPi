$(document).ready(function () {
    $("#stop").click(function () {
        if ($("#stop").text() == "Suspend") {
            $.post("/", { "stop": 1 });
            $("#stop").text("Resume");
        }
        else {
            $.post("/", { "stop": 0 });
            $("#stop").text("Suspend");
        }
    });
});