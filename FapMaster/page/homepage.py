from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# 主页
@login_required(login_url=settings.LOGIN_URL)
def homepage(request):
    context = {}
    return render(request, "FapMaster/homepage/homepage.html", context)
