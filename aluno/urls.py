from django.contrib import admin
from django.urls import path, include

from aluno import views

urlpatterns = [
    path('register/', views.register.as_view()),

]
