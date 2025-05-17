from django.shortcuts import render

def cadastrar_livro(request):
    return render(request, 'cadastrar_livro.html')
def cadastrar_bibliotecario(request):
    return render(request, 'template_cadastrar_bibliotecario.html')
