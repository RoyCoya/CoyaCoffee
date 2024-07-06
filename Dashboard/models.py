from django.db import models
from django.contrib.auth import settings

from Main.api.file_path_converter import user_img_path

class BaseInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='所属用户')
    sex_choices = (
        ('M', '男'),
        ('F', '女'),
        ('B', '小男孩'),
        ('G', '小女孩'),
        ('H', '武装直升机'),
        ('C', '沃尔玛购物袋'),
        ('R', 'RR的狗'),
        ('S', '不公开'),
    )
    sex = models.CharField(default='S', max_length=1, choices=sex_choices, verbose_name='性别')
    biography = models.CharField(null=True, blank=True,max_length=200, verbose_name='个签')
    avator = models.ImageField(null=True, blank=True, upload_to=user_img_path, verbose_name='头像')
