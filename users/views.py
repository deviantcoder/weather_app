from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm


def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('/')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {
        'page': page,
    }

    return render(request, 'users/login_register.html', context)


def register_user(request):
    page = 'register'

    if request.user.is_authenticated:
        return redirect('/')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            messages.success(request, f'Welcome, {user.username}! You successfully signed up')
            return redirect('/')
        else:
            messages.error(request, 'Something went wrong...')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return redirect('users:login')