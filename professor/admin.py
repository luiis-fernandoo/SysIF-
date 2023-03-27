from django.contrib import admin
from .models import Professor

#Durval - criando uma classe que pode ser manipulada pela interface do administrador do django
class Professor_Admin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'telefone', 'cod_professor', 'titulacaoMax', 'id_curso']
    search_fields = ['nome']
    
admin.site.register(Professor, Professor_Admin)