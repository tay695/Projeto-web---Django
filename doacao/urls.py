from django.urls import path
from doacao import views

urlpatterns = [
    path('', views.index, name='index'),
]