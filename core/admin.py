from django.contrib import admin
from.models import Raza, Estado, Genero, PerroFundacion
# Register your models here.

class PerroFundacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'genero', 'fechaIngreso', 'fechaNacimiento', 'descripcion', 'estado', 'imagen')
    search_fields = ('nombre', 'raza', 'genero', 'fechaIngreso', 'fechaNacimiento', 'descripcion', 'estado')
    list_filter = ('raza', 'genero', 'estado')

admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Genero)
admin.site.register(PerroFundacion, PerroFundacionAdmin)

