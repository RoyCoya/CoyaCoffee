from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from Dashboard.forms.profile import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from Utils.userinfo import get_user, delete_file

@login_required
def update(request):
    try:
        user = get_user(request.user)
        form = Profile(request.POST,request.FILES)
        if not form.is_valid(): raise Exception('非法表单内容')
        
        nickname = form.cleaned_data['nickname']
        email = form.cleaned_data['email']
        sex = form.cleaned_data['sex']
        biography = form.cleaned_data['biography']
        avator = form.cleaned_data['avator']
        
        user.first_name = nickname
        user.email = email
        user.base_info.sex = sex
        user.base_info.biography = biography
        if avator:
            old = user.base_info.avator
            if old: delete_file(old.path)
            user.base_info.avator = avator

        user.save()
        user.base_info.save()

        # publicize_log = form.cleaned_data['publicize_log']
        pass
        # pref : Preference = get_user(request.user).fapmaster_pref
        # pref.publicize_log = publicize_log
        # pref.save()

    except Exception as e: return JsonResponse({"message": str(e)}, status=503)
    return JsonResponse({"message": "个人资料更新成功！"})