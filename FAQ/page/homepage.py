from django.shortcuts import render

app = "FAQ"

def homepage(request):
    context = {

    }
    return render(request, "FAQ/homepage/homepage.html", context)
