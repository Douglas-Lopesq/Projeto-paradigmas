# core/urls.py
from django.urls import path
from ..core import views

urlpatterns = [
    path('cursos/', views.CursoListView.as_view(), name='curso-list'),
    path('cursos/novo/', views.CursoCreateView.as_view(), name='curso-create'),
    path('cursos/<pk>/editar/', views.CursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<pk>/excluir/', views.CursoDeleteView.as_view(), name='curso-delete'),

    path('alunos/', views.AlunoListView.as_view(), name='aluno-list'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='aluno-create'),
    path('alunos/<pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno-update'),
    path('alunos/<pk>/excluir/', views.AlunoDeleteView.as_view(), name='aluno-delete'),
]
