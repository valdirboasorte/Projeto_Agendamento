from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db import Error
from django.core.exceptions import ObjectDoesNotExist
from .models import Agenda
from django.contrib.auth.decorators import login_required

from .forms import AgendaForm


#Vai listar tudo
@login_required
def listarTudo(request):
    user = request.user
    agenda = Agenda.objects.all()
    return render(
        request,
        'global/templates/agenda/listarTudo.html',
        {'agendas': agenda, 'user': user}
    )

@login_required
def editar(request, id):

    #pego os dados do banco referente aquele contact
    agenda = Agenda.objects.get(pk=id)

    if request.method == 'POST':
        # return HttpResponse('Vai salvar no banco')
        #Salva os valores obtidos pelo metodo post informando também que é um aluno existente

        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/?msg=salvo')
    else:
        form = AgendaForm(instance=agenda)

    return render(
        request,
        'global/templates/agenda/editar.html',
        #enviando variaveis
        {
            'form': form,
            'id_agenda': id
         }
    )

@login_required
def adicionar(request):
    #verificar se está chegando a partir do metodo, pelos metodos get e post
    if request.method == 'POST':
        # return HttpResponse('Vai salvar no banco')
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/?msg=salvo')
    else:
        form = AgendaForm()

    return render(
        request,
        'global/templates/agenda/adicionar.html',
        {'forms': form},
    )

#confirma se o usuário realmente quer excluir esse registro
@login_required
def confirmarDelete(request, id):
    agenda = Agenda.objects.get(pk=id)

    return render(
    request,
    'global/templates/agenda/confirmarExcluir.html',
    {'agenda': agenda}
    )

@login_required
def excluir(request, id):
    contact = Agenda.objects.get(pk=id).delete()

    return HttpResponseRedirect('/agenda/')
