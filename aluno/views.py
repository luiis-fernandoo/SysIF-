from django.shortcuts import render
from aluno.models import Aluno
from turma.models import TurmaAluno

# Create your views here.
def cadastrar_aluno(request):
   
    context = Aluno.cadastrar(request) #Durval - aqui eu chamo a função de cadastro de aluno, a ordem de negócio se encontra lá
        
    return render(request, 'cadastrar_aluno.html', context)

def editar_aluno(request, id):
   
    context = Aluno.editar(request, id) #Durval - aqui eu chamo a função de editar aluno, a ordem de negócio se encontra lá
        
    return render(request, 'editar_aluno.html', context)

def deletar_aluno(request, id):
   
    context = {}
    aluno = Aluno.objects.get(id = id)
    turma_aluno = TurmaAluno.objects.filter(id_aluno_id = id)
    
    if turma_aluno:
        context['is_valid'] = True
    else:
        context['is_valid'] = False
        aluno.delete()

    return render(request, 'deletar_aluno.html', context)

def dashboard(request):
    
     alunos_cadastrados = Aluno.objects.all()
    
     context ={
        'alunos_cadastrados': alunos_cadastrados,
     }

     return render(request, 'aluno_dashboard.html', context)

