
from django.urls import path
from.views import home, galeria, formulario, listar_perros_fundacion, eliminar_perroFundacion, modificar_perroFundacion


urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('listar_perros_fundacion/', listar_perros_fundacion, name="listar_perros_fundacion"),
    path('eliminar-perro/<id>/', eliminar_perroFundacion, name="eliminar_perro"),
    path('modificar-perro/<id>/', modificar_perroFundacion, name="modoficar-perro"),
]
