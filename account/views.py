from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import Shopper
from store.models import Product

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Shopper.objects.filter(email=email).exists():
            messages.error(request, 'cet email est deja utilisé.')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')

    return render(request, 'account/signup.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print('error 1')
        # if not Shopper.objects.filter(email=email).exists():
        #     messages.error(request, 'cet email n\'existe pas.')
        # elif not Shopper.objects.filter(password=password).exists():
        #     messages.error(request, 'ce mot de passe n\'existe pas ou est incorrect.')
        try:
            if email == '':
                messages.error(request, 'entrer l\'email')
            elif password == '':
                messages.error(request, 'entrer le mot de passe')
            elif len(password) < 8:
                messages.error(request, 'le mot de passe doit contenir au moin 8 caracteres')
            else:
                print('error 2')
                user = authenticate(email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('index')
        except:
            pass
    return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
