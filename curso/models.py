from django.db import models
from django.shortcuts import get_object_or_404
from curso.forms import FormCadastrarCurso

# Durval - Classe curso
class Curso(models.Model):
    nome_curso = models.CharField('Nome', max_length=250)
    codigo_curso = models.CharField('Código curso', max_length=100)
    descricao = models.CharField('Descrição', max_length=500)
    
    def __str__(self):
        return self.nome_curso
    
    class Meta:
        verbose_name = 'Curso'
        ordering = ['nome_curso']

    # Luis metodo cadastrar Curso

    def cadastrar(request):

        context = {}
        context['is_not_cadastred'] = True

        if request.method == 'POST':
            form = FormCadastrarCurso(request.POST)

            #verifica se o preenchimento foi valido
            if form.is_valid():
                context['is_valid'] = True

                #recebe os valores digitados nos campos do form
                nome_curso  = request.POST['nome_curso']
                codigo_curso = request.POST['codigo_curso']
                descricao = request.POST['descricao']

                #cadastra o curso

                cadastra_curso = Curso(nome_curso = nome_curso, 
                codigo_curso = codigo_curso, 
                descricao = descricao)

                cadastra_curso.save()

                form = FormCadastrarCurso()
                context['is_not_cadastred'] = False

        else:
            form = FormCadastrarCurso()   
        
        context['form'] = form

        return context     

    #Luis Metodo de editar curso, nesse metodo, alem do request, ele recebe também o id do curso
    def editar(request, id):
        
        curso = get_object_or_404(Curso, id=id)
        context = {}
        context['is_not_edited'] = True
        
        if request.method == 'POST':
            form = FormCadastrarCurso(request.POST)

            #verifica se o preenchimento foi valido
            if form.is_valid():
                context['is_valid'] = True

                #recebe os valores digitados nos campos do form

                nome_curso  = request.POST['nome_curso']
                codigo_curso = request.POST['codigo_curso']
                descricao = request.POST['descricao']

                #editar curso
                edita_curso = Curso.objects.filter(id=id)
                edita_curso.update(
                    nome_curso=nome_curso, 
                    codigo_curso=codigo_curso, 
                    descricao=descricao
                )

                form = FormCadastrarCurso()
                context['is_not_edited'] = False

        #Se o formulario ja tiver sido preenchido anteriormente, ele irá retornar o formulario com os dados anteriores para edição

        else:

            form = FormCadastrarCurso()

            form.initial['nome_curso'] = curso.nome_curso
            form.initial['codigo_curso'] = curso.codigo_curso
            form.initial['descricao'] = curso.descricao

        context['form'] = form
        context['id'] = id
                    
        return (context)


    #LUIS metodo de deletar curso:

    def deletar(request, id):

        curso = get_object_or_404(Curso, id=id)
        curso.delete()



