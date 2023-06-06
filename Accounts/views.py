from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your desired homepage URL
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password2']
        email = request.POST['email']
        try:
            User.objects.get(username=username)
            messages.error(request, 'Username is already taken.')
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your desired homepage URL
    
    return render(request, 'sign_up.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the name of your desired homepage URL
