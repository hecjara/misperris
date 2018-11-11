from django.urls import path
from .views import listar_perros, agregar_perro, modificar_perro, eliminar_perro
urlpatterns = [
    path('perros/', listar_perros, name="api_listar_perros"),
    path('perros/agregar/', agregar_perro, name="api_agregar_perro"),
    path('perros/modificar/', modificar_perro, name="api_modificar_perro"),
    path('perros/<id>/eliminar/', eliminar_perro, name="api_eliminar_perro"),
]