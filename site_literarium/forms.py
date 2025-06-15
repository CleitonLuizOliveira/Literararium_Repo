from django import forms
from .models import Aluno, Bibliotecario

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

class BibliotecarioCreationForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = Bibliotecario
        fields = ['nome', 'email']

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmar = self.cleaned_data.get('confirmar_senha')
        if senha and confirmar and senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")
        return confirmar

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])
        if commit:
            usuario.save()
        return usuario
