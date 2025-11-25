from django.shortcuts import render, redirect
from doacao.form import DoacaoForm
from estoque.models import EntradaEstoque
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from doacao.models import Doacao
from django.db.models import Count, Sum

@login_required
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