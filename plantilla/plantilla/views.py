from re import template
from django.http import HttpResponse
import datetime
from django.template import Context, Template
def saludos(request):

    doc_ext=open("C:/django/plantilla/plantillas/plantilla1.html")
    plt=Template(doc_ext.read())
    doc_ext.close()
    contx=Context()
    pagina=plt.render(contx)
    return HttpResponse(pagina)

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