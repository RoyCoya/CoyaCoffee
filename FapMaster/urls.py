from django.urls import path

from . import views

app_name = 'FapMaster'

# 页面
pages = [
	path('', views.page_homepage, name='homepage'),
    path('log/', views.page_log, name='log'),
]

# 接口
apis = [
	path('api/add_log/', views.api_add_log, name='api_add_log'),
]

urlpatterns = pages + apis