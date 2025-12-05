# doador/views.py
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import CadastroDoadorForm, EditarDoadorForm
from .models import Doador
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied



@login_required
def perfil_doador(request, id):
    doador = get_object_or_404(Doador, pk=id)

    # Garante que o usuário só veja o próprio perfil
    if doador.usuario != request.user:
        raise PermissionDenied("Você não pode acessar o perfil de outro usuário.")

    return render(request, 'perfil_doador.html', {'doador': doador})


@login_required
@permission_required('doador.view_doador')
def listar_doador(request):
    doadores = Doador.objects.all()
    return render(request, 'listar_doador.html', {'doadores': doadores})


def cadastro_doador(request):
    if request.method == 'POST':
        form = CadastroDoadorForm(request.POST)
        if form.is_valid():
            
            new_user = form.save() 
            
            messages.success(request, "Cadastro realizado com sucesso! Você está logado(a).")
            return redirect('login') 
            
    else:
        form = CadastroDoadorForm()

    return render(request, 'cadastro_doador.html', {'form': form, 'action_type': 'add_doador'})


@login_required
@permission_required('doador.change_doador')
def editar_doador(request, id):
    doador = get_object_or_404(Doador, pk=id)
    if request.method == 'POST':
        form = EditarDoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados atualizados com sucesso.")
            
            if request.user.is_superuser or request.user.is_staff:
                return redirect('listar_doador') 
            else:
                return redirect('perfil_doador', id=doador.id)
    else:
        form = EditarDoadorForm(instance=doador)
    return render(request, 'cadastro_doador.html', {'form': form, 'doador': doador, 'action_type': 'edit_doador'})


@login_required
@permission_required('doador.delete_doador')
def deletar_doador(request, id):
    doador = get_object_or_404(Doador, pk=id)
    if request.method == 'POST':
        doador.delete()
        messages.success(request, "Doador excluído com sucesso.")
        return redirect('listar_doador')
    return render(request, 'cadastro_doador.html', {'doador': doador, 'action_type': 'delete_doador'})
