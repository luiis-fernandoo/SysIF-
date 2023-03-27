from django import forms
from curso.models import Curso
from professor.models import Professor
from disciplina.models import Disciplina
from aluno.models import Aluno
from .models import Turma

class FormCadastrarTurma(forms.Form):
    
    #Durval = abaixo eu preencho uma lista de opções de professores com todos os possiveis professores cadastrados
    all_professores = Professor.objects.all().values_list('id', 'nome')
    
    professores_choice = [('', '')]
    
    for i in all_professores:
        professores_choice.append(i)
    
    #Durval = abaixo eu preencho uma lista de opções de disciplinaas com todas as possiveis disciplinas cadastradas
    all_disciplina = Disciplina.objects.all().values_list('id', 'nome_disciplina')
    
    disciplina_choices = [('', '')]
    
    for i in all_disciplina:
        disciplina_choices.append(i)
        
    #Durval - abaixo eu crio os campos do meu formulario
    id_professor = forms.ChoiceField(label='Professor da turma', choices=professores_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher um professor para atrelar a turma
    id_disciplina = forms.ChoiceField(label='Disciplina da turma', choices=disciplina_choices, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher uma disciplina para atrelar a turma 
    cod_turma = forms.CharField(label='Codigo da turma', widget=forms.TextInput)
    semestre = forms.IntegerField(label='Semeste', widget=forms.NumberInput)
    horario = forms.TimeField()
    dia_semana = forms.IntegerField(label='Dia da semana', widget=forms.NumberInput)
    
    
class FormCadastrarAvaliacao(forms.Form):
    
    #Durval = abaixo eu preencho uma lista de opções de turmas com todas as possiveis turmas cadastradas
    all_turmas = Turma.objects.all().values_list('id', 'cod_turma')
    
    turmas_choice = [('', '')]
    
    for i in all_turmas:
        turmas_choice.append(i)
    
    #Durval = abaixo eu preencho uma lista de opções de alunos com todos os possiveis alunos cadastrados
    all_alunos = Aluno.objects.all().values_list('id', 'nome')
    
    alunos_choice = [('', '')]
    
    for i in all_alunos:
        alunos_choice.append(i)
    
    #Durval - abaixo eu crio os campos do meu formulario
    id_turma = forms.ChoiceField(label='Turma', choices=turmas_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher uma turma para atrelar a avaliação 
    id_aluno = forms.ChoiceField(label='Aluno', choices=alunos_choice, widget=forms.Select()) #Durval - esse é um campo onde o usuario irá escolher um aluno para atrelar a avaliação 
    nota1 = forms.FloatField(label='Nota 1', widget=forms.NumberInput)
    nota2 = forms.FloatField(label='Nota 2', widget=forms.NumberInput)
    provaFinal = forms.FloatField(label='Prova final', widget=forms.NumberInput)
    frequencia = forms.IntegerField(label='Frequencia', widget=forms.NumberInput)

class FormAlocarAluno(forms.Form):

    all_alunos = Aluno.objects.all().values_list('id', 'nome')

    alunos_choice = [('', '')]

    for i in all_alunos:
        alunos_choice.append(i)

    all_turmas = Turma.objects.all().values_list('id','cod_turma')

    turma_choice = [('', '')]

    for i in all_turmas:
        turma_choice.append(i)

    id_turma = forms.ChoiceField(label='Turma', choices=turma_choice, widget=forms.Select())
    id_aluno = forms.ChoiceField(label='Aluno', choices=alunos_choice, widget=forms.Select())

    
