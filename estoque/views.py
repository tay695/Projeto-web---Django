from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from estoque.models import Item
def index(request):
    return HttpResponse("Bem-vindo ao sistema de estoque!")

def listar_estoque(request):
    items = Item.objects.all().order_by('nome', 'categoria', 'quantidade')
    return render

def adcionar_estoque(request):

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
        print(item, created)
        return redirect('listar_estoque')

    return render(request, 'estoque/adicionar_estoque.html')

def editar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.nome = request.POST.get('nome')
        item.quantidade = int(request.POST.get('quantidade', 0))
        item.unidade_medida = request.POST.get('unidade_medida')
        item.categoria = request.POST.get('categoria')
        item.save()
        print(item, "editado com sucesso")
        return redirect('listar_estoque')

    return render(request, 'estoque/editar_item.html', {'item': item})

def deletar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.delete()
        print(item, "deletado com sucesso")
        return redirect('listar_estoque')
    return render(request, 'estoque/deletar_item.html', {'item': item})

def detalhar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'estoque/detalhar_item.html', {'item': item})