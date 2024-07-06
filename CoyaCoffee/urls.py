from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from Main.page.Main import register

djangoURLs = [
    # admin后台
    path('admin/', admin.site.urls),
    # 用户模板
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create', register, name='register'),
]
    
publicAPPs = [
    path('', include('Main.urls')),
    path('qqgroup/', include('QQGroup.urls')),
    path('bulletin/', include('Bulletin.urls')),
    path('faq/', include('FAQ.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('tool/fapmaster/', include('FapMaster.urls')),
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
