from django.shortcuts import render, redirect
from .forms import AlunoForm
from .forms import BibliotecarioCreationForm

def cadastrar_livro(request):
    return render(request, 'cadastrar_livro.html')
def cadastrar_bibliotecario(request):
    return render(request, 'template_cadastrar_bibliotecario.html')
def cadastrar_autor(request):
    return render(request, 'cadastrar_autor.html')
def cadastrar_genero(request):
    return render(request, 'cadastrar_genero.html')
def cadastrar_aluno(request):
    return render(request, 'cadastrar_aluno.html')

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_aluno') 
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})

def cadastrar_bibliotecario(request):
    if request.method == 'POST':
        form = BibliotecarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_bibliotecario')
    else:
        form = BibliotecarioCreationForm()

    return render(request, 'template_cadastrar_bibliotecario.html', {'form': form})
