from django.db import models
from django.contrib.auth import settings

class FapLog(models.Model):
    """The records of masturbation

    # Fields
    id: auto increase
    user: the one record belongs to
    start_time: auto calculated by end_time and duration
    end_time: defalt datetime.now (fetch in frontend, since you might rest for a while before you record your job)
    duration: timedelta type
    comments: max length 200
    """
    id = models.AutoField(primary_key=True, verbose_name='记录id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    duration = models.DurationField(null=True, blank=True, verbose_name='持续时间')
    comments = models.CharField(null=True, blank=True, max_length=200, verbose_name='备注')

class Preference(models.Model):
    # TODO: 补一下注释
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    publicize_log = models.BooleanField(default=False, verbose_name='公开FapMaster记录')