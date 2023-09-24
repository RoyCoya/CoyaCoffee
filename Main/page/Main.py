from django.shortcuts import render

# 主页
def homepage(request):
    context = {
        
    }
    return render(request, 'Main/homepage/homepage.html', context)