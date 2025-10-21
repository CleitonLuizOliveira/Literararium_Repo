from django.contrib import admin
from .models import Aluno, Autor, Bibliotecario, Genero, Livro, Notificacao

# --- Ações customizadas para o Admin ---

@admin.action(description='Simular Empréstimo (Decrementar quantidade)')
def simular_emprestimo(modeladmin, request, queryset):
    """ Ação para simular o empréstimo de livros selecionados. """
    for livro in queryset:
        sucesso = livro.emprestar_livro()
        if sucesso:
            modeladmin.message_user(request, f"Livro '{livro.titulo}' emprestado. Quantidade restante: {livro.quantidade}", 'success')
        else:
            modeladmin.message_user(request, f"Não foi possível emprestar '{livro.titulo}'. Quantidade em estoque: 0.", 'warning')

@admin.action(description='Simular Devolução (Incrementar quantidade e Notificar)')
def simular_devolucao(modeladmin, request, queryset):
    """ Ação para simular a devolução de livros e disparar notificações. """
    for livro in queryset:
        livro.devolver_livro()
        modeladmin.message_user(request, f"Livro '{livro.titulo}' devolvido. Quantidade atual: {livro.quantidade}.", 'success')


# --- Configurações do Admin ---

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'quantidade')
    search_fields = ('titulo', 'autor__nome')
    
    # Facilita a visualização e adição de alunos na lista de espera
    filter_horizontal = ('lista_espera',)
    
    # Adiciona as ações que criamos
    actions = [simular_emprestimo, simular_devolucao]

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'livro', 'mensagem', 'data_criacao', 'lida')
    list_filter = ('lida', 'data_criacao')
    search_fields = ('aluno__nome', 'livro__titulo')


# Registra os modelos
admin.site.register(Aluno)
admin.site.register(Autor)
admin.site.register(Bibliotecario)
admin.site.register(Genero)
admin.site.register(Livro, LivroAdmin) # Usa o LivroAdmin customizado
admin.site.register(Notificacao, NotificacaoAdmin) # Registra o novo modelo