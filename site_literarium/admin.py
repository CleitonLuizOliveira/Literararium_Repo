from django.contrib import admin
from .models import Aluno
from .models import Bibliotecario

admin.site.register(Bibliotecario)

admin.site.register(Aluno)