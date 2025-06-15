from django.db import models
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
