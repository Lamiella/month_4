from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models, forms
from .forms import LoginForm
from django.views import generic

#Register
class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomRegisterForm()
        return render(request, 'users/register.html', {"form": form})
    def post(self, request):
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/register.html', {"form": form})


#Login
class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
         form = AuthenticationForm(data=request.POST)
         if form.is_valid:
             user = form.get_user()
             login(request, user)
             return redirect("users:user_list")
         return render(request, 'users/login.html', {'form': form})


#Logout
class AuthLogoutView(generic.View):
    def get(self, request):
        logout()
        return redirect("users:logout")


def user_list_view(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all().order_by('-id')
    return render(request, 'users/user_list.html', {'users': users})


# def registerView(request):
#     if request.method == 'POST':
#         form = forms.CustomRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomRegisterForm()
#     return render(request, 'users/register.html', {'form': form})
#
#
# def authloginView(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('users:user_list')
#     else:
#         form = LoginForm()
#     return render(request, 'users/login.html', {'form': form})
#
#
# def authLogoutView(request):
#     logout(request)
#     return redirect('users:login')