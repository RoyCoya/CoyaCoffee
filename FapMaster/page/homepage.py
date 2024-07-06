from datetime import datetime, timezone

from django.shortcuts import render
from django.db.models import Max, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from FapMaster.models import FapLog, Preference
from Utils.userinfo import get_user


# 主页
def homepage(request):
    user = request.user
    # 个人记录
    preference = None
    if user.is_authenticated:
        my_logs = FapLog.objects.filter(user=request.user).order_by("-end_time")
        try: preference = Preference.objects.get(user=user)
        except: preference = Preference.objects.create(user=user)
        # 给记录增加时间戳
        for log in my_logs: log.timestamp = int(round(log.end_time.timestamp(), 3) * 1000)
    else: my_logs = None
    users_whom_public_log = [pref.user for pref in Preference.objects.filter(publicize_log=True)]
    logs = FapLog.objects.filter(user__in=users_whom_public_log).order_by("-end_time")[0:30]
    # nofap_duration排行榜
    users_shared_log = [preference.user for preference in Preference.objects.filter(publicize_log=True)]
    rank_duration = FapLog.objects.filter(user__in=users_shared_log).values('user').annotate(
        latest_end_time=Max('end_time'),
        nofap_duration = datetime.now() - F('latest_end_time')
    ).order_by('-nofap_duration')[:3]
    nofap_rank = []
    for rank in rank_duration:
        user = get_user_model().objects.get(id=rank['user'])
        user = get_user(user)
        user.duration = rank['nofap_duration']
        nofap_rank.append(user)
    
    context = {
        "my_logs" : my_logs,
        "preference" : preference,
        "logs" : logs,
        "nofap_rank" : nofap_rank,
    }
    return render(request, "FapMaster/homepage/homepage.html", context)
