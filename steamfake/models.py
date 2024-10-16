from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=23, unique=True)

    def __str__(self):
        return self.nome
    
    # Tag
    # id, nome, descricao (textarea)
    # 
    # Ordem:
    # models.py
    # gerar migração
    # aplicar migração
    # ursl.py para index da tag
    # views.py para index da tag
    # criar o arquivo templates/tags/index.html
    # Cadastrar, apagar, editar


# DROP DATABASE IF EXISTS steam_fake_db
# CREATE DATABASE steam_fake_db CHARACTER SET UTF8MB4;
# py manage.py makemigrations
# py manage.py migrate

# class Aluno(models.Model):
#     nome = models.CharField(max_length=10) # Varchar
#     nota1 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota2 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota3 = models.DecimalField(default=0, decimal_places=2, max_digits=4)

# class Curso(models.Model):
#     nome = models.CharField(max_length=50)
#     duracao = models.IntegerField(default=0)


# class Turma(models.Model):
#     data_inicio = models.DateTimeField()
#     curso = models.ForeignKey(
#         Curso, on_delete=models.CASCADE, blank=True, null=True,
#     )
    