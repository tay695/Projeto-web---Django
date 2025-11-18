from django.shortcuts import render
from django.http import HttpResponse
from form import doacaoForm


def criar_doacao(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = doacaoForm(request.POST)
            if form.is_valid():
                form.save()
        return HttpResponse("Doação criada com sucesso!")
    else:
        form = doacaoForm()
    return render(request, 'doacao/formulario_doacao.html')


def index(request):
    return HttpResponse("Página de Doações")
