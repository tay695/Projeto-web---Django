from django import forms
from doador.models import Doador

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'email', 'telefone', 'endereco']
