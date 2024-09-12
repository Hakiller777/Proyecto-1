from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de inicio de miapp")

def home(request):
    return HttpResponse("Bienvenido a la página principal de miapp")

