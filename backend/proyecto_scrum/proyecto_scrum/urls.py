from django.contrib import admin
from django.urls import path, include  # Agregar include para incluir las rutas de miapp
from miapp.views import index_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'), # Esta ruta ahora redirige a la vista de login
    path('', include('miapp.urls')),  # Incluir las rutas de 'miapp'
]




