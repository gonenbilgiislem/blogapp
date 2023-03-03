from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_request(request):
    context = {
        'title': 'Login',
        "error":"Kullanıcı adı veya şifre hatalı"
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'account/login.html',context)
    return render(request, 'account/login.html')


def register_request(request):
    context = {
        'title': 'Register'
    }
    return render(request, 'account/register.html',context)


def logot_request(request):
    return redirect("home")
