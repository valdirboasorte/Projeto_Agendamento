from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('usuario/', views.criar_usuario),
    path('', views.home),
    
]
