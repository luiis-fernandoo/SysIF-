from django import forms
from curso.models import Curso

class FormCadastrarProfessor(forms.Form):
    
    #Durval = abaixo eu preencho uma lista de opções de curso com todos os possiveis cursos cadastrados
    all_cursos = Curso.objects.all().values_list('id', 'nome_curso')
    
    cursos_choice = [('', '')]
    
    for i in all_cursos:
        cursos_choice.append(i)
    
    nome = forms.CharField(label='Nome do Professor', widget=forms.TextInput)
    cod_professor = forms.CharField(label='Código do professor', widget=forms.TextInput)
    titulacaoMax = forms.CharField(label='Titulação máxima', widget=forms.TextInput)
    endereco = forms.CharField(label='Endereço do Professor', widget=forms.TextInput)
    telefone = forms.CharField(label='Telefone do Professor', widget=forms.TextInput)
    id_curso = forms.ChoiceField(label='Curso do Professor', choices=cursos_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher um curso para atrelar ao professor 
