from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from doador.form import DoadorForm

def cadastro_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doador_cadastro.html') 
    else:
        form = DoadorForm()
    
    return render(request, 'cadastro_doador.html', {'form': form})

