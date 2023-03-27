from django.db import models
from django.shortcuts import get_object_or_404
from curso.models import Curso # Durval - importando classe Curso do modulo curso
from disciplina.forms import FormCadastrarDisciplina  # LUIS - chamando o formulario

# Durval - Classe disciplina
class Disciplina(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome_disciplina = models.CharField('Nome', max_length=250)
    codigo_disciplina = models.CharField('Código', max_length=250)
    descricao = models.CharField('Descrição', max_length=500)
    carga_horaria = models.IntegerField('Carga Horaria')
    
    def __str__(self):
        return self.nome_disciplina
    
    class Meta:
        verbose_name = 'Disciplina'
        ordering = ['nome_disciplina']

    #LUIS - Metodo de cadastrar disciplina


    def cadastrar(request):

        context = {}
        context['is_not_cadastred'] = True

        if request.method == 'POST':
            form = FormCadastrarDisciplina(request.POST)

            #verifica se o preenchimento foi valido
            if form.is_valid():
                context['is_valid'] = True

                id_curso = request.POST['id_curso']
                curso = Curso.objects.get(id=id_curso)
                nome_disciplina = request.POST['nome_disciplina']
                codigo_disciplina = request.POST['codigo_disciplina']
                descricao = request.POST['descricao']
                carga_horaria = request.POST['carga_horaria']

                cadastra_disciplina = Disciplina(
                    id_curso = curso,
                    nome_disciplina = nome_disciplina,
                    codigo_disciplina = codigo_disciplina,
                    descricao = descricao,
                    carga_horaria = carga_horaria)

                cadastra_disciplina.save()

                form = FormCadastrarDisciplina()
                context['is_not_cadastred'] = False

        else:
            form = FormCadastrarDisciplina()   
        
        context['form'] = form

        return context     

    #LUIS - Metodo para editar as disciplinas

    def editar(request, id):

        disciplina = get_object_or_404(Disciplina, id=id)
        context = {}
        context['is_not_edited'] = True

        if request.method == 'POST':
            form = FormCadastrarDisciplina(request.POST)

            #verifica se o preenchimento foi valido
            if form.is_valid():
                context['is_valid'] = True

                #recebe os valores digitados nos campos do form

                id_curso = request.POST['id_curso']
                curso = Curso.objects.get(id=id_curso)
                nome_disciplina = request.POST['nome_disciplina']
                codigo_disciplina = request.POST['codigo_disciplina']
                descricao = request.POST['descricao']
                carga_horaria = request.POST['carga_horaria']

                edita_disciplina = Disciplina.objects.filter(id=id)
                edita_disciplina.update(
                    id_curso = curso,
                    nome_disciplina = nome_disciplina,
                    codigo_disciplina = codigo_disciplina,
                    descricao = descricao,
                    carga_horaria = carga_horaria)

                form = FormCadastrarDisciplina()
                context['is_not_edited'] = False

        #Se o formulario ja tiver sido preenchido anteriormente, ele irá retornar o formulario com os dados anteriores para edição

        else:
            form = FormCadastrarDisciplina()
            form.initial['id_curso'] = disciplina.id_curso
            form.initial['nome_disciplina'] = disciplina.nome_disciplina
            form.initial['codigo_disciplina'] = disciplina.codigo_disciplina
            form.initial['descricao'] = disciplina.descricao
            form.initial['carga_horaria'] = disciplina.carga_horaria
            

        context['form'] = form
        context['id'] = id
                    
        return (context)

    #LUIS - Funcao para deletar as disciplinas
