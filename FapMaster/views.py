from FapMaster.page.homepage import homepage
from FapMaster.page.log import log

from FapMaster.api.log import add_log

# 页面
def page_homepage(request): return homepage(request)
def page_log(request): return log(request)

# 接口
def api_add_log(request): return add_log(request)