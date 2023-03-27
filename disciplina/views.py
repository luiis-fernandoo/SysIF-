from django.shortcuts import render
from disciplina.models import Disciplina
from turma.models import Turma

def cadastrar(request):
   
    context = Disciplina.cadastrar(request) #Luis - funcao sendo chamada do models 'disciplina' para cadastrar Disciplina

    return render(request, 'cadastrar_disciplina.html', context)

def editar(request, id):
   
    context = Disciplina.editar(request, id) #Luis - funcao sendo chamada do models 'disciplina' para editar Disciplina
        
    return render(request, 'editar_disciplina.html', context)

def deletar(request, id):
   
    context = {}
    discplina = Disciplina.objects.get(id = id)
    turma = Turma.objects.filter(id_disciplina_id = id)

    if turma:
        context['is_valid'] = False

    else:
        context['is_valid'] = True
        discplina.delete()
    
        
    return render(request, 'deletar_disciplina.html', context)

#Durval - CRUD de disciplina
def dashboard(request):
    
     disciplinas_cadastrados = Disciplina.objects.all()
    
     context ={
        'disciplinas_cadastrados': disciplinas_cadastrados,
     }

     return render(request, 'disciplina_dashboard.html', context)

