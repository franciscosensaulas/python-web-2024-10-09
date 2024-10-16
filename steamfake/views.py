from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from steamfake.models import Categoria


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


# Create your views here.
def categoria_index(request: HttpRequest) -> HttpResponse:
    categorias = Categoria.objects.all()
    dados = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=dados)

def categoria_cadastro(request: HttpRequest) -> HttpResponse:
    return render(request, "categorias/cadastro.html")


def categoria_cadastrar(request: HttpRequest) -> HttpResponse:
    # Obter o nome que o usuário preencheu na tela
    nome = request.POST.get("nome")
    # Instanciar um objeto da categoria
    categoria = Categoria(nome=nome)
    # Persistir a categoria na tabela, INSERT INTO (nome) VALUES (?)
    categoria.save()
    # REdirecionar para a tela de lista de categorias
    return redirect("categorias")


def categoria_apagar(request:HttpRequest, id: int) -> HttpResponse:
    # Buscar a categoria por id, SELECT * FROM categorias WHERE id = ?
    categoria = Categoria.objects.get(pk=id)
    # Apagar a categoria por id, DELETE FROM categorias WHERE id = ?
    categoria.delete()
    # Redirecionar para a tela de lista de categorias
    return redirect("categorias")

def categoria_editar(request: HttpRequest, id: int) -> HttpResponse:
    # Buscar a categoria do banco filtrando por id
    categoria = Categoria.objects.get(pk=id)
    dados = {
        "categoria": categoria
    }
    return render(request, "categorias/editar.html", context=dados)


def categoria_editado(request: HttpRequest, id: int) -> HttpResponse:
    # Obter o nome que o usuário preencheu na tela
    nome = request.POST.get("nome")
    # Buscar a categoria por id
    categoria = Categoria.objects.get(pk=id)
    categoria.nome = nome
    # Atualizar a categoria na tabela, UPDATE categorias SET nome = ? WHERE id = ?
    categoria.save()
    # Redirecionar para a tela de lista de categorias
    return redirect("categorias")
