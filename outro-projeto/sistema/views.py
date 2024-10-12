from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

#region outros
def index(request: HttpRequest) -> HttpResponse:
    # request => requisição que é feita no navegador para o back-end 
    # response => resposta que o back-end devolve para o navegador
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

#endregion

def calcular(request: HttpRequest) -> HttpResponse:
    # request.GET é o método da requisição, quais são possíveis de utilizar:
    # request.GET a inforamação vai na URL (https://localhost:8000/sistema/calcular?numero1=9&numero2=21)
    # request.POST a informação vai por de baixo dos panos (https://localhost:8000/sistema/calcular)
    # .get => é utilizado para obter um valor
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))

    soma = numero1 + numero2

    if numero1 > numero2:
        maior = "Primeiro número"
    else:
        maior = "Segundo número"
    
    dados_para_html = {
        "soma": soma,
        "maior": maior,
        "numero1": numero1,
        "numero2": numero2,
    }

    return render(request, "resultado.html", context=dados_para_html)