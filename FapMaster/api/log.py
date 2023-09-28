import datetime
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from FapMaster.models import FapLog

@login_required
def add_log(request):
    try:
        start_time = None
        end_time = datetime.datetime.strptime(
            request.POST.get("end_time"), "%Y-%m-%dT%H:%M"
        )
        duration = request.POST.get("duration")
        comments = request.POST.get("comments")
        duration = timedelta(minutes=int(duration))

        start_time = end_time - duration
        FapLog.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            comments=comments,
        )
    except Exception as e: return JsonResponse({"message": e}, status=503)

    return JsonResponse({"message": "打卡成功！"})