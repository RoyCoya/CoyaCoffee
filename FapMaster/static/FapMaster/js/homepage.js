// 设置默认打卡时间为现在
function setDateTime() {
    var now = new Date();
    var month = (now.getMonth() + 1).toString().padStart(2, '0');
    var day = now.getDate().toString().padStart(2, '0');
    var hour = now.getHours().toString().padStart(2, '0');
    var minute = now.getMinutes().toString().padStart(2, '0');
    var formattedDateTime = now.getFullYear() + '-' + month + '-' + day + 'T' + hour + ':' + minute;
    $('#start_time').val(formattedDateTime);
    $('#end_time').val(formattedDateTime);
}

$(document).ready(function () {
    setDateTime();
});