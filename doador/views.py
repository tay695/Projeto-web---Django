from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .form import CadastroDoadorForm, EditarDoadorForm
from .models import Doador
from django.contrib.auth.decorators import login_required, permission_required


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


@login_required
@permission_required('doador.add_doador')
def cadastro_doador(request):
    if request.method == 'POST':
        form = CadastroDoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doador') 
    else:
        form = CadastroDoadorForm()
    
    return render(request, 'cadastro_doador.html', {'form': form, 'action_type': 'add_doador'})


@login_required
@permission_required('doador.change_doador')
def editar_doador (request, id):
    doador = get_object_or_404(Doador, pk=id)
    
    if request.method == 'POST':
        form = EditarDoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            return redirect('listar_doador') 
        else:
            return render(request, 'cadastro_doador.html', {'form': form, 'doador': doador, 'action_type': 'edit_doador'})
    else:
        form = EditarDoadorForm(instance=doador)
    
    return render(request, 'cadastro_doador.html', {'form': form, 'doador': doador, 'action_type': 'edit_doador'})


@login_required
@permission_required('doador.delete_doador')
def deletar_doador (request, id):
    doador = get_object_or_404(Doador, pk=id)
    
    if request.method == 'POST':
        doador.delete()
        return redirect('listar_doador') 
        
    return render(request, 'cadastro_doador.html', {'doador': doador, 'action_type': 'delete_doador'})