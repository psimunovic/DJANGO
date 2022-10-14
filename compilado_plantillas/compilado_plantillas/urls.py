"""compilado_plantillas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from compilado_plantillas.vistas import atajo, lafecha, saludos, saludos2, saludos3, saludos4, calculo_edad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('atajos', atajo),
    path('saludo1', saludos),
    path('saludo2', saludos2),
    path('saludo3', saludos3),
    path('saludo4', saludos4),
    path('fecha', lafecha),
    path('edad/<int:edad>/<int:agno>', calculo_edad),
]
