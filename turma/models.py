from django.db import models
from aluno.models import Aluno
from professor.models import Professor #Durval - importando classe professor do modulo professor
from disciplina.models import Disciplina #Durval - importando classe disciplina do modulo disciplina
from django.shortcuts import get_object_or_404

#Durval - Classe turma, possui chave estrangeira de professor e disciplina
class Turma(models.Model):
    id_professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING) #Durval - chave estrangeira da tabela professor
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING) #Durval - chave estrangeira da tabela disciplina
    cod_turma = models.CharField('Codigo turma', max_length=250)
    semestre = models.IntegerField('Semestre')
    horario = models.TimeField('Horario')
    dia_semana = models.IntegerField('Dia da semana')
    
    def __str__(self):
        return self.cod_turma
    
    class Meta:
        verbose_name = 'Turma'
        ordering = ['cod_turma']
    # Durval - função para cadastrar turma, ela recebe o request da view e retorna um context para ser utilizado no template da view
    def cadastrar(request):
        
         from .forms import FormCadastrarTurma #Durval - por algum motivo n consigo importar no topo do codigo, fica dando erro
         context = {}
         context['is_not_cadastred'] = True
        
         if request.method == 'POST':
             form = FormCadastrarTurma(request.POST)
             
             if form.is_valid():
                 context['is_valid'] = True
                 
                 cod_turma = request.POST['cod_turma']
                 semestre = request.POST['semestre']
                 horario = request.POST['horario']
                 dia_semana = request.POST['dia_semana']
                 id_professor = request.POST['id_professor']
                 professor = Professor.objects.get(id=id_professor)
                 id_disciplina = request.POST['id_disciplina']
                 disciplina = Disciplina.objects.get(id=id_disciplina)
         
                 cadastra_turma = Turma(cod_turma=cod_turma,
                                     semestre=semestre,
                                     horario=horario,
                                     dia_semana=dia_semana,
                                     id_professor=professor,
                                     id_disciplina=disciplina
                                     )
                 
                 cadastra_turma.save()
                 
                 form = FormCadastrarTurma()
                 context['is_not_cadastred'] = False
                 
         else:
             form = FormCadastrarTurma()
             
         context['form'] = form
         
         return context
    
    #Durval - função para editar, ela recebe o request da view e o id da turma, e retorna um context para ser utilizado no template da view
    def editar(request, id):
        
        from .forms import FormCadastrarTurma #Durval - por algum motivo n consigo importar no topo do codigo, fica dando erro
        
        turma = get_object_or_404(Turma,id=id)
        context = {}
        context['is_not_edited'] = True
        
        if request.method == 'POST':
             form = FormCadastrarTurma(request.POST)
             
             if form.is_valid():
                 context['is_valid'] = True
                 
                 cod_turma = request.POST['cod_turma']
                 semestre = request.POST['semestre']
                 horario = request.POST['horario']
                 dia_semana = request.POST['dia_semana']
                 id_professor = request.POST['id_professor']
                 professor = Professor.objects.get(id=id_professor)
                 id_disciplina = request.POST['id_disciplina']
                 disciplina = Disciplina.objects.get(id=id_disciplina)
         
                 edita_turma = Turma.objects.filter(id=id)
                 edita_turma.update(cod_turma=cod_turma,
                                     semestre=semestre,
                                     horario=horario,
                                     dia_semana=dia_semana,
                                     id_professor=professor,
                                     id_disciplina=disciplina
                                     )
                 
                 form = FormCadastrarTurma()
                 context['is_not_edited'] = False
                
        else:
            form = FormCadastrarTurma()
            
            form.initial['cod_turma'] = turma.cod_turma
            form.initial['semestre'] = turma.semestre
            form.initial['horario'] = turma.horario
            form.initial['dia_semana'] = turma.dia_semana
            form.initial['id_professor'] = turma.id_professor
            form.initial['id_disciplina'] = turma.id_disciplina
            
        context['form'] = form
        context['id'] = id
                
        return (context)

    #Durval - função para deletar turma, ela recebe o request da view e o id da turma, não retorna nada
    def deletar(request, id):
        
        turma = get_object_or_404(Turma,id=id)
        turma.delete()
        
        
#-----------------------------------------------------------------------------------------------

#Durval - Classe avaliação, possui chave estrangeira de turma e aluno
class Avaliacao(models.Model):
    id_turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING) #Durval - chave estrangeira da tabela turma
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) #Durval - chave estrangeira da tabela aluno
    nota1 = models.FloatField('Nota 1')
    nota2 = models.FloatField('Nota 2')
    provaFinal = models.FloatField('Prova final')
    frequencia = models.IntegerField('Frequência')
    
    def __str__(self):
        return self
    
    class Meta:
        verbose_name = 'Avaliaçõe'
        ordering = ['id_aluno']
        
    # Durval - função para lancar avakiacao, ela recebe o request da view e retorna um context para ser utilizado no template da view
    def lancar(request):
        
         from .forms import FormCadastrarAvaliacao #Durval - por algum motivo n consigo importar no topo do codigo, fica dando erro
         
         context = {}
         context['is_not_cadastred'] = True
        
         if request.method == 'POST':
             form = FormCadastrarAvaliacao(request.POST)
             
             if form.is_valid():

                 id_turma = request.POST['id_turma']
                 id_aluno = request.POST['id_aluno']
                 aluno = Aluno.objects.get(id = id_aluno)
                 turma_aluno = TurmaAluno.objects.filter(id_turma_id = id_turma)

                 for i in turma_aluno:
                    if i.id_aluno == aluno:
                        
                        context['is_valid'] = True
                 
                        nota1 = request.POST['nota1']
                        nota2 = request.POST['nota1']
                        provaFinal = request.POST['provaFinal']
                        frequencia = request.POST['frequencia']
                        id_turma = request.POST['id_turma']
                        turma = Turma.objects.get(id=id_turma)
                        id_aluno = request.POST['id_aluno']
                        aluno = Aluno.objects.get(id=id_aluno)
                
                        cadastra_avaliacao = Avaliacao(nota1=nota1,
                                            nota2=nota2,
                                            provaFinal=provaFinal,
                                            frequencia=frequencia,
                                            id_turma=turma,
                                            id_aluno=aluno
                                            )
                        
                        cadastra_avaliacao.save()
                        break
                    else:
                        context['is_valid'] = False
                 
                 form = FormCadastrarAvaliacao()
                 context['is_not_cadastred'] = False
                 
         else:
             form = FormCadastrarAvaliacao()
             
         context['form'] = form
         
         return context
    
    #Durval - função para editar, ela recebe o request da view e o id da avalicao, e retorna um context para ser utilizado no template da view
    def editar(request, id):
        
        from .forms import FormCadastrarAvaliacao #Durval - por algum motivo n consigo importar no topo do codigo, fica dando erro
        avaliacao = get_object_or_404(Avaliacao,id=id)
        context = {}
        context['is_not_edited'] = True
        
        if request.method == 'POST':
             form = FormCadastrarAvaliacao(request.POST)
             
             if form.is_valid():
                 context['is_valid'] = True
                 
                 nota1 = request.POST['nota1']
                 nota2 = request.POST['nota1']
                 provaFinal = request.POST['provaFinal']
                 frequencia = request.POST['frequencia']
                 id_turma = request.POST['id_turma']
                 turma = Turma.objects.get(id=id_turma)
                 id_aluno = request.POST['id_aluno']
                 aluno = Aluno.objects.get(id=id_aluno)
         
                 edita_avaliacao= Avaliacao.objects.filter(id=id)
                 edita_avaliacao.update(nota1=nota1,
                                     nota2=nota2,
                                     provaFinal=provaFinal,
                                     frequencia=frequencia,
                                     id_turma=turma,
                                     id_aluno=aluno
                                     )
                 
                 form = FormCadastrarAvaliacao()
                 context['is_not_edited'] = False
                
        else:
            form = FormCadastrarAvaliacao()
            
            form.initial['nota1'] = avaliacao.nota1
            form.initial['nota2'] = avaliacao.nota2
            form.initial['provaFinal'] = avaliacao.provaFinal
            form.initial['frequencia'] = avaliacao.frequencia
            form.initial['id_turma'] = avaliacao.id_turma
            form.initial['id_aluno'] = avaliacao.id_aluno
            
        context['form'] = form
        context['id'] = id
                
        return (context)

    #Durval - função para deletar turma, ela recebe o request da view e o id da avaliacao, não retorna nada
    def deletar(request, id):
        
        avaliacao = get_object_or_404(Avaliacao,id=id)
        avaliacao.delete()
        

class TurmaAluno (models.Model):
    id_turma = models.ForeignKey(Turma, on_delete= models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete= models.SET_NULL, null = True)

    def alocar_aluno(request):
        from aluno.models import Aluno
        from .forms import FormAlocarAluno

        context = {}
        context['is_not_cadastred'] = True

        if request.method == 'POST':
            form = FormAlocarAluno(request.POST)

            if form.is_valid():

                id_aluno = request.POST['id_aluno']
                aluno = Aluno.objects.get(id = id_aluno)
                id_turma = request.POST['id_turma']
                turma = Turma.objects.get(id = id_turma)
                all_alunos = TurmaAluno.objects.filter(id_turma = id_turma)

                valid = True

                for i in all_alunos:
                    if aluno == i.id_aluno:
                       valid = False

                if valid == True:
                    context['is_valid'] = True
                    id_turma = request.POST['id_turma']
                    turma = Turma.objects.get(id = id_turma)
                    id_aluno = request.POST['id_aluno']
                    aluno = Aluno.objects.get(id = id_aluno)

                    aloca_aluno = TurmaAluno(id_turma = turma, id_aluno = aluno)

                    aloca_aluno.save()

                    form = FormAlocarAluno()

                    context['is_not_cadastred'] = False

                else:
                    context['is_valid'] = False
                    context['is_not_cadastred'] = False
        
        else:
            form = FormAlocarAluno()

        context['form'] = form

        return context

    def retirar_alunos(request, id, idt):

        turma_aluno = TurmaAluno.objects.filter(id_aluno = id)
        aluno = Aluno.objects.get(id = id)
        avaliacao = Avaliacao.objects.filter(id_aluno = aluno)
        turma = Turma.objects.get(id = idt)

        for i in avaliacao:
            if i.id_turma == turma and i.id_aluno == aluno:
                i.delete()

        for i in turma_aluno:
            if aluno == i.id_aluno and i.id_turma == turma:
                i.delete()



