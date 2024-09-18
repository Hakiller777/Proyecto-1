from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),  # Cambia a la vista bienvenida
]
