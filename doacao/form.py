from django import forms
from .models import doacao


class doacaoForm(forms.ModelForm):
    class Meta:
        model = doacao
        fields = ['doador', 'item', 'quantidade', 'data_doacao']
        
        
        
class doacaoStatusForm(forms.ModelForm):
    class Meta:
        model = doacao
        fields = ['status']