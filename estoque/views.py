from django.shortcuts import get_object_or_404, redirect, render
#from httpcore import request
from doacao.models import Doacao
from estoque.models import Item
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('estoque.view_item', raise_exception=True)
def listar_estoque(request):
    items = Item.objects.all().order_by('categoria', 'nome', 'quantidade')
    return render(request, 'estoque/listar_estoque.html', {'items': items})

@login_required
@permission_required('estoque.view_item', raise_exception=True)
def adicionar_estoque(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = int(request.POST.get('quantidade'))
        unidade_medida = request.POST.get('unidade_medida')
        categoria = request.POST.get('categoria')

        item, created = Item.objects.get_or_create(
            nome=nome,
            unidade_medida=unidade_medida,
            categoria=categoria,
            defaults={'quantidade': 0}
        )

        return redirect('listar_estoque')

    return render(request, 'estoque/adicionar_estoque.html')

@login_required
@permission_required('estoque.view_item', raise_exception=True)
def editar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        # Atualiza os campos do item
        item.nome = request.POST.get('nome')
        item.quantidade = int(request.POST.get('quantidade'))
        item.unidade_medida = request.POST.get('unidade_medida')
        item.categoria = request.POST.get('categoria')
        item.save()
        return redirect('listar_estoque')  
    return render(request, 'estoque/editar_deletar.html', {'item': item, 'acao': 'editar'})

@login_required
@permission_required('estoque.view_item', raise_exception=True)
def deletar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('listar_estoque')
    return render(request, 'estoque/editar_deletar.html', {'item': item, 'acao': 'deletar'})

@login_required
@permission_required('estoque.view_item', raise_exception=True)
def detalhar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    doacoes = Doacao.objects.filter(nome=item.nome)
    return render(request, 'estoque/detalhar_item.html', {'item': item, 'doacoes': doacoes})