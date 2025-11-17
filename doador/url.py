from django.urls import path
from . import views  # importa suas views locais

urlpatterns = [
    
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_doador, name='doador/cadastro_doador.html'),
    path
]