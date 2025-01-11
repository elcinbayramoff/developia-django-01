from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #Varsa istifadecini yoxdursa None
        if user is not None:
            login(request, user)
            return redirect('tasks')
    
    
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return render(request, 'account/register.html')

            
        if len(password) < 8:
            messages.error(request, 'Must be at least 8 characters')    
            return render(request, 'account/register.html')

        if User.objects.filter(username=username).exists() == True:
            messages.error(request, 'Username is already taken')
            return render(request, 'account/register.html')
  
        user = User.objects.create_user(username, email, password)
        Profile.objects.create(user=user)
        login(request, user)
        messages.success(request, 'Profile created succesfully')
        return redirect('tasks')
    
    if request.method == 'GET':
        return render(request, 'account/register.html')