from django.shortcuts import render, redirect
from doacao.form import DoacaoForm
from estoque.models import EntradaEstoque
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
