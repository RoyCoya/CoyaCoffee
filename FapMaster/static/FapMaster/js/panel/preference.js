// Fap Master Preference
$('#form_preference input, #form_preference select, #form_preference textarea').on('change', function() {
    $("#ctl_FapMaster").removeClass("d-none");
});

$('#form_preference').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: api_FapMaster_preference_update,
        type: 'post',
        data: $('#form_preference').serialize(),
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