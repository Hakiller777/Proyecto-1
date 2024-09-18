from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para login
    path('register/', views.register, name='register'),  # Ruta para registro
    path('home/', views.home, name='home'),  # Ruta para la página de inicio
     path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesió
]
