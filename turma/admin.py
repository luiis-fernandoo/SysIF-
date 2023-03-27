from django.contrib import admin
from .models import Turma
from .models import Avaliacao
from .models import TurmaAluno

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Turma_Admin(admin.ModelAdmin):
    list_display = ['cod_turma', 'semestre', 'horario', 'dia_semana', 'id_professor', 'id_disciplina']
    search_fields = ['cod_turma']
    
admin.site.register(Turma, Turma_Admin)

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Avaliacao_Admin(admin.ModelAdmin):
    list_display = ['id_turma', 'id_aluno', 'nota1', 'nota2', 'provaFinal', 'frequencia']
    search_fields = ['id_aluno']
    
admin.site.register(Avaliacao, Avaliacao_Admin)

class TurmaAluno_Admin(admin.ModelAdmin):
    list_display = ['id_turma', 'id_aluno']
    search_fields = ['id_turma']

admin.site.register(TurmaAluno, TurmaAluno_Admin)
