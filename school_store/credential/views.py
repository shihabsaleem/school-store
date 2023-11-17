from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            else:
                usr = User.objects.create_user(username=uname, password=pwd)
                usr.save()
                print("user created !!")
                return redirect('login')
        else:
            print("error in user creation...")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')