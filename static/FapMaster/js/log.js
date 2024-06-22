$('#modal_add_log').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: api_add_log,
        type: 'post',
        data: $('#form_add_log').serialize(),
        success: function (data) {
            alert(data.message);
            location.reload();
        },
        error: function (xhr, status, error) {
            var exception = "【" + xhr.status + "】" + xhr.responseJSON.message
            alert(exception)
        }
    })
})