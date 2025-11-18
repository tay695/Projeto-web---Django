from django.urls import path
from doacao import views

urlpatterns = [
    path('nova_doacao/', views.criar_doacao, name='criar_doacao'),

]