
from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.template import loader
#from django.template.loader import get_template #para cargar multiples templates
from django.shortcuts import render#simplifica la codificacion

#********************************************************

def saludos(request):
    nombre="paulo"
    apellido="simunovic"
    fecha=datetime.datetime.now()
    doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    plt=Template(doc_ext.read())
    doc_ext.close()
    contx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "fecha_act":fecha})#rescartar variable nombre y apellido
    pagina=plt.render(contx)
    return HttpResponse(pagina)

#***********************************************

class Persona(object):#Constructor
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludos2(request):
    #nombre="paulo"
    #apellido="simunovic"
    p1=Persona("Profe Tadeo", "Cepeda")
    temasCurso=["Plantillas","Modelos","ORM","Sesiones", "Seguridad"]
    fecha=datetime.datetime.now()
    doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    plt=Template(doc_ext.read())
    doc_ext.close()
    contx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})#llamar lista
    pagina=plt.render(contx)
    return HttpResponse(pagina)
#**************************************************
class Persona(object):#Constructor
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludos3(request):
    
    p1=Persona("Profe Tadeo", "Cepeda")
    temasCurso=["Plantillas","Modelos","ORM","Sesiones", "Seguridad"]
    fecha=datetime.datetime.now()
    doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    plt=Template(doc_ext.read())
    doc_ext.close()
    contx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})#llamar lista
    pagina=plt.render(contx)
    return HttpResponse(pagina)


#**************************************************
class Persona(object):#Constructor
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludos4(request):
    
    p1=Persona("Profe Tadeo", "Cepeda")
    temasCurso=["Plantillas","Modelos","ORM","Sesiones", "Seguridad"]
    fecha=datetime.datetime.now()
    #doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    #plt=Template(doc_ext.read())
    #doc_ext.close()
    #Con esto hay que ir al archivo settings.py y dentro de la lista template buscar DIRS,
    #donde se colocara la ruta hacia la carpeta de las plantillas
    #contx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})#llamar lista
    doc_ext=loader.get_template('plantilla1.html')
    pagina=doc_ext.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})
    return HttpResponse(pagina)

def atajo(request):
    
    p1=Persona("Profe Tadeo", "Cepeda")
    temasCurso=["Plantillas","Modelos","ORM","Sesiones", "Seguridad"]
    fecha=datetime.datetime.now()
    #doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    #plt=Template(doc_ext.read())
    #doc_ext.close()
    #Con esto hay que ir al archivo settings.py y dentro de la lista template buscar DIRS,
    #donde se colocara la ruta hacia la carpeta de las plantillas
    #contx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})#llamar lista
    #doc_ext=loader.get_template('plantilla2.html')
    #pagina=doc_ext.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})
    return render(request, "plantilla2.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_act":fecha, "temas":temasCurso})

def lafecha(request):

    fecha_actual=datetime.datetime.now()
    
    pagina="""
    <html>
    <body>
        <h1> Esta la fecha y hora actuales %s
        </h1>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(pagina)

def calculo_edad(request ,edad, agno):
    
    #edad_actual=41
    periodo=agno-2022
    edad_fut=edad+periodo
    documento="<html><body><h2> en el año %s tendras %s años </h2></body></html>"%(agno,edad_fut)

    return HttpResponse(documento)