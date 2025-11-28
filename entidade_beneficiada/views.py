from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import EntidadeBeneficiadaForm
from .models import EntidadeBeneficiada


def is_assistente_social(user):
    return user.is_superuser


@login_required
def entidade_list(request):
    entidades = EntidadeBeneficiada.objects.all()
    return render(request, 'entidade_beneficiada/entidade_list.html', {
        'entidades': entidades,
    })

@login_required
def entidade_create(request):
    if request.method == 'POST':
        form = EntidadeBeneficiadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entidade_list')
    else:
        form = EntidadeBeneficiadaForm()
    return render(request, 'entidade_beneficiada/entidade_form.html', {
        'form': form,
        'acao': 'Criar'
    })

@login_required
def entidade_update(request, pk):
    entidade = get_object_or_404(EntidadeBeneficiada, pk=pk)

    if request.method == 'POST':
        form = EntidadeBeneficiadaForm(request.POST, instance=entidade)
        if form.is_valid():
            form.save()
            return redirect('entidade_list')
    else:
        form = EntidadeBeneficiadaForm(instance=entidade)

    return render(request, 'entidade_beneficiada/entidade_form.html', {
        'form': form,
        'acao': 'Editar'
    })

@login_required
def entidade_delete(request, pk):
    entidade = get_object_or_404(EntidadeBeneficiada, pk=pk)

    if request.method == 'POST':
        entidade.delete()
        return redirect('entidade_list')

    return render(request, 'entidade_beneficiada/entidade_confirm_delete.html', {
        'entidade': entidade
    })

@login_required
def entidade_detail(request, pk):
    entidade = get_object_or_404(EntidadeBeneficiada, pk=pk)
    return render(request, 'entidade_beneficiada/entidade_detail.html', {
        'entidade': entidade
    })
