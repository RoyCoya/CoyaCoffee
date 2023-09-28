from FapMaster.page.homepage import homepage
from FapMaster.api.log import add_log

# 主页
def page_homepage(request): return homepage(request)

# 打卡
def api_add_log(request): return add_log(request)