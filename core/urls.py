
from django.urls import path
from.views import home, galeria, formulario, eliminar_perroFundacion, modificar_perroFundacion, listaperro


urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    
    path('eliminar-perro/<id>/', eliminar_perroFundacion, name="eliminar_perro"),
    path('modificar-perro/<id>/', modificar_perroFundacion, name="modoficar-perro"),
    path('listaperro/', listaperro, name="listaperro"),
]
