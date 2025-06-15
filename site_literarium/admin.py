from django.contrib import admin
from .models import Autor
from .models import Aluno
from .models import Bibliotecario

admin.site.register(Bibliotecario)


admin.site.register(Autor)
admin.site.register(Aluno)

