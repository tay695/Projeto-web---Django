from django.urls import path
from . import views  # importa suas views locais

urlpatterns = [
    
    path('', views.index, name='index'),
]