from django import forms
from doador.models import Doador

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'email', 'telefone', 'endereco']

class DoadorDeleteForm(forms.ModelForm):
    def __init__(sefl, *args, **kwargs):
        super(DoadorDeleteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True