from django.http import HttpResponse
import datetime
from django.template import Template, context
from django.template import loader

def musica(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)
def tecnologias(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("tecnologias.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)
    
def games(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)
def saludar(request):
    return HttpResponse("hola")
def fecha(request):
    fechaActual=datetime.datetime.now()
    documento= """<HTML>
                        <HEAD>
                            <TITLE>Esta es una nueva estructura basica de un documento HTML</TITLE>
                        </HEAD>
                        <BODY>
                            <H1>Usted ingresó o actualizó esta vista en la fecha %s </h1>
                        </BODY>
                   </HTML>""" % fechaActual
    return HttpResponse(documento)     
def tareasEnlistadas(request):
    Tareas=["Aprender sobre la internet", "Aprender HTML", "Aprender CSS", "Practicar Python", "Aprender Django", "Construir mi propia WEB"]
    doc_externo=loader.get_template("SegundaPlantilla.html")
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)