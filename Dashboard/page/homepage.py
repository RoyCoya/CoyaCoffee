from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseBadRequest

from FapMaster.models import Preference as FapMaster_pref, FapLog


# 主页
def homepage(request, user_name):
    User = get_user_model()
    print(user_name)
    if not User.objects.filter(username=user_name).exists():
        return HttpResponseBadRequest("该用户不存在")
    host = User.objects.get(username=user_name)
    visitor = request.user
    is_host = False
    if host == visitor:
        is_host = True

    context = {
        "host": host,
        "visitor": visitor,
        "is_host": is_host,
        'fap_records':getFapLog(host),
    }
    return render(request, "Dashboard/homepage/homepage.html", context)

# 获取FapMaster公开log
def getFapLog(user):
    if not FapMaster_pref.objects.filter(user=user).exists():
        pref_fapmaster = FapMaster_pref.objects.create(user=user)
    pref_fapmaster = FapMaster_pref.objects.get(user=user)
    if pref_fapmaster.publicize_log:
        fap_records = FapLog.objects.filter(user=user).order_by("-end_time")
        for record in fap_records: record.timestamp = int(round(record.end_time.timestamp(), 3) * 1000)
        return fap_records
    return None