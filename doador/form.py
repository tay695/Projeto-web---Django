from models import Doador
from django import forms


class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        class DoadorForm(forms.ModelForm):
            class Meta:
                model = Doador
                fields = ['nome', 'email', 'telefone', 'endereco']