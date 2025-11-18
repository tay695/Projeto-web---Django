from django.urls import path
from doador import views

urlpatterns = [
    path('cadastro/', views.cadastro_doador, name='doador_cadastro'),
]