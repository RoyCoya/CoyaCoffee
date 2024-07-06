from django.shortcuts import render
from Utils import markdown

app = "Bulletin"

def homepage(request):
    context = {
        "Main": markdown.readmd(app, "Main"),
        "Bulletin": markdown.readmd(app, "Bulletin"),
        "QQGroup": markdown.readmd(app, "QQGroup"),
        "FapMaster": markdown.readmd(app, "FapMaster"),
        "Dashboard": markdown.readmd(app, "Dashboard"),
    }
    return render(request, "Bulletin/homepage/homepage.html", context)
