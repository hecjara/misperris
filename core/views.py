from django.shortcuts import render, redirect
from .models import Raza, Estado, Genero, PerroFundacion
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404
from django_xhtml2pdf.utils import pdf_decorator
from datetime import datetime

# Create your views here.

def home(request):
    perros = PerroFundacion.objects.filter(estado=1)
    return render(request, 'core/home.html',
    {
        'perros':perros
    })


def galeria(request):
    perros2 = PerroFundacion.objects.filter(estado=2)
    return render(request, 'core/galeria.html',{
        'perros2':perros2

    })



def listaperro(request):
    perros = PerroFundacion.objects.all()
    return render(request, 'core/listaperro.html',{
        'perros':perros
    })



def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)



@login_required
@group_required('Voluntario')
def formulario(request):
    generos = Genero.objects.all()
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    perros = PerroFundacion.objects.all()
    variables = {
        'generos': generos,
        'razas': razas,
        'estados': estados,
        'perros':perros
    }

    if(request.POST):

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

@group_required('Voluntario')
def eliminar_perroFundacion(request, id):

    perroFundacion = PerroFundacion.objects.get(id=id)

    try:
        perroFundacion.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listaperro')

@group_required('Voluntario')
def modificar_perroFundacion(request, id):

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
        return redirect('listaperro')

    return render(request, 'core/modificar_perro.html', variables)


fechaActual = str(datetime.now().strftime('%d-%m-%Y'))

@pdf_decorator(pdfname="informeMisPerris_Fecha"+fechaActual+".pdf")
def perros_pdf(request):
    perros = PerroFundacion.objects.all()
    return render(request, 'core/perros_pdf.html',{
       'perros':perros 
    })