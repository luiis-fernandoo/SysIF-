from django.shortcuts import render
from curso.models import Curso
from aluno.models import Aluno
from professor.models import Professor
from disciplina.models import Disciplina

def cadastrar(request):
   
    context = Curso.cadastrar(request) #Luis - funcao sendo chamada do models 'Curso' para cadastrar curso

    return render(request, 'cadastrar_curso.html', context)

def editar(request, id):
   
    context = Curso.editar(request, id) #Luis - funcao sendo chamada do models 'curso' para editar curso
        
    return render(request, 'editar_curso.html', context)

def deletar(request, id):
   
    context = {}
    
    curso = Curso.objects.get(id = id)
    aluno = Aluno.objects.filter(id_curso = id)
    professor = Professor.objects.filter(id_curso = id)
    disciplina = Disciplina.objects.filter(id_curso = id)

    valid = True 

    mensagem = 'O curso está alocado em '

    if aluno:
        mensagem = mensagem + 'aluno, '
        context['is_valid'] = False
        valid = False

    if valid == False:
        if disciplina:
            mensagem = mensagem + 'disciplina,'
            context['is_valid'] = False
            valid = False
    if valid == False:
        if professor:
            mensagem = mensagem + 'professor,'
            context['is_valid'] = False
            valid = False

    mensagem = mensagem + 'portanto não pode ser deletado'

    context['mensagem'] = mensagem

    if valid == True:
        context['is_valid'] = True
        curso.delete()




    return render(request, 'deletar_curso.html', context)

#durval - tela de CRUD de curso
def dashboard(request):
    
     cursos_cadastrados = Curso.objects.all()
    
     context ={
        'cursos_cadastrados': cursos_cadastrados,
     }

     return render(request, 'curso_dashboard.html', context)