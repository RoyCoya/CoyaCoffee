from Dashboard.page.homepage import homepage
from Dashboard.api.profile import update
from django.http.response import HttpResponse

# 页面
def page_public(request): return HttpResponse("dashboard public")
def page_homepage(request, user_name): return homepage(request, user_name)

# 接口
def api_profile_update(request): return update(request)