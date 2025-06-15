from django.contrib import admin
from .models import Aluno, Autor, Bibliotecario, Genero, Livro

admin.site.register(Aluno)
admin.site.register(Autor)
admin.site.register(Bibliotecario)
admin.site.register(Genero)
admin.site.register(Livro)
