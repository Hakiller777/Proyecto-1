from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirecciona a la página de inicio
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirecciona a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirecciona a la página de inicio
