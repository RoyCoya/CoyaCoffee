# 动态创建用户相关的子目录
def user_img_path(instance, filename):
    return f'{instance.user.username}/{filename}'
