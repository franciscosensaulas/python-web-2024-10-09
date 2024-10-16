from django.urls import path

from steamfake import views

# http://127.0.0.1:8000/steamfake/categoria
urlpatterns = [
    path("", views.home),
    path("categoria", views.categoria_index, name="categorias"),
    path("categoria/cadastro", views.categoria_cadastro),
    path("categoria/cadastrar", views.categoria_cadastrar),
    path("categoria/apagar/<int:id>", views.categoria_apagar),
    path("categoria/editar/<int:id>", views.categoria_editar),
    path("categoria/editado/<int:id>", views.categoria_editado),
]