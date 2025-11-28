# doador/views.py
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import CadastroDoadorForm, EditarDoadorForm
from .models import Doador


@login_required
@permission_required('doador.view_doador')
def perfil_doador(request, id):
    doador = get_object_or_404(Doador, pk=id)
    return render(request, 'doador/perfil_doador.html', {'doador': doador})


@login_required
@permission_required('doador.view_doador')
def listar_doador(request):
    doadores = Doador.objects.all()
    return render(request, 'listar_doador.html', {'doadores': doadores})


def cadastro_doador(request):
    if request.method == 'POST':
        form = CadastroDoadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso. Faça login para continuar.")
            return redirect('login')
        # se inválido: reexibe o form com erros (sem criar usuário)
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
            return redirect('listar_doador')
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
