from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite o nome do autor',
                'autocomplete': 'off',
                'id': 'autor'
            })
        }
        labels = {
            'nome': 'Autor'
        }
