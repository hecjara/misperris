from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json
from core.models import PerroFundacion, Genero, Raza, Estado
# Create your views here.

def listar_perros(request):
    perros = PerroFundacion.objects.all()

    perrosJson = serializers.serialize('json', perros)

    return HttpResponse(perrosJson, content_type="application/json")


