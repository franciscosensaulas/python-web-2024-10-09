from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

# request => requisição que é feita no navegador para o back-end 
# response => resposta que o back-end devolve para o navegador
def index(request: HttpRequest) -> HttpResponse:
    # Obteve o arquivo templates/index.html e armazena na variável template
    template = loader.get_template(template_name="index.html")
    # Renderizar o template armazenando na variável html, ou seja, 
    # vai gerar o html
    html = template.render(context={}, request=request)
    # Instanciando um objeto da classe HttpResponse defindindo o que será 
    # retornado da requisição
    response = HttpResponse(content=html)
    # Retornar o response
    return response


def contato(request: HttpRequest) -> HttpResponse:
    # # Obteve o arquivo templates/contato.html e armazena na variável template
    # template = loader.get_template(template_name="contato.html")
    # # Renderizar o template armazenando na variável html, ou seja, 
    # # vai gerar o html
    # html = template.render(context={}, request=request)
    # # Instanciando um objeto da classe HttpResponse defindindo o que será 
    # # retornado da requisição
    # response = HttpResponse(content=html)
    # # Retornar o response
    # return response
    return render(request, "contato.html", context={})


def calculadora(request: HttpRequest) -> HttpResponse:
    return render(request, "calculadora.html", context={})

def calcular(request: HttpRequest) -> HttpResponse:
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    soma = numero1 + numero2
    dados_para_html = {
        "soma": soma
    }
    return render(request, "resultado.html", context=dados_para_html)