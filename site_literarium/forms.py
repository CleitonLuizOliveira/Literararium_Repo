from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'turma', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', "As senhas não coincidem.")