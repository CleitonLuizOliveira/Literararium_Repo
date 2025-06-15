from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

    def __str__(self):
        return self.titulo