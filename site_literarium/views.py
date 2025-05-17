from django.shortcuts import render

def cadastrar_livro(request):
    return render(request, 'cadastrar_livro.html')
