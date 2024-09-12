from django.contrib import admin
from django.urls import path, include
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta para la página principal
    path('miapp/', include('miapp.urls')),  # Incluye las rutas de la aplicación miapp
]

