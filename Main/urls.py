from django.urls import path

from . import views

app_name = 'Main'

# 页面
pages = [
	path('', views.index, name='index'),
]

# 接口
# apis = [
# 	path('api_index/', views.api_index, name=''),
# ]

urlpatterns = pages