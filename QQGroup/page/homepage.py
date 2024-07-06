from django.shortcuts import render
import markdown
from django.contrib.staticfiles.storage import staticfiles_storage

def homepage(request):
    with open(staticfiles_storage.path('QQGroup/markdown/喵喵屋.md')) as f:
        html = markdown.markdown(f.read())
    context = {
        "html" : html
    }
    return render(request, "QQGroup/homepage/homepage.html", context)
