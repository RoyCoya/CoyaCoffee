// Fap Master Preference
$('#form_FapMaster input, #form_FapMaster select, #form_FapMaster textarea').on('change', function() {
    $("#ctl_FapMaster").removeClass("d-none");
});

$('#form_FapMaster').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: api_FapMaster_preference_update,
        type: 'post',
        data: $('#form_FapMaster').serialize(),
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