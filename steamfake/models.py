from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=23, unique=True)

# DROP DATABASE IF EXISTS steam_fake_db
# CREATE DATABASE steam_fake_db CHARACTER SET UTF8MB4;