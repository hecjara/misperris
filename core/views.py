from django.shortcuts import render, redirect
from .models import Raza, Estado, Genero, PerroFundacion
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404


# Create your views here.


def home(request):
    perros = PerroFundacion.objects.filter(estado=1)
    return render(request, 'core/home.html',
    {
        'perros':perros
    })


def galeria(request):
    perros = PerroFundacion.objects.filter(estado=1)
    perros2 = PerroFundacion.objects.filter(estado=2)
    return render(request, 'core/galeria.html',{
        'perros':perros,
        'perros2':perros2

    })

def listar_perros(request):
    perros = PerroFundacion.objects.filter(estado=1)
    return render(request, 'core/listar_perros_fundacion.html',{
        'perros':perros
    })




@login_required
def formulario(request):

    generos = Genero.objects.all()
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    perros = PerroFundacion.objects.filter(estado=1)
    variables = {
        'generos': generos,
        'razas': razas,
        'estados': estados,
        'perros':perros
    }

    if(request.POST):

        #PERMISOS PARA VOLUNTARIOS Y MIEMBROS DEL STAFF
        if not request.user.is_staff or not request.user.is_Voluntario:
            raise Http404

        perro = PerroFundacion()
        perro.nombre = request.POST.get('txtnombre')
        raza = Raza()
        raza.id = request.POST.get('cboraza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cbogenero')
        perro.genero = genero
        perro.fechaIngreso = request.POST.get('dtFechaIngreso')
        perro.fechaNacimiento = request.POST.get('dtFechaNacimiento')
        perro.descripcion = request.POST.get('txtdescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboestado')
        perro.estado = estado
        perro.imagen = request.FILES.get('imagenperro')

        try:
            perro.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/formulario.html', variables)








    



# CRUD PERROS FUNDACION

def listar_perros_fundacion(request):

    perroFundacion = PerroFundacion.objects.all()

    return render(request, 'core/listar_perros_fundacion.html', {
        'perroFundacion': perroFundacion
    })


def eliminar_perroFundacion(request, id):

    #PERMISOS PARA VOLUNTARIOS Y MIEMBROS DEL STAFF
    if not request.user.is_staff or not request.user.VOLUNTARIOS:
        raise Http404

    perroFundacion = PerroFundacion.objects.get(id=id)

    try:
        perroFundacion.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('perros-fundacion')


def modificar_perroFundacion(request, id):

    #PERMISOS PARA VOLUNTARIOS Y MIEMBROS DEL STAFF
    if not request.user.is_staff or not request.user.VOLUNTARIOS:
        raise Http404

    perro = PerroFundacion.objects.get(id=id)
    generos = Genero.objects.all()
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    variables = {
        'perro': perro,
        'generos': generos,
        'razas': razas,
        'estados': estados
    }


    if(request.POST):
        perro = PerroFundacion()
        perro.id = request.POST.get('txtid')
        perro.nombre = request.POST.get('txtnombre')
        raza = Raza()
        raza.id = request.POST.get('cboraza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cbogenero')
        perro.genero = genero
        perro.fechaIngreso = request.POST.get('dtFechaIngreso')
        perro.fechaNacimiento = request.POST.get('dtFechaNacimiento')
        perro.descripcion = request.POST.get('txtdescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboestado')
        perro.estado = estado

        try:
            perro.save()
            messages.success(request, 'Modificado correctamente')
        except:
            messages.error(request, 'No se ha podido modificar')
        return redirect('perros-fundacion')

    return render(request, 'core/modificar_perro.html', variables)
