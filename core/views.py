# core/views.py
from django.views import generic
from .models import Curso, Aluno

# Cursos
class CursoListView(generic.ListView):
    model = Curso
    context_object_name = 'cursos'

class CursoCreateView(generic.CreateView):
    model = Curso
    fields = ['nome', 'descricao']
    success_url = '/cursos/'

class CursoUpdateView(generic.UpdateView):
    model = Curso
    fields = ['nome', 'descricao']
    success_url = '/cursos/'

class CursoDeleteView(generic.DeleteView):
    model = Curso
    success_url = '/cursos/'


# Alunos
class AlunoListView(generic.ListView):
    model = Aluno
    context_object_name = 'alunos'

class AlunoCreateView(generic.CreateView):
    model = Aluno
    fields = ['nome', 'email', 'curso']
    success_url = '/alunos/'

class AlunoUpdateView(generic.UpdateView):
    model = Aluno
    fields = ['nome', 'email', 'curso']
    success_url = '/alunos/'

class AlunoDeleteView(generic.DeleteView):
    model = Aluno
    success_url = '/alunos/'
