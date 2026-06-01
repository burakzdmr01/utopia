from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import LoginForm, SignupForm


def login_view(request):
    """Handles user login with form validation."""
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user     = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('products:product_list')
        else:
            return render(request, 'users/login.html', {
                'form':  form,
                'error': 'Invalid username or password.',
            })
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """Logs out the current user."""
    logout(request)
    return redirect('products:product_list')


def signup_view(request):
    """Handles user registration with form validation."""
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {
                'form':  form,
                'error': 'This username is already taken.'
            })
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('products:product_list')
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile_view(request):
    """Displays user profile and order history."""
    orders = request.user.orders.all()
    return render(request, 'users/profile.html', {'orders': orders})
