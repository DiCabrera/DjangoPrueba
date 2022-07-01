from django.shortcuts import render
from app_gestion.models import Persona
from django.http import HttpResponse
from django.db.models import Q

def ingreso_persona(request):
    return render(request,"ingreso_persona.html")

def busqueda_persona(request):
    return render(request,"busqueda_persona.html")

def eliminacion_persona(request):
    return render(request,"eliminacion_persona.html")

def listado_persona(request):
    return render(request,"listado_persona.html")

def home(request):
    return render(request,"home.html")


# Create your views here.

# INGRESAR PERSONA
def ingresar_persona(request):
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    rut=request.GET["txt_rut"]
    edad=request.GET["num_edad"]
    nom_vacuna=request.GET["sel_vacuna"]
    fecha=request.GET["dt_fecha"]

    if len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0 and len(rut)>7 and len(rut)<10 and len(edad)>0:
        pro=Persona(nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,rut=rut,edad=edad,nom_vacuna=nom_vacuna,fecha=fecha)
        pro.save()
        mensaje="Datos guardados correctamente en la Base de Datos."
    else:
        mensaje="Ha habido un error en el inggreso de los datos."
    return HttpResponse(mensaje)

# BUSCAR PERSONA
#def buscar_persona(request):
#    if request.GET["txt_rut"]:
#        rut_persona = request.GET["txt_rut"]
#        personas = Persona.objects.filter(nombre_icontains=rut_persona, appaterno_icontains=rut_persona, apmaterno_icontains=rut_persona, edad_icontains=rut_persona, nom_vacuna_icontains=rut_persona, fecha_icontains=rut_persona)
#        return render(request,"busqueda_persona.html",{"Persona":personas , "query":rut_persona})
#    else:
#        mensaje = "El rut ingresado no existe en la Base de Datos"
#        return HttpResponse(mensaje)

def buscar_persona(request):
    if request.GET["txt_rut"]:
        rut_persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(
            Q(nombre__icontains = rut_persona) | 
            Q(appaterno__icontains=rut_persona) | 
            Q(apmaterno__icontains=rut_persona) | 
            Q(edad__icontains=rut_persona) | 
            Q(nom_vacuna__icontains=rut_persona) | 
            Q(fecha__icontains=rut_persona)
        )
        return render(request,"listar.html",{"Persona":personas , "query":rut_persona})
    else:
        mensaje = "El rut ingresado no existe en la Base de Datos"
        return HttpResponse(mensaje)

# ELIMINAR PERSONA
def eliminar_persona(request):
    if request.GET["txt_rut"]:
        rut_persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut=rut_persona)
        if personas:
            pro=Persona.objects.get(rut=rut_persona)
            pro.delete()
            mensaje = "Los registros de la persona han sido eliminados."
                
        else:
            mensaje = "El rut ingresado no existe en la Base de Datos"
    else:
        mensaje = "Debe ingresar un rut"
    return HttpResponse(mensaje)

# LISTAR PERSONAS
def listar_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listado_persona.html",{'personas':datos})
