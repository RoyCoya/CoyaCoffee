from django.shortcuts import render

# 主页
def homepage(request):
    
    context = {
        
    }
    return render(request, 'FapMaster/homepage/homepage.html', context)