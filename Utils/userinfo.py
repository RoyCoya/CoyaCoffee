from Dashboard.models import BaseInfo
from FapMaster.models import Preference as FapMasterPref
import os

# 组装用户的所有app下preference
def get_user(user):
    if not BaseInfo.objects.filter(user=user).exists(): BaseInfo.objects.create(user=user)
    if not FapMasterPref.objects.filter(user=user).exists(): FapMasterPref.objects.create(user=user)

    user.base_info = BaseInfo.objects.get(user=user)
    user.fapmaster_pref = FapMasterPref.objects.get(user=user)
    return user

def delete_file(path):
    try: os.remove(path)
    except: pass