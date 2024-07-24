from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from . forms import LoginForm
# Create your views here.

def user_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect("home:home_page")        
    context = {"loginform": form}
    return render(request, 'home/user_login.html', context)


def home_page(request):
    return render(request, 'home/home_page.html')

def user_logout(request):
    auth.logout(request)
    return redirect("home:user_login")