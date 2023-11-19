from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already taken")
                return redirect('credential:register')
            else:
                usr = User.objects.create_user(username=uname, password=pwd)
                usr.save()
                messages.success(request, "User created successfully!")
                return redirect('credential:login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('credential:register')
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username=uname, password=pwd)

        if user is not None:
            auth_login(request, user)
            return redirect('homepage:form')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('credential:login')
    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return redirect('/')
