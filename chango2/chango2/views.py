from django.http import HttpResponse
import datetime

def hola(request):
    return HttpResponse("Hola amiguillos esto es perfectijillo ")

def malditoflanders(request):

    pagina="""
    <html>
    <body>
        <h1> Saludirijillos ALUMNILLOS!!!!
        </h1>
    </body>
    </html>
    """
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