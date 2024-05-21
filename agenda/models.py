from django.db import models
from django.utils import timezone


#id (primay key - automático)
# Create your models here.

class Agenda(models.Model):
    data_da_agenda = models.DateField()
    data_de_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    status = models.BooleanField(default=False) 
    
