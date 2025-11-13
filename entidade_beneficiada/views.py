from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import EntidadeBeneficiada 

class AssistenteSocialRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser



class EntidadeListView(AssistenteSocialRequiredMixin, ListView):
    model = EntidadeBeneficiada
    template_name = 'entidade_beneficiada/entidade_list.html'
    context_object_name = 'entidades' # Variável usada no template HTML

class EntidadeCreateView(AssistenteSocialRequiredMixin, CreateView):
    model = EntidadeBeneficiada
    # Lembre-se de incluir o campo 'num_membros' que você adicionou
    fields = ['nome', 'responsavel', 'endereco', 'prioridade', 'num_membros']
    template_name = 'entidade_beneficiada/entidade_form.html'
    success_url = reverse_lazy('entidade_list')

class EntidadeUpdateView(AssistenteSocialRequiredMixin, UpdateView):
    model = EntidadeBeneficiada
    fields = ['nome', 'responsavel', 'endereco', 'prioridade', 'num_membros']
    template_name = 'entidade_beneficiada/entidade_form.html'
    success_url = reverse_lazy('entidade_list')

class EntidadeDeleteView(AssistenteSocialRequiredMixin, DeleteView):
    model = EntidadeBeneficiada
    template_name = 'entidade_beneficiada/entidade_confirm_delete.html'
    success_url = reverse_lazy('entidade_list')