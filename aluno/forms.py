from django import forms
from curso.models import Curso #Durval - importando classe curso do modulo curso

class FormCadastrarAluno(forms.Form):
    
    #Durval - abaixo eu preencho uma lista de opções de curso com todos os possiveis cursos cadastrados
    all_cursos = Curso.objects.all().values_list('id', 'nome_curso')
    
    cursos_choice = [('', '')]
    
    for i in all_cursos:
        cursos_choice.append(i)
        
    #Durval - abaixo eu crio os campos do meu formulario
    matricula = forms.CharField(label='Matricula do Aluno', widget=forms.TextInput)
    nome = forms.CharField(label='Nome do Aluno', widget=forms.TextInput)
    endereco = forms.CharField(label='Endereço do Aluno', widget=forms.TextInput)
    telefone = forms.CharField(label='Telefone do Aluno', widget=forms.TextInput)
    id_curso = forms.ChoiceField(label='Curso do aluno', choices=cursos_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher um curso para atrelar ao aluno 
    situacao = forms.CharField(label='Situação do aluno',  widget=forms.TextInput)
