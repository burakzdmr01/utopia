from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('products:product_list')
        else:
            return render(request, 'users/login.html', {
                'error': 'Invalid username or password.',
                'username': username,
            })
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('products:product_list')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {
                'error': 'This username is already taken. Please choose another.'
            })
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('products:product_list')
    return render(request, 'users/signup.html')


@login_required
def profile_view(request):
    orders = request.user.orders.all()
    return render(request, 'users/profile.html', {'orders': orders})
