from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

djangoURLs = [
    path('admin/', admin.site.urls),
]
    
publicAPPs = [
    path('', include('Main.urls')),
    path('fap_master/', include('FapMaster.urls')),
]
    
privateAPPs = [

]
    
urlpatterns = djangoURLs + publicAPPs + privateAPPs

# 开发时可显示用户文件
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^userfile/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]