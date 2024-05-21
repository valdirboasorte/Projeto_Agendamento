from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = [
            'data_da_agenda',
            'data_de_criacao',
            'descricao',
            'status',
        ]

        labels = {
            'data_da_agenda': 'Data da Agenda',
            'data_de_criacao': 'Data de Criação',
            'descricao': 'Descrição',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione a classe CSS para o campo data_da_agenda
        self.fields['data_da_agenda'].widget.attrs.update({'type': 'date'})