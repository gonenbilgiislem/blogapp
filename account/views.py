from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_request(request):
    context = {
        'title': 'Login',
        "kvkk_alert": "KVKK kapsamında kişisel verileriniz, sadece bu site içerisinde kullanılacaktır.Aydınlatma metnine ulaşmak için"}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context["error"] = "Kullanıcı adı veya parola hatalı"
            return render(request, 'account/login.html', context)
    return render(request, 'account/login.html', context)


def register_request(request):
    context = {
        'title': 'Register',
        'username': "username",
        'email': "email",
        'firstname': "firstname",
        'lastname': 'lastname',
        "kvkk_alert": "KVKK kapsamında kişisel verileriniz, sadece bu site içerisinde kullanılacaktır.Aydınlatma metnine ulaşmak için tıklayınız."
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'account/register.html',
                              {
                                  "error": "Bu kullanıcı adı zaten alınmış",
                                  "username": username,
                                  "email": email,
                                  "firstname": firstname,
                                  "lastname": lastname
                              })
            elif User.objects.filter(email=email).exists():
                context['error'] = "Bu email zaten alınmış"
                return render(request, 'account/register.html', context)
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,last_name=lastname)
                user.save()
            return redirect("login")
        else:
            return render(request, 'account/register.html', context)
    return render(request, 'account/register.html', context)


def logot_request(request):
    return redirect("home")
