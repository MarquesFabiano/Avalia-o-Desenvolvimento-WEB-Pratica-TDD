from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar/', views.listar, name='listar'),
    path('atualizar/<int:livro_id>/', views.atualizar, name='atualizar'),
    path('excluir/<int:livro_id>/', views.excluir, name='excluir'),
]
