from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
import json
from core.models import PerroFundacion, Genero, Raza, Estado
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def listar_perros(request):
    perros = PerroFundacion.objects.all()

    perrosJson = serializers.serialize('json', perros)

    return HttpResponse(perrosJson, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def agregar_perro(request):
    body = request.body.decode('utf-8')

    body_diccionario = json.loads(body)

    perro = PerroFundacion()
    perro.nombre = body_diccionario['nombre']
    perro.raza = Raza(id=body_diccionario['raza_id'])
    perro.genero = Genero(id=body_diccionario['genero_id'])
    perro.fechaIngreso = body_diccionario['fechaIngreso']
    perro.fechaNacimiento = body_diccionario['fechaNacimiento']
    perro.estado = Estado(id=body_diccionario['estado_id'])

    try:
        perro.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")