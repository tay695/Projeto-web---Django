from django.urls import path
from . import views  # importa suas views locais

urlpatterns = [
    path('listar/', views.listar_estoque, name='listar_estoque'),
    path('criar/', views.adcionar_estoque, name='adicionar_estoque'),
    path('editar/<int:item_id>/', views.editar_item, name='editar_item'),
    path('deletar/<int:item_id>/', views.deletar_item, name='deletar_item'),
    path('detalhar/<int:item_id>/', views.detalhar_item, name='detalhar_item'),
]
