from django.urls import path
from .views import listar_perros, agregar_perro
urlpatterns = [
    path('perros/', listar_perros, name="api_listar_perros"),
    path('perros/agregar/', agregar_perro, name="api_agregar_perro"),
]