
from django.http import HttpResponse
from django.urls import path


from agenda import views
# Create your views here.
app_name = 'agenda'
urlpatterns = [    
    path('', views.listarTudo),
    path('editar/<int:id>/', views.editar),
    path('excluir/<int:id>/', views.excluir), 
    path('excluir/confirmar/<int:id>/', views.confirmarDelete), 
    path('add/', views.adicionar), 


]
