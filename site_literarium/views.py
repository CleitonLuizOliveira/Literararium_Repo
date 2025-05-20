from django.shortcuts import render

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
