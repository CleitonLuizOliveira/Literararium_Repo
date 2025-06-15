from django.shortcuts import render
from .forms import AutorForm

def cadastrar_livro(request):
    return render(request, 'cadastrar_livro.html')
def cadastrar_bibliotecario(request):
    return render(request, 'template_cadastrar_bibliotecario.html')
def cadastrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_autor') 
    else:
        form = AutorForm()
    return render(request, 'cadastrar_autor.html', {'form': form})
def cadastrar_genero(request):
    return render(request, 'cadastrar_genero.html')
def cadastrar_aluno(request):
    return render(request, 'cadastrar_aluno.html')
