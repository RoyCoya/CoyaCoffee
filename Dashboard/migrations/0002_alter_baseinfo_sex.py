# Generated by Django 4.2.4 on 2024-07-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='sex',
            field=models.CharField(choices=[('M', '男'), ('F', '女'), ('B', '小男孩'), ('G', '小女孩'), ('H', '武装直升机'), ('C', '沃尔玛购物袋'), ('R', 'RR的狗'), ('S', '不公开')], default='S', max_length=1, verbose_name='性别'),
        ),
    ]
