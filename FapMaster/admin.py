from django.contrib import admin
from .models import FapLog

class admin_FapLog(admin.ModelAdmin):
	list_display = [
        'id',
		'user',
        'start_time',
		'end_time',
		'comments',
    ]
admin.site.register(FapLog, admin_FapLog)