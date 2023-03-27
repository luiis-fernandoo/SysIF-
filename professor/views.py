from django.shortcuts import render

from professor.models import Professor
from turma.models import Turma

def cadastrar(request):
   
    context = Professor.cadastrar(request) #Luis - funcao sendo chamada do models 'professor' para cadastrar professor
        
    return render(request, 'cadastrar_professor.html', context)

def editar(request, id):
   
    context = Professor.editar(request, id) #Luis - funcao sendo chamada do models 'professor' para editar professor
        
    return render(request, 'editar_professor.html', context)

def deletar(request, id):
   
    context = {}

    professor = Professor.objects.get(id = id)
    turma = Turma.objects.filter(id_professor_id = id)
    if turma:
        context['is_valid'] = True
    else:
        context['is_valid'] = False
        professor.delete()

        
    return render(request, 'deletar_professor.html', context)

def dashboard(request):
    
     professores_cadastrados = Professor.objects.all()
    
     context ={
        'professores_cadastrados': professores_cadastrados,
     }

     return render(request, 'professor_dashboard.html', context)