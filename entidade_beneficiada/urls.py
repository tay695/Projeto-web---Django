from django.urls import path
from .views import (
    EntidadeListView, EntidadeCreateView, EntidadeUpdateView, EntidadeDeleteView
)

urlpatterns = [
    path('', EntidadeListView.as_view(), name='entidade_list'),
    path('novo/', EntidadeCreateView.as_view(), name='entidade_create'),
    path('<int:pk>/editar/', EntidadeUpdateView.as_view(), name='entidade_update'),
    path('<int:pk>/deletar/', EntidadeDeleteView.as_view(), name='entidade_delete'),
]