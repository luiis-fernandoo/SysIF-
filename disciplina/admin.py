from django.contrib import admin
from .models import Disciplina

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Disciplina_Admin(admin.ModelAdmin):
    list_display = ['nome_disciplina', 'codigo_disciplina', 'descricao', 'carga_horaria', 'id_curso']
    search_fields = ['nome_disciplina']
    
admin.site.register(Disciplina, Disciplina_Admin)