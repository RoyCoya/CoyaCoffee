from django.urls import path

from . import views

app_name = 'Dashboard'

# 页面
pages = [
	path('<str:user_name>/', views.page_homepage, name='homepage'),
]

# 接口
# apis = [
# 	path('api_index/', views.api_index, name=''),
# ]

urlpatterns = pages
# urlpatterns += apis