from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from .models import PontoColeta 
from .forms import PontoColetaForm
from doacao.models import Doacao


def is_doador(user):
    try:
        return user.groups.filter(name='Doador').exists()
    except:
        return False



@login_required
@permission_required('ponto_coleta.view_pontocoleta')
def ponto_list(request):

    pontos = PontoColeta.objects.filter(status='ATIVO').order_by('nome') 
    usuario_e_doador = is_doador(request.user)
    
    if usuario_e_doador:
        pontos_filtrados_com_doacoes = [] 
        
        try:
          
            objeto_doador = request.user.doador 
        except:
            objeto_doador = None
        
        for ponto in pontos:
            if objeto_doador:
             
                doacoes_do_usuario = ponto.doacao_set.filter(doador=objeto_doador)
            else:
                doacoes_do_usuario = ponto.doacao_set.none() 
            
           
            ponto.doacoes_filtradas = doacoes_do_usuario
            
            pontos_filtrados_com_doacoes.append(ponto)
        
       
        pontos = pontos_filtrados_com_doacoes
        
    context = {'pontos': pontos, 'is_doador' : usuario_e_doador}
    return render(request, 'ponto_coleta/ponto_list.html', context)


@login_required
@permission_required('ponto_coleta.add_pontocoleta')
def ponto_create(request):
 
    if request.method == 'POST':
        form = PontoColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ponto_full_list') 
    else:
        form = PontoColetaForm()

    return render(request, 'ponto_coleta/ponto_form.html', {'form': form, 'acao': 'Criar'})

@login_required
@permission_required('ponto_coleta.view_pontocoleta')
def ponto_detail(request, pk):

    ponto = get_object_or_404(PontoColeta, pk=pk)
    return render(request, 'ponto_coleta/ponto_detail.html', {'ponto': ponto})

@login_required
@permission_required('ponto_coleta.change_pontocoleta')
def ponto_update(request, pk):

    ponto = get_object_or_404(PontoColeta, pk=pk)
    if request.method == 'POST':
        form = PontoColetaForm(request.POST, instance=ponto)
        if form.is_valid():
            form.save()
            return redirect('ponto_full_list')
    else:
        form = PontoColetaForm(instance=ponto)

    return render(request, 'ponto_coleta/ponto_form.html', {'form': form, 'acao': 'Editar'})

@login_required
@permission_required('ponto_coleta.delete_pontocoleta')
def ponto_delete(request, pk):
 
    ponto = get_object_or_404(PontoColeta, pk=pk)
    if request.method == 'POST':
        ponto.delete()
        return redirect('ponto_full_list')

    return render(request, 'ponto_coleta/ponto_delete.html', {'ponto': ponto})


@login_required
@permission_required('ponto_coleta.view_pontocoleta')
def ponto_full_list(request):
   
    pontos = PontoColeta.objects.all().order_by('nome') 
    usuario_e_doador = is_doador(request.user)

    if usuario_e_doador:
        pontos_filtrados_com_doacoes = []
        try:
            objeto_doador = request.user.doador
        except:
            objeto_doador = None
        
        for ponto in pontos:
            if objeto_doador:
                
                doacoes_do_usuario = ponto.doacao_set.filter(doador=objeto_doador)
            else:
                doacoes_do_usuario = ponto.doacao_set.none()

          
            ponto.doacoes_filtradas = doacoes_do_usuario
            
            pontos_filtrados_com_doacoes.append(ponto)
        
        
        pontos = pontos_filtrados_com_doacoes
        
    context = {'pontos': pontos, 'is_doador': usuario_e_doador}
    return render(request, 'ponto_coleta/ponto_list.html', context)


@login_required
@permission_required('ponto_coleta.change_pontocoleta')
def confirmar_coleta(request, pk):
   
    ponto = get_object_or_404(PontoColeta, pk=pk)
    ponto.coletado = True 
    ponto.save()
    return redirect('ponto_full_list')

@login_required
@permission_required('doacao.change_doacao')
def confirmar_doacao(request, doacao_pk):
   
    doacao = get_object_or_404(Doacao, pk=doacao_pk)
    
    doacao.coletada = True
    doacao.save()
    
    return redirect('ponto_full_list')