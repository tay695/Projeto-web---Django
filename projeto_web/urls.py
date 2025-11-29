"""
URL configuration for projeto_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from operator import index
from django.contrib import admin
from django.urls import path, include
from projeto_web.views import Index
from projeto_web import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index, name='index'),
    path('admin/', admin.site.urls),
    path('pontos/', include('ponto_coleta.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('estoque/', include('estoque.urls')),
    path('entidades/', include('entidade_beneficiada.urls')),
    path('doador/', include('doador.urls')),
    path('doacao/', include('doacao.urls')),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'), 

]
