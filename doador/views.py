from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from doador.form import DoadorForm
from doador.models import Doador
from django.contrib.auth.decorators import login_required, permission_required 


@login_required
@permission_required('doador.view_doador')
def perfil_doador(request, id):
    doador = Doador.objects.get(id=id)
    return render(request, 'doador/perfil_doador.html', {'doador': doador})

@login_required
@permission_required('doador.listar_doador')
def listar_doador(request):
    doadores = Doador.objects.all()
    return render(request, 'listar_doador.html', {'doadores': doadores})   


@login_required
@permission_required('doador.add_doador')
def cadastro_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doador') 
    else:
        form = DoadorForm()
    
    return render(request, 'cadastro_doador.html', {'form': form})



@login_required
@permission_required('doador.change_doador')
def editar_doador (request, id):
    doador = Doador.objects.get(id=id)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect('doador_cadastro'))
    else:
        form = DoadorForm(instance=doador)
    
    return render(request, 'cadastro_doador.html', {'form': form, 'doador': doador, 'action_type': 'edit_doador'})



@login_required
@permission_required('doador.delete_doador')
def deletar_doador (request, id):
    doador = Doador.objects.get(doador, id=id)
    if request.method == 'POST':
        doador.delete()
        return HttpResponseRedirect(redirect('doador_cadastro'))
    return render(request, 'doador/cadastro_doador.html', {'doador': doador, 'action_type': 'delete_doador'})
