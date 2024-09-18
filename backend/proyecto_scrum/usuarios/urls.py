from django.urls import path
from . import views, home

urlpatterns = [
    path('', home.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
