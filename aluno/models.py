from django.db import models
from professor.models import Pessoa #Durval - importando classe pessoa do modulo professor
from curso.models import Curso #Durval - importando classe Curso do modulo curso
from aluno.forms import FormCadastrarAluno
from django.shortcuts import get_object_or_404

#Durval - Subclasse aluno, herda da classe Pessoa que se encontra no modulo professor
class Aluno(Pessoa):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)#Durval - passando a chave estangeira da classe(tabela) curso
    matricula = models.CharField('Matricula', max_length=250)
    situacao = models.CharField('Situação', max_length=250)
    
    def __str__(self):
        return self.matricula
    
    class Meta:
        verbose_name = 'Aluno'
        ordering = ['nome']
        
    #Durval - função para cadastrar aluno, ela recebe o request da view e retorna um context para ser utilizado no template da view
    def cadastrar(request):
         context = {}
         context['is_not_cadastred'] = True
        
         if request.method == 'POST':
             form = FormCadastrarAluno(request.POST)
             
             if form.is_valid():
                 context['is_valid'] = True
                 
                 matricula = request.POST['matricula']
                 nome = request.POST['nome']
                 endereco = request.POST['endereco']
                 telefone = request.POST['telefone']
                 id_curso = request.POST['id_curso']
                 curso = Curso.objects.get(id=id_curso)
                 situacao = request.POST['situacao']
         
                 cadastra_aluno = Aluno(matricula=matricula,
                                     nome=nome,
                                     endereco=endereco,
                                     telefone=telefone,
                                     id_curso=curso,
                                     situacao=situacao
                                     )
                 
                 cadastra_aluno.save()
                 
                 form = FormCadastrarAluno()
                 context['is_not_cadastred'] = False
                 
         else:
             form = FormCadastrarAluno()
             
         context['form'] = form
         
         return context
    
    #Durval - função para editar aluno, ela recebe o request da view  e o id do aluno, e retorna um context para ser utilizado no template da view
    def editar(request, id):
    
        aluno = get_object_or_404(Aluno,id=id)
        context = {}
        context['is_not_edited'] = True
        
        if request.method == 'POST':
             form = FormCadastrarAluno(request.POST)
             
             if form.is_valid():
                 context['is_valid'] = True
                 
                 matricula = request.POST['matricula']
                 nome = request.POST['nome']
                 endereco = request.POST['endereco']
                 telefone = request.POST['telefone']
                 id_curso = request.POST['id_curso']
                 curso = Curso.objects.get(id=id_curso)
                 situacao = request.POST['situacao']
         
                 edita_aluno = Aluno.objects.filter(id=id)
                 edita_aluno.update(matricula=matricula,
                                     nome=nome,
                                     endereco=endereco,
                                     telefone=telefone,
                                     id_curso=curso,
                                     situacao=situacao
                                     )
                 
                 form = FormCadastrarAluno()
                 context['is_not_edited'] = False
                
        else:
            form = FormCadastrarAluno()
            
            form.initial['matricula'] = aluno.matricula
            form.initial['nome'] = aluno.nome
            form.initial['endereco'] = aluno.endereco
            form.initial['telefone'] = aluno.telefone
            form.initial['id_curso'] = aluno.id_curso
            form.initial['situacao'] = aluno.situacao
            
        context['form'] = form
        context['id'] = id
                
        return (context)


    #Durval - função para deletar aluno, ela recebe o request da view e o id do aluno, não retorna nada
