import pytz
import calendar
from datetime import timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render

from FapMaster.models import FapLog

# 所有记录
@login_required
def log(request):
    # 默认30天内的记录
    all_logs = FapLog.objects.filter(user=request.user).order_by('-end_time')
    thirty_days_ago = timezone.now() - timedelta(days=30)
    logs = all_logs.filter(end_time__gte=thirty_days_ago)
    # 备选年月
    years = [i for i in range(2022, datetime.now().year + 1)]
    years.reverse()
    monthes = [1,2,3,4,5,6,7,8,9,10,11,12]
    # TODO: all和单独年情况下的翻页功能
    # 查询全部
    get_all = request.GET.get('all')
    all = False
    if get_all:
        all = True
        logs = all_logs
    # 查询特定年份
    year = request.GET.get('year')
    if year:
        year = int(year)
        year_start = pytz.timezone('Asia/Shanghai').localize(datetime(year, 1, 1))
        year_end = pytz.timezone('Asia/Shanghai').localize(
            datetime(year, 12, 31, 23, 59, 59)
        )
        logs = all_logs.filter(
            end_time__gte=year_start,
            end_time__lte=year_end,
        )
    # 查询特定月份
    month = request.GET.get('month')
    if year and month:
        month = int(month)
        month_start = pytz.timezone('Asia/Shanghai').localize(datetime(year, month, 1))
        month_end = pytz.timezone('Asia/Shanghai').localize(
            datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
        )
        logs = logs.filter(
            end_time__gte=month_start,
            end_time__lte=month_end,
        )

    context = {
        'logs': logs,
        'all' : all,
        'year': year,
        'years' : years,
        'month' : month,
        'monthes' : monthes,
    }
    return render(request, 'FapMaster/log/log.html', context)
