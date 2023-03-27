from django.shortcuts import render
from turma.models import Turma, Avaliacao, TurmaAluno
from aluno.models import Aluno

# views para turma
def cadastrar_turma(request):
   
    context = Turma.cadastrar(request) #Durval - aqui eu chamo a função de cadastro de turma, a ordem de negócio se encontra lá
        
    return render(request, 'cadastrar_turma.html', context)

def editar_turma(request, id):
   
    context = Turma.editar(request, id) #Durval - aqui eu chamo a função de editar turma, a ordem de negócio se encontra lá
        
    return render(request, 'editar_turma.html', context)

def deletar_turma(request, id):
   
    context = Turma.deletar(request, id) #Durval - aqui eu chamo a função de deletar turma, a ordem de negócio se encontra lá
        
    return render(request, 'deletar_turma.html', context)

def dashboard_turma(request):
    
     turmas_cadastradas = Turma.objects.all()
    
     context ={
        'turmas_cadastradas': turmas_cadastradas,
     }

     return render(request, 'turma_dashboard.html', context)
 
#----------------------------------------------------------

# views para avaliacao
def lancar_avaliacao(request):
   
    context = Avaliacao.lancar(request) #Durval - aqui eu chamo a função de cadastro de avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'lancar_avaliacao.html', context)

def editar_avaliacao(request, id):
   
    context = Avaliacao.editar(request, id) #Durval - aqui eu chamo a função de editar avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'editar_avaliacao.html', context)

def deletar_avaliacao(request, id):
   
    context = Avaliacao.deletar(request, id) #Durval - aqui eu chamo a função de deletar avaliacao, a ordem de negócio se encontra lá
        
    return render(request, 'deletar_avaliacao.html', context)

def dashboard_avaliacao(request):
    
     avaliacoes_lancadas = Avaliacao.objects.all()
    
     context ={
        'avaliacoes_lancadas': avaliacoes_lancadas,
     }

     return render(request, 'avaliacao_dashboard.html', context)


def alocar_aluno(request):
    context = TurmaAluno.alocar_aluno(request)

    return render(request, 'alocar_aluno.html', context)

def ver_alunos(request, id):

    turma = Turma.objects.get(id = id)

    alunos_alocados = TurmaAluno.objects.filter(id_turma = id)

    context = {
        'alunos_alocados': alunos_alocados,
    }

    context ['turma'] = turma

    return render(request, 'ver_alunos.html', context)

def retirar_alunos(request, id, idt):

    context = TurmaAluno.retirar_alunos(request, id, idt)

    return render(request,'retirar_alunos.html', context)

    
 