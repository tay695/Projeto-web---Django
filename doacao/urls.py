from django.urls import path
from doacao import views

urlpatterns = [
    path('nova_doacao/', views.criar_doacao, name='criar_doacao'),
    path('dashboard/', views.dashboard_doacoes, name='dashboard_doacoes'),
    path('confirmar/<int:id>/', views.confirmar_coleta, name='confirmar_coleta'),
    
]