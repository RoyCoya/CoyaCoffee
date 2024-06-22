// 上传记录
function addLog(data) {
    $.ajax({
        url: api_add_log,
        type: 'post',
        data: data,
        success: function (data) {
            alert(data.message);
            location.reload();
        },
        error: function (xhr, status, error) {
            var exception = "【" + xhr.status + "】" + xhr.responseJSON.message;
            alert(exception);
        }
    })
}
