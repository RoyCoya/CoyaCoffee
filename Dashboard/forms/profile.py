from django import forms

class Profile(forms.Form):
    nickname = forms.CharField(max_length=10, required=False, label="昵称")
    email = forms.EmailField(required=False, label="邮箱")
    sex_choices = (
        ('M', '男'),
        ('F', '女'),
        ('B', '小男孩'),
        ('G', '小女孩'),
        ('H', '武装直升机'),
        ('C', '沃尔玛购物袋'),
        ('R', 'RockyRoo的小狗狗'),
        ('S', '不公开'),
    )
    sex = forms.ChoiceField(required=True, choices=sex_choices, initial='S', label="性别")
    biography = forms.CharField(max_length=50, required=False, label="个人签名")
    avator = forms.ImageField(required=False, label="头像")
