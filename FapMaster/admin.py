from django.contrib import admin
from .models import FapLog, Preference

class admin_FapLog(admin.ModelAdmin):
	list_display = [
        'id',
		'user',
        'start_time',
		'end_time',
		'comments',
    ]
admin.site.register(FapLog, admin_FapLog)

class admin_Preference(admin.ModelAdmin):
	list_display = [
		'user',
        'publicize_log',
    ]
admin.site.register(Preference, admin_Preference)