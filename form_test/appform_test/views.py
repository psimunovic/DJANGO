from django.shortcuts import render
from appform_test.forms import RegForm 
from appform_test.models import registrado

# Create your views here.

def inicio(request):
    form=RegForm(request.POST or None)
    if form.is_valid():
        form_data= form.cleaned_data
        abc= form_data.get("email")
        nombre=form_data.get("nombre")
        obj=registrado.objects.create(email=abc, nombre=nombre)
    context={"elform": form}
    return render(request, "inicio.html",context)