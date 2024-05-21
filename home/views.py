from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role, get_user_roles#determinado grupo de usuário
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.permissions import revoke_permission, grant_permission
# Create your views here.

#@has_permission_decorator('ver_agenda') #Se eu colocar Aluno não terei acesso n
def home(request):
       
    #grant_permission(request.user, 'ver_alunos')
    print(get_user_roles(request.user))

    return render(
        request, 
        'home/home.html'

    )

def criar_usuario(request):
    user = User.objects.create_user(username='Professor4', password='1234')
    user.save()
    assign_role(user, 'professor')
    return HttpResponse('Usuário salvo')
