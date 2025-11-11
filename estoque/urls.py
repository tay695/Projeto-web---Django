from django.urls import path
from . import views  # importa suas views locais

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
=======
>>>>>>> 035f39511a7fba4fcf823daf71445e3bff1c11b2
    path('listar/', views.listar_estoque, name='listar_estoque'),
    path('criar/', views.adcionar_estoque, name='adicionar_estoque'),
    path('editar/<int:item_id>/', views.editar_item, name='editar_item'),
    path('deletar/<int:item_id>/', views.deletar_item, name='deletar_item'),
    path('detalhar/<int:item_id>/', views.detalhar_item, name='detalhar_item'),
]
