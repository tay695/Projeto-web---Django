from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PontoColeta
from .forms import PontoColetaForm

def is_assistente_social(user):
    return user.is_superuser

@login_required
def ponto_list(request):
    pontos = PontoColeta.objects.filter(status='ATIVO').order_by('nome') 
    context = {'pontos': pontos}
    return render(request, 'ponto_coleta/ponto_list.html', context)

@login_required
@user_passes_test(is_assistente_social)
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
@user_passes_test(is_assistente_social)
def ponto_detail(request, pk):
    ponto = get_object_or_404(PontoColeta, pk=pk)
    return render(request, 'ponto_coleta/ponto_detail.html', {'ponto': ponto})

@login_required
@user_passes_test(is_assistente_social)
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
@user_passes_test(is_assistente_social)
def ponto_delete(request, pk):
    ponto = get_object_or_404(PontoColeta, pk=pk)
    if request.method == 'POST':
        ponto.delete()
        return redirect('ponto_full_list')

    return render(request, 'ponto_coleta/ponto_delete.html', {'ponto': ponto})

@login_required
@user_passes_test(is_assistente_social)
def ponto_full_list(request):
    pontos = PontoColeta.objects.all().order_by('nome') 
    context = {'pontos': pontos}
    return render(request, 'ponto_coleta/ponto_list.html', context)

@login_required
@user_passes_test(is_assistente_social)
def confirmar_coleta(request, pk):
    ponto = get_object_or_404(PontoColeta, pk=pk)
    ponto.coletado = True
    ponto.save()
    return redirect('ponto_full_list')

@login_required
@user_passes_test(is_assistente_social)
def confirmar_doacao(request, doacao_pk):
    doacao = get_object_or_404(doacao, pk=doacao_pk)
    doacao.coletada = True
    doacao.save()
    return redirect('ponto_full_list')
