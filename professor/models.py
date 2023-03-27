from django.db import models
from django.shortcuts import get_object_or_404
from curso.models import Curso # Durval - importando classe Curso do modulo curso
from professor.forms import FormCadastrarProfessor

# classe pessoa, super classe com as subclasses professor e aluno
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=250)
    telefone = models.CharField('Telefone', max_length=250)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Pessoa'
        ordering = ['nome']

    def cadastrar():
        
        return 0
    
    def editar():
        
        return 0
    
    def deletar():
        
        return 0
#Durval - subclasse professor, herda de pessoa
class Professor(Pessoa):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE) #Durval - passando a chave estangeira da classe (tabela) curso
    cod_professor = models.CharField('Codigo', max_length=250)
    titulacaoMax = models.CharField('Titulação Máxima', max_length=250)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Professore'
        ordering = ['nome']
        
     #LUIS - criando o metodo cadastrar professor

    def cadastrar(request):
        
        context={}
        context['is_not_cadastred'] = True
        
        if request.method == 'POST':
            
            form = FormCadastrarProfessor(request.POST)
            
            #verifica se o preenchimento foi valido
            if form.is_valid():
                context['is_valid'] = True
                
                #recebe os valores digitados no form
                nome = request.POST['nome']
                cod_professor = request.POST['cod_professor']
                titulacaoMax = request.POST['titulacaoMax']
                endereco = request.POST['endereco']
                telefone = request.POST['telefone']
                id_curso = request.POST['id_curso']

                curso = Curso.objects.get(id = id_curso)
                
                #cadastrando professor
                cadastra_professor = Professor(nome=nome, 
                        cod_professor=cod_professor, 
                        titulacaoMax=titulacaoMax, 
                        endereco=endereco, 
                        telefone=telefone, 
                        id_curso= curso)
                
                cadastra_professor.save()
                
                form = FormCadastrarProfessor()
                
                context['is_not_cadastred'] = False
                
        else:
            form = FormCadastrarProfessor()   
            
        context['form'] = form
        
        return context   
        
    #LUIS - Criando o metodo de editar professor
    def editar(request, id):
        professor = get_object_or_404(Professor, id=id)
        context = {}
        context['is_not_edited'] = True
        
        if request.method == 'POST':
            form = FormCadastrarProfessor(request.POST)
            #verifica se o preenchimento foi valido
            if form.is_valid():
                
                context['is_valid'] = True 
                
            #recebe os valores digitados no form
                nome = request.POST['nome']
                cod_professor = request.POST['cod_professor']
                titulacaoMax = request.POST['titulacaoMax']
                endereco = request.POST['endereco']
                telefone = request.POST['telefone']
                id_curso = request.POST['id_curso']
                
                #editando curso
                edita_professor = Professor.objects.filter(id=id)
                edita_professor.update(nome=nome, 
                            cod_professor=cod_professor, 
                            titulacaoMax=titulacaoMax, 
                            endereco=endereco, 
                            telefone=telefone, 
                            id_curso=id_curso)
                
                form = FormCadastrarProfessor()
                
                context['is_not_edited'] = False
        else:
            form = FormCadastrarProfessor()
            
            #se o formulario ja foi preenchido antes, ele irá retornar todas as respostas preenchidas e pronto para serem substituidas
            form.initial['nome'] = professor.nome
            form.initial['cod_professor'] = professor.cod_professor
            form.initial['titulacaoMax'] = professor.titulacaoMax
            form.initial['endereco'] = professor.endereco
            form.initial['telefone'] = professor.telefone
            form.initial['id_curso'] = professor.id_curso
            
        context['form'] = form
        context['id'] = id
                    
        return (context)
        
    #LUIS - Função para deletar professores

