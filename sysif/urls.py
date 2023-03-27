from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('aluno/', include('aluno.urls')),
    path('turma/', include('turma.urls')),
    path('professor/', include('professor.urls')),
    path('disciplina/', include('disciplina.urls')),
    path('curso/', include('curso.urls')),
]
