from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . import models, forms
from .forms import LoginForm


def registerView(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def authloginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def authLogoutView(request):
    logout(request)
    return redirect('users:login')


def user_list_view(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all().order_by('-id')
    return render(request, 'users/user_list.html', {'users': users})