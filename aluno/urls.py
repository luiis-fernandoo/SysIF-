from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar'),
    path('editar/<int:id>', views.editar_aluno, name='editar'),
    path('deletar/<int:id>', views.deletar_aluno, name='deletar'),
]
