from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from Utils import markdown

# 主页
def homepage(request):
    update = markdown.readmd('Bulletin', 'Main')
    context = {
        "update": update
    }
    return render(request, 'Main/homepage/homepage.html', context)

# 注册
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('Main:homepage'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/create.html', {'form': form})
