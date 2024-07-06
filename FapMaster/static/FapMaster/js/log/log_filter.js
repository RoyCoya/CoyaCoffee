// 加载
$(document).ready(function () {
    if (year == null) return;
    $("#select_year").val(year);
    $("#tip").addClass("d-none");
    if (year != 0) {
        $("#select_month").removeClass("d-none");
        $("#label_select_month").removeClass("d-none");
        $("#select_month").val(0);
    }
    if (month != null) {
        $("#select_month").val(month);
    }
});

// 年份筛选
$("#select_year").change(function (e) {
    parameters = ""
    year = parseInt(this.value)
    switch (year) {
        case -1: break;
        case 0:
            parameters += "all=1";
            break;
        default:
            parameters += "year=" + year;
            break;
    }
    window.location.replace(url_log + parameters)
});

// 月份筛选
$("#select_month").change(function (e) {
    parameters = "year=" + year + "&"
    month = parseInt(this.value);
    if (month != 0) parameters += "month=" + month;
    window.location.replace(url_log + parameters);
});

// 重置筛选
$("#reset").click(function (e) { 
    window.location.replace(url_log)
});