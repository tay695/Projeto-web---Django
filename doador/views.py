from django.shortcuts import render
from http import HttpResponseRedirect
from form import DoadorForm


def cadastro_doador(request):
   if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request, 'cadastro_doador.html')

