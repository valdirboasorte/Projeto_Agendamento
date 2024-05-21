from rolepermissions.roles import AbstractUserRole


class Professor(AbstractUserRole):
    available_permissions = {'ver_agendamento': True, 'ver_alunos': True, 'ver_agenda': True} 


class Aluno(AbstractUserRole):
    available_permissions = {'solocitar_agendamento': True, 'ver_agenda': True} 
    
    