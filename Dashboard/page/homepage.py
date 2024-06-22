from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseBadRequest

from Main.api.utils import get_user
from Dashboard.models import BaseInfo
from FapMaster.models import Preference as FapMaster_pref, FapLog


# 主页
def homepage(request, user_name):
    User = get_user_model()
    if not User.objects.filter(username=user_name).exists():
        return HttpResponseBadRequest("该用户不存在")
    host = User.objects.get(username=user_name)
    visitor = request.user
    is_host = False
    if host == visitor:
        is_host = True
    host = get_user(host)

    context = {
        "host": host,
        "visitor": visitor,
        "is_host": is_host,
        'fap_records':getFapLog(host),
    }
    return render(request, "Dashboard/homepage/homepage.html", context)

# 获取FapMaster公开log
def getFapLog(user):
    if user.fapmaster_pref.publicize_log:
        fap_records = FapLog.objects.filter(user=user).order_by("-end_time")
        for record in fap_records: record.timestamp = int(round(record.end_time.timestamp(), 3) * 1000)
        return fap_records
    return None