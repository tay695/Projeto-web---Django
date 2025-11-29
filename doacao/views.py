from django.shortcuts import get_object_or_404, render, redirect
from doacao.forms import DoacaoForm
from estoque.models import EntradaEstoque
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from doacao.models import Doacao
from django.db.models import Count, Sum


@login_required
@permission_required('doacao.add_doacao')
def criar_doacao(request):
    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("listar_estoque")
    else:
        form = DoacaoForm()

    return render(request, "doacao/criar_doacao.html", {"form": form})

@login_required
@permission_required('doacao.view_doacao')
def dashboard_doacoes(request):
    stats = Doacao.objects.aggregate(
        total_doacoes=Count('id'),
        total_quantidade=Sum('quantidade'),
    )
    por_categoria = (
        Doacao.objects
        .values('categoria')
        .annotate(count=Count('id'), total_qtd=Sum('quantidade'))
        .order_by('-total_qtd')
    )
    
    ultimas_doacoes = (
        Doacao.objects
        .all()
        .order_by('-data_doacao')[:10]
    )
    
    top_doadores = (
        Doacao.objects
        .values('doador')
        .annotate(total_qtd=Sum('quantidade'), count=Count('id'))
        .order_by('-total_qtd')[:5]
    )
    
    context = {
        'stats': stats,
        'por_categoria': list(por_categoria),
        'ultimas_doacoes': ultimas_doacoes,
        'top_doadores': list(top_doadores),
    }
    return render(request, "doacao/dashboard_doacoes.html", context)

@login_required
@permission_required('doacao.change_doacao')
def editar_doacao(request, id):
    doacao = Doacao.objects.get(id=id)
    if request.method == "POST":
        form = DoacaoForm(request.POST, instance=doacao)
        if form.is_valid():
            form.save()  
            return redirect("listar_estoque")
    else:
        form = DoacaoForm(instance=doacao)  
        
    return render(request, "doacao/editar_doacao.html", {"form": form, "doacao": doacao, 'action_type': 'edit_doacao'})

@login_required
def confirmar_coleta(request, id):
    doacao = get_object_or_404(Doacao, id=id)

    doacao.coletada = True
    doacao.save()  # aqui o estoque é atualizado automaticamente!

    return redirect('dashboard_doacoes')

@login_required
@permission_required('doacao.delete_doacao')
def deletar_doacao(request, id):
    doacao = Doacao.objects.get(id=id)
    if request.method == "POST":
        doacao.delete()
        return redirect("listar_estoque")
    
    return render(request, "doacao/confirmar_delete.html", {"doacao": doacao, 'action_type': 'delete_doacao'})