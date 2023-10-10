// 回忆打卡默认时间为现在
function setDateTime() {
    var now = new Date();
    var month = (now.getMonth() + 1).toString().padStart(2, "0");
    var day = now.getDate().toString().padStart(2, "0");
    var hour = now.getHours().toString().padStart(2, "0");
    var minute = now.getMinutes().toString().padStart(2, "0");
    var formattedDateTime = now.getFullYear() + "-" + month + "-" + day + "T" + hour + ":" + minute;
    $("#review_start_time").val(formattedDateTime);
    $("#review_end_time").val(formattedDateTime);
};

// 回忆打卡上传
$('#form_add_review_log').on('submit', function (e) {
    e.preventDefault();
    addLog($('#form_add_review_log').serialize())
});

// 时间字符串获取
function getTimeStr(seconds) {
    let hours = parseInt(seconds / (60 * 60));
    seconds -= hours * 60 * 60;
    let minutes = parseInt(seconds / 60);
    seconds = parseInt(seconds - minutes * 60);
    hours = hours.toString().padStart(2, "0");
    minutes = minutes.toString().padStart(2, "0");
    seconds = seconds.toString().padStart(2, "0");
    return [hours.toString(),minutes.toString(),seconds.toString()]
};

// Date对象转input格式
function formatDate(date) {
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    if(month < 10) month = '0' + month;
    if(day < 10) day = '0' + day;
    if(hour < 10) hour = '0' + hour;
    if(minute < 10) minute = '0' + minute;
    return year + '-' + month + '-' + day + 'T' + hour + ':' + minute;
}

// 计时打卡初始化
let timer;
function initTimer() {
    timer = setInterval(function () {
        let seconds = Number(localStorage.getItem("fap_total_seconds"))
        localStorage.setItem(
            "fap_total_seconds",
            seconds + 1
        )
        $("#time").text(getTimeStr(seconds).join(' : '));
    }, 1000);
};

// 计时打卡加载
function loadTimer() {
    if (localStorage.getItem("fap_start_time") != null && localStorage.getItem("fap_total_seconds") != null) {
        $("#timer").removeClass("d-none");
        $("#check").addClass("d-none");
        $("#time").text(getTimeStr(localStorage.getItem("fap_total_seconds")).join(' : '));
        if (!Number(localStorage.getItem("paused"))) {
            $("#timer_pause").removeClass("d-none");
            $("#timer_resume").addClass("d-none");
            initTimer()
        } else {
            $("#timer_pause").addClass("d-none");
            $("#timer_resume").removeClass("d-none");
            $("#time").text(getTimeStr(localStorage.getItem("fap_total_seconds")).join(' : '));
        }
    }
};

// 计时打卡开始
$("#timer_start").click(function (e) {
    $("#timer").removeClass("d-none");
    $("#check").addClass("d-none");
    $("#timer_pause").removeClass("d-none");
    $("#timer_resume").addClass("d-none");
    localStorage.setItem("fap_start_time", formatDate(new Date()));
    localStorage.setItem("fap_total_seconds", 0);
    localStorage.setItem("paused", 0)
    initTimer();
});

// 计时打卡暂停
$("#timer_pause").click(function (e) {
    clearInterval(timer);
    localStorage.setItem("paused", 1)
    $("#timer_pause").addClass("d-none");
    $("#timer_resume").removeClass("d-none");
});

// 计时打卡继续
$("#timer_resume").click(function (e) {
    initTimer();
    localStorage.setItem("paused", 0)
    $("#timer_pause").removeClass("d-none");
    $("#timer_resume").addClass("d-none");
});

// 计时打卡结束
let modal_add_timer_log = new bootstrap.Modal($('#modal_add_timer_log'), {keyboard: false})
$("#timer_stop").click(function (e) {
    clearInterval(timer)
    $("#timer_start_time").val(formatDate(new Date(localStorage.getItem("fap_start_time"))));
    $("#timer_end_time").val(formatDate(new Date()));
    let time = getTimeStr(Number(localStorage.getItem("fap_total_seconds")))
    $("#timer_duration_hours").val(time[0]);
    $("#timer_duration_minutes").val(time[1]);
    $("#timer_duration_seconds").val(time[2]);
    modal_add_timer_log.show();
});

// 计时打卡结束页面取消，继续计时
$("#modal_add_timer_log").on('hide.bs.modal', function () {
    initTimer()
});

// 计时打卡上传
$('#form_add_timer_log').on('submit', function (e) {
    e.preventDefault();
    $("#timer").addClass("d-none");
    $("#check").removeClass("d-none");
    addLog($('#form_add_timer_log').serialize())
    localStorage.removeItem("paused")
    localStorage.removeItem("fap_start_time")
    localStorage.removeItem("fap_total_seconds")
})