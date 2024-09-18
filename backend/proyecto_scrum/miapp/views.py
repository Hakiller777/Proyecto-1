from django.shortcuts import render

def bienvenida(request):
    return render(request, 'miapp/bienvenida.html')
