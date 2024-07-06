from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from FapMaster.forms.preferences import FapMaster as pref_FapMaster
from FapMaster.models import Preference
from Utils.userinfo import get_user


@login_required
def update(request):
    try:
        form = pref_FapMaster(request.POST)
        if not form.is_valid(): raise Exception('非法表单内容')
        
        publicize_log = form.cleaned_data['publicize_log']
        
        pref : Preference = get_user(request.user).fapmaster_pref
        pref.publicize_log = publicize_log
        pref.save()

    except Exception as e: return JsonResponse({"message": str(e)}, status=503)
    return JsonResponse({"message": "设置保存成功！"})