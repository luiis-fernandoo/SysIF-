from django.contrib import admin
from .models import Aluno

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Aluno_Admin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'matricula', 'situacao', 'id_curso']
    search_fields = ['nome']
    
admin.site.register(Aluno, Aluno_Admin)