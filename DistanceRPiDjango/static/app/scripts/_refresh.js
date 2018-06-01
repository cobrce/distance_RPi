$(function () {
    update();
});
function update() {
    $.post("/", { "read": true }, function (result) {
        $('#dist').html(result);
    });
    setTimeout("update()", 200);
}