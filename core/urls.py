
from django.urls import path
from.views import home, galeria, formulario, eliminar_perroFundacion, modificar_perroFundacion, listaperro, perros_pdf


urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    
    path('eliminar-perro/<id>/', eliminar_perroFundacion, name="eliminar_perro"),
    path('modificar-perro/<id>/', modificar_perroFundacion, name="modoficar-perro"),
    path('listaperro/', listaperro, name="listaperro"),
    path('perros_pdf/', perros_pdf, name="perros_pdf"),
]
