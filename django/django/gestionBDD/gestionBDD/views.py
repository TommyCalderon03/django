from django.http import HttpResponse
from django.shortcuts import render
import datetime

from gestor.models import articulo, cliente


def formulario(request):
    return render(request, "formulario.html")

def respuesta(request):
    agnoActual=datetime.datetime.now().year
    diaActual=datetime.datetime.now().day
    mesActual=datetime.datetime.now().month
    agnoNacimiento= int(request.GET["nacimiento"].split('-')[0])
    mesNacimeinto=int(request.GET["nacimiento"].split('-')[1])
    diaNacimiento=int(request.GET["nacimiento"].split('-')[2])
    
    edad=agnoActual - agnoNacimiento
    if mesNacimeinto > mesActual:
        edad-=1
    elif mesActual==mesNacimeinto:
        if diaActual < diaNacimiento:
            edad-=1
            
    nombre=request.GET["nombre"]
    genero=request.GET["genero"]
    return render(request, 'respu.html', {'nombre':nombre, 'edad':edad, 'genero':genero})
        
def formularioBusqueda(request):
    arti=[]
    ar=articulo.objects.all()
    for i in ar:
        arti.append(i.seccion)
    arti=sorted(list(set(arti)))
    return render(request, "formuBusqueda.html", {'articulo':arti})

def resultado(request):
    
    if len(request.GET["producto"])>=20:
        arti=[]
        ar=articulo.objects.all()
        for i in ar:
            arti.append(i.seccion)
        arti=sorted(list(set(arti)))
        return render(request, "formuBusqueda.html", {'articulo': arti, 'error':True})
    
    encontrado=True
    if not(request.GET["producto"]=="") and not (request.GET["seccion"]=="todos"):
        nombre=request.GET["producto"]
        seccion=request.GET["seccion"]
        resultado=articulo.objects.filter(nombre__icontains=nombre, seccion=seccion)
        
    elif not(request.GET["producto"]=="") and request.GET["seccion"]=="todos":
        nombre=request.GET["producto"]
        resultado=articulo.objects.filter(nombre__icontains=nombre)
        
    elif request.GET["producto"]=="" and not (request.GET["seccion"]=="todos"):
        seccion=request.GET["seccion"]
        resultado=articulo.objects.filter(seccion=seccion)
        
    elif request.GET["producto"]=="" and request.GET["seccion"]=="todos":
        resultado=articulo.objects.all()
    if not resultado:
        encontrado=False
        
    return render(request, "resulBusqueda.html",{'registro':resultado, 'estatus':encontrado})

def Vali(request):
    return render(request, "registro.html")
    
def validacion(request):
    nombre=request.POST["nombre"]
    direccion=request.POST["direccion"]
    telefono=request.POST["telefono"]
    password=request.POST["password"]
    passwordRep=request.POST["passwordRep"]
    email=request.POST["email"]
    status=verificacion(nombre, direccion, telefono, password, passwordRep, email)
    
    if len(list(status.keys()))>0:
        return render(request, 'registro.html', {'status':status} )
    else:
        cliente.objects.create(nombre=nombre, direccion=direccion, email=email, telefono=telefono, password=password)
        return render(request, "registroExitoso.html", {'nombre':nombre,} )
    
def verificacion(nombre, direccion, telefono, password, passwordRep, correo):
    dicError={}
    
    if len(nombre)>=40 or len(nombre) <3:
        dicError.setdefault('errorNombre', "El nombre debe contener mas de 3 letras y menor o igual a 40 letras")
    
    if not(len(telefono)==10):
        dicError.setdefault('errorTelefono', "El numero telefonico debe tener 10 digitos")
    for i in telefono:
        if ord(i) < 48 or ord(i) >58:
            if 'errorTelefono' in dicError:
                dicError['errorTelefono']="El telefono solo puede contener numeros"
                break
            else:
                 dicError.setdefault('errorTelefono', "El numero telefonico no puede contener letras")
                 break
    if len(password)==0:
        dicError.setdefault('errorDireccion', "Debe ingresar una direccion")
        
    if len(password)>= 21 or len(password)<=7:
        if 'errorPassword' in dicError:
            dicError['errorPassword']= "La contraseña debe tener al menos 8 caracteres y no ser mayor de 20 caracteres"
        else:
            dicError.setdefault('errorPassword', "La contraseña debe tener al menos 8 caracteres y no ser mayor a 20 caracteres")
            
    if not(password==passwordRep):
        if 'errorPassword' in dicError:
            dicError['errorPassword']= "La contraseña y la repeticion de la contraseña no coincide"
        else:
            dicError.setdefault('errorPassword, "la contraseña y la repeticion de la contraseña no coincide')
        
    if len(correo)==0:
        dicError.setdefault('errorEmail', "Debe ingresar un correo")
    emailEnBase= cliente.object.filter(email=correo)
    if not len(emailEnBase)==0:
        if "errorEmail" in dicError:
            dicError['errorEmail']="El correo electronico no esta disponible"
        else:
            dicError.setdefault('errorEmail', "El correo electronico no esta disponible") 
    return dicError    