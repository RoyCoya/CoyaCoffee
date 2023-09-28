from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from FapMaster.models import FapLog

# 主页
@login_required
def homepage(request):
    # 所有记录
    logs = FapLog.objects.filter(user=request.user).order_by('-end_time')

    context = {
        'logs' : logs
    }
    return render(request, "FapMaster/homepage/homepage.html", context)