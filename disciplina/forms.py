from django import forms
from curso.models import Curso

class FormCadastrarDisciplina(forms.Form):
    
    #Durval = abaixo eu preencho uma lista de opções de curso com todos os possiveis cursos cadastrados
    all_cursos = Curso.objects.all().values_list('id', 'nome_curso')
    
    cursos_choice = [('', '')]
    
    for i in all_cursos:
        cursos_choice.append(i)
    
    #Durval - abaixo eu crio o formulario de Disciplina
    id_curso = forms.ChoiceField(label='Disciplina pertence ao curso', choices=cursos_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher um curso para atrelar a disciplina 
    nome_disciplina = forms.CharField(label='Nome da disciplina', widget=forms.TextInput)
    codigo_disciplina = forms.CharField(label='Codigo da disciplina', widget=forms.TextInput)
    carga_horaria = forms.IntegerField(label='Horario', widget=forms.NumberInput)
    descricao = forms.CharField(label='Descrição da disciplina', widget=forms.Textarea)
        