from django.shortcuts import render


# Create your views here.
def login_request(request):
    return render(request, 'account/login.html')


def login_request(request):
    return render(request, 'account/register.html')


def login_request(request):
    return redirect("home")
