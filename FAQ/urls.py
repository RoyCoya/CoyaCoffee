from django.urls import path

from . import views

app_name = 'FAQ'

# 页面
pages = [
	path('', views.page_homepage, name='homepage'),
    # path('log/', views.page_log, name='log'),
]

# 接口
apis = [
	# path('api/log/add/', views.api_add_log, name='api_add_log'),
    # path('api/preference/update/', views.api_preference_update, name='api_preference_update')
]

urlpatterns = pages + apis
