from django.urls import path
from .views import listar_perros
urlpatterns = [
    path('perros/', listar_perros, name="api_listar_perros")
]