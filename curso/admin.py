from django.contrib import admin
from .models import Curso

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Curso_Admin(admin.ModelAdmin):
    list_display = ['nome_curso', 'codigo_curso', 'descricao']
    search_fields = ['nome_curso']
    
admin.site.register(Curso, Curso_Admin)