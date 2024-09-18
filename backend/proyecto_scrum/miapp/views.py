from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm

def login_view(request):
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, '¡Has iniciado sesión con éxito!')
                return redirect('home')  # Redirige a la página 'home' después de iniciar sesión
                
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                
    return render(request, 'miapp/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Registro exitoso para {username}!')
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = UserRegistrationForm()
    return render(request, 'miapp/register.html', {'form': form})

def home(request):
    return render(request, 'miapp/home.html')  # Página a la que se redirige después del login

def index_view(request):
    return redirect('login')  # Redirige a la vista 'login'

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión con éxito.')
    return redirect('login')  # Redirige al login después de cerrar sesión

