import pytz
from datetime import datetime, timezone

from django.shortcuts import render
from django.db.models import Max, F
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from FapMaster.models import FapLog, Preference
from Main.api.utils import get_user


# 主页
@login_required
def homepage(request):
    # 个人记录
    logs = FapLog.objects.filter(user=request.user).order_by("-end_time")
    # 给记录增加时间戳
    for log in logs: log.timestamp = int(round(log.end_time.timestamp(), 3) * 1000)
    print(datetime.now(tz=timezone.utc))
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
        "logs" : logs,
        "nofap_rank" : nofap_rank,
    }
    return render(request, "FapMaster/homepage/homepage.html", context)
