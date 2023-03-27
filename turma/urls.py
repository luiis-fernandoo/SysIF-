from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('', views.dashboard_turma, name='dashboard'),
    path('cadastrar/', views.cadastrar_turma, name='cadastrar'),
    path('editar/<int:id>', views.editar_turma, name='editar'),
    path('deletar/<int:id>', views.deletar_turma, name='deletar'),
    path('avaliacao/', views.dashboard_avaliacao, name='dashboardAvaliacao'),
    path('lancarAvaliacao/', views.lancar_avaliacao, name='lancarAvaliacao'),
    path('editarAvaliacao/<int:id>', views.editar_avaliacao, name='editarAvaliacao'),
    path('deletarAvaliacao/<int:id>', views.deletar_avaliacao, name='deletarAvaliacao'),
    path('alocarAluno/', views.alocar_aluno, name = 'alocarAluno'),
    path('verAlunos/<int:id>', views.ver_alunos, name='verAlunos'),
    path('retirarAlunos/<int:id>, <int:idt>', views.retirar_alunos, name ='retirarAlunos'),
]
