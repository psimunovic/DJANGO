from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.template import loader
#from django.template.loader import get_template #para cargar multiples templates


#**************************************************
class Persona(object):#Constructor
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludos3(request):
    
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


