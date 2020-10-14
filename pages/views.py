from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('index')
    else:
        return render(request, 'pages/home.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'pages/dashboard.html')

