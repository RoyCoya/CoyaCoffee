$('#form_edit_profile').on('submit', function (e) {
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
        url: api_profile_update,
        type: 'post',
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
            alert(data.message);
            location.reload();
        },
        error: function (xhr, status, error) {
            var exception = "【" + xhr.status + "】" + xhr.responseJSON.message;
            alert(exception);
        }
    })
});