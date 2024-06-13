from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from app.urls import *
from app.views import *


def is_upper_in_word(word:str):
        for a in word:
            if a == a.upper():
                return True
        return False


def is_lower_in_word(word: str):
    for a in word:
        if a == a.lower():
            return True
    return False


def is_symbol_in_word(word):
    for a in word:
        if a == a.digit():
            return True
    return False


def authorization(request):
    message: str = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect('directory_list')
        else:
            message = "Неправильный логин или пароль"
    context = {
        'message': message,
    }
    return render(request, 'authorization.html', context)


def log_out(request):
    logout(request)
    return redirect('authorization')


def registration(request):
    message = None
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if User.objects.filter(email=email, is_active=True).exists():
                message = "Эта почта уже зарегистрирована"
            elif len(password1) < 8:
                message = "Пароль должен содержать не менее 8 символов"
            elif password1.isdigit():
                message = "Пароль не может быть полностью числовым"
            elif password1 != password2:
                message = "Пароли не совпадают"
            else:
                user = form.save(commit=False)
                user.set_password(password1)
                user.save()
                login(request, user)
                return redirect('directory_list')
        else:
            message = "Пожалуйста, исправьте ошибки в форме"

    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'registration.html', context)


