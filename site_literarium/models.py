from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone 

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50, unique=True)
    turma = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class BibliotecarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not nome:
            raise ValueError("O nome é obrigatório")

        email = self.normalize_email(email)
        usuario = self.model(email=email, nome=nome)
        usuario.set_password(senha)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nome, senha):
        usuario = self.create_user(email, nome, senha)
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Bibliotecario(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BibliotecarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField()
    sinopse = models.TextField()
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    
    # Relação Observer: Alunos (Observers) na lista de espera do Livro (Subject)
    lista_espera = models.ManyToManyField(
        Aluno, 
        related_name='livros_em_espera', 
        blank=True,
        verbose_name="Alunos na lista de espera"
    )

    def __str__(self):
        return self.titulo

    # --- Implementação do Padrão Observer ---

    def emprestar_livro(self):
        """ Tenta emprestar o livro. Retorna True se bem-sucedido, False se não houver estoque. """
        if self.quantidade > 0:
            self.quantidade -= 1
            self.save()
            return True
        return False

    def devolver_livro(self):
        """ Devolve um livro ao acervo e notifica a lista de espera se o livro estava esgotado. """
        # Verifica se o livro estava esgotado (quantidade == 0) ANTES de adicionar
        notificar = (self.quantidade == 0)
        
        self.quantidade += 1
        self.save()

        # Se estava esgotado (e agora não está mais), notifica os observadores
        if notificar:
            self.notificar_alunos()

    def adicionar_aluno(self, aluno):
        """ Adiciona um aluno (Observer) à lista de espera, se o livro estiver esgotado. """
        if self.quantidade == 0:
            self.lista_espera.add(aluno)
            return True # Aluno adicionado à lista
        return False # Livro disponível, não precisa de lista de espera

    def notificar_alunos(self):
        """ Notifica todos os Alunos (Observers) na lista de espera. """
        alunos_na_lista = self.lista_espera.all()
        
        for aluno in alunos_na_lista:
            # Cria um objeto de notificação (forma de testar a notificação)
            mensagem = f"O livro '{self.titulo}' que você estava aguardando está disponível!"
            Notificacao.objects.create(
                aluno=aluno, 
                livro=self, 
                mensagem=mensagem
            )
            
            # (Opcional) Log no console
            print(f"Notificando {aluno.nome}: {mensagem}")

        # Limpa a lista de espera após notificar
        self.lista_espera.clear()


class Notificacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notificacoes')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificação para {self.aluno.nome} sobre {self.livro.titulo}"