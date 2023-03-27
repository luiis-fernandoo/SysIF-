from django import forms

#Durval - Abaixo eu crio um formulario para curso
class FormCadastrarCurso(forms.Form):
    
    nome_curso = forms.CharField(label='Nome do curso', widget=forms.TextInput)
    codigo_curso = forms.CharField(label='Codigo do curso', widget=forms.TextInput)
    descricao = forms.CharField(label='Descrição do curso', widget=forms.Textarea)
        
